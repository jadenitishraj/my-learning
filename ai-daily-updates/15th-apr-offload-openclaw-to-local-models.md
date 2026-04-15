```
OFFLOAD OPENCLAW TO LOCAL MODELS — SAVE COSTS WITH NVIDIA RTX & DGX SPARK
│
├── The problem
│   ├── OpenClaw is expensive
│   ├── People spend $10,000+/month
│   └── Processing everything in cloud costs a lot
│
├── The solution
│   ├── Offload to open-source models locally
│   ├── Use Nvidia RTX GPUs or DGX Spark
│   └── Even old gaming laptops and desktops work
│
├── Why local models
│   ├── Cut costs
│   ├── Increase security
│   ├── Increase privacy
│   ├── More personalized
│   └── 90% of use cases don't need frontier models
│
├── Hardware
│   ├── Any Nvidia RTX hardware
│   │   ├── 30 series
│   │   ├── 40 series
│   │   └── 5090
│   ├── DGX Spark
│   │   └── 128 gigs unified memory
│   └── Trade-off is model size
│       ├── More VRAM = bigger models
│       └── Less VRAM = simpler use cases only
│
├── Hybrid architecture
│   ├── Cloud models (frontier)
│   │   ├── Opus 46
│   │   ├── GPT 5.4
│   │   ├── Too large to host locally
│   │   └── No open weights available
│   ├── Local models
│   │   ├── Quen
│   │   ├── Llama
│   │   ├── GLM
│   │   ├── Neotron
│   │   └── Gemma 4
│   └── LM Studio
│       ├── Simplest to use
│       ├── Has its own interface
│       └── Determines which model fits your machine
│
├── When to use frontier models
│   ├── Coding
│   ├── Complex planning
│   └── Orchestration
│
├── When to use local models
│   ├── Embeddings
│   ├── Transcriptions
│   ├── Voice generation
│   ├── PDF extraction
│   ├── Classification
│   ├── Chat
│   └── Summarization
│
├── Process to transition
│   ├── Step 1 — Experiment
│   │   ├── Use frontier models only
│   │   ├── Test different workflows
│   │   └── Make sure integrations work
│   ├── Step 2 — Productionize
│   │   ├── Still using frontier model
│   │   ├── Start identifying parts to offload
│   │   └── Like writing down processes to train new guy
│   └── Step 3 — Scale
│       ├── Transition to local models
│       ├── Find repeatable use cases
│       └── Test on real production data
│
├── Architecture setup
│   ├── OpenClaw on MacBook
│   ├── SSH into RTX/Spark machines
│   │   ├── They act as external GPUs
│   │   ├── Need username, password, IP address
│   │   └── OpenClaw can find machines on local network
│   └── Single machine setup also works
│       └── Phone via Telegram → OpenClaw → local GPU
│
├── Model sizing
│   ├── 30B parameter range is perfect
│   │   ├── Balance of size and quality
│   │   └── Fits on consumer-grade GPUs
│   ├── Neotron 3 Super 12B on Spark
│   ├── Quen 3.5 122B on Spark
│   └── Different quantizations available
│
├── Real use cases offloaded
│   ├── Notification classifier
│   ├── Company news relevance
│   ├── CRM context extraction
│   ├── Knowledge base article ingestion
│   │   ├── Was $12-$20/month with Sonnet
│   │   └── Now free with Quen locally
│   └── CRM queries
│       ├── Email and transcript summaries
│       ├── Was $12-$20/month
│       └── Now free, data stays local
│
├── Quen 3.5 on Spark
│   ├── 35B parameters, 3B active
│   ├── 65 tokens per second
│   ├── 256K context window
│   ├── Thinking model
│   ├── Vision model
│   └── 1000-word story almost instant vs 5-8 sec on Sonnet
│
├── Cost comparison
│   ├── Fully hosted: $300/month
│   └── Local: ~$3/month electricity
│
├── Nvidia ecosystem
│   ├── Neotron v3 open-source model
│   ├── Neoclaw — enterprise OpenClaw
│   └── Building hardware + software + models
│
└── Bottom line
    ├── Future is hybrid
    ├── Complex use cases → cloud
    ├── Everything else → local
    └── After 10B tokens: offload to local as often as you can
```
