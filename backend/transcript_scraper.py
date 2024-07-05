from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeScrapeService:
  def __init__(self):
    pass

  def clear_file(self):
    with open("./transcript_data/transcripts.txt", "w", encoding="utf-8"):
      pass
  
  def scrape_transcript(self,url:str):
    self.clear_file()
    transcript = YouTubeTranscriptApi.get_transcript(self.get_video_id(url=url), languages=["en"])
    text_outputs = []

    with open("./transcript_data/transcripts.txt","a",encoding="utf-8") as wrt:
      for i in transcript:
        txt = i['text']
        if not txt.startswith("[") and not txt.endswith("]"):
          wrt.write(txt + "\n")
          text_outputs.append(txt)

  def get_video_id(self,url:str):
    start_index = url.find("=")
    return url[start_index+1:start_index+12]