from langchain_community.document_loaders import YoutubeLoader

class YoutubeLoaderService():
  def __init__(self):
    pass

  def load_video(self,url:str):
    loader = YoutubeLoader.from_youtube_url(youtube_url=url,add_video_info=False,translation="en")
    docs = loader.load()
    transcript = docs[0].page_content
    return transcript