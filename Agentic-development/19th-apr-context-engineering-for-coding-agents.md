```
CONTEXT ENGINEERING FOR CODING AGENTS
│
├── The Problem
│   ├── Too much slop
│   ├── Codebase churn
│   ├── Brownfield codebases fail
│   └── AI rework required
├── Strategy
│   ├── Intentional compaction
│   ├── Manage context window
│   └── Avoid dumb zone
├── Context Window Optimization
│   ├── Models are stateless
│   ├── Better tokens in
│   ├── Better tokens out
│   ├── Optimize for correctness
│   ├── Optimize for completeness
│   ├── Optimize for size
│   └── Optimize for trajectory
├── The Dumb Zone
│   ├── Past 40 percent line
│   ├── Diminishing returns
│   ├── Too many MCPs
│   └── Suboptimal outcomes
├── Sub Agents
│   ├── Control context
│   ├── Prevent anthropomorphizing
│   ├── Read large codebases
│   ├── Find things
│   └── Return succinct message
├── RPI Workflow
│   ├── Research
│   │   ├── Understand system
│   │   ├── Find files
│   │   └── Stay objective
│   ├── Plan
│   │   ├── Compression of intent
│   │   ├── Outline steps
│   │   ├── Include code snippets
│   │   └── Mental alignment
│   └── Implement
│       ├── Execute plan
│       ├── Keep context low
│       └── Test after changes
└── Keys to Success
    ├── Do not outsource thinking
    ├── Always read plans
    ├── Keep human in loop
    ├── Pick one tool
    └── Get more reps
```

This is a mental model for working effectively with AI coding agents (Claude Code, Cursor, etc.), sir. Here's the gist:

**Core idea:** LLMs are stateless — they only know what's in the context window right now. So the skill isn't "prompting" anymore, it's _context engineering_ — deciding what tokens go in so you get good tokens out.

**The Dumb Zone:** Past roughly 40% of the context window, model quality degrades. More tokens ≠ better answers. Stuffing 10 MCP servers, huge file dumps, and long chat history makes the agent dumber, not smarter. "Intentional compaction" = deliberately keeping context lean.

**Sub-agents:** Instead of loading a 50-file codebase into your main agent, spawn a sub-agent to go read it and return a one-paragraph summary. The sub-agent burns its own context; your main agent stays sharp. Treat them as _tools_, not coworkers — don't anthropomorphize.

**RPI Workflow** (the practical loop):

- **Research** — sub-agent explores the code, finds relevant files, reports back
- **Plan** — write a concrete plan (steps + code snippets) _before_ touching code. This is "compression of intent" — aligning you and the agent on what's about to happen
- **Implement** — execute the plan with minimal context, test after each change

**Keys to success:**

- Don't outsource _thinking_ — outsource typing. You still drive.
- Always read the plan before letting it code.
- Pick one tool and get reps in, rather than tool-hopping.

The whole philosophy maps well to your "No Agents, Just Tools" stance, sir — it's the same instinct: fewer abstractions, tighter control over what the LLM sees, let the model do what it's good at without drowning it.
