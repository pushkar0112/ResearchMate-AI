# ResearchMate AI

ResearchMate AI is a professional, beginner-friendly project for **Assignment 5: Paper-to-Presentation & Viva Agent**. It is designed to help a student understand a research paper, prepare a presentation, and practice explaining the work.

#Deployed Link
https://pushkar0112-researchmate-ai-app-op6ivt.streamlit.app/
## Current status

The Streamlit app currently supports page-aware PDF extraction, Gemini-grounded paper chat and analysis, PowerPoint generation with an in-app presenter, interactive viva practice (up to six questions per session), paper-grounded flashcards with citations, and a learning dashboard with local score history and topic performance. Gemini-backed features require a local `GEMINI_API_KEY` in `.env`.

## Setup

You need Python 3.11 or newer. From this project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env             # Windows: copy .env.example .env
```

Open `.env` in a local editor and replace `your_gemini_api_key_here` with your Gemini API key. Keep `.env` private; it is ignored by Git. Do not paste the key into chat or commit it.

Launch the app with:

```bash
streamlit run app.py
```

The initial screen is an application shell; most feature controls are placeholders until their roadmap phase is built. No key is needed just to view the shell. Gemini-backed features will require a valid key.

## Architecture

- **Streamlit** provides the interactive GUI.
- **Gemini** handles generation; the key is read from `GEMINI_API_KEY`.
- **LangChain prompt templates + LCEL** form explicit, inspectable prompt/model/parser chains.
- **PyMuPDF** will extract PDF text while preserving page numbers.
- **Gemini embeddings + ChromaDB** will power Agentic RAG retrieval.
- **python-pptx** will create customizable PowerPoint files.
- **Pandas + Plotly** will support performance summaries and charts.

## Project map

```text
app.py                 Streamlit interface shell
researchmate/
  config.py            Environment-based settings
  prompts.py           Prompt template and Gemini LCEL chain
requirements.txt       Python dependencies
.env.example           Safe configuration template (no secret)
ROADMAP.md             Phased delivery plan and assignment mapping
```

See [ROADMAP.md](ROADMAP.md) for the full implementation sequence and acceptance checklist.
