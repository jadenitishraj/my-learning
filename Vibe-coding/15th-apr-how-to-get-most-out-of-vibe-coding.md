```
HOW TO GET THE MOST OUT OF VIBE CODING — YC STARTUP SCHOOL
│
├── Where to start
│   ├── Never coded before
│   │   ├── Replit or Lovable
│   │   ├── Easy visual interface
│   │   └── Struggles with backend logic changes
│   ├── Written code before (even rusty)
│   │   └── Windsurf, Cursor, or Claude Code
│   └── Product managers and designers
│       └── Going straight to code instead of Figma mockups
│
├── Start with a plan
│   ├── Don't dive in and write code first
│   ├── Write comprehensive plan with the LLM
│   ├── Put in markdown file inside project folder
│   ├── Go through it, delete what you don't like
│   ├── Mark features as "won't do" or "ideas for later"
│   ├── Implement section by section
│   │   ├── "Let's just do section 2 right now"
│   │   ├── Check it works, run tests
│   │   ├── Commit to Git
│   │   └── Mark section as complete
│   └── Don't expect models to one-shot entire products yet
│
├── Version control
│   ├── Use Git religiously
│   ├── Don't trust tool revert functionality yet
│   ├── Start with clean git slate before new feature
│   ├── git reset --hard if not working
│   ├── Bad results from prompting AI multiple times
│   │   └── Accumulates layers of bad code
│   └── Find solution → git reset → feed clean solution on clean codebase
│
├── Write tests
│   ├── LLMs pretty good at writing tests
│   ├── They default to low-level unit tests
│   ├── Prefer high-level integration tests
│   │   └── Simulate clicking through site/app end to end
│   ├── LLMs make unnecessary changes to unrelated logic
│   └── Test suites catch regressions early
│
├── TDD approach (from community)
│   ├── Start from test cases first
│   ├── Handcraft test cases, don't use LLMs for them
│   ├── Strong guardrails for LLM code generation
│   ├── LLM freely generates code
│   └── Green flags on tests = job done
│
├── Use multiple tools
│   ├── Load Cursor and Windsurf on same project
│   ├── Cursor is faster — frontend, full-stack linking
│   ├── Windsurf thinks longer — agents, prompts
│   ├── Run both at same time for different iterations
│   │   └── Pick which one you like better
│   └── If IDE stuck, paste code into LLM website UI
│
├── LLMs beyond coding
│   ├── DNS server configuration
│   ├── Heroku hosting setup via CLI
│   ├── DevOps engineer acceleration (10x)
│   ├── Favicon image generation (ChatGPT)
│   └── Image resizing script (Claude)
│
├── Bug fixes
│   ├── Copy paste error message straight into LLM
│   │   └── Often enough to identify and fix problem
│   ├── Complex bugs: ask LLM to think through 3-4 causes first
│   ├── After each failed attempt, reset and start again
│   │   └── Don't accumulate layers of crust
│   ├── Add logging — logging is your friend
│   ├── Switch models if stuck
│   │   ├── Claude Sonnet 3.7
│   │   ├── OpenAI models
│   │   └── Gemini
│   └── Find root cause → reset all changes → fix on clean codebase
│
├── Write instructions for LLM
│   ├── Cursor rules, Windsurf rules, Claude markdown file
│   ├── Founders writing hundreds of lines of instructions
│   └── Makes agents way more effective
│
├── Documentation
│   ├── Pointing agents at online docs still patchy
│   ├── MCP server for docs — overkill
│   ├── Download all docs, put in subdirectory
│   ├── Tell LLM "read docs before implementing"
│   └── Much more accurate
│
├── LLM as teacher
│   ├── Implement something, then ask AI to explain line by line
│   └── Better than scrolling Stack Overflow
│
├── Complex functionality
│   ├── Build as standalone project in clean codebase
│   ├── Get small reference implementation working
│   ├── Or download one from GitHub
│   ├── Point LLM at it, tell it to follow while reimplementing
│   └── Works surprisingly well
│
├── Architecture advice
│   ├── Small files, modularity
│   ├── Shift towards modular/service-based architecture
│   ├── Clear API boundaries for LLM to work within
│   ├── Consistent external interface
│   └── Huge monorepos with interdependencies hard for both humans and LLMs
│
├── Choosing tech stack
│   ├── Ruby on Rails — AI performs great
│   │   ├── 20-year-old framework
│   │   ├── Well-established conventions
│   │   └── Tons of consistent high-quality training data
│   └── Rust, Elixir — less training data, less success
│
├── Screenshots and voice
│   ├── Copy paste screenshots into coding agents
│   │   ├── Demonstrate UI bugs
│   │   └── Pull design inspiration from other sites
│   └── Voice input (Aqua by YC)
│       ├── Talk at computer, transcribes into tool
│       ├── 140 words/minute — double typing speed
│       └── AI tolerant of grammar/punctuation mistakes
│
├── Refactor frequently
│   ├── When code works and tests pass
│   ├── Refactor at will, tests catch regressions
│   ├── Ask LLM to identify repetitive parts
│   └── Keep files small and modular
│
├── Key mindset
│   ├── Think of AI as a different programming language
│   ├── Provide detailed context for good results
│   ├── Monitor if LLM falls into rabbit hole
│   ├── Take step back if copy-pasting errors repeatedly
│   └── Make LLM follow processes of good professional developer
│
└── Keep experimenting
    ├── State of the art changes week by week
    ├── Try every new model release
    ├── Gemini — best for codebase indexing and implementation plans
    ├── Sonnet 3.7 — leading for implementing code changes
    └── GPT 4.1 — too many questions, got implementation wrong
```
