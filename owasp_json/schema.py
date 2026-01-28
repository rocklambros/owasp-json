"""Pydantic schemas for OWASP document structure."""

from pydantic import BaseModel, Field


class RiskEntry(BaseModel):
    """A single risk entry from an OWASP Top 10 document."""

    rank: int = Field(description="Risk ranking (1-10)")
    identifier: str = Field(description="Risk identifier, e.g. 'LLM01:2025'")
    title: str = Field(description="Risk title")
    description: str = Field(default="", description="Risk description")
    impact: str = Field(default="", description="Potential impact")
    mitigations: list[str] = Field(default_factory=list, description="Recommended mitigations")


class OWASPDocument(BaseModel):
    """Structured representation of an OWASP Top 10 document."""

    title: str = Field(description="Document title")
    source_file: str = Field(description="Original PDF filename")
    entries: list[RiskEntry] = Field(default_factory=list, description="Top 10 risk entries")

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON string."""
        return self.model_dump_json(indent=indent)
