"""Audit and cost logging: one structured JSON line per request in `logs/`.

Fields: query, route, retrieved chunk IDs, tools called, final answer,
tokens, cost, latency. Never writes API keys or full personal data.
"""


def redact(text: str) -> str:
    """Mask emails, phone numbers and similar PII before text is logged."""
    ...


def log_request(record: dict) -> None:
    """Redact and append one request record to today's log file."""
    ...
