```
AUTOGEN MULTI-AGENT FRAMEWORK — BIA WORKSHOP
│
├── 1. AutoGen Introduction
│   ├── What is AutoGen
│   │   ├── Open-source, Microsoft Research
│   │   ├── Multi-agent framework
│   │   ├── Chat-based orchestration
│   │   │   └── Not fixed workflow graphs
│   │   └── Conversation as orchestration
│   │       ├── Workflows = dialogues between agents
│   │       ├── Agents + humans + tools exchange messages
│   │       ├── Ask questions, invoke functions/code
│   │       └── Dynamic problem-solving via natural language
│   ├── Agents with roles
│   │   ├── Specific roles and capabilities
│   │   │   └── e.g. Coder, Reviewer
│   │   ├── Backed by LLM (e.g. GPT-4)
│   │   ├── Optional tools / knowledge base
│   │   ├── Prompt = persona + goals
│   │   └── Conversation emerges autonomously
│   ├── AI Personas in dialogue
│   │   ├── Group brainstorming metaphor
│   │   ├── Nudge behavior via prompts
│   │   └── Abstractions
│   │       ├── AssistantAgent
│   │       └── UserProxyAgent
│   └── Agent structure
│       ├── Name
│       ├── Description
│       ├── Model
│       ├── System Message
│       └── Tools (optional)
│
├── 2. Why Use AutoGen
│
├── 3. Tools & Function Calling
│   ├── Built-in tools
│   │   ├── PythonCodeExecutionTool → run Python
│   │   ├── HttpTool → web/API calls
│   │   └── LangChainToolAdapter → LangChain integration
│   ├── Function calling mechanism
│   │   ├── OpenAI-style function calling
│   │   ├── LLM generates JSON function calls
│   │   ├── AutoGen intercepts and executes
│   │   └── Returns results to the agent
│   ├── Custom tools (FunctionTool)
│   │   ├── Wrap any Python function as callable tool
│   │   ├── Type annotations + descriptions
│   │   └── e.g. get_stock_price(company, date)
│   └── Code as a tool
│       ├── Agents output Python code blocks
│       ├── Detected and executed via UserProxyAgent
│       ├── Results injected back into chat
│       └── On-the-fly solving (math, data tasks)
│
├── 4. Memory & Persistence
│   ├── State persistence
│   │   ├── save_state() / load_state()
│   │   ├── Serialized as JSON-compatible dict
│   │   ├── Resume chats across sessions
│   │   └── Crucial for multi-session chats
│   ├── Long-term memory (external stores)
│   │   ├── Default: full history in-memory
│   │   │   └── Until LLM token limit hit
│   │   ├── Integrates with Mem0
│   │   └── Mem0Memory capabilities
│   │       ├── Log all interactions
│   │       ├── Retrieve past conversations
│   │       └── Recall preferences, names, past issues
│   ├── Vector stores & RAG
│   │   ├── Store knowledge as vectors
│   │   ├── Query relevant info when needed
│   │   ├── ChromaDB integration
│   │   └── Expand knowledge beyond current conversation
│   └── Memory management
│       ├── Trimming, summarizing, compressing old messages
│       ├── LLMLingua for text compression
│       ├── MemGPT for hierarchical memory
│       └── Default: full chat history until token limit
│
├── 5. Human-in-the-Loop
│   ├── UserProxyAgent
│   │   ├── Bridge between AI agents and human
│   │   ├── Pauses for input
│   │   └── Direct human participation
│   ├── Automatic code execution
│   │   ├── Detects Python code blocks
│   │   ├── Executes automatically
│   │   ├── Returns results to conversation
│   │   └── Manual or auto-triggered
│   ├── Live human feedback (human_input_mode)
│   │   ├── ALWAYS → ask every turn
│   │   ├── NEVER → fully autonomous
│   │   └── TERMINATE (default) → only at critical steps
│   ├── Intervention and approval
│   │   ├── InterventionHandler
│   │   ├── Custom logic / pauses at events
│   │   ├── e.g. "Allow this action?"
│   │   └── Active ↔ passive ↔ hands-off
│   └── Collaborative dialogues
│       ├── Human feedback → conversation memory
│       ├── Agents adapt to corrections in real time
│       └── Humans act as co-agents
│
├── 6. Conversation & State Management
│   ├── Teams & group chats
│   │   ├── Organize via Teams (e.g. RoundRobinGroupChat)
│   │   ├── AutoGen routes messages automatically
│   │   └── Round-Robin mode
│   │       ├── Agents take turns: A → B → C → A...
│   │       └── No manual message passing
│   ├── Orchestration patterns
│   │   ├── Sequential → pipeline fashion
│   │   ├── Concurrent → parallel agents, same message
│   │   ├── Group chat → shared thread, turn-taking
│   │   ├── Handoff → generalist → expert delegation
│   │   ├── Debate & reflection → challenge/verify answers
│   │   └── Patterns mixable via team classes + agent configs
│   ├── Message routing (pub-sub)
│   │   ├── Agents subscribe to topics/message types
│   │   ├── Decoupled communication
│   │   └── e.g. multiple agents handle same input in parallel
│   ├── State management & termination
│   │   ├── Termination conditions
│   │   │   ├── Max turns / MaxMessageTermination
│   │   │   └── Output contains "DONE"
│   │   ├── Prevents infinite loops
│   │   └── Conversation state checked each turn
│   └── Dynamic emergent flow
│       ├── Driven by agent prompts + message content
│       ├── Not hardcoded steps
│       ├── Agents decide when/how to interact
│       │   └── e.g. handoffs, verifications
│       ├── Adaptive workflows based on real-time context
│       └── Requires careful prompt design
│
├── 7. Agent Teams
│   ├── Multi-agent collaboration
│   │   ├── Specialized agent teams
│   │   │   └── e.g. Developer + Reviewer (AI software team)
│   │   ├── Collaborate via chat, iterate to solve
│   │   └── Share information via conversation
│   ├── Agent types & roles
│   │   ├── AssistantAgent → autonomous LLM-powered
│   │   ├── UserProxyAgent → human input / code executor
│   │   └── Custom agents
│   │       └── e.g. MathAgent, KnowledgeBaseAgent
│   ├── Many-to-many communication
│   │   ├── Multiple agents in same conversation
│   │   ├── AI group chat
│   │   ├── e.g. Questioner + multiple Experts
│   │   └── Subscribe to shared messages, aggregate insights
│   ├── Coordination & termination
│   │   ├── Prompt-based instructions
│   │   │   └── e.g. "ask Agent X if unsure"
│   │   ├── Termination conditions
│   │   │   ├── Max message count
│   │   │   ├── Specific output ("DONE")
│   │   │   └── Task success (no code errors)
│   │   └── Optional moderator agent
│   └── Emergent reasoning
│       ├── Collective intelligence
│       ├── Agents ask, verify, correct, collaborate
│       ├── Focus on writing good prompts
│       ├── Conversations evolve dynamically
│       └── Prompt design + guardrails = stable behavior
│
└── 8. Hands-on Coding
```
