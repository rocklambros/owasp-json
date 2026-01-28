"""Tests for OWASP JSON schema models."""

import json

from owasp_json.schema import OWASPDocument, RiskEntry


def test_risk_entry_creation():
    entry = RiskEntry(
        rank=1,
        identifier="LLM01:2025",
        title="Prompt Injection",
        description="Manipulating LLM via crafted inputs",
        impact="Unauthorized actions",
        mitigations=["Input validation", "Output filtering"],
    )
    assert entry.rank == 1
    assert entry.identifier == "LLM01:2025"
    assert len(entry.mitigations) == 2


def test_owasp_document_to_json():
    doc = OWASPDocument(
        title="OWASP Top 10 for LLM Applications",
        source_file="test.pdf",
        entries=[
            RiskEntry(
                rank=1,
                identifier="LLM01:2025",
                title="Prompt Injection",
            )
        ],
    )
    data = json.loads(doc.to_json())
    assert data["title"] == "OWASP Top 10 for LLM Applications"
    assert len(data["entries"]) == 1
    assert data["entries"][0]["rank"] == 1


def test_empty_document():
    doc = OWASPDocument(title="Test", source_file="test.pdf")
    assert doc.entries == []
