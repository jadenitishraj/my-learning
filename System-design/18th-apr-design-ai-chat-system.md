```
SYSTEM DESIGN: AI CHAT PLATFORM (like ChatGPT)
│
├── 1. Requirements & Scale
│   ├── Scale
│   │   ├── 800M Weekly Active Users / 200M Daily Active Users
│   │   ├── 2.5B prompts per day
│   │   └── 20M concurrent connections at peak
│   ├── Functional
│   │   ├── Authentication & accounts
│   │   ├── Create, list, and delete conversations
│   │   ├── Stream AI responses (word-by-word)
│   │   └── Content moderation
│   └── Non-Functional
│       ├── 99.9% Availability
│       ├── < 2s latency for first token
│       └── Zero message loss (strict ordering)
│
├── 2. Data Estimations (Traffic is 90% Read / 10% Write)
│   ├── Why it's Read-Heavy
│   │   └── Before any write, system must read: user profile, tier/quota, rate limits, moderation rules, and chat history
│   ├── Storage
│   │   ├── ~7.5 KB stored per user daily (prompt + response)
│   │   ├── ~550 Terabytes annually for chat histories
│   │   └── Cold storage (Azure Blob) for old inactive chats
│   └── Bandwidth
│       └── ~6 GB/s sustained throughput during peak streaming
│
├── 3. System Architecture
│   ├── Client Layer: Web/Mobile App
│   ├── Edge Layer: CDN + Load Balancer
│   ├── API Gateway: Handles routing & SSL termination
│   └── Microservices
│       ├── Auth Service (User validation & JWT)
│       ├── Rate Limiter Service (Redis-backed quota tracking)
│       ├── Moderation Service (Safety checks)
│       ├── Conversation Service (CRUD for chat metadata & history)
│       └── Message Service (Core orchestrator for LLM streaming)
│
├── 4. Streaming Responses (SSE vs WebSockets)
│   ├── Option 1: WebSockets
│   │   ├── Bidirectional but complex
│   │   └── Overkill — keeps persistent unneeded connections open draining resources
│   ├── Option 2: Server-Sent Events (SSE) (★ Chosen Approach)
│   │   ├── Runs over standard HTTP
│   │   ├── One-way stream (Server → Client)
│   │   ├── Native browser support, auto-reconnections
│   │   └── Low overhead
│   └── Flow
│       └── User HTTP POST → Backend chunks LLM tokens → Streams via SSE → Client updates UI progressively
│
├── 5. Database Choice & Sharding Reality
│   ├── The Shocking Truth (OpenAI's approach)
│   │   ├── 800M users running on a SINGLE unsharded primary database
│   │   └── Massively scaled Read Replicas (~50 replicas) handle the 90% read load
│   ├── Option 1: Traditional PostgreSQL (★ Chosen Approach)
│   │   ├── Single primary for writes
│   │   ├── Auto-scaling read replicas
│   │   └── Strict ACID compliance (no lost messages, correct chronological order)
│   ├── Option 2: Serverless Postgres (Neon)
│   │   ├── Good for early stages (0 - 5M DAU)
│   │   └── Managed DB, instant branching, auto-scales compute
│   ├── Option 3: MongoDB
│   │   ├── Good for writes/flexible schemas
│   │   └── Eventual consistency creates out-of-order messages (dealbreaker for chat)
│   └── Option 4: Sharded PostgreSQL
│       ├── Highly complex application-layer routing
│       └── Rule of thumb: avoid until absolutely forced to (OpenAI hasn't yet)
│
└── 6. Rate Limiting Strategy
    ├── The Token Problem
    │   └── Small request payloads might require massive compute (high tokens)
    ├── Two-Tier Guardrails
    │   ├── Request Limits (Prevents API spam of tiny queries)
    │   └── Token Limits (Prevents large-payload compute abuse)
    └── Enforced via Tier
        ├── Free: Lower token/request caps
        └── Paid: Higher caps
```
