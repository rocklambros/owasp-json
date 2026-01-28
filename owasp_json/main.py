"""Main entry point for OWASP JSON schema generation."""

from pathlib import Path

from owasp_json.parser import parse_pdf
from owasp_json.schema import OWASPDocument


def convert(pdf_path: str | Path) -> OWASPDocument:
    """Convert an OWASP PDF to a structured document."""
    return parse_pdf(Path(pdf_path))
