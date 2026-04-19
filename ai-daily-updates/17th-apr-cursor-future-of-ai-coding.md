```
FUTURE OF AI CODING — CURSOR FOUNDER (AMAN)
│
├── Evolution of AI Coding (4 Eras)
│   ├── Era 1: No AI (2021-2022)
│   │   └── IntelliSense-only autocomplete
│   │
│   ├── Era 2: Tab Complete / Autocomplete
│   │   ├── Models predict next few minutes of edits
│   │   └── Cursor launched in this era
│   │
│   ├── Era 3: Synchronous Coding Agents (NOW)
│   │   ├── Natural language → full feature implementation
│   │   ├── Vast majority of Cursor code now from agents
│   │   ├── Agent requests surpassed tab accepts
│   │   └── Limitations
│   │       ├── Runs on local machine (resource hungry)
│   │       └── Can't scale to tens of agents locally
│   │
│   └── Era 4: Async Agents (EMERGING)
│       ├── Agents get their own cloud VMs
│       ├── Can test, iterate, use full desktop
│       ├── 30% of Cursor's merged PRs from cloud agents
│       └── Real examples
│           ├── Video rendering refactor (React → Rust, 25x faster, 8hrs)
│           └── 10,000-line network policy PR
│
├── Artifacts (New Review Paradigm)
│   ├── Problem: too much agent code to manually review
│   ├── Solution: review OUTPUTS, not just code
│   ├── Types
│   │   ├── Video artifacts (demo of working feature)
│   │   ├── Research reports (ML experiments)
│   │   └── Architecture diagrams, plans
│   ├── Like a manager reviewing engineer output
│   └── Iterate via reprompting without reading code
│
├── Multi-Agent Architecture
│   ├── Why Single Agent Fails
│   │   ├── Long runs = millions/tens of millions of tokens
│   │   ├── Outside RL training distribution
│   │   └── Agent loses track, goes off rails
│   │
│   ├── Solution: Planner → Sub-Planners → Workers
│   │   ├── Recursive decomposition
│   │   ├── Each subtask within training distribution
│   │   ├── Outer agent runs hundreds of thousands of tokens
│   │   └── Sub-agents handle leaf-level work
│   │
│   ├── Model Specialization
│   │   ├── OpenAI → best for planning & orchestration
│   │   ├── Gemini → best for computer use & multimodal
│   │   ├── Anthropic → best for UI & computer use
│   │   └── Faster models for simpler sub-tasks
│   │
│   └── Weaknesses
│       ├── Still hits limits at extreme task lengths
│       ├── Models not yet trained as great orchestrators
│       └── Model UX (artifact quality) needs improvement
│
├── Self-Driving Codebases (Future Vision)
│   ├── Self-Healing & Fixing
│   │   ├── Changes merged with NO human review
│   │   ├── Agent auto-fixes issues from tracker
│   │   ├── On-call: agent is primary, human is secondary
│   │   ├── Training run monitoring
│   │   │   ├── Agents check logs every few steps
│   │   │   └── Catch failures before silent degradation
│   │   └── Security: finds PR vulnerabilities pre-ship
│   │
│   ├── Full Project Generation
│   │   ├── Build entire products with minimal human input
│   │   ├── Browser experiment
│   │   │   ├── 1-week run, billions of tokens
│   │   │   ├── Tens of thousands of dollars compute
│   │   │   ├── Produced working (but rough) browser
│   │   │   └── Renders arbitrary HTML/CSS → pixels
│   │   └── Architecture: recursive planner → sub-planner → worker
│   │
│   ├── Off-Peak Improvement
│   │   ├── While you sleep, agents clean tech debt
│   │   ├── Simplify gnarly code
│   │   └── Use spare compute in off-hours
│   │
│   └── UX Challenges
│       ├── Currently requires detailed spec (like prompt engineering)
│       ├── Need intervention points during long runs
│       ├── Artifacts at maximum ambiguity points
│       └── Burden of spec quality will decrease over time
│
├── Cursor as "R&D Cloud"
│   ├── Old clouds = deliver products to users (COGS)
│   ├── Cursor = help enterprises BUILD more ambitious software
│   └── New kind of infrastructure
│
├── Role of the Engineer (Future)
│   ├── What stays valuable
│   │   ├── Taste (product & architecture)
│   │   ├── Deciding WHAT to build
│   │   ├── Holding entire codebase in your head
│   │   │   └── Broader but less detailed knowledge
│   │   └── Attention to detail (shifted to outputs)
│   │
│   ├── What changes
│   │   ├── Less low-level code writing
│   │   ├── More reviewing artifacts & outputs
│   │   └── Bottleneck = quality of ideas, not code
│   │
│   └── Cursor scaling engineers 3x this year
│       ├── Not cutting headcount despite AI productivity
│       └── Instead: tackling more ambitious projects
│
└── Q&A Highlights
    ├── Education needs to adapt to AI tools
    ├── Don't lose the battle to "slop"
    │   └── Taste matters in UX AND architecture
    ├── Code review will shift heavily to AI
    │   └── Humans prefer writing > reviewing
    ├── Enterprise: more software companies will emerge
    │   └── Bottleneck moves to idea quality
    └── Hiring: 2-day on-site with Cursor agents
        └── Scope of project keeps increasing as agents improve
```
