from llama_index.core import SimpleDirectoryReader, ServiceContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.response_synthesizers import TreeSummarize
from llama_index.llms.ollama import Ollama

class SummarizeService():
  def __init__(self):
    self.embed_model = Ollama(model="nomic-embed-text",request_timeout=300.0)
    self.model = Ollama(model="gemma2",request_timeout=300.0)
    self.splitter = SentenceSplitter(chunk_size=1024)

  def summarize(self):
    docs = SimpleDirectoryReader(input_files=["./transcript_data/transcripts.txt"]).load_data()
    service_context = ServiceContext.from_defaults(embed_model=self.embed_model,llm=self.model)
    summarizer = TreeSummarize(service_context=service_context,verbose=True,streaming=True)
    response = summarizer.get_response(query_str="Summarize this video transcript",text_chunks=docs[0].text)
    return response