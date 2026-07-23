# Architecture

## Overview

The solution separates reasoning from execution. An AI desktop client owns the conversation and model interaction, while a local MCP server exposes narrow tools that perform document operations.

```text
User request
    |
    v
AI desktop client
    |-- model inference
    |-- reasoning loop
    |-- tool selection
    v
MCP transport: stdio
    v
Local Python MCP server
    |-- document catalog adapter
    |-- metadata normalization and search
    |-- PDF download policy
    |-- optional SMTP notification
    v
Public sources, local filesystem and SMTP provider
```

## Responsibilities

### AI desktop client

- Presents the conversational interface.
- Selects and hosts the language model.
- Decides when to invoke MCP tools.
- Converts tool results into a user-facing response.

### MCP server

- Registers tools with explicit input contracts.
- Validates tool arguments.
- Calls local adapters and external services.
- Returns structured results to the client.
- Does not decide independently which tool to execute.

### Document catalog adapter

- Opens the configured public source.
- Extracts document identifiers, dates, subjects and download links.
- Normalizes metadata into a consistent record structure.
- Maintains a short-lived in-memory cache to reduce repeated browsing.

### Download policy

- Parses the requested URL.
- Checks the scheme and allowed domain.
- Enforces the expected PDF extension.
- Sanitizes the local filename.
- Avoids unnecessary duplicate downloads.

### Notification adapter

- Reads SMTP settings from the process environment.
- Validates required configuration.
- Sends a plain-text notification when explicitly invoked by the client.

## Trust boundaries

The most important boundary is between the untrusted tool input produced through the conversation and local side effects. Search is read-only, while downloads and email notifications create external or local effects and therefore require stricter validation.

## Deployment model

The original implementation runs locally on Windows and communicates with the client through standard input/output. A packaged executable is possible, but this public repository does not include private binaries or browser runtimes.
