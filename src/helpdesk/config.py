"""Central settings: the one place every tunable value lives.

Loads secrets from `.env` (never hard-coded) and exposes paths and knobs
(model names, chunk size, top-k) so ADRs and eval runs can point at one file.
"""

from pathlib import Path


def project_root() -> Path:
    """Return the repository root directory."""
    ...


def get_api_key() -> str:
    """Read the LLM provider API key from the environment. Never log it."""
    ...


def get_settings() -> dict:
    """Return all settings: paths, model names, chunk size/overlap, top-k, max searches."""
    ...
