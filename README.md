# owasp-json

Parse OWASP Top 10 PDFs into structured JSON schemas.

## Install

```bash
pip install -e ".[dev]"
```

## Usage

```python
from owasp_json import convert

doc = convert("llm-top-10/docs/2025_LLMAll_en-US_final_rc.pdf")
print(doc.to_json())
```

## Development

```bash
pytest
ruff check .
mypy owasp_json/
```
