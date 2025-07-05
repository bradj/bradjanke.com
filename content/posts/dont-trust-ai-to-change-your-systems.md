---
title: "Don't Trust AI to Change Your Systems"
date: 2025-07-05T08:00:00-05:00
draft: false
tags: ["ai", "security"]
categories: []
---

AI coding assistants are powerful tools for understanding and analyzing codebases. The challenge is balancing their analytical capabilities with system safety.

## The Risk of Automatic Write Access

AI models hallucinate, make assumptions about business logic, and lack context about system dependencies. A single automated change can break production, corrupt data, or introduce security vulnerabilities.

**Common AI Mistakes:**

- Deleting files it thinks are unused
- Moving configuration files to "better" locations
- Modifying permissions without understanding security implications
- Creating directories that conflict with existing deployment scripts
- Copying files with incorrect ownership or permissions

## The Solution: Read-Only Access

Give AI comprehensive read access to gather information quickly. Require human approval for all modifications.

**Safe Commands to Automate:**

- `find` - Locate files and directories
- `ls` - List directory contents
- `cat` - Display file contents
- `head/tail` - Show file beginnings/endings
- `grep` - Search file contents
- `wc` - Count lines, words, characters
- `sort/uniq` - Organize and deduplicate data

**Commands Requiring Human Approval:**

- `rm` - Delete files and directories
- `mv` - Move or rename files
- `cp` - Copy files and directories
- `mkdir/rmdir` - Create or remove directories
- `chmod/chown/chgrp` - Modify permissions and ownership
- `ln` - Create links
- `mount` - Mount filesystems

## Why This Approach Works

**Faster Analysis:** AI can quickly traverse your entire codebase, read configuration files, and understand system architecture without waiting for human input.

**Maintained Control:** Every modification requires explicit human review and approval. You see exactly what changes before they happen.

**Reduced Risk:** Read-only operations cannot break your system, corrupt data, or introduce security vulnerabilities.

**Better Recommendations:** AI with comprehensive read access makes more informed suggestions because it can analyze the full context of your system.

## Implementation

Configure your AI tools with read-only file system permissions. Use containers or restricted user accounts that can read but not write. Set up approval workflows for any proposed changes.

The goal isn't to eliminate AI assistance – it's to harness AI's analytical capabilities while keeping humans in control of system modifications. AI can understand your codebase in seconds. It should still ask permission before changing it.
