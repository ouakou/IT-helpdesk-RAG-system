"""Seed data/tickets.db from Tobi-Bueck/customer-support-tickets (CC-BY-NC-4.0).

Keeps English rows from IT-relevant queues, maps queue/type/priority to
category/priority, uses `answer` as resolution, and synthesises user and status
with a fixed random seed so the result is reproducible.
"""


def load_dataset_rows() -> list[dict]:
    """Download and filter the dataset to English IT-queue rows."""
    ...


def to_ticket(row: dict, index: int, rng_seed: int) -> dict:
    """Map a dataset row to the tickets-table schema."""
    ...


def write_db(tickets: list[dict]) -> None:
    """Create the tickets table and insert the rows."""
    ...


def main() -> None:
    """CLI entry point."""
    ...
