from langchain.prompts import PromptTemplate

str_template = """
You are a helpful assistant that gives a clear summary of youtube videos. Based on the following video transcript:
{transcript}
give a summary.
"""

prompt = PromptTemplate(
  input_variables=["transcript"],
  template=str_template
)