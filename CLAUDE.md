# owasp-json

Python library to parse OWASP Top 10 PDFs into structured JSON schemas.

## Commands
- `uv pip install -e ".[dev]"` - Install
- `pytest` - Test
- `ruff check .` - Lint
- `mypy owasp_json/` - Type check

## Structure
- `owasp_json/` - Main package (parser.py, schema.py, main.py)
- `tests/` - Test suite
- `agentic-top-10/docs/` - OWASP Agentic Top 10 PDF source
- `llm-top-10/docs/` - OWASP LLM Top 10 PDF source

<!-- SECURITY_RULES_START -->
## Security Rules

Auto-generated from TikiTribe/claude-secure-coding-rules

### Detected Stack
- **Languages**: python
- **Frameworks**: pydantic

### Imported Rules
@.claude/security-rules/owasp-2025.md
@.claude/security-rules/python.md
<!-- SECURITY_RULES_END -->
