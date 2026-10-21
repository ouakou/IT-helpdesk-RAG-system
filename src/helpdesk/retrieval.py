"""Retrieval: the `search_kb` tool. The only module that talks to Chroma."""


def search_kb(query: str, k: int = 4) -> list[dict]:
    """Return the top-k chunks for a query.

    Each result: chunk_id, article_id, title, last_updated, text, score.
    """
    ...
