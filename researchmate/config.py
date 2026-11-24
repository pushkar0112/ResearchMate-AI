"""Application settings loaded from environment variables or a local .env."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


def _get_setting(name: str, default: str | None = None) -> str | None:
    """Read a setting from the environment/.env or Streamlit Cloud secrets."""
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st

        secret_value = st.secrets.get(name)
        return str(secret_value) if secret_value else default
    except Exception:
        # Local runs without a secrets.toml raise when st.secrets is accessed.
        return default


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str | None = _get_setting("GEMINI_API_KEY")
    gemini_model: str = _get_setting("GEMINI_MODEL", "gemini-3.8-flash") or "gemini-3.8-flash"
    gemini_embedding_model: str = (
        _get_setting("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-001")
        or "models/gemini-embedding-001"
    )
    chroma_dir: str = _get_setting("CHROMA_DIR", "./chroma_db") or "./chroma_db"


settings = Settings()
