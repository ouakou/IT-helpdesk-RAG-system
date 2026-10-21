"""Agent: the tool-use loop tying guardrails, router, tools and responder together.

Tools: search_kb, check_ticket_status, create_ticket, escalate_to_human.
Writes always require explicit user confirmation. Max-iteration cap prevents loops.
"""


def run_agent(question: str, user_id: str, history: list[dict] | None = None) -> dict:
    """Handle one turn end to end; return answer, route, tools_called, chunk_ids, tokens, cost, latency."""
    ...


def execute_tool(name: str, args: dict, user_id: str) -> dict:
    """Dispatch a tool call by name, injecting the trusted user_id (never taken from the model)."""
    ...
