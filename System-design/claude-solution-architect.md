# CLAUDE CERTIFIED ARCHITECT — FOUNDATIONS (ASCII Tree)

Claude Certified Architect — Foundations
│
├── [0] EXAM META
│ ├── Target: Solution architect, 6+ months hands-on
│ ├── Format: MCQ (1 of 4), 100–1000 scale, pass = 720
│ ├── No guessing penalty → answer every question
│ ├── 4 of 6 scenarios randomly selected
│ └── Scenarios
│ ├── S1: Customer Support Agent (returns, billing, escalation, 80% FCR)
│ ├── S2: Code Generation with Claude Code
│ ├── S3: Multi-Agent Research System (coordinator + subagents)
│ ├── S4: Developer Productivity Tools
│ ├── S5: Claude Code in CI/CD
│ └── S6: Structured Data Extraction
│
├── [D1] AGENT ARCHITECTURE & ORCHESTRATION (27%)
│ ├── Agentic Loop
│ │ ├── Lifecycle: send → stop_reason → tool_use/end_turn → repeat
│ │ ├── Model-driven (NOT hard-coded decision trees)
│ │ ├── Append tool results to history each iteration
│ │ └── Anti-patterns
│ │ ├── Parsing assistant text for "done"
│ │ ├── Arbitrary max_iterations as primary stop
│ │ └── Using presence of text as completion signal
│ │
│ ├── AgentDefinition (Agent SDK)
│ │ ├── name / description / system_prompt
│ │ ├── allowed_tools (least privilege)
│ │ └── Coordinator MUST include "Task" in allowed_tools
│ │
│ ├── Hub-and-Spoke (Coordinator ↔ Subagents)
│ │ ├── Coordinator: decompose, delegate, aggregate, recover
│ │ ├── Subagents have ISOLATED context
│ │ ├── Context passed EXPLICITLY in subagent prompt
│ │ └── All communication routes through coordinator
│ │
│ ├── Task Tool & Parallel Spawning
│ │ ├── Multiple Task calls in one coordinator turn → parallel
│ │ └── Explicit context passing is mandatory
│ │
│ ├── Hooks (Deterministic)
│ │ ├── PostToolUse → normalize tool results (e.g. Unix → ISO 8601)
│ │ ├── PreToolUse → block policy violations (e.g. refund > $500)
│   │   └── Hooks (100%) vs Prompts (>90%)
│   │       └── RULE: financial/legal/safety → hooks, not prompts
│   │
│   ├── Task Decomposition
│   │   ├── Fixed pipelines (prompt chaining) → predictable tasks
│   │   ├── Dynamic/adaptive → open-ended investigations
│   │   └── Multi-pass review (per-file + integration pass)
│   │
│   └── Session Management
│       ├── --resume <name> → continue named session
│       ├── fork_session → branch from shared context
│       └── Start new session when tool results are stale
│
├── [D2] TOOL DESIGN & MCP INTEGRATION (18%)
│   ├── Tool Descriptions (primary selection mechanism)
│   │   ├── Include: what, returns, input formats, edge cases, when-vs-alternatives
│   │   ├── Avoid overlapping descriptions
│   │   └── Built-in tools may dominate MCP → strengthen MCP descriptions
│   │
│   ├── tool_choice Parameter
│   │   ├── "auto" → model decides (default)
│   │   ├── "any" → must call some tool (guaranteed structured)
│   │   └── {"type":"tool","name":"X"} → force specific tool
│   │
│   ├── JSON Schemas (tool_use)
│   │   ├── Eliminates SYNTAX errors only
│   │   ├── Semantic errors still possible
│   │   ├── required vs nullable fields
│   │   ├── enums with "other" + detail
│   │   └── "unclear" enum for low-confidence cases
│   │
│   ├── Model Context Protocol (MCP)
│   │   ├── Three primitives: Tools, Resources, Prompts
│   │   ├── Server configs
│   │   │   ├── Project: .mcp.json (VCS, team)
│   │   │   └── User: ~/.claude.json (personal, experimental)
│   │   ├── Env-var substitution for secrets (${GITHUB_TOKEN})
│ │ └── Prefer community servers for standard integrations
│ │
│ ├── MCP Error Responses
│ │ ├── isError: true flag
│ │ ├── Structured: errorCategory, isRetryable, message, partial_results
│ │ └── Generic "Operation failed" = anti-pattern
│ │
│ └── Built-in Tools (Claude Code)
│ ├── Glob → filename patterns
│ ├── Grep → content search
│ ├── Read / Write / Edit / Bash
│ └── Fallback: Read + Write when Edit match non-unique
│
├── [D3] CLAUDE CODE CONFIGURATION & WORKFLOWS (20%)
│ ├── CLAUDE.md Hierarchy
│ │ ├── User: ~/.claude/CLAUDE.md (not in VCS)
│ │ ├── Project: .claude/CLAUDE.md or root CLAUDE.md (VCS)
│ │ └── Directory: CLAUDE.md in subdirs
│ │ └── Common bug: team-wide rules placed in user-level
│ │
│ ├── @path Imports
│ │ ├── Modularizes CLAUDE.md
│ │ ├── Relative paths resolved from importing file
│ │ └── Max nesting depth: 5
│ │
│ ├── .claude/rules/ (path-conditional)
│ │ ├── YAML frontmatter: paths: ["src/api/**/*"]
│ │ ├── Loads only when editing matching files
│ │ └── Better than dir-level CLAUDE.md for cross-cutting patterns
│ │
│ ├── Slash Commands & Skills
│ │ ├── .claude/commands/ (legacy, supported)
│ │ ├── .claude/skills/name/SKILL.md (current)
│ │ ├── Project (VCS) vs User (~/.claude/...)
│ │ └── Frontmatter
│ │ ├── context: fork → isolated subagent
│ │ ├── allowed-tools: [...]
│ │ └── argument-hint: "..."
│ │
│ ├── Planning Mode vs Direct Execution
│ │ ├── Planning → large changes, multi-approach, unfamiliar codebase
│ │ ├── Direct → single-file, clear stack trace
│ │ ├── Combined → plan first, approve, then execute
│ │ └── Explore subagent → isolates verbose discovery
│ │
│ ├── Built-in Commands
│ │ ├── /compact → summarize history (risks losing numbers/dates)
│ │ └── /memory → edit CLAUDE.md across sessions
│ │
│ └── CLI for CI/CD
│ ├── -p / --print → non-interactive (REQUIRED for CI)
│ ├── --output-format json + --json-schema → structured output
│ ├── Session isolation: independent instance for review
│ └── Re-review: include prior findings, report only new/unresolved
│
├── [D4] PROMPT ENGINEERING & STRUCTURED OUTPUT (20%)
│ ├── Few-shot Prompting
│ │ ├── 2–4 examples for ambiguous scenarios
│ │ ├── Demonstrate output format unambiguously
│ │ ├── Distinguish acceptable vs problematic patterns
│ │ └── Most effective for non-standard extraction (informal units)
│ │
│ ├── Explicit Criteria > Vague Instructions
│ │ ├── "flag only when comment contradicts code"
│ │ ├── Severity definitions with code examples
│ │ └── Explicit "do not flag" lists
│ │
│ ├── Prompt Chaining
│ │ ├── Per-file passes → prevents attention dilution
│ │ ├── Integration pass for cross-file issues
│ │ └── Use for predictable, repeatable tasks
│ │
│ ├── Interview Pattern
│ │ ├── Agent asks clarifying questions pre-implementation
│ │ └── For unfamiliar domains, multiple valid approaches
│ │
│ ├── Validation & Retry-with-Feedback
│ │ ├── Retry prompt: original doc + incorrect extraction + specific error
│ │ ├── Pydantic: structural + semantic validation
│ │ ├── JSON Schema generated from Pydantic models
│ │ └── Won't help if info is absent from source
│ │
│ ├── Self-correction
│ │ └── Extract both stated_total and calculated_total → detect conflict
│ │
│ ├── Message Batches API
│ │ ├── 50% savings, up to 24hr window
│ │ ├── NO multi-turn tool calling
│ │ ├── custom_id for correlation
│ │ ├── Use: overnight reports, audits, bulk extraction
│ │ └── Don't use: blocking checks, interactive review
│ │
│ └── Multi-instance / Multi-pass Review
│ ├── Self-review limitation: model retains reasoning bias
│ ├── Independent instance for review (no generation context)
│ └── Multi-pass: per-file + integration
│
├── [D5] CONTEXT MANAGEMENT & RELIABILITY (15%)
│ ├── Context Window Issues
│ │ ├── Lost-in-the-middle → place key info at start/end
│ │ ├── Tool result accumulation → trim via hooks
│ │ └── Progressive summarization loses numbers/dates
│ │
│ ├── Preservation Techniques
│ │ ├── Case-facts block (outside summarization)
│ │ ├── Scratchpad files for long investigations
│ │ ├── Position-aware input (key findings first)
│ │ └── Structured state persistence (crash recovery)
│ │
│ ├── Escalation Patterns
│ │ ├── Triggers
│ │ │ ├── Explicit request for human → immediate
│ │ │ ├── Policy gap (e.g., competitor price match)
│ │ │ ├── Cannot make progress after attempts
│ │ │ ├── Financial threshold (enforce via hook)
│ │ │ └── Multiple customer matches → ask for identifier
│ │ ├── Unreliable triggers
│ │ │ ├── Sentiment analysis
│ │ │ ├── Self-rated confidence (1–10)
│ │ │ └── Ad-hoc classifiers
│ │ ├── Nuanced pattern: acknowledge → resolve → escalate on reiteration
│ │ └── Structured handoff protocol (self-contained summary)
│ │
│ ├── Error Handling (Multi-agent)
│ │ ├── Categories: transient / validation / business / permission
│ │ ├── Structured subagent error (type, query, partial, alternatives)
│ │ ├── Local recovery in subagent → propagate only what can't resolve
│ │ └── Coverage annotations in synthesis (FULL / PARTIAL / gap)
│ │
│ ├── Provenance Preservation
│ │ ├── Claim → source mapping (URL, name, date, quote)
│ │ ├── Conflicting data: preserve both with attribution
│ │ ├── Include publication dates (avoid false contradictions)
│ │ └── Render by type: tables / prose / lists / time-series
│ │
│ └── Confidence Calibration
│ ├── Field-level confidence scores
│ ├── Calibration on labeled sets
│ ├── Stratified random sampling (even high-confidence)
│ └── Analyze by document type + field (not just overall)
│
├── [API] CLAUDE API CORE
│ ├── Request fields: model, max_tokens, system, messages, tools, tool_choice
│ ├── Roles: user / assistant / tool_result
│ ├── MUST send full history each request (stateless)
│ └── stop_reason
│ ├── end_turn → show result
│ ├── tool_use → execute + continue
│ ├── max_tokens → truncated
│ └── stop_sequence → app-specific
│
├── [OUT-OF-SCOPE]
│ ├── Fine-tuning / custom training
│ ├── API auth, billing, account mgmt
│ ├── Language/framework implementation specifics
│ ├── MCP server hosting/deployment
│ ├── Internal architecture, RLHF, Constitutional AI
│ ├── Vector DB implementation
│ ├── Computer use, Vision, Streaming
│ ├── Rate limits, pricing math, token counting
│ ├── OAuth, key rotation
│ ├── Cloud-specific configs (AWS/GCP/Azure)
│ └── Benchmarks, caching internals
│
└── [PREP CHECKLIST]
├── Build SDK agent (loop + tools + hooks + subagents)
├── Configure Claude Code (hierarchy + rules + skills + MCP)
├── Design MCP tools with structured errors
├── Extraction pipeline (schemas + retry + batches)
├── Few-shot + explicit criteria + multi-pass review
├── Context patterns (scratchpad, fact-blocks, subagent delegation)
├── Escalation rules + human-in-loop workflows
└── Take practice exam before real one

# KEY DECISION RULES (CHEAT SHEET)

Deterministic guarantee needed? → Hook (not prompt)
Vague vs precise output? → Few-shot examples
Similar tools misrouting? → Fix descriptions FIRST
CI/CD pipeline hanging? → Add -p flag
Large architectural change? → Planning mode
Tests scattered across codebase? → .claude/rules/ with paths
Team-wide command? → .claude/commands/ (VCS)
Personal variant? → ~/.claude/skills/ (same name)
Multiple customer matches? → Ask for identifier, don't guess
Conflicting source data? → Preserve both with attribution
Blocking pre-merge check? → Sync API
Overnight audit? → Batch API (50% savings)
Self-review missing bugs? → Independent Claude instance
14-file PR review inconsistent? → Per-file + integration passes
Context degrading in long session? → Scratchpad + subagent delegation
Need structured JSON output? → tool_use + JSON schema
Ambiguous category in extraction? → enum with "unclear" / "other"
Business rule > $threshold? → PreToolUse hook blocks it
Subagent timeout? → Structured error + partial results
History losing numbers/dates? → Case-facts block outside summary
