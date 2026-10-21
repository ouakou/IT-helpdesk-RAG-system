"""Guardrails: input screen, retrieved-chunk screen, output PII check."""


def screen_input(question: str, user_id: str) -> dict:
    """Check for prompt injection, requests for other people's data, urgent/security incidents.

    Returns: allowed (bool), action ('allow' | 'refuse' | 'escalate'), reason.
    """
    ...


def screen_chunks(chunks: list[dict]) -> list[dict]:
    """Drop retrieved chunks that contain embedded instructions; log what was removed."""
    ...


def check_output(answer: str) -> dict:
    """Detect or redact PII in the final answer before it is sent."""
    ...
