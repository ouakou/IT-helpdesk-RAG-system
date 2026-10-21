"""Router: a cheap LLM call that picks the workflow for a request."""

ROUTES = ("fixed", "rag", "ticket", "escalate")


def route_request(question: str) -> dict:
    """Return {"route": one of ROUTES}. Falls back to 'escalate' on invalid output."""
    ...
