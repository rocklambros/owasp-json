# OWASP Top 10 — Structured JSON

Machine-readable JSON versions of the OWASP Top 10 for **Agentic Applications** (2026) and **LLM Applications** (2025).

Parsed from the official OWASP PDF releases into structured schemas so you can build tooling, dashboards, checklists, and integrations without scraping PDFs.

## Files

| File | Document | Version | Entries |
|------|----------|---------|---------|
| [`agentic-top-10/...FINAL.json`](agentic-top-10/2025-OWASP-Top-10-for-Agentic-Applications-2026-12.6-1-FINAL.json) | OWASP Top 10 for Agentic Applications | 2026 | 10 |
| [`llm-top-10/...final_rc.json`](llm-top-10/2025_LLMAll_en-US_final_rc.json) | OWASP Top 10 for LLM Applications | 2025 | 10 |

## Agentic Top 10 (ASI01–ASI10)

| Rank | ID | Title |
|------|----|-------|
| 1 | ASI01 | Agent Goal Hijack |
| 2 | ASI02 | Tool Misuse and Exploitation |
| 3 | ASI03 | Identity and Privilege Abuse |
| 4 | ASI04 | Agentic Supply Chain Vulnerabilities |
| 5 | ASI05 | Unexpected Code Execution (RCE) |
| 6 | ASI06 | Memory & Context Poisoning |
| 7 | ASI07 | Insecure Inter-Agent Communication |
| 8 | ASI08 | Cascading Failures |
| 9 | ASI09 | Human-Agent Trust Exploitation |
| 10 | ASI10 | Rogue Agents |

Each entry contains: `rank`, `identifier`, `title`, `description`, `common_examples`, `attack_scenarios`, `prevention_guidelines`, `references`.

## LLM Top 10 (LLM01–LLM10)

| Rank | ID | Title |
|------|----|-------|
| 1 | LLM01:2025 | Prompt Injection |
| 2 | LLM02:2025 | Sensitive Information Disclosure |
| 3 | LLM03:2025 | Supply Chain |
| 4 | LLM04:2025 | Data and Model Poisoning |
| 5 | LLM05:2025 | Improper Output Handling |
| 6 | LLM06:2025 | Excessive Agency |
| 7 | LLM07:2025 | System Prompt Leakage |
| 8 | LLM08:2025 | Vector and Embedding Weaknesses |
| 9 | LLM09:2025 | Misinformation |
| 10 | LLM10:2025 | Unbounded Consumption |

Each entry contains: `rank`, `identifier`, `title`, `description`, `common_examples`, `prevention_strategies` (with optional nested sub-headings), `attack_scenarios`, `references`, `related_frameworks`.

## Schema

Both files share a common wrapper:

```json
{
  "title": "OWASP Top 10 for ...",
  "version": "2025",
  "source_file": "original_filename.txt",
  "entries": [ ... ]
}
```

### Agentic entry

```json
{
  "rank": 1,
  "identifier": "ASI01",
  "title": "Agent Goal Hijack",
  "description": "AI Agents exhibit autonomous ability to ...",
  "common_examples": ["Prompt injection ...", "..."],
  "attack_scenarios": ["An attacker ...", "..."],
  "prevention_guidelines": ["Implement strict ...", "..."],
  "references": ["OWASP Agentic AI ...", "..."]
}
```

### LLM entry

```json
{
  "rank": 1,
  "identifier": "LLM01:2025",
  "title": "Prompt Injection",
  "description": "A Prompt Injection Vulnerability occurs when ...",
  "common_examples": ["Direct Prompt Injections ...", "..."],
  "prevention_strategies": [
    {
      "heading": "",
      "items": ["Constrain model behavior ...", "..."]
    }
  ],
  "attack_scenarios": ["An attacker injects a prompt ...", "..."],
  "references": ["ChatGPT Plugin Vulnerabilities ...", "..."],
  "related_frameworks": ["AML.T0051.000 - LLM Prompt Injection: Direct MITRE ATLAS", "..."]
}
```

LLM entries with sub-headed prevention strategies (e.g. LLM02) use a non-empty `heading` field:

```json
"prevention_strategies": [
  { "heading": "Sanitization", "items": ["Integrate Data Sanitization ...", "..."] },
  { "heading": "Access Controls", "items": ["Enforce Strict Access Controls ...", "..."] }
]
```

## Source

Parsed from the official OWASP releases:
- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org)

This content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) per the original OWASP documents.
