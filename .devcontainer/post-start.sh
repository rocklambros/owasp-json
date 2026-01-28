#!/bin/bash

WORKER_ID=${ZERG_WORKER_ID:-0}
FEATURE=${ZERG_FEATURE:-unknown}
BRANCH=${ZERG_BRANCH:-main}

echo "═══════════════════════════════════════════════════"
echo "  ZERG Worker Starting"
echo "  Worker ID: $WORKER_ID"
echo "  Feature: $FEATURE"
echo "  Branch: $BRANCH"
echo "  Task List: $CLAUDE_CODE_TASK_LIST_ID"
echo "═══════════════════════════════════════════════════"

# Checkout the assigned branch
if [ "$BRANCH" != "main" ]; then
  git fetch origin 2>/dev/null || true
  git checkout "$BRANCH" 2>/dev/null || git checkout -b "$BRANCH"
fi

echo "Worker $WORKER_ID ready for tasks"
