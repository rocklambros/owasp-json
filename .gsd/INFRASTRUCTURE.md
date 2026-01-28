# Infrastructure Requirements

## Project: owasp-json
## Generated: 2026-01-28

---

## Runtime Environment

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.12 | Primary runtime |
| uv | latest | Package manager |
| pdfplumber | 0.11+ | PDF text extraction |
| Pydantic | 2.0+ | JSON schema models |

---

## Services

No external services required. This is a standalone library.

---

## Claude Code Configuration

### MCP Servers
| Server | Purpose | Credentials |
|--------|---------|-------------|
| filesystem | File operations | None |

---

## Environment Variables

### Required
None.

### Optional
| Variable | Description | Default |
|----------|-------------|---------|
| LOG_LEVEL | Logging verbosity | info |

---

## Resource Requirements

| Resource | Per Worker | Total (3 workers) |
|----------|------------|-------------------|
| CPU | 1 core | 3 cores |
| Memory | 1 GB | 3 GB |
| Disk | 2 GB | 6 GB |
