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
  try:
    return StreamingResponse(summarize_service.summarize(prompt),media_type='text/event-stream')
  except Exception as e:
    raise HTTPException(status_code=404, detail="Item not found")
  

