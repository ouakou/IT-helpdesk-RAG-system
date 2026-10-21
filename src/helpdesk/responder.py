"""Responder: writes the grounded, cited answer. This is the baseline RAG step.

Fixed pipeline (retrieve -> answer), kept separate from the agent loop so the
two can be compared on the same dev set in Phase 3.
"""


def build_prompt(question: str, chunks: list[dict]) -> tuple[str, list[dict]]:
    """Build (system, messages): answer only from the chunks, cite article IDs,
    say 'not covered' if the chunks do not support an answer."""
    ...


def answer_question(question: str) -> dict:
    """Retrieve, generate and return: answer, cited_article_ids, chunk_ids, tokens, cost, latency."""
    ...
