```
AWS CERTIFIED GENERATIVE AI DEVELOPER PROFESSIONAL (AIP-C01)
│
├── 1. EXAM PRE-REQUISITES & TARGET CANDIDATE
│   ├── Target Candidate Profile
│   │   ├── 2+ years experience with AWS and ML/AI
│   │   ├── 1+ year of hands-on experience implementing GenAI solutions
│   │   └── AWS basics required (storage, security, etc.)
│   └── Not Required:
│       ├── Model development and training from scratch
│       ├── Advanced Machine Learning mathematics
│       └── Feature Engineering / Data Engineering at scale
│
├── 2. GENERATIVE AI FUNDAMENTALS & BEDROCK
│   ├── Foundation Models (FMs)
│   │   ├── Definition: Giant, pre-trained transformer models
│   │   ├── Third-Party Examples: GPT-n (OpenAI), Claude (Anthropic), DALL-E, LLaMa, DeepSeek
│   │   └── AWS Foundation Models (Base Models)
│   │       ├── Jurassic-2 (AI21labs): Multilingual LLMs (Spanish, French, German, etc.)
│   │       ├── Claude (Anthropic): Conversations, Q&A, workflow automation
│   │       ├── Stable Diffusion (stability.ai): Image, art, logo generation
│   │       ├── Llama (Meta): Text generation, LLM tasks
│   │       ├── Amazon Titan: Summarization, Embeddings, Personalization
│   │       ├── Amazon Nova Pro: LLM portfolio
│   │       └── Amazon Nova Reels: Video generation
│   │
│   ├── Amazon Bedrock API Endpoints
│   │   ├── bedrock: Manage, deploy, train models
│   │   ├── bedrock-runtime: Perform inference (InvokeModel, Converse)
│   │   ├── bedrock-agent: Manage, deploy, train LLM agents and knowledge bases
│   │   └── bedrock-agent-runtime: Perform inference against agents (RetrieveAndGenerate)
│   │
│   ├── The Converse API
│   │   ├── Unified API for models that support messages
│   │   ├── Key JSON payload fields:
│   │   │   ├── messages (array of roles and content)
│   │   │   ├── system (system prompts)
│   │   │   ├── inferenceConfig (maxTokens, temperature, stopSequences, topP)
│   │   │   ├── guardrailConfig (identifier, version, trace)
│   │   │   ├── toolConfig (tools array, toolChoice)
│   │   │   ├── outputConfig (enforcing structured JSON outputs)
│   │   │   └── promptVariables (placeholders for prompts)
│   │   └── Requires IAM Permissions: AmazonBedrockFullAccess / ReadOnly
│   │
│   ├── Fine-Tuning & Model Customization
│   │   ├── Fine-Tuning (Custom Models)
│   │   │   ├── Uses labeled training pairs ({"prompt":"...", "completion":"..."})
│   │   │   ├── Uploaded via S3, runs in VPC using PrivateLink
│   │   │   └── Supported by Titan, Cohere, Meta
│   │   ├── Continued Pre-Training
│   │   │   ├── Uses unlabeled data (unstructured text like documents)
│   │   │   └── Familiarizes model with company vocabulary without prompts
│   │   └── Low-Rank Adaptation (LoRA)
│   │       ├── Highly efficient storage/training mechanism
│   │       ├── Adds "low-rank matrices" to the attention weights
│   │       └── Base model remains unchanged; weights added at inference
│   │
│   ├── Retrieval-Augmented Generation (RAG)
│   │   ├── Concept: "Open-book exam" for LLMs to query external databases
│   │   ├── Prevents hallucinations & answers proprietary info without training
│   │   ├── Embeddings:
│   │   │   ├── Vectors mapped to N-dimensional space
│   │   │   ├── Sparse Embeddings (One-hot encoding, high dimensionality, mostly zeros)
│   │   │   └── Dense Embeddings (Smaller vectors, packed with semantic info)
│   │   │   └── Similarity searches typically use Cosine Similarity
│   │   └── Bedrock Knowledge Bases
│   │       ├── Automatically handles RAG embedding and chunking
│   │       ├── Required Embedding Models: Cohere or Amazon Titan
│   │       └── Vector Store Support:
│   │           ├── Amazon OpenSearch Serverless (Default)
│   │           ├── Amazon MemoryDB
│   │           ├── Amazon Aurora
│   │           ├── MongoDB Atlas, Pinecone, Redis Enterprise Cloud
│   │
│   ├── RAG Pre-Retrieval (Chunking Strategies)
│   │   ├── Fixed Size Chunking (Default configuration)
│   │   │   ├── e.g. 300 tokens per chunk with ~20% overlap
│   │   │   └── Honors sentence boundaries
│   │   ├── Hierarchical Chunking
│   │   │   ├── Nested parent/child chunks
│   │   │   ├── Search hits small *child* chunks for precision
│   │   │   └── Retriever pulls the *parent* chunk for broader context
│   │   ├── Semantic Chunking
│   │   │   ├── Uses FM to break text based on meaning, not just length
│   │   │   ├── Configuration: Base FM, Buffer size, Breakpoint percentile
│   │   │   └── Costs money per chunk (uses LLM compute)
│   │   └── Divider Strings & Metadata
│   │       ├── Extract HTML structures (`<SECTION_BREAK>`) for better organization
│   │       └── Metadata.json to tag documents (e.g. topic, date) for hybrid search
│   │
│   ├── Evaluating RAG Systems
│   │   ├── Bedrock native evaluation metrics:
│   │   │   ├── Correctness, Completeness, Helpfulness
│   │   │   ├── Groundedness & Faithfulness (Does answer match the retrieved text?)
│   │   │   ├── Citation Precision & Coverage
│   │   │   └── Harmfulness & Refusal (Is it evasive?)
│   │   └── Uses LLM-as-a-judge: Feed a Prompt Dataset + Ground Truth to evaluate
│   │
│   ├── Multimodal Models & Pipelines
│   │   ├── Mixing Text, Images, Video
│   │   └── Titan Multimodal Embeddings G1: Expects base64-encoded image payloads
│   │
│   ├── Amazon Bedrock Guardrails
│   │   ├── Applied to both Prompts AND Responses
│   │   ├── Filters: Word filtering, Topic filtering, PII removal/masking
│   │   ├── Contextual Grounding Check: Directly measures if LLM is hallucinating against source
│   │   └── Automated Reasoning Checks
│   │       ├── You provide a complex policy PDF (e.g. mortgage logic)
│   │       ├── Runs through CreateAutomatedReasoningPolicy API
│   │       └── Bedrock breaks it into strict True/False validation logic
│   │
│   ├── Prompt Engineering
│   │   ├── Anatomy of a Prompt: Instructions + Context + Input data + Output indicator
│   │   ├── Prompt Management: Save, version, and share prompts with double curly brace variables `{{genre}}`
│   │   ├── Types of Prompts
│   │   │   ├── Zero-shot (No examples)
│   │   │   ├── Few-shot (Provides input->output examples)
│   │   │   └── Chain of Thought (CoT - "Think step by step")
│   │   ├── Mitigating Prompt Misuse (Injection & Leaking)
│   │   │   └── Protect via robust system prompts and Guardrails
│   │   └── Mitigating Bias
│   │       ├── Frameworks: TIED (Text-to-image disambiguation), TAB (Text-to-image ambiguity benchmark)
│   │       └── Strategies: Forced disambiguation in prompt, counterfactual data augmentation
│   │
│   ├── Bedrock Flows
│   │   └── Visual dashboard (Flow Builder) to chain Prompts, FMs, and knowledge bases conditionally
│   │
│   └── AWS Well-Architected Generative AI Lens
│       └── Lifecycle: Scoping -> Model Selection -> Model Customization -> Development -> Integration -> Deployment -> Continuous Improvement
│
├── 3. MANAGING DATA FOR GENERATIVE AI
│   ├── Amazon Bedrock Data Automation (BDA)
│   │   ├── Extracts structured data from multimodal formats (PDF, DOCX, Img, Vid, Audio)
│   │   ├── Blueprints: Define strict target schemas (e.g. Driver's License blueprint)
│   │   ├── Granularity: Page-level, element-level (default bounding boxes), word-level
│   │   ├── Media extraction outputs to JSON:
│   │   │   ├── Video: IAB taxonomy, chapter summaries, on-screen text, logos
│   │   │   └── Audio: Speaker labels, topics, full transcripts
│   │   └── Great for replacing custom ETL code for Intelligent Document Processing
│   │
│   ├── Amazon SageMaker Data Wrangler
│   │   ├── Visual Studio environment to prep data for ML training
│   │   ├── 300+ built-in transformations
│   │   ├── Capabilities: Impute missing data, Class balancing (SMOTE, oversampling), PCA (Dimensionality reduction)
│   │   ├── Image manipulation: Resize, enhance, deliberately corrupt images
│   │   └── Quick Model tab to test data viability immediately
│   │
│   ├── AWS Glue
│   │   ├── Serverless ETL and Data Cataloging
│   │   ├── Glue Crawlers: Scans S3 datalakes to infer schemas & extract partitions
│   │   │   └── Partitions: S3 structure `yyyy/mm/dd/device` matters for Athena costs!
│   │   ├── Glue Studio: Visual DAG creation
│   │   └── Glue Data Quality: Enforces rules using DQDL (Data Quality Definition Language)
│   │
│   ├── NLP & Audio Processing
│   │   ├── Amazon Transcribe
│   │   │   ├── Automatic Speech Recognition (ASR)
│   │   │   ├── Features: PII Redaction, Language ID, Toxicity Detection (Tone & Text cues)
│   │   │   └── Enhancing Accuracy:
│   │   │       ├── Custom Vocabularies (brand names, acronyms)
│   │   │       └── Custom Language Models (trained on your domain text for broader context)
│   │   ├── Amazon Comprehend
│   │   │   ├── Serverless NLP for entities, sentiment, classification
│   │   │   ├── Custom Classification: Train it to sort customer support emails
│   │   │   ├── NER (Named Entity Recognition): Extract policy numbers, organizations
│   │   │   └── Pattern: Put Lambda + Comprehend BEFORE Bedrock to strip PII before LLM sees it
│   │   └── Amazon Comprehend Medical
│   │       ├── HIPAA-certified extraction of PHI (Protected Health Information)
│   │       └── Search for specific medical ontologies
│   │
│   ├── Amazon OpenSearch Service (The Vector Backend)
│   │   ├── Foundational Concepts:
│   │   │   ├── Index: Collection of documents. Has shards and replicas.
│   │   │   ├── Primary Shard: Self-contained Lucene index segment (Handles Writes)
│   │   │   └── Replica Shard: Redundancy copy (Handles Reads)
│   │   ├── Storage Tiers (Index State Management - ISM)
│   │   │   ├── Hot: Highest performance, EBS backed
│   │   │   ├── UltraWarm: S3 + caching (Requires dedicated master node)
│   │   │   └── Cold: S3 strictly, highly infrequent access
│   │   ├── Cluster Management & Sizing
│   │   │   ├── Requires at least 3 dedicated master nodes to prevent "Split Brain"
│   │   │   ├── Sizing rule: Source Data * (1 + Replicas) * 1.45 (for overhead)
│   │   │   └── Index Rollups & Transforms: Shrink aging data
│   │   ├── OpenSearch Serverless
│   │   │   ├── "Collections" instead of domains. Measures compute in OCUs (Opensearch Compute Units).
│   │   │   └── NOT scale-to-zero (baseline is 2 indexing OCUs, 2 search OCUs always running!)
│   │   ├── OpenSearch as a Vector Store
│   │   │   ├── Hybrid Search: Combines keyword (Lucene) + Vector (Semantic) queries
│   │   │   ├── Top Vector Engines: FAISS, NMSLib, Apache Lucene
│   │   │   ├── Exact Nearest Neighbor (Perfect but terribly slow)
│   │   │   ├── Approximate Nearest Neighbor (ANN)
│   │   │   │   ├── HNSW (Hierarchical Navigable Small World): Fast, high-quality, eats RAM (Change M and ef_construction limits)
│   │   │   │   └── IVF (Inverted File): Trades recall for speed, better for massive datasets
│   │   │   ├── Vector Compression: FP16 (Scalar Quantization) or Binary Vectors (32x smaller)
│   │   │   ├── Sharding Rules: Semantic requires 30-50GB shards, Hybrid needs 10-30GB shards
│   │   │   └── Neural Plugin: Direct API ingest -> FM Embedding pipeline inside OpenSearch
│   │   └── Security
│   │       └── Complex to expose Dashboards securely via VPC (Requires Nginx Proxy / Cognito)
│   │
│   ├── Amazon S3 & S3 Vectors
│   │   ├── S3 Tiers & Lifecycle
│   │   │   ├── Standard (99.99% Avail, Fast, Multi-AZ)
│   │   │   ├── Standard-IA (Less frequent, fast retrieval, Multi-AZ)
│   │   │   ├── One Zone-IA (Warning: Destroyed if AZ dies)
│   │   │   ├── Glacier Instant Retrieval (Access 1x quarter)
│   │   │   ├── Glacier Flexible Retrieval (Expedited 1-5min, Standard 3-5hr, Bulk 5-12hr)
│   │   │   └── Glacier Deep Archive (12hr - 48hr retrieve)
│   │   ├── Intelligent Tiering: Pays small monitoring fee to auto-tier based on use
│   │   ├── S3 Access Points
│   │   │   └── Separate DNS limits via VPC Origins & distinct policies for subgroups
│   │   ├── S3 Encryption
│   │   │   ├── SSE-S3 (AES-256 AWS managed, default)
│   │   │   ├── SSE-KMS (Audit key usage via CloudTrail, subject to KMS req/s limits)
│   │   │   ├── SSE-C (Customer sends key in HTTPS header)
│   │   │   └── Client-Side (User encrypts completely locally)
│   │   └── Amazon S3 Vectors
│   │       ├── Radically new & ultra-cheap method for storing vectors in S3
│   │       ├── Uses Boto3 `put_vectors()` or `s3vectors-embed-cli`
│   │       ├── Max indices: 10,000 per bucket. Auto performance tuning under the hood.
│   │       └── Tiered Search Strategy: Sync active queries to OpenSearch, keep archives in S3 vectors
│   │
│   ├── Databases (Relational vs NoSQL for AI)
│   │   ├── Amazon RDS
│   │   │   ├── Managed SQL Server, Postgres, MySQL, Oracle
│   │   │   └── Vector Store support: Microsoft SQL Server Vector Store plugin
│   │   ├── Amazon Aurora
│   │   │   ├── Auto-expanding storage (Up to 256TB), 15 Read Replicas, Sub-10ms lag
│   │   │   ├── HA 6 copies across 3 AZs. Quorum: 4 writes, 3 reads
│   │   │   └── Vector Store: `pgvector` extension (Cosine, L2, Inner-product distance SQL operations + HNSW)
│   │   └── Amazon DynamoDB
│   │       ├── Serverless NoSQL. Unlimited scaling
│   │       ├── Primary Keys: Partition (HASH) vs. Partition + Sort (HASH+RANGE)
│   │       ├── Capacity Modes
│   │       │   ├── Provisioned: RCU & WCU. Throws ProvisionedThroughputExceededException if bursted out.
│   │       │   └── On-Demand: 2.5x more expensive, handles massive spike uncertainty
│   │       ├── Math Basics
│   │       │   ├── WCU: 1 write/sec per 1KB (Round strictly up! 4.5KB = 5 WCU)
│   │       │   ├── Eventually Consistent Read (ECR): 2 reads/sec per 4KB
│   │       │   └── Strongly Consistent Read (SCR): 1 read/sec per 4KB (Consumes 2x capacity of ECR!)
│   │       ├── Advanced DDB
│   │       │   ├── DAX (DynamoDB Accelerator): Microsecond in-memory cache, solves "Hot Key" Partitions
│   │       │   ├── DynamoDB TTL: Free background cleanup via Unix Epoch timestamp
│   │       │   └── PartiQL: Run pseudo-SQL queries on NoSQL tables
│   │       └── DDB with GenAI: Serves as low-latency "Long term memory" / Chat History retrieval for Agent workflows
│   │
│   └── Event-Driven Vector Updates
│       ├── Architecture: S3 update → trigger EventBridge → hit Bedrock `StartIngestionJob`
│       └── Vector maintenance via AWS Batch (create embeddings -> swap old index for new)
│
└── 4. AGENTIC AI
    ├── Fundamentals & Structure
    │   ├── LLM Agent Anatomy: Planning Module + Core Memory + External Tools via API
    │   ├── Tool Assignment
    │   │   ├── Bedrock Action Groups point agents to specific tools (Lambda functions)
    │   │   └── Requires precise OpenAPI parameter schemas so the LLM knows *what* fields to provide
    │   └── Agentic RAG: Passing a Knowledge base as a queryable "Tool" to an Agent
    │
    ├── Multi-Agent Workflows
    │   ├── Why Multi-Agent? Complex prompts break down; specific LLMs excel at specific subsets.
    │   ├── Pattern 1: Routing
    │   │   └── A single "Router" LLM looks at the user input and picks 1 out of N specialist LLM agents.
    │   ├── Pattern 2: Parallelization
    │   │   ├── Sectioning (distinct tasks sent to specific workers simultaneously)
    │   │   └── Voting (sending the same task to multiple models to crowdsource the best answer)
    │   ├── Pattern 3: Prompt Chaining
    │   │   └── Pipeline sequence. LLM 1 -> evaluation "Gate" -> LLM 2
    │   ├── Pattern 4: Evaluator-Optimizer
    │   │   └── Generator LLM writes output, Evaluator LLM assesses. Loops until perfect.
    │   └── Pattern 5: Orchestrator-Worker
    │       └── Head Node breaks intent into pieces, feeds to multiple workers, sub-node Synthesizer unites data
    │
    ├── Agent Frameworks & Tooling
    │   ├── Strands Agents
    │   │   ├── Open-sourced generic Python SDK built by Amazon
    │   │   ├── Features predefined tools: AWS Services/Boto3, Call API, Math calculators, Memory
    │   │   └── Allows `@tool` Python decorators to immediately expose logic to Bedrock Agents
    │   ├── AWS Agent Squad
    │   │   ├── Another AWS open-source framework
    │   │   ├── High emphasis on Intelligent Intent Classification and Supervisor Agent coordination
    │   │   └── Built to natively wrap and extend Bedrock Flows
    │   └── Amazon Bedrock AgentCore
    │       ├── Managed runtime execution environment for ALL multi-agent deployments
    │       ├── Provides zero-infrastructure "Serverless" scaling specifically for Agent swarms
    │       └── Agnostic to framework (Supports LangChain, CrewAI, AutoGen, Strands)
    │
    └── Agent Memory Design
        ├── Short-Term Memory: Active chat session (In-memory, ElastiCache, etc.)
        └── Long-Term Memory: Preference extraction, historic user facts, strategies (DynamoDB, Vector Store, RDS)
```
