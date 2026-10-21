"""Eval harness: run a golden or red-team JSONL file and score the system.

Usage: python evals/run_evals.py <file.jsonl> [--system baseline|agent]
Writes timestamped per-question results and a summary to evals/results/.
Metrics: retrieval hit rate, answer correctness, faithfulness,
refusal/escalation accuracy, cost per query, p50/p95 latency.
"""

from pathlib import Path


def load_cases(path: Path) -> list[dict]:
    """Read a JSONL file: question, expected_answer, expected_source, expected_behaviour."""
    ...


def run_case(case: dict, system: str) -> dict:
    """Run one question through the chosen system and return its raw result."""
    ...


def score_case(case: dict, result: dict) -> dict:
    """Score one result: hit, correct, faithful, behaviour_ok."""
    ...


def summarise(scored: list[dict]) -> dict:
    """Aggregate metrics, including p50/p95 latency and mean cost."""
    ...


def save_results(scored: list[dict], summary: dict) -> Path:
    """Write results to evals/results/ with a timestamp; return the file path."""
    ...


def main() -> None:
    """CLI entry point."""
    ...
