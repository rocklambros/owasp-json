"""PDF parsing logic for OWASP documents."""

from pathlib import Path

import pdfplumber

from owasp_json.schema import OWASPDocument, RiskEntry


def parse_pdf(pdf_path: Path) -> OWASPDocument:
    """Parse an OWASP Top 10 PDF into a structured document."""
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text = _extract_text(pdf_path)
    entries = _extract_entries(text)

    return OWASPDocument(
        title=_extract_title(text),
        source_file=pdf_path.name,
        entries=entries,
    )


def _extract_text(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""
    pages: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                pages.append(page_text)
    return "\n".join(pages)


def _extract_title(text: str) -> str:
    """Extract the document title from the first lines."""
    lines = text.strip().splitlines()
    for line in lines[:10]:
        stripped = line.strip()
        if stripped and len(stripped) > 10:
            return stripped
    return "Unknown OWASP Document"


def _extract_entries(text: str) -> list[RiskEntry]:
    """Extract risk entries from the document text.

    This is a baseline implementation. Parsing logic should be refined
    per document format.
    """
    # Placeholder: returns empty list until format-specific parsing is added
    return []
