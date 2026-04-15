---
description: Create an ASCII tree summary from video transcripts or content
---

# ASCII Tree Workflow

When the user says "ascii" or asks for an ASCII tree, follow these rules exactly:

## Format
- Use box-drawing characters: `├──`, `│`, `└──` for the tree structure
- Wrap the entire tree in a markdown code block (triple backticks)
- The root node is the TITLE in ALL CAPS at the top

## Content Rules
1. **Short labels** — each node should be 2-4 words max
2. **Expand as children** — details go as child nodes, never as long sentences
3. **No paragraphs** — break everything into individual tree nodes
4. **Multiple children allowed** — a node can have as many children as needed
5. **No timestamps** — unless the user explicitly asks for them
6. **Don't invent** — only include points explicitly mentioned in the source content. Do NOT add, interpret, or make up points that aren't there

## Bad Example (DON'T DO THIS)
```
├── Reliability Engineering
│   └── APIs fail — you need retry logic, timeouts, fallback paths, and circuit breakers
```
This is a paragraph crammed into one line. Break it up!

## Good Example (DO THIS)
```
├── Reliability Engineering
│   ├── APIs fail
│   ├── Services go down
│   ├── Networks time out
│   ├── Solutions
│   │   ├── Retry logic with backoff
│   │   ├── Timeouts
│   │   ├── Fallback paths
│   │   └── Circuit breakers
│   └── Backend engineers solved this decades ago
```
Short labels, details expanded as child nodes.

## Example Structure
```
TITLE IN ALL CAPS
│
├── Main Point 1
│   ├── Sub point A
│   ├── Sub point B
│   │   ├── Detail 1
│   │   └── Detail 2
│   └── Sub point C
│
└── Final Point
    ├── Sub point A
    └── Sub point B
```

## File Placement
- **Date prefix** — always start the filename with TODAY's date (the actual current date when creating the file) in format `DDth-mon-` (e.g., `3rd-mar-`, `21st-jun-`). Never hardcode a date — always check the current date.
- Use kebab-case for the rest of the filename (e.g., `15th-apr-offload-openclaw-to-local-models.md`)
- Default location: `/Users/macbookpro/Documents/my-learning/ai-daily-updates/`

## YouTube Transcript Fetching
If the user provides a YouTube URL without a transcript, auto-fetch it before building the tree:
```bash
/Users/macbookpro/Documents/my-learning/.venv/bin/python3 /Users/macbookpro/Documents/my-learning/fetch_transcript.py "<YOUTUBE_URL>"
```
- This fetches the full transcript as plain text
- Use the output as the source content for the ASCII tree
- If fetching fails, ask the user to paste the transcript manually

