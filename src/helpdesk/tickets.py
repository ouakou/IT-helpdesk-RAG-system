"""Ticket database (SQLite) access and the agent's ticket tools.

Rules enforced in code, not in the prompt:
- users may only see their own tickets
- create_ticket needs explicit user confirmation
"""

import sqlite3


def get_connection() -> sqlite3.Connection:
    """Open data/tickets.db."""
    ...


def check_ticket_status(ticket_id: str, user_id: str) -> dict:
    """Return the ticket if it belongs to user_id; otherwise a refusal result."""
    ...


def create_ticket(user_id: str, subject: str, body: str, category: str, priority: str, confirmed: bool) -> dict:
    """Insert a ticket only if confirmed is True; otherwise return a preview and write nothing."""
    ...


def escalate_to_human(user_id: str, reason: str, summary: str) -> dict:
    """Record an escalation for a human analyst."""
    ...
