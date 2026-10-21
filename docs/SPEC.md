# Acme IT Helpdesk Assistant — Specification

Status: DRAFT v0.2 — not approved. Items marked **[OPEN]** need an owner decision (see §12).

## 1. Problem

Acme Ltd (fictional, ~500 staff) has an IT helpdesk overwhelmed by repetitive tickets (password resets, VPN, printers, software installs). The answers already exist in the knowledge base (KB), but staff raise tickets instead of reading it.

**Goal:** an assistant that answers staff IT questions from the KB with citations, checks or raises tickets when needed, escalates urgent or sensitive issues to a human, and is *proven* accurate, safe and affordable with measurements.

## 2. Users

| User | Needs |
|---|---|
| Staff (primary) | Fast, correct, cited answer; clear "I don't know" rather than a guess; easy path to a ticket |
| Helpdesk analysts | Fewer repetitive tickets; escalations that arrive with a reason and context |
| Security / governance reviewer | Audit trail, evidence of refusal behaviour, no data leakage |

Assumed identity model: the chat session carries a trusted `user_id` (stubbed in v1; no real auth).

## 3. Request flow (target design)

1. Staff question arrives (chat).
2. **Guardrail** — screen for prompt injection, requests for other people's data, urgent/security incidents. Risky → escalate.
3. **Router** — `fixed | rag | ticket | escalate`.
4. **Retrieve** KB chunks (semantic search, Chroma).
5. **Generate** answer grounded only in retrieved chunks, citing source articles. If the KB doesn't cover it, say so.
6. **Resolved?** If not, offer a ticket. Always confirm before any write.
7. **Log** query, route, chunk IDs, tools called, answer, tokens, cost, latency.

## 4. Functional requirements

IDs are referenced by tests and evals.

- **G-1** Input guardrail blocks prompt-injection attempts and requests for other users' data.
- **G-2** Urgent/security incidents (suspected breach, lost device, ransomware, phishing clicked) → `escalate`, never self-service advice only.
- **G-3** Retrieved chunks are screened for embedded instructions; flagged chunks are dropped and logged.
- **G-4** Output check redacts/blocks PII before sending.
- **R-1** Router returns exactly one of `fixed | rag | ticket | escalate`.
- **S-1** `search_kb(query)` returns top-k chunks with article ID, title, last-updated.
- **S-2** Agent may rewrite the query and search again (bounded: max N searches).
- **A-1** Answers use only retrieved chunks; every answer cites ≥1 article by ID.
- **A-2** If retrieval is weak or the KB is silent, the answer says so and offers a ticket. No guessing.
- **A-3** Contradictory or outdated sources: answer prefers the newer, in-date article and flags the conflict. **[OPEN Q4]**
- **T-1** `check_ticket_status(ticket_id)` returns only tickets owned by the session user.
- **T-2** `create_ticket(...)` executes only after explicit user confirmation in a prior turn.
- **T-3** `escalate_to_human(reason)` records reason and conversation summary.
- **L-1** Every request writes one structured JSON log line (fields in §3 step 7). No API keys, no full personal data.

## 5. Data

| Set | Location | Notes |
|---|---|---|
| Knowledge base | `data/kb/*.md` | 20–30 articles; front-matter: title, last-updated, applies-to |
| Ticket DB | `data/tickets.db` | SQLite; schema per CLAUDE.md; seeded from Tobi-Bueck/customer-support-tickets (CC-BY-NC-4.0, non-commercial — fine for a portfolio, attribute it) |
| Golden set | `evals/golden_dev.jsonl` (~35), `evals/golden_test.jsonl` (~15) | Written by the owner. Mix ~60% easy / 20% hard / 10% refuse / 10% escalate. Every KB article covered ≥ once |
| Red-team set | `evals/redteam.jsonl` | Same schema; expected behaviour is refuse or escalate |

**Deliberate KB traps:** one contradictory pair, one outdated article, one article with a hidden injected instruction.

**Dataset caveats found while researching it** (61.8k rows):
- Bilingual: 33.5k German, 28.3k English. Seed the DB from `language == "en"` only. **[OPEN Q5]**
- Only a minority is IT-relevant. 52 queues, dominated by Technical Support (14.2k), Product Support (9.0k), Customer Service (7.4k), IT Support (5.7k); the rest are ~300-row noise queues (Pets, Games, Real Estate…). Filter to IT queues.
- `queue`, `type` (Incident/Request/Problem/Change), and `priority` (very_low…critical) map well onto our `category` and `priority`. There is no `user`, `status`, or `resolution` column in the sense we need — `answer` can seed `resolution`; `user` and `status` must be synthesised (documented, deterministic seed).
- ~21% of rows have missing `type`/`answer`.

## 6. Success criteria (initial)

| Metric | Target | Measured on |
|---|---|---|
| Answer correctness with correct citation | ≥ 85% | held-out test (milestones only) |
| Refusal/escalation accuracy | 100% | red-team |
| Write actions without confirmation | 0 | red-team + unit tests |
| Retrieval hit rate (expected source in top-k) | reported, baseline first | dev |
| Faithfulness (claims supported by chunks) | reported | dev |
| Cost per query, p50/p95 latency | reported | dev |

Note: with ~15 test questions, one miss moves the score ~7 points; 85% means ≤2 misses. Report counts, not just percentages. **[OPEN Q6]**

## 7. Out of scope (v1)

Streamlit UI, LangGraph, multi-agent frameworks, real authentication/SSO, real ITSM integration, voice/attachments/screenshots, non-English support, actions other than ticket create/check/escalate (no password resets actually performed), production deployment.

## 8. Risks

| Risk | Mitigation / evidence |
|---|---|
| Wrong article chosen when KB contradicts itself or is stale | Planted traps; metric: contradiction handled correctly |
| Prompt injection via user or KB content | G-1, G-3; red-team set including the poisoned article |
| Answers beyond evidence / hallucinated steps | A-1/A-2; faithfulness metric; critic in phase 3+ |
| Cross-user data leakage via ticket tool | T-1 enforced in code, not in the prompt; unit tests |
| Over-escalation hurts usefulness | Track false-escalation rate on answerable dev questions |
| Eval overfitting | Test set sealed; run at milestones only |
| LLM-judge bias in grading | Spot-check judge verdicts by hand; log disagreements |
| Fictional KB is too tidy, inflating scores | Include messy, overlapping, reworded content |

## 9. Constraints

Python 3.11+, plain provider tool-use API (no agent framework), Chroma, SQLite. Keys in `.env` only, `.env.example` provided. Ask before adding dependencies. Decisions with real alternatives get an ADR in `docs/decisions/`.

## 10. Phase plan

1. **Spec** (this doc), KB articles, golden + red-team sets (owner-written).
2. Baseline RAG + eval harness; record baseline scores.
3. Agentic v1; compare loop vs fixed pipeline on dev.
4. Security & governance. 5. FinOps. 6. LangGraph v2 + packaging.

## 11. Phase 1 definition of done

- This spec approved.
- 20–30 KB articles with traps, topics approved by owner.
- `golden_dev`, `golden_test`, `redteam` written by owner; coverage check passes (every article ≥ 1 question).
- ADR decisions recorded for anything chosen in Phase 2 planning.

## 12. Open questions

1. **Ticket creation in v1:** real write into SQLite after confirmation, or a drafted-ticket preview only until Phase 3?
2. **Fixed workflows:** which tasks bypass RAG (e.g. password reset = fixed script that points to a self-service link)? Which 2–3 to start with?
3. **Identity:** is a hard-coded `user_id` per eval case acceptable for testing own-tickets-only?
4. **Contradiction policy:** prefer newer article, or present both and flag the conflict? (Affects how you write expected answers for those questions.)
5. **Language:** English-only seeding of tickets OK?
6. **Grading:** exact-match on source ID plus LLM-judge for answer correctness, or fully manual for the first runs?
7. **Provider/models:** Anthropic or OpenAI for v1, and is there a monthly budget cap to design the FinOps phase around?
8. **Escalation definition:** what counts as urgent beyond security incidents (e.g. "whole office offline", "executive can't log in")?
9. **Refuse vs escalate:** confirm the distinction. Proposed: *refuse* = out of scope or disallowed (other people's data, off-topic, injection); *escalate* = legitimate but needs a human (incident, outage, access approval).
