# My Learning — Project Instructions

## Default Behavior
When the user pastes any of the following, **automatically apply the `/ascii-tree` workflow** without needing to be told:
- A YouTube URL (e.g., `https://www.youtube.com/watch?v=...`, `https://youtu.be/...`)
- A video transcript (timestamped or plain text)
- Any content that looks like lecture/video notes

**Do NOT ask for confirmation** — just fetch the transcript (if YouTube URL), build the ASCII tree, and save it.

## Folder Routing
Automatically place the file in the most relevant existing folder based on the content topic:

| Folder | Topics |
|---|---|
| `Agentic-development/` | AI agents, agentic workflows, agent frameworks |
| `BIA/` | Business intelligence, AutoGen, agent workshops |
| `Computers/` | General computing, hardware, operating systems |
| `Deep-learning/` | Neural networks, deep learning, training |
| `Fine-tuning/` | Model fine-tuning, LoRA, adapters |
| `LLM/` | Large language models, GPT, Claude, prompting |
| `Machine-learning/` | ML algorithms, classical ML, data science |
| `Management/` | Leadership, team management, business strategy |
| `Motivation/` | Motivational content, inspirational talks, mindset |
| `Python/` | Python programming, libraries, tools |
| `QuntumComputers/` | Quantum computing, qubits |
| `RAG/` | RAG, retrieval augmented generation, GraphRAG, vector databases, embeddings |
| `System-design/` | System architecture, distributed systems |
| `Vibe-coding/` | Vibe coding, AI-assisted development |
| `World-affairs/` | Geopolitics, global events, economics, food/energy crisis, trade |
| `ai-daily-updates/` | **Default fallback** — anything that doesn't clearly fit above |

### Routing Rules
1. Read the content first, determine the primary topic
2. Match to the most relevant folder from the table above
3. If the content spans multiple topics or doesn't clearly fit — use `ai-daily-updates/`
4. Always use the date-prefixed filename format from the ascii-tree workflow
