# Acme IT Helpdesk Assistant — Project Context

## Why this project exists
This is a portfolio project for a graduate Agentic Engineering role (FDM Group). The role values
**specifying, evaluating, securing and defending** AI systems over raw code output. Every part of
this project should produce evidence of those skills: specs, eval scores, red-team results, cost
data and written decisions.

I am learning. When you make a design choice, explain it briefly and offer the alternative.
Do not hide complexity behind frameworks until the plain version works and is measured.

## The problem (business framing)
Acme Ltd (fictional, ~500 staff) has an IT helpdesk overwhelmed by repetitive tickets
(password resets, VPN, printers, software installs). The answers already exist in the
knowledge base (KB), but staff raise tickets instead of reading it.

**Goal:** an assistant that answers staff IT questions from the KB with citations, checks or
raises tickets when needed, escalates urgent or sensitive issues to a human, and is proven
accurate, safe and affordable with measurements.

## Request workflow (target design)
1. **Staff question** arrives (chat message).
2. **Guardrail check** — screen for prompt injection, requests for other people's data,
   urgent/security incidents. Risky → escalate to human.
3. **Router** — common fixed task (e.g. password reset) → fixed workflow; otherwise → RAG.
4. **Retrieve KB chunks** — semantic search over the vector store.
5. **Generate answer** — grounded only in retrieved chunks, always cite the source article.
   If the KB doesn't cover it, say so; never guess.
6. **Resolved?** — if not, **offer a ticket**. Always ask for confirmation before any write action.
7. **Log and evaluate** — every request logs: query, route, retrieved chunk IDs, tools called,
   final answer, tokens, cost, latency.

## Data (four separate sets)
| Set | Location | Form | Purpose |
|---|---|---|---|
| Knowledge base | `data/kb/*.md` | 20–30 Markdown articles with title, last-updated, applies-to | What the AI reads (chunked + embedded) |
| Ticket database | `data/tickets.db` (SQLite) | Tickets table: ticket_id, user, subject, body, category, priority, status, resolution, created_at | What the agent's tools query/write. Seeded from the Tobi-Bueck customer-support-tickets dataset (Hugging Face, CC-BY-NC-4.0) |
| Golden dataset | `evals/golden_dev.jsonl`, `evals/golden_test.jsonl` | question, expected_answer, expected_source, expected_behaviour (answer / refuse / escalate) | Accuracy evaluation |
| Red-team set | `evals/redteam.jsonl` | Same schema; expected_behaviour is refuse or escalate | Security evaluation |

**KB must deliberately include:** one pair of contradictory articles, one outdated article,
and one article containing a hidden injected instruction (for red-team testing).

**Golden set split:** ~35 dev (tune against freely), ~15 held-out test (run only at milestones,
never tune against). Mix: ~60% easy, ~20% hard (multi-article or reworded), ~10% refuse,
~10% escalate. Every KB article covered at least once.

**IMPORTANT:** I write the golden and red-team questions myself. You may suggest formats,
draft candidates for me to edit, and check coverage — but never silently generate or modify
expected answers. Never read `golden_test.jsonl` while tuning prompts or retrieval.

## Agent roles (implemented as tools/steps, not separate frameworks at first)
- **Guardrail** — input screen before the loop; output check for PII after.
  Also screen retrieved chunks for embedded instructions.
- **Router** — cheap LLM call returning `{"route": "fixed" | "rag" | "ticket" | "escalate"}`.
- **Retrieval** — `search_kb(query)` tool; the agent may rewrite the query and search again.
- **Responder** — writes the grounded, cited answer.
- **Action** — `check_ticket_status(ticket_id)`, `create_ticket(...)`, `escalate_to_human(reason)`.
  Users may only see their own tickets. `create_ticket` requires explicit user confirmation.
- **Critic** (phase 3+) — checks every claim is supported by retrieved chunks before sending.

## Tech stack
- Python 3.11+, `pytest`, `ruff`
- LLM: plain Anthropic (or OpenAI) API tool use for v1 — **no agent framework in v1**
- Vector store: Chroma (local)
- Tickets: SQLite
- UI: Streamlit (later)
- v2 orchestration: LangGraph (only after v1 is measured)
- Evals: own harness first; Ragas/promptfoo optional later
- Tracing: structured JSON logs in `logs/`; Langfuse optional later
- API keys from `.env` only (never hard-coded, never committed). Provide `.env.example`.

## Suggested structure
```
src/helpdesk/
  ingest.py        # load KB, chunk, embed, store in Chroma
  retrieval.py     # search_kb
  tickets.py       # SQLite access + ticket tools
  guardrails.py
  router.py
  agent.py         # the tool-use loop
  logging_utils.py # audit + cost logging
  app.py           # Streamlit UI (later)
evals/
  run_evals.py     # runs a golden/red-team file, outputs scores + per-question results
  results/         # timestamped result files
data/
docs/
  SPEC.md
  decisions/       # ADRs: 001-chunking.md, 002-framework.md, ...
  ai-was-wrong.md  # log of AI-generated mistakes I caught
tests/
```

## Build phases
1. **Spec** — `docs/SPEC.md`: problem, users, success criteria, out of scope, risks. KB articles.
   Golden + red-team sets (written by me).
2. **Baseline RAG + eval harness** — ingest, `search_kb`, simple answer step, `run_evals.py`.
   Record baseline scores.
3. **Agentic v1** — tool-use loop with the four tools, confirmation before writes,
   guardrail + router. Compare agent loop vs fixed pipeline on the dev set.
4. **Security & governance** — red-team runs, PII redaction, audit log, own-tickets-only enforcement.
5. **FinOps** — tokens + cost per query; compare 2–3 models on accuracy vs cost vs latency.
6. **v2 in LangGraph + packaging** — rebuild orchestration, compare with v1, README,
   architecture diagram, demo.

## Success criteria (initial — refine in SPEC.md)
- ≥85% correct on held-out test set, each with correct citation
- 100% correct refusal/escalation on red-team set
- Zero write actions without confirmation
- Cost per query recorded and reported

## Eval metrics to report
Retrieval hit rate (expected source in top-k), answer correctness, faithfulness
(claims supported by chunks), refusal/escalation accuracy, cost per query, p50/p95 latency.

## Working rules for Claude Code
- Work one phase at a time. Don't jump ahead without my go-ahead.
- Before writing code for a phase, propose a short plan and wait for approval.
- Write tests for tools and guardrails. Run tests and evals after changes, and report the
  before/after numbers.
- Ask before adding any dependency.
- When a decision has real alternatives (chunk size, top-k, model, framework), write a short
  ADR in `docs/decisions/`: context, options, choice, why, how we'll know if it was wrong.
- If you notice your own earlier output was wrong, say so and add it to `docs/ai-was-wrong.md`.
- Keep functions small and readable — I need to be able to explain every line in an interview.
- Never print or log API keys or full personal data.
