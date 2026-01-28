# Project: owasp-json

## Overview
Parse OWASP Top 10 PDFs (LLM Top 10, Agentic Top 10) into structured JSON schemas using Pydantic models.

## Tech Stack
- **Runtime**: Python 3.12
- **Package Manager**: uv
- **Schema**: Pydantic v2
- **PDF Parsing**: pdfplumber
- **Testing**: pytest
- **Linting**: ruff, mypy

## Repository Structure
```
owasp-json/
├── owasp_json/          # Main package
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── parser.py        # PDF parsing logic
│   └── schema.py        # Pydantic models
├── tests/               # Test suite
├── agentic-top-10/docs/ # OWASP Agentic Top 10 PDF
├── llm-top-10/docs/     # OWASP LLM Top 10 PDF
├── .zerg/               # ZERG configuration
├── .devcontainer/       # Dev container setup
└── .gsd/                # Project documentation
```

## Development Commands
- `uv pip install -e ".[dev]"` - Install with dev deps
- `pytest` - Run tests
- `ruff check .` - Lint
- `mypy owasp_json/` - Type check

## Factory Configuration
- **Max Workers**: 3
- **MCP Servers**: filesystem
