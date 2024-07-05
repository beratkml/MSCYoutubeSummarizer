from langchain_community.document_loaders import YoutubeLoader
from langchain_community.chat_models import ChatOllama
from ..prompts import prompt
from fastapi import HTTPException

class YoutubeLoaderService():
  def __init__(self):
    pass

  def load_video(self,url:str):
    loader = YoutubeLoader.from_youtube_url(youtube_url=url,add_video_info=False,translation="en")
    docs = loader.load()
    transcript = docs[0].page_content
    return transcript
  
  async def summarize(self,url:str):
    if not url.startswith("https://www.youtube.com/"):
      raise HTTPException(status_code=500, detail="Invalid URL")
    print("Started summarizing...")
    llm = ChatOllama(model="gemma2")
    transcript = self.load_video(url)
    chain = prompt | llm

    async for chunk in chain.astream({"transcript":transcript}):
      yield chunk.content.strip()
    print("Finished summarizing")