# MSC Youtube Summarizer

## Overview

MSC Youtube Summarizer is a tool that summarizes english youtube videos locally using Ollama and Llamaindex. It provides a simple FastAPI server that scrapes youtube transcripts and streams the summarized content to client using Streamlit.

## Getting Started

### Dependencies

All dependencies can be found inside the requirements.txt file.

### Installing

1. Clone the repository

```
git clone <repository_url>
cd <repositroy_url>
```

2. Install dependencies:

```
pip install -r requirements.txt
```

### Executing program

1. Run the FastAPI Server:

```
cd backend
fastapi run
```

- FastAPI server will be running at `http://0.0.0.0:8000`

2. Run the Streamlit App:

```
cd frontend
streamlit run streamlit_main.py
```

- Streamlit App will be runnnig at `http://localhost:8501`

## Authors

- Berat Kamali

## License

This project is licensed under the All Rights Reserved License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [LlamaIndex](https://www.llamaindex.ai/)
