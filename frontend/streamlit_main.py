import streamlit as st
import requests
import time

st.title("YouTube Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")
if st.button("Summarize"):
    if url:
        api_url = f"http://localhost:8000/sse?url={url}"
        status_placeholder = st.empty()
        status_placeholder.write("summarizing transcript, please wait")
        response = requests.get(api_url, stream=True)
        status_placeholder.empty()

        summary_placeholder = st.empty()
        summary = ""
        for chunk in response.iter_content(chunk_size=128):
            if chunk:
                summary+=chunk.decode("utf-8")
                summary_placeholder.markdown(summary)
                time.sleep(0.02)
        
