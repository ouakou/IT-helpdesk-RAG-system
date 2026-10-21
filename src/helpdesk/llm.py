"""Thin wrapper around the LLM provider API.

Every model call goes through here so token counts, cost and latency are
captured in one place, and swapping models for the FinOps comparison needs
no changes elsewhere.
"""


def call_llm(
    system: str,
    messages: list[dict],
    model: str,
    tools: list[dict] | None = None,
    max_tokens: int = 1024,
) -> dict:
    """Make one model call.

    Returns: text, tool_calls, input_tokens, output_tokens, cost_usd, latency_s.
    """
    ...


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Convert token counts to USD using the price table for the model."""
    ...
