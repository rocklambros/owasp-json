#!/bin/bash
set -e

echo "═══════════════════════════════════════════════════"
echo "  ZERG Worker Post-Create Setup"
echo "═══════════════════════════════════════════════════"

# Install Python dependencies with uv
if [ -f "pyproject.toml" ]; then
  echo "Installing Python project with uv..."
  uv pip install -e ".[dev]"
fi

# Copy MCP server configuration
if [ -f ".devcontainer/mcp-servers/config.json" ]; then
  cp .devcontainer/mcp-servers/config.json /root/.claude/mcp_servers.json
fi

# Setup git identity for commits
git config --global user.email "factory-worker@agentic.local"
git config --global user.name "ZERG Worker ${ZERG_WORKER_ID:-0}"

echo "Post-create setup complete"
