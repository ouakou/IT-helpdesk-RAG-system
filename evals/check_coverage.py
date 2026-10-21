"""Coverage check: is every KB article cited by at least one golden question?

Reads only question metadata (expected_source) from golden_dev/golden_test,
never the answers, and never runs the system.
"""


def kb_article_ids() -> set[str]:
    """Return the article IDs found in data/kb/."""
    ...


def covered_article_ids(golden_paths: list[str]) -> set[str]:
    """Return the article IDs referenced by expected_source across the given files."""
    ...


def main() -> None:
    """Print uncovered articles and the behaviour mix (answer/refuse/escalate) vs the target."""
    ...
