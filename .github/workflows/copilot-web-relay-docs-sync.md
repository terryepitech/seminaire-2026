---
description: Detect code changes under 2.copilotWebRelay/ and update documentation to keep specs aligned with source code
on:
  push:
    branches: [main]
    paths:
      - "2.copilotWebRelay/**"
      - "!2.copilotWebRelay/docs/**"
  workflow_dispatch:
permissions:
  contents: read
  pull-requests: read
  issues: read
tools:
  github:
safe-outputs:
  create-pull-request:
    title-prefix: "docs(copilotWebRelay): "
    labels: [documentation]
    draft: true
---

# Copilot Web Relay Documentation Sync

You are an AI agent responsible for keeping the documentation under `2.copilotWebRelay/docs/` aligned with the source code under `2.copilotWebRelay/`.

## Your Task

When code changes are pushed to `2.copilotWebRelay/`, analyze the current source code and update the documentation to reflect the actual implementation.

## Steps

1. **Read the source code** under `2.copilotWebRelay/`:
   - `backend/main.py` — FastAPI application entry point
   - `backend/cli_bridge.py` — Copilot CLI process management (PTY control)
   - `backend/websocket_handler.py` — WebSocket handler (message routing and status responses)
   - `backend/config.py` — Configuration management
   - `backend/requirements.txt` — Python dependencies
   - `frontend/src/App.tsx` — Main React application (terminal UI, WebSocket connection, session management)
   - `frontend/src/` — Other frontend TypeScript/React source files
   - `frontend/package.json` — Frontend dependencies
   - `frontend/vite.config.ts` — Vite configuration and WebSocket proxy
   - `e2e/` — Playwright E2E tests

2. **Read the existing documentation** under `2.copilotWebRelay/docs/` (if any exists).

3. **Read the planning document** for reference:
   - `2.copilotWebRelay/planning.md` — Architecture design and feature specifications

4. **Compare and identify discrepancies** between the documentation and the actual source code:
   - New endpoints or changed WebSocket message protocol
   - New or modified backend modules or classes
   - Changed frontend components or state management logic
   - New or updated configuration options
   - Dependency changes

5. **Update or create documentation files** under `2.copilotWebRelay/docs/`:
   - `2.copilotWebRelay/docs/architecture.md` — Current architecture overview (components, data flow, dependencies)
   - `2.copilotWebRelay/docs/api-reference.md` — WebSocket protocol reference (message types, request/response formats)
   - `2.copilotWebRelay/docs/backend.md` — Backend module documentation (FastAPI routes, CLI bridge, configuration)
   - `2.copilotWebRelay/docs/frontend.md` — Frontend module documentation (React components, WebSocket client, xterm.js integration)

6. **Create a pull request** with the documentation updates using `create-pull-request` safe output.
   - Title: `docs(copilotWebRelay): sync documentation with latest code changes`
   - Body should summarize what documentation was updated and why.

## Guidelines

- Write documentation in Japanese (日本語) to match the existing project documentation style.
- Be precise and factual — only document what the code actually does, not what it should do.
- Include code examples and message format examples where helpful.
- If there are no discrepancies and documentation is up to date, use `noop` to signal no changes needed.
- Do NOT modify any source code — only update documentation files.
- Keep documentation concise and well-structured with clear headings.
