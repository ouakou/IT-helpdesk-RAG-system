"""KB ingestion: load Markdown articles, chunk, embed, store in Chroma.

Run once, and again whenever `data/kb/*.md` changes. Chunking choices are
recorded in docs/decisions/001-chunking.md.
"""

from pathlib import Path


def load_articles(kb_dir: Path) -> list[dict]:
    """Read each .md file; return dicts with article_id, title, last_updated, applies_to, text."""
    ...


def chunk_article(article: dict, chunk_size: int, overlap: int) -> list[dict]:
    """Split one article into chunks; each keeps article_id and metadata for citation."""
    ...


def build_index(chunks: list[dict]) -> None:
    """Embed the chunks and (re)write them into the Chroma collection."""
    ...


def main() -> None:
    """CLI entry point: load, chunk, index."""
    ...
