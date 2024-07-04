from services.youtube_loader import YoutubeLoaderService
from langchain_community.chat_models import ChatOllama
from prompts import prompt

youtube_loader_service = YoutubeLoaderService()
llm = ChatOllama(model="gemma2")
transcript = youtube_loader_service.load_video("https://www.youtube.com/watch?v=jBFFUwL0TyY")
chain = prompt | llm

print(chain.invoke({"transcript":transcript}).content)

