from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from .services.youtube_loader import YoutubeLoaderService

app = FastAPI()
origins = [
  "*",
  "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
summarize_service = YoutubeLoaderService()

@app.post("/sse")
async def response(prompt:str):
  return StreamingResponse(summarize_service.summarize(prompt),media_type='text/event-stream')
  

