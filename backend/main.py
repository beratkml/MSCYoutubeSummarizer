from transcript_scraper import YoutubeScrapeService
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from summarize_service import SummarizeService

app = FastAPI()
scraper = YoutubeScrapeService()
summarize = SummarizeService()

@app.get("/sse")
async def main(url:str):
    scraper.scrape_transcript(url=url)
    return StreamingResponse(summarize.summarize(),media_type="text/event-stream")


