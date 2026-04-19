AIP-C01 FULL COURSE
│
├── [I] GENERATIVE AI FUNDAMENTALS & BEDROCK
│ │
│ ├── FOUNDATION MODELS (FMs)
│ │ ├── Giant pre-trained TRANSFORMER models
│ │ ├── Generic examples → GPT-n, Claude, DALL-E, LLaMa, DeepSeek, Nova
│ │ └── AWS-supported FMs
│ │ ├── Jurassic-2 (AI21 Labs) → multilingual (ES/FR/DE/PT/IT/NL)
│ │ ├── Claude (Anthropic) → convo, Q&A, workflow automation
│ │ ├── Stable Diffusion (stability.ai) → image/art/logo/design
│ │ ├── Llama (Meta) → LLM
│ │ ├── Amazon Titan → summarize, generate, Q&A, embed, personalize, search
│ │ ├── Amazon Nova Pro → LLM portfolio
│ │ └── Amazon Nova Reels → VIDEO generation
│ │
│ ├── AMAZON BEDROCK
│ │ ├── API for GenAI Foundation Models
│ │ ├── Invoke chat/text/image models
│ │ ├── Pre-built, fine-tuned, or your own imported models
│ │ ├── 3rd party models billed via AWS (their own pricing)
│ │ ├── Supports RAG + LLM agents
│ │ ├── SERVERLESS
│ │ └── Integrates with SageMaker Canvas
│ │
│ ├── BEDROCK API ENDPOINTS
│ │ ├── bedrock → manage, deploy, train models
│ │ ├── bedrock-runtime → inference (prompts, embeddings)
│ │ │ └── Converse, ConverseStream, InvokeModel, InvokeModelWithResponseStream
│ │ ├── bedrock-agent → manage/deploy/train agents + KBs
│ │ └── bedrock-agent-runtime → InvokeAgent, Retrieve, RetrieveAndGenerate
│ │
│ ├── CONVERSE API
│ │ ├── Unified API for message-based models
│ │ ├── Fields → messages, modelId
│ │ └── Optional → guardrailConfig, inferenceConfig (maxTokens, temperature, topP, stopSequences),
│ │ promptVariables, toolConfig, performanceConfig, system, outputConfig
│ │
│ ├── IAM PERMISSIONS
│ │ ├── Must use IAM user (not root)
│ │ ├── AmazonBedrockFullAccess
│ │ └── AmazonBedrockReadOnly
│ │
│ ├── FINE-TUNING ("Custom Models")
│ │ ├── Purpose → adapt LLM to use case, reduce prompt eng, save tokens
│ │ ├── Bedrock-tunable → Titan, Cohere, Meta
│ │ ├── Text data → {"prompt":..., "completion":...} pairs in S3
│ │ ├── Image data → S3 paths + descriptions
│ │ ├── Security → VPC + PrivateLink for sensitive data
│ │ └── Can fine-tune a fine-tuned model (compound learning)
│ │
│ ├── CONTINUED PRE-TRAINING
│ │ ├── Like fine-tuning but UNLABELED
│ │ ├── Just {"input":"..."} text to familiarize model
│ │ └── Bakes extra data INTO the model
│ │
│ ├── LoRA (Low-Rank Adaptation)
│ │ ├── Don't update whole model
│ │ ├── Slap low-rank matrices on attention weights, train those
│ │ ├── At inference → add fine-tuned weights to base
│ │ ├── Base unchanged → efficient storage/training/inference
│ │ └── ≠ adapter layer (added on top)
│ │
│ ├── RAG (Retrieval-Augmented Generation)
│ │ ├── "Open-book exam" for LLMs
│ │ ├── Query external DB → inject into prompt
│ │ ├── Pros
│ │ │ ├── Faster + cheaper than fine-tuning
│ │ │ ├── Easy info updates (just update DB)
│ │ │ ├── Semantic search via vector stores
│ │ │ ├── Prevents hallucinations
│ │ │ └── Easy "AI search" delivery
│ │ └── Cons
│ │ ├── Overcomplicated search engine
│ │ ├── Sensitive to prompt templates
│ │ ├── Non-deterministic
│ │ ├── Can still hallucinate
│ │ └── Sensitive to retrieval relevance
│ │
│ ├── VECTOR DB CHOICES (for RAG)
│ │ ├── Graph DB (Neo4j) → recommendations/relationships
│ │ ├── OpenSearch/Elasticsearch → text (TF/IDF), also vector
│ │ ├── Purpose-built vector DBs
│ │ │ ├── Commercial → Pinecone, Weaviate
│ │ │ └── Open-source → Chroma, Marqo, Vespa, Qdrant, LanceDB, Milvus, vectordb
│ │ └── Coerced DBs → SQL, Neptune, Redis, MongoDB, Cassandra
│ │
│ ├── EMBEDDINGS
│ │ ├── Big vectors representing data (100s-1000s dims)
│ │ ├── Similar items = close in space
│ │ ├── Titan-like models compute them
│ │ ├── SPARSE vs DENSE
│ │ │ ├── Sparse → large, mostly empty (one-hot); greater similarity factors
│ │ │ └── Dense → smaller, more semantic info; memory efficient
│ │ └── Cosine similarity → common metric (angle between vectors)
│ │
│ ├── BEDROCK KNOWLEDGE BASES
│ │ ├── Sources → S3, Web crawler, Confluence, Salesforce, SharePoint
│ │ ├── Embedding models → Cohere OR Amazon Titan ONLY
│ │ ├── Vector stores
│ │ │ ├── OpenSearch (default serverless for dev)
│ │ │ ├── MemoryDB (now has vector)
│ │ │ ├── Aurora
│ │ │ ├── MongoDB Atlas
│ │ │ ├── Pinecone
│ │ │ └── Redis Enterprise Cloud
│ │ ├── Controls → vector dimension, chunking
│ │ └── Uses → "Chat with your document", agentic RAG
│ │
│ ├── BREAKING UP THE "R" IN RAG
│ │ ├── Pre-Retrieval → Indexing, granularity/chunking, extraction, query rewriting
│ │ ├── Retrieval
│ │ └── Post-Retrieval → augment, generate
│ │
│ ├── CHUNKING
│ │ ├── Principles
│ │ │ ├── Stay within context/token limits
│ │ │ └── Granularity matters (sentences vs blocks vs summaries)
│ │ ├── Semantic Chunking approaches
│ │ │ ├── Embedding-based (LlamaIndex/LangChain)
│ │ │ ├── Model-based (BERT)
│ │ │ └── LLM-based (costly)
│ │ └── Bedrock Chunking Types
│ │ ├── Fixed Size (default 300 tokens, honors sentence boundaries)
│ │ ├── None → each doc = 1 chunk
│ │ ├── Hierarchical → small CHILD (precision) → replaced by PARENT (context)
│ │ └── Semantic
│ │ ├── Hits FM to split by meaning
│ │ ├── Parameters → Max tokens, Buffer size, Breakpoint percentile threshold
│ │ └── Costs money (pays for FM)
│ │
│ ├── OPTIMIZING EMBEDDINGS
│ │ ├── Smaller vector size → cheaper (fewer dims)
│ │ ├── Titan default → 1024+ dimensions
│ │ ├── Tradeoff → dim vs retrieval perf
│ │ └── Balance dimensionality with domain fit
│ │
│ ├── METADATA OPTIMIZATION
│ │ ├── Specify content vs metadata via metadata.json
│ │ ├── Avoid chunking metadata but still retrievable
│ │ └── Examples → Document ID, category, access control, lineage, section, topic, keywords
│ │
│ ├── KB UPDATES
│ │ ├── S3 event → Lambda → new embeddings
│ │ ├── Batch for efficiency
│ │ └── StartIngestionJob API (maybe scheduled)
│ │
│ ├── RAG EVALUATION (Bedrock Evaluation Jobs)
│ │ ├── Metrics
│ │ │ ├── Correctness
│ │ │ ├── Completeness
│ │ │ ├── Helpfulness
│ │ │ ├── Logical coherence
│ │ │ ├── Faithfulness → response ↔ retrieved text
│ │ │ ├── Citation precision & coverage
│ │ │ ├── Harmfulness, Stereotyping
│ │ │ └── Refusal (evasiveness)
│ │ ├── Provides → prompt dataset (JSON) w/ reference responses + contexts
│ │ ├── LLM-as-judge → Llama, Claude, Nova, Mistral
│ │ └── Triangle concepts → Answer Relevance, Context Relevance, Groundedness
│ │
│ ├── MULTIMODAL MODELS & PIPELINES
│ │ ├── Bedrock multimodal → Claude, Nova, Titan
│ │ ├── Titan Multimodal Embeddings G1 → JSON w/ base64-encoded image + text
│ │ └── Pipeline needs to do conversion (SageMaker/Glue)
│ │
│ ├── BEDROCK GUARDRAILS
│ │ ├── Content filtering → text FMs
│ │ ├── Filters on INPUTS + OUTPUTS
│ │ ├── Types → Word, Topic, Profanities, PII removal/masking
│ │ ├── Contextual Grounding Check
│ │ │ ├── Measures grounding (response ↔ context)
│ │ │ └── Measures relevance (response ↔ query)
│ │ └── Attachable → Agents + Knowledge Bases
│ │
│ ├── AUTOMATED REASONING CHECKS (Guardrails)
│ │ ├── For complex policies (mortgage, medical)
│ │ ├── Detects hallucinations in complex scenarios
│ │ ├── Provide policy as PDF
│ │ ├── CreateAutomatedReasoningPolicy API
│ │ └── Bedrock breaks into structured rules/logic
│ │
│ ├── TOKEN-LEVEL REDACTION
│ │ ├── Beyond Guardrails
│ │ ├── Pre/post handlers around inference endpoints
│ │ ├── Pattern matching + NER (Amazon Comprehend)
│ │ └── Apply at ingestion too
│ │
│ ├── PROMPT MANAGEMENT
│ │ ├── Reusable stored prompts
│ │ ├── Shareable across apps, versioned
│ │ ├── Variables → {{double curly braces}}
│ │ ├── Prompt Variants (different models/configs)
│ │ ├── Prompt Builder tool in console
│ │ └── Can associate Tools + Caching
│ │
│ ├── BEDROCK FLOWS
│ │ ├── Chain models/prompts/conditions
│ │ ├── Absorbed old "Prompt Flows"
│ │ ├── Nodes + Connections (conditional)
│ │ ├── Visual (Flow Builder) OR JSON
│ │ └── Can enforce pre/post-processing
│ │
│ ├── STRUCTURED JSON OUTPUT
│ │ ├── Option 1 → specify in prompt (schema + example)
│ │ └── Option 2 → Tool Use via Converse API (response format template)
│ │
│ ├── PROMPT ANATOMY (I-C-I-O)
│ │ ├── Instructions
│ │ ├── Context
│ │ ├── Input data
│ │ └── Output indicator
│ │
│ ├── PROMPT BEST PRACTICES
│ │ ├── Clear + concise
│ │ ├── Include context
│ │ ├── Specify response type
│ │ ├── Desired output at END
│ │ ├── Phrase as question
│ │ ├── Provide example response
│ │ ├── Break complex tasks
│ │ └── Experiment, be creative
│ │
│ ├── PROMPT TYPES
│ │ ├── Zero-shot → no examples
│ │ ├── Few-shot → examples included
│ │ └── Chain of Thought (CoT) → "think step by step"
│ │
│ ├── PROMPT MISUSE
│ │ ├── Prompt Injection
│ │ │ ├── "## Ignore the above…"
│ │ │ ├── "Imagine a fictional character…"
│ │ │ └── Fix → system prompt guardrails
│ │ └── Prompt Leaking
│ │ ├── PII exposure
│ │ └── "Tell me your initial instructions"
│ │
│ ├── MITIGATING BIAS
│ │ ├── Disambiguation (user-specified attributes)
│ │ ├── TIED → text-to-image disambiguation framework
│ │ ├── TAB → text-to-image ambiguity benchmark
│ │ ├── Few-shot clarification
│ │ ├── System prompt diversity enforcement
│ │ ├── Fix training data
│ │ ├── Counterfactual data augmentation
│ │ └── Detect / Segment / Augment
│ │
│ ├── ENTERPRISE INTEGRATION
│ │ ├── KBs as integration point (S3, SharePoint, Confluence)
│ │ ├── Cross-account access
│ │ │ ├── Bedrock + OpenSearch in diff accounts
│ │ │ └── OpenSearch remote-inference connector + IAM roles
│ │ └── Event-Driven → loose coupling via SQS/Kafka/pub-sub
│ │
│ └── WELL-ARCHITECTED GENAI LENS
│ ├── 6 Pillars → Operational Excellence, Security, Reliability, Performance, Cost, Sustainability
│ └── GenAI Lifecycle
│ ├── Scoping
│ ├── Model Selection
│ ├── Model Customization
│ ├── Development
│ ├── Integration
│ ├── Deployment
│ └── Continuous Improvement
│
├── [II] MANAGING DATA FOR GENAI
│ │
│ ├── STRUCTURED DATA HANDLING
│ │ ├── Bedrock → JSON payloads
│ │ ├── SageMaker endpoints → JSON (LLMs), CSV (classical ML)
│ │ └── Your app is responsible for formatting
│ │
│ ├── UNSTRUCTURED TEXT
│ │ ├── Convert to HTML → preserves headings/tables
│ │ ├── Tools → pandoc, Textract, Comprehend
│ │ ├── Pipeline → AWS Glue
│ │ └── Newer → Bedrock Data Automation (BDA)
│ │
│ ├── DIVIDER STRINGS
│ │ ├── <SECTION_BREAK:Title>
│ │ ├── Lambda Preprocessor (HTML → dividers)
│ │ └── Glue ETL pipeline option
│ │
│ ├── CONVERSATION FORMAT (Converse API)
│ │ ├── role → user / assistant
│ │ └── content → [{text: "..."}]
│ │
│ ├── BEDROCK DATA AUTOMATION (BDA)
│ │ ├── Extracts structured data from multimodal inputs
│ │ ├── IDP + KB prep use cases
│ │ ├── Concepts
│ │ │ ├── Standard Output → auto-guesses format
│ │ │ ├── Custom Output → Blueprints specify fields
│ │ │ └── Project → contains many Blueprints
│ │ ├── API → InvokeDataAutomationAsync
│ │ ├── Document Processing
│ │ │ ├── Accepts → PDF, TIFF, JPEG, PNG, DOCX
│ │ │ ├── Outputs → JSON, JSON+files, HTML, CSV
│ │ │ ├── Files → CSV for tables, markdown, text extraction
│ │ │ └── Granularity → page, element (default), word
│ │ ├── Image Processing
│ │ │ ├── JPEG, PNG
│ │ │ └── Outputs → summary/caption, IAB taxonomy, logos, text, moderation
│ │ ├── Video Processing
│ │ │ ├── MP4, MOV, AVI, MKV, WEBM
│ │ │ └── Outputs → full summary, CHAPTER summaries, IAB taxonomy, transcript, text, logos, moderation
│ │ ├── Audio Processing
│ │ │ ├── AMR, FLAC, M4A, MP3, Ogg, WAV
│ │ │ └── Outputs → summary, transcript, speaker/channel labels, topics, moderation
│ │ └── Blueprints
│ │ ├── Basic fields (explicit/implicit)
│ │ ├── Table fields, Groups, Custom types
│ │ └── Uses → Classification, Extraction, Normalization, Transformation, Validation
│ │
│ ├── SAGEMAKER DATA WRANGLER
│ │ ├── Visual interface in SageMaker Studio
│ │ ├── 300+ transforms (also custom pandas/PySpark)
│ │ ├── Quick Model feature
│ │ ├── Image xforms (resize, enhance, corrupt)
│ │ ├── Balance data → random over/under-sampling, SMOTE
│ │ ├── Impute missing, handle outliers
│ │ ├── Dimensionality reduction (PCA)
│ │ └── Sources → S3, Athena, Redshift, Lake Formation, Feature Store, JDBC (Databricks, SaaS)
│ │
│ ├── AWS GLUE
│ │ ├── Serverless table/schema discovery
│ │ ├── Crawler → scans S3, creates schema
│ │ ├── Data Catalog → table definitions (data stays in S3)
│ │ ├── Consumers → Redshift Spectrum, Athena, EMR, QuickSight
│ │ ├── Partitions → from S3 structure
│ │ ├── Glue Studio → visual ETL workflows (DAGs)
│ │ │ └── Sources → S3, Kinesis, Kafka, JDBC
│ │ └── Data Quality → DQDL (Data Quality Definition Language)
│ │
│ ├── CLOUDWATCH (GenAI relevance)
│ │ ├── Metrics belong to namespaces, have dimensions (up to 30)
│ │ ├── Custom metrics supported
│ │ └── Metric Streams → Kinesis Firehose → Datadog/Dynatrace/NewRelic/Splunk/Sumo
│ │
│ ├── AMAZON TRANSCRIBE
│ │ ├── ASR speech-to-text
│ │ ├── PII Redaction
│ │ ├── Automatic Language Identification
│ │ ├── Accuracy Boosters
│ │ │ ├── Custom Vocabularies → words (brands, acronyms)
│ │ │ └── Custom Language Models → context (domain-specific text)
│ │ └── Toxicity Detection → ML voice-based
│ │ └── Categories → sexual harassment, hate, threat, abuse, profanity, insult, graphic
│ │
│ ├── AMAZON COMPREHEND
│ │ ├── NLP fully managed + serverless
│ │ ├── Capabilities → language, entities, key phrases, sentiment, topics
│ │ ├── Custom Classification → user-defined categories (real-time + async)
│ │ ├── NER → predefined entities (people, places, orgs)
│ │ ├── Custom Entity Recognition → business-specific (policy numbers)
│ │ ├── Lambda pre-Bedrock → redact PII, classify, extract, detect language
│ │ └── Comprehend Medical
│ │ ├── HIPAA-certified
│ │ ├── Pre-trained for health (prescriptions, procedures, PHI)
│ │ ├── Separate DetectPHI API (vs DetectEntities)
│ │ ├── Medical ontology search
│ │ └── VPC Endpoints / PrivateLink supported
│ │
│ ├── AMAZON OPENSEARCH SERVICE
│ │ ├── Fork of Elasticsearch + Kibana
│ │ ├── Concepts → Documents, Indices, Types
│ │ ├── Shards → index split; hashed to shards
│ │ ├── Redundancy → primary + replicas per shard
│ │ ├── Managed (not serverless by default)
│ │ │ ├── Scales up/down (not automatic)
│ │ │ ├── Domains → bundled cluster config
│ │ │ ├── Snapshots to S3
│ │ │ └── Zone Awareness
│ │ ├── Storage Tiers
│ │ │ ├── Hot → instance stores / EBS (fastest)
│ │ │ ├── UltraWarm → S3 + caching (indices w/ few writes); requires dedicated master
│ │ │ └── Cold → S3, cheapest, requires UltraWarm + dedicated master
│ │ │ ├── Not compatible with T2/T3
│ │ │ └── Fine-grained access → cold_manager role
│ │ ├── Index State Management (ISM)
│ │ │ ├── Delete old, move tiers, snapshots, reduce replicas
│ │ │ └── Runs every 30-48 min w/ jitter
│ │ ├── Index Rollups → summarized indices (fewer fields, coarser buckets)
│ │ ├── Index Transforms → different view w/ groupings
│ │ ├── Cross-cluster Replication → leader/follower (requires FGAC + node encryption)
│ │ │ └── Remote Reindex → on-demand copy
│ │ ├── Stability
│ │ │ ├── 3 dedicated masters (avoid split-brain)
│ │ │ ├── Storage ≈ Source × (1+Replicas) × 1.45
│ │ │ └── Shards = (source+growth) × (1+overhead) / desired shard size
│ │ ├── Security → Resource/Identity/IP policies, request signing, VPC, Cognito
│ │ └── Anti-patterns → OLTP (use RDS/DynamoDB), Ad-hoc (use Athena)
│ │
│ ├── OPENSEARCH SERVERLESS
│ │ ├── On-demand autoscaling
│ │ ├── "Collections" instead of domains → search OR time series
│ │ ├── Always KMS encrypted
│ │ ├── Capacity → OCUs (Opensearch Compute Units)
│ │ │ └── Min 2 for indexing, 2 for search
│ │ └── "Serverless" ≠ scales to zero → SHUT IT DOWN when unused
│ │
│ ├── OPENSEARCH AS VECTOR STORE
│ │ ├── Primary Bedrock KB implementation
│ │ ├── Works w/ SageMaker, HuggingFace, custom
│ │ ├── Search Types
│ │ │ ├── SEMANTIC → vector search
│ │ │ └── HYBRID → vector + keyword (needs filterable metadata fields)
│ │ ├── Vector Engines
│ │ │ ├── FAISS (Facebook AI Similarity)
│ │ │ ├── NMSLib (Non-Metric Space Library)
│ │ │ └── Apache Lucene
│ │ ├── Search Methods
│ │ │ ├── Exact Nearest Neighbor → slow
│ │ │ └── ANN (Approximate NN)
│ │ │ ├── HNSW (Hierarchical Navigable Small World)
│ │ │ │ └── Fast, high-quality, lots of RAM
│ │ │ └── IVF (Inverted File)
│ │ │ └── Best for huge datasets; trade recall for speed/memory
│ │ ├── HNSW Tuning
│ │ │ ├── M → edges per node (denser = higher recall, more memory)
│ │ │ ├── ef_construction → KNN graph build list size
│ │ │ └── ef_search → graph exploration depth
│ │ ├── Vector Compression
│ │ │ ├── Binary vectors → bit sequences, 32x compression vs float32
│ │ │ └── FP16 → scalar quantization (used by HNSW)
│ │ ├── Sharding
│ │ │ ├── Semantic → 30-50 GB (fewer, larger)
│ │ │ ├── Hybrid → 10-30 GB
│ │ │ └── Serverless → automatic
│ │ ├── Multi-index → specialized per doc type
│ │ ├── Hierarchical Indices → small top-level routes to detailed
│ │ └── Neural Plugin → OpenSearch calls Bedrock for embeddings
│ │
│ ├── AMAZON S3 VECTORS (NEW)
│ │ ├── Up to 90% CHEAPER
│ │ ├── Create S3 vector bucket + vector index (dims + distance metric)
│ │ ├── put_vectors / query_vectors APIs
│ │ ├── CLI → s3vectors-embed-cli (put/query)
│ │ ├── Integrates w/ Bedrock KBs + SageMaker Unified Studio
│ │ ├── Strongly consistent (immediately available)
│ │ ├── Performance → 100ms-1s (not fast)
│ │ ├── Tiered search strategy → S3 for infrequent, OpenSearch for perf
│ │ ├── OpenSearch integration → COPIES data (pay for both!)
│ │ ├── OR use OpenSearch managed clusters w/ S3 Vectors engine backend
│ │ ├── Limits → 10,000 indices per bucket, 2B vectors per index
│ │ └── Best Practices
│ │ ├── Batch insert/delete (500/API call)
│ │ ├── Concurrent for smaller batches (up to 2500/sec)
│ │ ├── Retry on 429 (hundreds/sec per index limit)
│ │ ├── Multiple indexes
│ │ └── Mark non-filterable metadata
│ │
│ ├── AMAZON RDS
│ │ ├── Relational DB service: Postgres, MySQL, MariaDB, Oracle, MS SQL, IBM DB2, Aurora
│ │ ├── Managed → auto provisioning, OS patching, PITR, read replicas, Multi-AZ, scaling
│ │ ├── NO SSH access
│ │ ├── Storage Auto Scaling
│ │ │ ├── Triggers → <10% free + 5min + 6hr since last mod
│ │ │ └── Must set Max Storage Threshold
│ │ └── GenAI → RDS as vector store (RDS SQL Server Vector Store)
│ │ └── Pattern → RDS for structured + pointer to S3 unstructured
│ │
│ ├── AMAZON AURORA
│ │ ├── AWS-proprietary (Postgres + MySQL compatible)
│ │ ├── 5x perf vs MySQL, 3x vs Postgres
│ │ ├── Storage → auto-grows 10GB increments up to 256TB
│ │ ├── Up to 15 read replicas (sub-10ms lag)
│ │ ├── Failover → instantaneous, HA native
│ │ ├── 20% more than RDS but more efficient
│ │ ├── 6 copies across 3 AZs
│ │ │ ├── 4/6 for writes
│ │ │ └── 3/6 for reads
│ │ ├── Features
│ │ │ ├── Auto fail-over, backup/recovery, isolation, compliance
│ │ │ ├── Push-button scaling, zero-downtime patching
│ │ │ └── Backtrack → restore at any point w/o backups
│ │ └── pgvector extension
│ │ ├── vector column type
│ │ ├── Cosine, L2, Inner Product distances
│ │ ├── IVF/HNSW similarity search
│ │ ├── Advantage over OpenSearch → complex SQL filtering
│ │ └── Good for small/medium RAG with structured data
│ │
│ ├── AMAZON DYNAMODB
│ │ ├── NoSQL, fully managed, Multi-AZ replication
│ │ ├── Millions req/sec, trillions of rows
│ │ ├── Integrated w/ IAM + DynamoDB Streams
│ │ ├── Standard + Infrequent Access table classes
│ │ ├── Basics
│ │ │ ├── Tables, Primary Keys (HASH or HASH+RANGE)
│ │ │ ├── Max item size → 400KB
│ │ │ └── Types → Scalar, Document, Set
│ │ ├── Capacity Modes
│ │ │ ├── Provisioned → specify RCU/WCU, burst capacity
│ │ │ └── On-Demand (default) → auto-scaling, 2.5x more expensive
│ │ ├── WCU
│ │ │ └── 1 WCU = 1 write/sec up to 1KB (items > round up)
│ │ ├── RCU
│ │ │ └── 1 RCU = 1 Strongly Consistent Read OR 2 Eventually Consistent Reads up to 4KB
│ │ ├── Consistency
│ │ │ ├── Eventually Consistent (default)
│ │ │ └── Strongly Consistent → ConsistentRead=True, 2x RCU
│ │ ├── Partitions formula
│ │ │ ├── by_capacity = RCU/3000 + WCU/1000
│ │ │ ├── by_size = TotalSize/10GB
│ │ │ └── Total = ceil(max(by_capacity, by_size))
│ │ ├── Throttling → "ProvisionedThroughputExceededException"
│ │ │ └── Causes → hot keys, hot partitions, large items
│ │ ├── Operations
│ │ │ ├── Write → PutItem, UpdateItem (+atomic counters), Conditional Writes
│ │ │ ├── Read → GetItem (+ProjectionExpression), Query, Scan
│ │ │ ├── Query → KeyConditionExpression + FilterExpression
│ │ │ ├── Scan → entire table (inefficient), Parallel Scan option
│ │ │ ├── Delete → DeleteItem, DeleteTable
│ │ │ └── Batch → BatchWriteItem (25, 16MB, 400KB/item), BatchGetItem (100, 16MB)
│ │ ├── PartiQL → SQL-compatible
│ │ ├── DAX (DynamoDB Accelerator)
│ │ │ ├── In-memory cache, microsecond latency
│ │ │ ├── Solves hot-key problem
│ │ │ ├── 5-min TTL default
│ │ │ └── Up to 10 nodes, Multi-AZ (3+ for prod)
│ │ │ └── vs ElastiCache → DAX for individual objects/queries/scans; ElastiCache for aggregations
│ │ ├── TTL → auto-delete expired items (no WCU cost)
│ │ └── GenAI Uses
│ │ ├── NOT a vector store (store yes, search no)
│ │ ├── Near real-time data for models
│ │ ├── Chat history storage (long-term memory)
│ │ └── Zero-ETL to OpenSearch (for KBs)
│ │
│ ├── VECTOR STORE MAINTENANCE
│ │ ├── EventBridge for scheduled refresh
│ │ ├── AWS Batch for rebuild jobs
│ │ └── Swap old→new atomically
│ │
│ ├── RE-RANKER MODELS
│ │ ├── Bedrock Rerank API
│ │ ├── Improves RAG relevance
│ │ ├── Specify reranker on KB
│ │ └── Amazon + Cohere models (limited regions)
│ │
│ └── S3 STORAGE (detail cluster)
│ ├── Storage Classes
│ │ ├── Standard → 99.99% avail
│ │ ├── Standard-IA → 99.9%
│ │ ├── One Zone-IA → 99.5%, single AZ
│ │ ├── Glacier Instant Retrieval → ms, 90d min
│ │ ├── Glacier Flexible Retrieval → 1-5min/3-5hr/5-12hr, 90d min
│ │ ├── Glacier Deep Archive → 12hr/48hr, 180d min
│ │ └── Intelligent-Tiering → auto, small monitoring fee
│ ├── Durability → 11 9's across classes
│ ├── Lifecycle Rules → transitions + expiration
│ ├── S3 Analytics → storage class recommendations (Standard/IA only)
│ ├── Replication → CRR (cross-region), SRR (same-region)
│ │ └── Versioning required; not chained
│ ├── Encryption
│ │ ├── SSE-S3 → AES-256 default; "x-amz-server-side-encryption: AES256"
│ │ ├── SSE-KMS → "aws:kms"; uses GenerateDataKey + Decrypt APIs (KMS quotas apply)
│ │ ├── SSE-C → customer-provided key, HTTPS required
│ │ └── Client-Side Encryption
│ ├── TLS → HTTPS endpoints, enforce via aws:SecureTransport
│ ├── Access Logs → target bucket must be same region; DO NOT loop!
│ └── Access Points
│ ├── Own DNS + policy per AP
│ ├── Internet or VPC origin
│ └── VPC Endpoint required for VPC origin
│
├── [III] AGENTIC AI
│ │
│ ├── LLM AGENTS (CONCEPT)
│ │ ├── Memory + Planning Module + Tools + Core (LLM)
│ │ ├── "Memory" = chat history + external stores
│ │ └── "Planning" = prompt guidance for task decomposition
│ │
│ ├── BEDROCK AGENTS
│ │ ├── Foundation model + Action Groups (tools) + Knowledge Bases
│ │ ├── Action Groups
│ │ │ ├── Lambda functions as tools
│ │ │ ├── Prompts guide WHEN to use
│ │ │ ├── Parameters → name, description, type, required
│ │ │ └── OpenAPI-style schemas (or UI table)
│ │ ├── Code Interpreter (optional)
│ │ ├── Deployment
│ │ │ ├── Create Alias (snapshot)
│ │ │ ├── On-Demand Throughput (ODT) → account quotas
│ │ │ └── Provisioned Throughput (PT) → purchased rate
│ │ └── InvokeAgent API using alias ID
│ │
│ ├── MULTI-AGENT PATTERNS
│ │ ├── Manager (Orchestrator-Workers)
│ │ │ ├── Orchestrator delegates
│ │ │ ├── Workers execute (each w/ tools/memory)
│ │ │ └── Synthesizer combines
│ │ ├── Routing
│ │ │ └── Router LLM picks ONE specialized agent
│ │ ├── Parallelization
│ │ │ ├── Sectioning → independent subtasks (guardrails, evals)
│ │ │ └── Voting → same task, different models/prompts
│ │ ├── Prompt Chaining
│ │ │ ├── Sequential steps
│ │ │ └── Gates to exit early
│ │ └── Evaluator-Optimizer
│ │ ├── Generator + Evaluator loop
│ │ └── Feedback until acceptable
│ │
│ ├── AGENT MEMORY
│ │ ├── Short-term
│ │ │ ├── Chat history / immediate context
│ │ │ ├── Sessions + Events
│ │ │ └── Storage → in-memory / ElastiCache / MemoryDB / DynamoDB
│ │ ├── Long-term
│ │ │ ├── Extracted insights, summaries, preferences, facts
│ │ │ ├── Memory Records + Strategies
│ │ │ └── Storage → DynamoDB, SQLLite, RDS, Aurora
│ │ └── Options → AgentCore Memory, Mem0 (Strands), KBs as long-term
│ │
│ ├── STRANDS AGENTS
│ │ ├── Amazon open-source Python SDK
│ │ ├── Peers → OpenAI Agents SDK, CrewAI, LangGraph, Google ADK
│ │ ├── Tight AWS integration (Bedrock, Lambda, Step Functions)
│ │ ├── Not AWS-locked (OpenAI etc. supported)
│ │ ├── Multimodal (text/speech/images/video)
│ │ ├── MCP support
│ │ ├── Built-in Tools
│ │ │ ├── AWS services / boto3
│ │ │ ├── RAG via Bedrock KBs
│ │ │ ├── Mem0 memory
│ │ │ ├── Python code execution
│ │ │ ├── http, shell, file manipulation
│ │ │ ├── Agent swarms coordination
│ │ │ └── Polly (speak), custom Python tools
│ │ └── Agent Loop
│ │ └── Input/context → Tool selection → LLM/Reasoning → Tool execution → Response
│ │
│ ├── AWS AGENT SQUAD
│ │ ├── Open-source multi-agent framework
│ │ ├── Python + TypeScript
│ │ ├── Intent classification → routes to right agent
│ │ ├── Shared context, prebuilt agents/classifiers
│ │ ├── Integrates w/ Bedrock Agents + Flows
│ │ ├── Supervisor Agent (coordinates)
│ │ └── Agent Squad = ROUTING, Strands = TOOL USE (single loop)
│ │
│ ├── AMAZON BEDROCK AGENTCORE
│ │ ├── Serverless deployment for agents AT SCALE
│ │ ├── Framework-agnostic (Strands, OpenAI SDK, LangGraph, CrewAI)
│ │ ├── Starter toolkit (CodeBuild under hood)
│ │ ├── Capabilities
│ │ │ ├── Agent Runtime
│ │ │ ├── Agent Identity
│ │ │ ├── Tools
│ │ │ ├── Memory
│ │ │ ├── Gateways
│ │ │ └── Observability
│ │ ├── Agent Runtime
│ │ │ ├── Serverless endpoints
│ │ │ ├── Deploy to ECR (enhanced w/ capabilities)
│ │ │ ├── Multiple endpoints
│ │ │ └── GenAI Observability in CloudWatch
│ │ ├── Memory (short/long-term, same as above)
│ │ ├── Built-in Tools
│ │ │ ├── Browser Tool → control browser
│ │ │ └── Code Interpreter → Python/JS/TS isolated container
│ │ ├── Importing Bedrock Agents → agentcore import-agent
│ │ │ └── Generates Strands / LangChain / LangGraph code
│ │ ├── Gateway
│ │ │ ├── APIs/Lambda → MCP tools
│ │ │ ├── Targets → OpenAPI (REST), Smithy, Lambda
│ │ │ ├── Manages OAuth
│ │ │ └── Semantic tool selection
│ │ ├── Identity
│ │ │ ├── Agent's OWN identity (not end-user)
│ │ │ ├── Central identity repo (like Cognito)
│ │ │ ├── OAuth 2.0
│ │ │ └── Built-in → Google, GitHub, Slack, Salesforce, Atlassian
│ │ ├── Policy
│ │ │ ├── Integrates w/ Gateways
│ │ │ ├── Cedar language
│ │ │ ├── NLP or form construction
│ │ │ └── Enforcement
│ │ │ ├── Deny by default
│ │ │ ├── Contextual validation
│ │ │ └── Enforce OR Log-only mode
│ │ └── Evaluations
│ │ ├── Integrates → Strands, LangGraph, OpenTelemetry, OpenInference
│ │ ├── CloudWatch viz (AgentCore Observability Insights)
│ │ ├── Cross-region inference (data residency preserved)
│ │ ├── Built-in metrics
│ │ │ ├── Correctness, Helpfulness, Conciseness
│ │ │ ├── Instruction following, Faithfulness
│ │ │ ├── Response relevance, Coherence
│ │ │ ├── Refusal, Goal success rate
│ │ │ ├── Tool selection + parameter accuracy
│ │ │ └── Harmfulness, Stereotyping
│ │ └── Custom evaluators → model, prompt, scales, levels (session/trace/tool)
│ │
│ ├── MCP (Model Context Protocol)
│ │ ├── "USB-C port for AI Applications" (Anthropic)
│ │ ├── Data layer → JSON-RPC 2.0
│ │ ├── Transport → stdio OR HTTP streaming
│ │ ├── Servers expose → tools, resources, prompts
│ │ ├── Examples → GitHub, Atlassian, PostgreSQL, Slack, Google Maps, Udemy
│ │ └── Own MCP Server Deployment
│ │ ├── Lightweight → Lambda
│ │ ├── Complex → ECS/Fargate
│ │ ├── API Gateway can expose
│ │ └── AgentCore can host
│ │
│ ├── OPENAPI & GENAI
│ │ ├── Originally Swagger
│ │ ├── Defines FM-tool interfaces
│ │ ├── Standardizes functions/params/outputs/errors
│ │ └── Uploaded to S3 for Bedrock action groups
│ │
│ ├── HUMANS IN THE LOOP (HITL)
│ │ ├── Human Augmentation (AI drafts, human refines)
│ │ ├── Escalation Criteria (confidence scores → experts)
│ │ └── Feedback pipeline → API Gateway + DynamoDB (indexed)
│ │
│ ├── AMAZON Q BUSINESS
│ │ ├── Managed GenAI assistant for employees
│ │ ├── Built on Bedrock (FM not choosable)
│ │ ├── 40+ Data Connectors (S3, RDS, Aurora, WorkDocs, M365, SharePoint, Slack, Salesforce, Gmail, GDrive)
│ │ ├── Plugins → Jira, ServiceNow, Zendesk, Salesforce + Custom
│ │ ├── IAM Identity Center auth (respects doc permissions)
│ │ │ └── Supports external IdPs (Google, AD)
│ │ └── Admin Controls (Guardrails)
│ │ ├── Block words/topics
│ │ ├── Global + topic-level rules
│ │ └── Internal-only responses
│ │
│ ├── AMAZON Q APPS
│ │ └── Non-coders build GenAI apps in natural language
│ │
│ ├── AMAZON Q DEVELOPER
│ │ ├── AWS doc Q&A
│ │ ├── CLI suggestions
│ │ ├── Security scans
│ │ ├── Code gen/completion
│ │ ├── Bill analysis, troubleshooting
│ │ ├── Languages → Java, JS, Python, TS, C#
│ │ ├── IDE Extensions → VS Code, Visual Studio, JetBrains
│ │ └── Rules → .amazon/rules directory (Markdown .md files)
│ │ └── Like claude.md in Claude Code
│ │
│ └── AGENT TRACING (Bedrock Agents)
│ └── Trace types
│ ├── PreProcessing → user input categorization
│ ├── Orchestration → action group/KB calls
│ ├── PostProcessing → final response
│ ├── CustomOrchestration → action ordering
│ ├── RoutingClassifier → classification/routing
│ ├── Failure → step failures
│ └── Guardrail → guardrail actions
│
├── [IV] OPERATIONAL EFFICIENCY & OPTIMIZATION
│ │
│ ├── TOKEN EFFICIENCY
│ │ ├── Bedrock CountTokens API (FREE, pre-invoke)
│ │ ├── CloudWatch → InputTokenCount, outputTokenCount
│ │ ├── CloudWatch also → count, time, TTFT, throttles, errors, latency
│ │ ├── Context Pruning
│ │ │ ├── Limit RAG chunks
│ │ │ ├── Metadata filtering
│ │ │ └── Summarize old chat
│ │ ├── Response Size Controls
│ │ │ ├── maxTokens
│ │ │ ├── Prompt directive
│ │ │ ├── Few-shot examples
│ │ │ └── JSON output
│ │ └── Prompt Compression → small model summarizes before big
│ │
│ ├── COST-EFFECTIVE MODEL SELECTION
│ │ ├── Cost/Capability tradeoff
│ │ ├── Small models for preprocessing (summarize, classify, chunk)
│ │ ├── Dynamic Routing = Intelligent Prompt Routing (built into Bedrock)
│ │ └── Routing mechanisms → Flow, Lambda, Agent Squad, Strands
│ │
│ ├── PRICE:PERFORMANCE MEASUREMENT
│ │ ├── Bedrock Evaluations (human OR LLM judges)
│ │ └── Pair w/ token counting
│ │
│ ├── RESOURCE UTILIZATION
│ │ ├── Batching (embeddings + Bedrock Batch Inference)
│ │ ├── Capacity planning → TPM/RPM, Service Quotas
│ │ ├── CloudFormation for capacity planning
│ │ ├── Tensor parallelism → shard LLM weights across GPUs
│ │ ├── Provisioned Throughput
│ │ │ ├── By Tokens or Model Units (MU)
│ │ │ ├── Required for custom models
│ │ │ └── TIED TO MODEL ARN
│ │ ├── CloudWatch dashboards + Cost Explorer
│ │ └── Auto-scaling → Lambda, Bedrock, OpenSearch Serverless, AgentCore
│ │
│ ├── INTELLIGENT CACHING
│ │ ├── Semantic Caching
│ │ │ ├── Cache embeddings of prompts/responses
│ │ │ ├── Store → ElastiCache for Valkey, MemoryDB, or OpenSearch
│ │ │ ├── NN search on new prompts; similarity > threshold → cached
│ │ │ └── Tune threshold carefully
│ │ ├── Prompt Caching (built-in Bedrock)
│ │ │ ├── Caches STATIC PREFIX (instructions, system prompt, examples)
│ │ │ ├── Dynamic content at END
│ │ │ ├── Cache checkpoint separates
│ │ │ ├── Cached reads DISCOUNTED; writes may cost more
│ │ │ ├── Monitored in CloudWatch
│ │ │ └── Available in Prompt Management
│ │ └── Edge Caching (CloudFront)
│ │ ├── GET /ask?fingerprint=<hash>
│ │ ├── Deterministic request hashing
│ │ └── TTL based on change frequency
│ │
│ ├── RESPONSIVE AI SYSTEMS
│ │ ├── Parallel requests, Step Functions
│ │ ├── Cache/pre-compute predictable queries
│ │ ├── Response streaming
│ │ └── Latency-Optimized Inference (Bedrock feature)
│ │ ├── performanceConfig={'latency':'optimized'}
│ │ └── Optimizes → TTFT, OTPS (Output Tokens/Sec), E2E latency
│ │
│ ├── MORE RESPONSIVENESS
│ │ ├── Intelligent Prompt Routing
│ │ ├── Concise prompts (important stuff first)
│ │ ├── Context pruning
│ │ ├── Limit response sizes
│ │ └── Break complex tasks
│ │
│ ├── RETRIEVAL PERFORMANCE
│ │ ├── Hybrid search + custom scoring
│ │ ├── Query pre-processing
│ │ │ ├── Normalize style
│ │ │ ├── Split multi-part
│ │ │ ├── Filter irrelevant
│ │ │ └── Reduce ambiguity
│ │ └── Keyword extraction
│ │
│ ├── PARAMETER TUNING
│ │ ├── A/B → Bedrock Evaluations or CloudWatch Evidently
│ │ ├── Temperature → 0 deterministic, 1 creative
│ │ ├── Top_p → nucleus sampling (probability threshold)
│ │ └── Top_k → sample size of token options
│ │ ├── NOTE: Use temperature OR top_p, not both
│ │
│ ├── FM SYSTEM PERFORMANCE
│ │ ├── API call profiling
│ │ ├── Structured input/output (JSON/XML)
│ │ ├── Chain of Thought for reasoning
│ │ ├── Feedback loops for user satisfaction
│ │ └── SageMaker stuff
│ │ ├── Models up to 500GB
│ │ ├── Adjust container health check + download timeout quotas
│ │ ├── 3rd party parallelization → Triton, FasterTransformer, DeepSpeed
│ │ └── Instance types
│ │ ├── ml.p4d.24xlarge → large GPU
│ │ └── ml.c5.9xlarge → small CPU (NER)
│ │
│ ├── ULTRASERVERS
│ │ ├── Trn2, P6e-GB200
│ │ └── Low-latency interconnects for EC2 AI/ML
│ │
│ ├── LAMBDA ENDPOINT LIFECYCLE
│ │ ├── Auto-initialize endpoints
│ │ ├── Download model artifacts from S3
│ │ └── On-demand trigger
│ │
│ ├── EXPONENTIAL BACKOFF (SkillBuilder specifics!)
│ │ ├── Start 100ms
│ │ ├── Backoff factor 2
│ │ ├── Max retry 3-5
│ │ └── Jitter ±100ms
│ │
│ ├── CONNECTION POOLING (SkillBuilder specifics!)
│ │ ├── 10-20 connections per instance
│ │ └── TTL 60-300 seconds
│ │
│ └── BEDROCK CROSS-REGION INFERENCE
│ ├── Distributes across regions (interruptions, quotas)
│ ├── Org SCPs can block regions :/
│ ├── Inference Profiles
│ │ ├── Specific geography → data residency
│ │ └── Global → commercial regions
│ ├── Doesn't work w/ Provisioned Throughput
│ ├── Geographic → data residency, standard pricing
│ ├── Global → max throughput, 10% savings, price from origin region
│ └── Encrypted in transit, logged in CloudTrail
│
├── [V] MANAGING MODELS WITH SAGEMAKER AI
│ │
│ ├── WORKFLOW
│ │ ├── Fetch/clean/prepare data
│ │ ├── Train/evaluate model
│ │ └── Deploy + evaluate in production
│ │
│ ├── TRAINING & DEPLOYMENT
│ │ ├── Training code image in ECR
│ │ ├── Training data in S3
│ │ ├── Output → model artifacts in S3
│ │ ├── Inference code image in ECR
│ │ └── Endpoint for client apps
│ │
│ ├── NOTEBOOKS
│ │ ├── EC2-based
│ │ ├── S3 data access
│ │ ├── Scikit_learn, Spark, Tensorflow
│ │ └── Spin up training + deploy
│ │
│ ├── DATA PREP
│ │ ├── Usually from S3
│ │ ├── RecordIO / Protobuf common
│ │ ├── Athena, EMR, Redshift, Keyspaces
│ │ └── Spark + scikit, numpy, pandas
│ │
│ ├── PROCESSING JOBS
│ │ ├── Copy data from S3
│ │ ├── Spin up container (built-in or custom)
│ │ └── Output to S3
│ │
│ ├── DEPLOYMENT OPTIONS
│ │ ├── Persistent Endpoint (real-time)
│ │ ├── Batch Transform (offline)
│ │ ├── Inference Pipelines
│ │ ├── SageMaker Neo → edge
│ │ ├── Elastic Inference → deep learning accel
│ │ ├── Auto-scaling
│ │ └── Shadow Testing → eval new vs current
│ │
│ ├── DEPLOYMENT SAFEGUARDS
│ │ ├── Deployment Guardrails (async/real-time)
│ │ ├── Blue/Green Deployments
│ │ │ ├── All at once
│ │ │ ├── Canary (small portion, monitor)
│ │ │ └── Linear (spaced steps)
│ │ ├── Auto-rollbacks
│ │ └── Shadow Tests (promote manually)
│ │
│ ├── SAGEMAKER FEATURES
│ │ ├── JumpStart → 150+ open source models
│ │ ├── Data Wrangler
│ │ ├── Feature Store (Online/Offline, Feature Groups)
│ │ ├── Edge Manager (w/ Neo)
│ │ └── Async Inference endpoints
│ │
│ ├── FM DEPLOYMENT OPTIMIZATION
│ │ ├── Single/multi-model/multi-container endpoints
│ │ ├── Deployment guardrails, VPC, network isolation
│ │ ├── Train in SageMaker → deploy via Bedrock (Custom Model Import)
│ │ │ └── Now serverless
│ │ ├── SageMaker AI Inference Components → per-model scaling
│ │ ├── Cross-region inference profiles (Bedrock endpoints)
│ │ ├── Auto Scaling Groups + Load Balancers
│ │ ├── Model Servers
│ │ │ ├── TorchServe
│ │ │ ├── DJL Serving (Deep Java Library — Amazon-created, exam-likely)
│ │ │ ├── Deep Learning Containers
│ │ │ └── Triton Inference Server
│ │ ├── Async inference (latency not critical)
│ │ └── Model Compression
│ │ ├── Quantization (weights)
│ │ ├── Pruning
│ │ └── Knowledge Distillation (smaller from larger)
│ │
│ ├── GROUND TRUTH
│ │ ├── Human labeling at scale
│ │ ├── Active learning → model learns, only ambiguous → humans (70% savings)
│ │ ├── Labelers → Mechanical Turk, internal team, pro companies
│ │ └── Ground Truth Plus → AWS manages team + workflow
│ │
│ ├── OTHER LABEL GENERATORS
│ │ ├── Rekognition → image
│ │ ├── Comprehend → text/topic
│ │ └── Pre-trained / unsupervised models
│ │
│ ├── MODEL MONITOR
│ │ ├── CloudWatch alerts on quality deviations
│ │ ├── Data drift viz
│ │ ├── Anomaly/outlier detection
│ │ ├── New feature detection
│ │ ├── + Clarify for bias monitoring
│ │ └── Monitoring Types
│ │ ├── Data quality drift (vs baseline)
│ │ ├── Model quality drift
│ │ ├── Bias drift
│ │ └── Feature attribution drift (NDCG)
│ │
│ ├── CLARIFY (Bias + Explainability)
│ │ ├── Pre-training Bias Metrics
│ │ │ ├── CI → Class Imbalance
│ │ │ ├── DPL → Difference in Proportions of Labels
│ │ │ ├── KL, JS → divergence
│ │ │ ├── LP → p-norm
│ │ │ ├── TVD → total variation
│ │ │ ├── KS → Kolmogorov-Smirnov
│ │ │ └── CDD → Conditional Demographic Disparity
│ │ └── Explainability → feature contribution
│ │
│ ├── MODEL REGISTRY
│ │ ├── Catalog + versions
│ │ ├── Metadata + approval status
│ │ ├── CI/CD deployments
│ │ └── SageMaker Model Collections
│ │
│ ├── ML LINEAGE TRACKING
│ │ ├── MLOps history
│ │ ├── Auditing + compliance
│ │ ├── Entities
│ │ │ ├── Trial component → processing/training/transform
│ │ │ ├── Trial → model composed of components
│ │ │ ├── Experiment → group of trials
│ │ │ ├── Context → logical grouping
│ │ │ ├── Action → workflow/deployment step
│ │ │ ├── Artifact → S3 object / ECR image
│ │ │ └── Association → connects entities
│ │ │ └── Types → ContributedTo, AssociatedWith, DerivedFrom, Produced, SameAs
│ │ ├── Query → LineageQuery API (SageMaker SDK)
│ │ └── Cross-account → AddAssociation API + AWS RAM
│ │
│ ├── SAGEMAKER NEO
│ │ ├── Train once, run anywhere
│ │ ├── Edge → ARM, Intel, Nvidia
│ │ ├── Frameworks → TF, MXNet, PyTorch, ONNX, XGBoost, DarkNet, Keras
│ │ ├── Compiler + runtime
│ │ └── + IoT Greengrass → deploy to edge, Lambda inference apps
│ │
│ ├── SAGEMAKER UNIFIED STUDIO
│ │ ├── Single interface (data, analytics, AI, ML)
│ │ ├── Includes → Bedrock, Q, QuickSight, notebooks
│ │ ├── Admins manage users/groups
│ │ ├── Domain → connects assets/users/projects
│ │ └── VS Code connectable
│ │
│ └── SAGEMAKER PIPELINES
│ ├── DAG for ML workflows
│ ├── Visual designer OR JSON
│ └── Integrated w/ Unified Studio + SageMaker AI
│
├── [VI] MORE TOOLS FOR BUILDING AI APPS
│ │
│ ├── AWS LAMBDA
│ │ ├── Serverless cloud code
│ │ ├── Uses → real-time files, streams, ETL, cron, AWS events
│ │ ├── Languages → Node.js, Python, Java, C#, Go, PowerShell, Ruby
│ │ ├── Triggers → S3, DynamoDB Streams, SNS, SQS, Kinesis, API Gateway, EventBridge, etc.
│ │ ├── + Kinesis → sync processing, batch size/payload limits, shard stalls on errors
│ │ └── + Bedrock/GenAI
│ │ ├── Connect agents to tools
│ │ ├── Param validation, error handling
│ │ ├── On-demand FM invocation
│ │ ├── Webhook handling
│ │ └── Custom aggregation/voting
│ │
│ ├── AWS API GATEWAY
│ │ ├── + Lambda = serverless API
│ │ ├── WebSocket support
│ │ ├── Versioning, environments, auth
│ │ ├── API keys, throttling
│ │ ├── Swagger/OpenAPI import
│ │ ├── Request/response transform + validation
│ │ ├── SDK generation
│ │ ├── Response caching
│ │ ├── Integrations → Lambda, HTTP, AWS Service
│ │ ├── Endpoint Types
│ │ │ ├── Edge-Optimized (default) → global via CloudFront
│ │ │ ├── Regional
│ │ │ └── Private → VPC interface endpoint only
│ │ ├── Security → IAM, Cognito, Custom Authorizer
│ │ ├── Custom domain HTTPS via ACM
│ │ │ ├── Edge-Optimized → cert in us-east-1
│ │ │ └── Regional → cert in API region
│ │ └── GenAI Uses
│ │ ├── Feedback/model front-end
│ │ ├── Usage plans
│ │ │ ├── Throttling ~10-50/sec
│ │ │ └── Burst ~2-3X
│ │ ├── Response filtering
│ │ ├── Retry strategies
│ │ ├── Request Validator + JSON schema
│ │ └── Routing logic via transformations
│ │
│ ├── AWS APPCONFIG
│ │ ├── Dynamic config deploys w/o redeploys
│ │ ├── Feature flags, allow/block lists
│ │ ├── Sources → Parameter Store, SSM Docs, S3
│ │ ├── Gradual rollouts + rollback
│ │ ├── Validation → JSON Schema (syntactic), Lambda (semantic)
│ │ ├── CloudWatch alarm rollback trigger
│ │ └── GenAI → dynamic FM selection, A/B, rollbacks
│ │
│ ├── AWS STEP FUNCTIONS
│ │ ├── Workflow design
│ │ ├── Visual + error handling + retry
│ │ ├── History audit + "Wait" state
│ │ ├── Max execution → 1 year
│ │ ├── State Machine
│ │ │ ├── Task → Lambda/AWS/3rd party
│ │ │ ├── Choice → conditional (Choice Rules)
│ │ │ ├── Wait → delay
│ │ │ ├── Parallel → separate branches
│ │ │ ├── Map → set of steps per item (JSON/S3/CSV)
│ │ │ └── Pass, Succeed, Fail
│ │ ├── Circuit Breaker Pattern
│ │ │ ├── Step Functions + Lambda + DynamoDB
│ │ │ ├── Prevents calling timing-out services
│ │ │ └── Fallback models / degraded mode
│ │ ├── ReAct Patterns
│ │ │ ├── Reasoning + Acting
│ │ │ ├── Chain of Thought
│ │ │ └── Dynamic FM routing
│ │ ├── 256KB data-between-steps limit
│ │ │ └── Squirrel in DynamoDB/S3 if larger
│ │ └── Bedrock integration
│ │ ├── InvokeModel, CreateModelCustomizationJob
│ │ └── Chain FM calls + guardrails
│ │
│ ├── AWS CODEPIPELINE
│ │ ├── CI/CD orchestration
│ │ ├── Stages → Source, Build, Test, Deploy, Invoke
│ │ ├── Sequential + parallel actions
│ │ ├── Manual approval
│ │ └── Artifacts in S3 passed between stages
│ │
│ ├── AWS CODEBUILD
│ │ ├── Fully managed CI (scales, no servers)
│ │ ├── Docker-based reproducible builds
│ │ ├── Supports prepackaged or custom images
│ │ ├── Charged per-minute
│ │ ├── Security → KMS, IAM, VPC, CloudTrail
│ │ ├── Sources → CodeCommit, S3, Bitbucket, GitHub
│ │ ├── buildspec.yml at repo root
│ │ │ ├── env → variables, parameter-store, secrets-manager
│ │ │ ├── phases → install, pre_build, build, post_build
│ │ │ ├── artifacts → uploaded to S3 (KMS encrypted)
│ │ │ └── cache → S3 for speed
│ │ └── Environments → Java, Ruby, Python, Go, Node.js, Android, .NET Core, PHP, Docker
│ │
│ ├── AWS CODEDEPLOY
│ │ ├── Deploy to EC2, on-prem, Lambda, ECS
│ │ ├── Auto rollback + CloudWatch alarm triggers
│ │ ├── appspec.yml defines deployment
│ │ ├── EC2 → in-place OR blue/green
│ │ │ └── Speeds → AllAtOnce, HalfAtATime, OneAtATime, Custom
│ │ ├── Agent required on EC2 (auto install via SSM)
│ │ ├── Lambda → Linear / Canary / AllAtOnce (traffic shifts)
│ │ └── ECS → Blue/Green ONLY, Linear / Canary / AllAtOnce
│ │
│ ├── MLFLOW
│ │ ├── Open-source ML/GenAI workflows
│ │ ├── Observability, evaluations, tracking, tracing, AI gateway
│ │ ├── SageMaker AI integration (managed)
│ │ └── Integration points → Studio, Model Registry, Inference, IAM, CloudTrail, EventBridge
│ │
│ ├── AWS APPSYNC
│ │ ├── GraphQL + Pub/Sub APIs
│ │ ├── Serverless, JS/TS business logic
│ │ ├── GenAI → Lambda resolvers for FM inference
│ │ └── VTL (Apache Velocity Template Language) → GraphQL ↔ data source
│ │
│ ├── AWS OUTPOSTS
│ │ ├── Hybrid cloud, "server racks" on-prem
│ │ ├── Same AWS infra/services/APIs
│ │ ├── You responsible for physical security
│ │ ├── Benefits → low-latency, local proc, residency, migration
│ │ ├── Services → EC2, EBS, S3, EKS, ECS, RDS, EMR
│ │ └── GenAI → data compliance, privacy, on-prem FM inference w/ local caching
│ │
│ ├── AWS WAVELENGTH
│ │ ├── Infra at 5G network edges
│ │ ├── Ultra-low latency
│ │ ├── Traffic stays in CSP network
│ │ ├── High BW to parent region
│ │ ├── No extra charges
│ │ ├── Uses → Smart Cities, ML-assisted diagnostics, AR/VR, gaming, streaming
│ │ └── GenAI → edge deployments, mobile FM apps, traffic balance edge↔region
│ │
│ ├── AMAZON SQS
│ │ ├── Managed queue (decoupling)
│ │ ├── Unlimited throughput + messages
│ │ ├── Retention → default 4d, max 14d
│ │ ├── Latency <10ms
│ │ ├── Message size ≤1024 KB
│ │ ├── At-least-once delivery, best-effort ordering
│ │ ├── Producer → SendMessage API
│ │ ├── Consumer → poll, process, DeleteMessage
│ │ ├── Scale horizontally (more consumers)
│ │ ├── ASG + CloudWatch ApproximateNumberOfMessages alarm
│ │ └── Security → TLS, KMS, client-side enc, IAM + Access Policies
│ │
│ ├── AWS AMPLIFY
│ │ ├── Full-stack web/mobile dev
│ │ ├── Auth, Storage, API, CI/CD, PubSub, Analytics, AI/ML
│ │ └── Connects to GitHub, CodeCommit, Bitbucket, GitLab
│ │
│ ├── AMAZON EVENTBRIDGE
│ │ ├── Formerly CloudWatch Events
│ │ ├── Schedule (cron) OR Event Pattern rules
│ │ ├── Destinations → Lambda, Batch, ECS Task, SQS, SNS, Kinesis, Step Functions, CodePipeline, CodeBuild, SSM, EC2
│ │ ├── Event buses → Default, Partner, Custom
│ │ ├── Archive + replay
│ │ ├── Schema Registry → infer schemas, code gen, versioned
│ │ └── Resource-based policies → cross-account events
│ │
│ ├── AMAZON SNS
│ │ ├── Pub/Sub (one-to-many)
│ │ ├── Subscribers → SQS, Lambda, Firehose, HTTP(S), SMS, Email, Mobile Push
│ │ ├── Up to 12.5M subs/topic, 100K topics
│ │ ├── Direct Publish → GCM, APNS, ADM
│ │ └── Security → TLS, KMS, IAM + Access Policies
│ │
│ └── AMAZON APPFLOW
│ ├── SaaS ↔ AWS data integration
│ ├── Sources → Salesforce, SAP, Zendesk, Slack, ServiceNow
│ ├── Destinations → S3, Redshift, Snowflake, Salesforce
│ ├── Frequency → scheduled / event / on-demand
│ ├── Filtering + validation transforms
│ └── Public internet OR PrivateLink
│
├── [VII] GOVERNANCE & QA
│ │
│ ├── BEDROCK AGENT TRACING (repeated)
│ │ └── See [III]
│ │
│ ├── FM EVALUATION CRITERIA
│ │ ├── Human Evaluation
│ │ │ ├── UX, context relevance/sensitivity
│ │ │ ├── Creativity + flexibility
│ │ │ └── Complex/unexpected problems
│ │ ├── Benchmark Datasets
│ │ │ ├── SME-generated prompts/answers
│ │ │ ├── Leaderboards
│ │ │ ├── Measured → Accuracy, Speed, Scalability, Context retrieval
│ │ │ └── Flawed if eval data is flawed
│ │ ├── LLM as Judge
│ │ │ ├── Trusted model evaluates responses
│ │ │ └── Watch shared biases
│ │ ├── Hybrid approaches → reveal limitations of both
│ │ ├── ROUGE
│ │ │ ├── Text summarization + translation
│ │ │ ├── RECALL of overlapping units
│ │ │ ├── ROUGE-N → n-grams (ROUGE-1 uni, ROUGE-2 bi)
│ │ │ └── ROUGE-L → longest common subsequence (coherence/order)
│ │ ├── BLEU
│ │ │ ├── Machine translation
│ │ │ ├── PRECISION of n-grams (vs ROUGE=recall)
│ │ │ ├── Sentence level
│ │ │ ├── Brevity penalty
│ │ │ └── Limited for fluency/grammar
│ │ └── BERTscore
│ │ ├── Uses embedding vectors
│ │ ├── Semantic similarity
│ │ └── Tolerant of synonyms/paraphrasing
│ │
│ ├── BEDROCK MODEL EVALUATIONS
│ │ ├── Automatic → built-in task types, datasets, metrics
│ │ ├── Human-based → Cognito / Ground Truth / A2I work teams
│ │ ├── LLM-as-judge (generator + evaluator)
│ │ ├── RAG Evaluation Jobs
│ │ │ ├── Retrieve only → relevance/coverage
│ │ │ └── Retrieve + generate → correctness/completeness/helpfulness/coherence
│ │ └── Prompt dataset → S3 JSON lines
│ │
│ ├── DEPLOYMENT VALIDATION
│ │ ├── Synthetic user workflows
│ │ │ ├── CloudWatch Synthetic Monitoring (canaries)
│ │ │ ├── Step Functions, EventBridge, Lambda
│ │ │ └── S3/Athena/QuickSight for results
│ │ ├── AI-Specific validation
│ │ │ ├── Hallucination rate, semantic drift, faithfulness, compliance
│ │ │ └── Bedrock Evaluations OR Lambda+Step Functions
│ │ └── Response consistency → test prompt dataset in accepted variance
│ │
│ ├── RESPONSIBLE AI (8 DIMENSIONS)
│ │ ├── Fairness
│ │ ├── Explainability
│ │ ├── Privacy & Security
│ │ ├── Safety
│ │ ├── Controllability
│ │ ├── Veracity & Robustness
│ │ ├── Governance
│ │ └── Transparency
│ │
│ ├── AWS RESPONSIBLE AI TOOLS
│ │ ├── Bedrock Model Evaluation
│ │ ├── SageMaker Clarify → bias, eval, explainability
│ │ ├── Model Monitor → alerts
│ │ ├── Amazon A2I → human review/correction
│ │ └── SageMaker ML Governance
│ │ ├── Role Manager
│ │ ├── Model Cards
│ │ └── Model Dashboard
│ │
│ ├── CLOUDWATCH LOGS
│ │ ├── Log groups + streams
│ │ ├── Expiration policies (never, 1d-10y)
│ │ ├── Destinations → S3, Kinesis Streams, Firehose, Lambda, OpenSearch
│ │ ├── Encrypted by default (KMS supported)
│ │ ├── Sources → SDK, CW Agent, Beanstalk, ECS, Lambda, VPC Flow Logs, API Gateway, CloudTrail, Route53
│ │ ├── Logs Insights → purpose-built query language, saveable, cross-account
│ │ ├── S3 Export → CreateExportTask (up to 12hr delay)
│ │ ├── Subscriptions → real-time to Kinesis/Firehose/Lambda w/ filters
│ │ └── GenAI Uses
│ │ ├── Prompt regression testing
│ │ ├── Monitor KPIs (effectiveness, quality, latency, errors)
│ │ ├── FM interaction tracing
│ │ ├── Business impact metrics
│ │ ├── Hallucination rates
│ │ ├── Anomaly detection (token bursts, drift)
│ │ ├── Bedrock model invocation logs
│ │ └── Cost anomaly detection
│ │
│ ├── CLOUDWATCH ALARMS
│ │ ├── States → OK, INSUFFICIENT_DATA, ALARM
│ │ ├── Period → min 10 sec high-res, multiples of 60s
│ │ ├── Targets → EC2 actions, ASG, SNS
│ │ ├── Composite Alarms → AND/OR multiple alarms (reduces noise)
│ │ ├── EC2 Recovery → StatusCheckFailed_System triggers
│ │ └── Metric filter → alarm chain
│ │
│ ├── CLOUDWATCH RUM (Real User Monitoring)
│ │ ├── Mobile app testing (iOS/Android)
│ │ ├── Page load, errors, launch times
│ │ ├── Integrates w/ Application Signals + X-Ray
│ │ └── GenAI → end-to-end mobile app perf
│ │
│ ├── AWS CLOUDTRAIL
│ │ ├── Enabled by default
│ │ ├── Audit API calls (console, SDK, CLI, AWS services)
│ │ ├── Logs to CloudWatch Logs OR S3
│ │ ├── All regions or single
│ │ ├── Event Types
│ │ │ ├── Management → operations on resources (default logged)
│ │ │ ├── Data → S3 object-level, Lambda Invoke (NOT default)
│ │ │ └── Insights Events → detects unusual activity
│ │ ├── Retention → 90 days in CloudTrail (S3 for longer)
│ │ └── GenAI → audit Bedrock API calls + prompt resources
│ │
│ ├── AWS X-RAY
│ │ ├── Visual distributed tracing
│ │ ├── Compatible → Lambda, Beanstalk, ECS, ELB, API Gateway, EC2
│ │ ├── Traces = segments + subsegments + annotations
│ │ ├── Every request OR sampled
│ │ ├── Security → IAM + KMS
│ │ ├── Setup
│ │ │ ├── SDK import (Java/Python/Go/Node/.NET)
│ │ │ ├── X-Ray daemon (Linux/Win/Mac) or AWS integration
│ │ │ └── Captures → AWS calls, HTTP(S), DBs, SQS
│ │ └── Troubleshooting
│ │ ├── EC2 → IAM role + daemon
│ │ └── Lambda → execution role + AWSX-RayWriteOnlyAccess + Active Tracing
│ │
│ └── AWS LAKE FORMATION
│ ├── Built on Glue
│ ├── Data lake setup (loading, partitions, encryption, ACL, audit)
│ ├── Sources → S3, RDBMS, NoSQL, on-prem
│ ├── Consumers → Athena, Redshift, EMR
│ ├── Cross-account via RAM
│ ├── Doesn't support manifests in Athena/Redshift queries
│ ├── Governed Tables → ACID transactions multi-table
│ │ ├── New S3 table type (can't revert)
│ │ ├── Streaming support (Kinesis)
│ │ └── Auto compaction
│ ├── Granular Access → row + cell-level security
│ ├── Data Filters
│ │ ├── Column-level (All rows + specific columns)
│ │ ├── Row-level (All columns + row filter)
│ │ ├── Cell-level (both)
│ │ └── CreateDataCellsFilter API
│ └── Permissions → IAM/SAML/external accounts + policy tags
│
├── [VIII] SECURITY, IDENTITY & COMPLIANCE
│ │
│ ├── PRINCIPLE OF LEAST PRIVILEGE
│ │ ├── Start broad, lock down
│ │ └── IAM Access Analyzer → least-privilege policy gen
│ │
│ ├── DATA MASKING & ANONYMIZATION
│ │ ├── Masking (Glue DataBrew, Redshift)
│ │ └── Anonymization → random, shuffle, encrypt, hash, delete
│ │
│ ├── KEY SALTING
│ │ ├── Append/prepend random salt before hash
│ │ ├── Defeats rainbow tables
│ │ ├── Unique salts per user
│ │ ├── Rotate periodically
│ │ └── Hash SHA256(Password + Salt)
│ │
│ ├── IAM
│ │ ├── Global service
│ │ ├── Users + Groups (groups contain users, not groups)
│ │ ├── Policies → JSON
│ │ │ ├── Version (2012-10-17)
│ │ │ ├── Id (optional)
│ │ │ ├── Statement → Sid, Effect, Principal, Action, Resource, Condition
│ │ │ └── Inline OR managed
│ │ ├── Password Policy → length, types, rotation, reuse
│ │ ├── MFA
│ │ │ ├── Virtual → Google Authenticator, Authy
│ │ │ ├── U2F Security Key → YubiKey
│ │ │ └── Hardware Key Fob → Gemalto, SurePassID (GovCloud)
│ │ └── IAM Roles for Services (EC2, Lambda, CloudFormation)
│ │
│ ├── AWS IAM IDENTITY CENTER (fka SSO)
│ │ ├── SSO for → AWS Orgs, SaaS (Salesforce/Box/M365), SAML2.0 apps, Windows EC2
│ │ ├── Built-in IdP OR 3rd party (AD, OneLogin, Okta)
│ │ ├── Permission Sets → collection of IAM policies
│ │ ├── Multi-account permissions
│ │ ├── Application assignments (SAML 2.0)
│ │ └── ABAC → attribute-based (cost center, title, locale)
│ │
│ ├── AWS CONTROL TOWER
│ │ ├── Secure multi-account setup
│ │ ├── Uses AWS Orgs
│ │ ├── Guardrails
│ │ │ ├── Preventive → SCPs (restrict regions)
│ │ │ └── Detective → AWS Config (find untagged)
│ │ └── Compliance dashboard
│ │
│ ├── ENCRYPTION OVERVIEW
│ │ ├── In-flight → TLS/SSL (prevents MITM)
│ │ ├── Server-side at rest → server decrypts
│ │ └── Client-side → client encrypts, server never decrypts (envelope encryption)
│ │
│ ├── AWS KMS
│ │ ├── Fully integrated w/ IAM + CloudTrail
│ │ ├── Symmetric (AES-256) → most AWS services
│ │ ├── Asymmetric (RSA, ECC) → encrypt/decrypt or sign/verify
│ │ ├── Key Types
│ │ │ ├── AWS Owned (free)
│ │ │ ├── AWS Managed (free) → aws/service-name
│ │ │ ├── Customer-Managed → $1/month
│   │   │   └── Imported → $1/month
│   │   ├── API cost → $0.03 per 10,000 calls
│   │   └── Rotation
│   │       ├── AWS-managed → yearly (auto)
│   │       ├── Customer-managed → auto + on-demand
│   │       └── Imported → manual via alias
│   │
│   ├── AMAZON MACIE
│   │   ├── Managed data security + privacy
│   │   ├── ML + pattern matching
│   │   ├── Discovers PII in S3
│   │   └── Alerts via EventBridge
│   │
│   ├── AWS SECRETS MANAGER
│   │   ├── Secrets storage
│   │   ├── Force rotation (Lambda-based)
│   │   ├── Auto generation on rotation
│   │   ├── RDS integration (MySQL/Postgres/Aurora)
│   │   ├── KMS encrypted
│   │   └── Multi-Region Secrets
│   │       ├── Primary + read replicas in sync
│   │       ├── Promote replica to standalone
│   │       └── DR + multi-region DB
│   │
│   ├── AMAZON COGNITO
│   │   ├── User Pools (CUP)
│   │   │   ├── Sign-in for web/mobile
│   │   │   ├── Integrates → API Gateway + ALB
│   │   │   ├── Password reset, email/phone verify
│   │   │   ├── MFA
│   │   │   └── Federated (Facebook, Google, SAML)
│   │   └── Identity Pools (Federated Identities)
│   │       ├── Temp AWS creds for users
│   │       ├── Sources → CUP, 3rd party, etc.
│   │       ├── IAM policies for auth/guest
│   │       └── Fine-grained via user_id (row-level security DynamoDB)
│   │
│   ├── AWS WAF
│   │   ├── Layer 7 (HTTP)
│   │   ├── Deploy on → ALB, API Gateway, CloudFront, AppSync, Cognito User Pool
│   │   └── Web ACL Rules
│   │       ├── IP Set (up to 10K)
│   │       ├── HTTP headers/body/URI
│   │       ├── SQL injection + XSS protection
│   │       ├── Size constraints, geo-match
│   │       ├── Rate-based (DDoS protection)
│   │       └── Regional except CloudFront
│   │
│   ├── VPC CRASH COURSE
│   │   ├── VPC → regional private network
│   │   ├── Subnets → AZ-level partitions
│   │   ├── Public vs Private subnets
│   │   ├── Internet Gateway (IGW) → internet access
│   │   ├── NAT Gateway/Instance → private subnet internet
│   │   ├── NACL (Network ACL)
│   │   │   ├── Subnet-level firewall
│   │   │   ├── ALLOW + DENY rules
│   │   │   ├── IP addresses only
│   │   │   └── Stateless
│   │   ├── Security Groups
│   │   │   ├── ENI/instance level
│   │   │   ├── ALLOW only
│   │   │   ├── IPs + other SGs
│   │   │   └── Stateful
│   │   ├── VPC Flow Logs → VPC/Subnet/ENI traffic to S3/CW/Firehose
│   │   ├── VPC Peering → non-overlapping CIDR, non-transitive
│   │   ├── VPC Endpoints
│   │   │   ├── Gateway → S3, DynamoDB
│   │   │   └── Interface → most services (ENI)
│   │   ├── Site-to-Site VPN → encrypted over public internet
│   │   └── Direct Connect → physical private, takes ≥1 month
│   │
│   └── AWS PRIVATELINK
│       ├── Expose service to 1000s of VPCs
│       ├── No peering/IGW/NAT
│       └── Requires NLB (service VPC) + ENI (customer VPC)
│
├── [IX] OTHER SERVICES
│   │
│   ├── ANALYTICS
│   │   ├── Amazon Athena
│   │   │   ├── Interactive S3 SQL (Presto)
│   │   │   ├── Serverless
│   │   │   ├── Formats → CSV/TSV, JSON, ORC, Parquet, Avro, Snappy/Zlib/LZO/Gzip
│   │   │   └── Uses → ad-hoc web logs, staging, CloudTrail/CloudFront/VPC/ELB logs, notebooks, QuickSight
│   │   ├── Amazon EMR
│   │   │   ├── Managed Hadoop on EC2
│   │   │   ├── Spark, HBase, Presto, Flink, Hive
│   │   │   ├── Cluster → Master, Core (HDFS+tasks), Task (tasks only)
│   │   │   ├── Transient vs Long-running
│   │   │   └── Spot for task nodes, RI for long-running
│   │   ├── Amazon QuickSight
│   │   │   ├── BI, serverless
│   │   │   ├── Viz, paginated reports, ad-hoc, anomaly detection
│   │   │   ├── Sources → Redshift, Aurora/RDS, Athena, OpenSearch, IoT Analytics, EC2 DBs, Excel, CSV, logs
│   │   │   ├── SPICE
│   │   │   │   ├── Super-fast Parallel In-memory Calc Engine
│   │   │   │   ├── Columnar, in-memory, machine code
│   │   │   │   ├── 10GB/user
│   │   │   │   └── 30-min import timeout
│   │   │   ├── Security → MFA, VPC, row-level, column-level (Enterprise)
│   │   │   ├── Redshift cross-region → SG w/ QS IP range OR Enterprise + ENI
│   │   │   ├── Cross-account → peering/Transit Gateway/PrivateLink/VPC sharing
│   │   │   ├── Users → IAM or email; AD connector (Enterprise)
│   │   │   ├── AWS-managed KMS keys only (Enterprise)
│   │   │   └── Anti-pattern → ETL (use Glue)
│   │   ├── Amazon Kinesis Data Streams
│   │   │   ├── Real-time streaming
│   │   │   ├── Retention → up to 365 days
│   │   │   ├── Ordering by Partition ID
│   │   │   ├── 1 MB/record
│   │   │   ├── KMS at-rest, HTTPS in-flight
│   │   │   ├── KPL/KCL libraries
│   │   │   ├── Provisioned → shards (1MB/s in, 2MB/s out)
│   │   │   └── On-demand → auto, 4MB/s default
│   │   └── Amazon MSK
│   │       ├── Managed Apache Kafka
│   │       ├── Multi-AZ (up to 3)
│   │       ├── Data on EBS
│   │       ├── MSK Serverless option
│   │       ├── Message size → 1MB default (configurable to 10MB)
│   │       ├── Kafka Topics w/ Partitions (can only add)
│   │       ├── PLAINTEXT or TLS, KMS at-rest
│   │       └── Consumers → Flink, Glue Streaming ETL, Lambda, EC2 apps (ECS/EKS)
│   │
│   ├── COMPUTE / CONTAINERS / CUSTOMER ENGAGEMENT
│   │   ├── AWS App Runner
│   │   │   ├── Managed web apps / APIs at scale
│   │   │   ├── From source code OR container image
│   │   │   ├── Auto build/deploy, scaling, LB, encryption
│   │   │   └── VPC access supported
│   │   ├── Amazon EC2
│   │   │   ├── IaaS — VMs, EBS, ELB, ASG
│   │   │   ├── Sizing → OS, CPU, RAM, storage, network, SG, user data
│   │   │   └── User Data → runs once on first boot as root
│   │   ├── Amazon ECS
│   │   │   ├── EC2 Launch Type → you manage EC2 instances (ECS Agent)
│   │   │   ├── Fargate Launch Type → serverless
│   │   │   ├── IAM Roles
│   │   │   │   ├── EC2 Instance Profile → ECS agent API calls, logs, ECR pulls, secrets
│   │   │   │   └── ECS Task Role → per-task role (defined in task def)
│   │   │   ├── LB Integrations → ALB (most), NLB (high perf + PrivateLink), CLB (not recommended)
│   │   │   └── EFS volumes supported (Fargate+EFS = serverless shared storage)
│   │   │       └── S3 NOT mountable
│   │   ├── Amazon EKS
│   │   │   ├── Managed Kubernetes
│   │   │   ├── EC2 workers OR Fargate
│   │   │   ├── Node Types → Managed Node Groups, Self-Managed, Fargate
│   │   │   ├── Data Volumes → CSI driver → EBS, EFS (w/ Fargate), FSx Lustre, FSx NetApp
│   │   │   └── CloudWatch Container Insights
│   │   └── Amazon Lex + Connect
│   │       ├── Lex → ASR + NLU (Alexa tech)
│   │       └── Connect → cloud virtual contact center
│   │
│   ├── DATABASE
│   │   ├── DocumentDB
│   │   │   ├── MongoDB-compatible NoSQL
│   │   │   ├── Stores/queries/indexes JSON
│   │   │   ├── Multi-AZ (3 replicas)
│   │   │   └── Storage auto-grows 10GB
│   │   ├── ElastiCache
│   │   │   ├── Redis OR Memcached
│   │   │   ├── Uses → DB cache (cache-aside), session store
│   │   │   ├── Redis → Multi-AZ, read replicas, persistence (AOF), backups, sets/sorted sets, replication
│   │   │   ├── Memcached → sharding, no HA, non-persistent, multi-threaded
│   │   │   └── ElastiCache for Valkey → alt to Redis OSS, supports vector search
│   │   ├── MemoryDB (Redis/Valkey)
│   │   │   ├── Vector search support
│   │   │   ├── All in-memory, Multi-AZ
│   │   │   └── Vector algorithms → Flat (brute force), HNSW (approx)
│   │   └── Neptune
│   │       ├── Managed graph DB
│   │       ├── Multi-AZ, up to 15 read replicas
│   │       ├── Billions of relations, ms latency
│   │       ├── Uses → knowledge graphs, fraud, recommendations, social
│   │       └── Neptune Analytics
│   │           └── vectors.topKByEmbedding → vector query w/ vertex attrs, top nodes + scores
│   │
│   ├── DEVELOPER TOOLS
│   │   ├── AWS CDK
│   │   │   ├── IaC in JS/TS, Python, Java, .NET
│   │   │   ├── Constructs → high-level components
│   │   │   ├── Compiles to CloudFormation
│   │   │   ├── Good for Lambda + Docker (ECS/EKS)
│   │   │   └── + SAM → sam local invoke after cdk synth
│   │   ├── AWS CLI + SDK
│   │   │   ├── Access Keys (ID + Secret)
│   │   │   ├── CLI open-source (Python SDK based)
│   │   │   └── SDK languages → JS, Python, PHP, .NET, Ruby, Java, Go, Node, C++
│   │   ├── CloudFormation
│   │   │   ├── Declarative IaC
│   │   │   ├── Tagged resources for cost attribution
│   │   │   ├── Infrastructure Composer → visual
│   │   │   └── Custom resources for unsupported
│   │   └── AWS CodeArtifact
│   │       ├── Managed artifact storage
│   │       ├── Tools → Maven, Gradle, npm, yarn, twine, pip, NuGet
│   │       ├── Repositories + Domains
│   │       ├── Proxy public repos
│   │       ├── EventBridge integration (package events)
│   │       └── Resource-based policy → cross-account
│   │
│   ├── MACHINE LEARNING
│   │   ├── Amazon Augmented AI (A2I)
│   │   │   ├── Human review of ML predictions
│   │   │   ├── Your employees / 500K contractors / Mechanical Turk
│   │   │   └── High confidence → immediate; low → humans
│   │   ├── Amazon Kendra
│   │   │   ├── ML doc search (NL queries)
│   │   │   ├── PDF, HTML, PPT, MS Word
│   │   │   ├── Incremental Learning
│   │   │   ├── Manual fine-tuning
│   │   │   └── Sources → S3, RDS, Drive, SharePoint, OneDrive, 3rd party
│   │   ├── Amazon Lex
│   │   │   ├── Chatbots (voice + text)
│   │   │   ├── Multiple languages
│   │   │   ├── Integrates → Lambda, Connect, Comprehend, Kendra
│   │   │   └── Intents + Slots
│   │   ├── Amazon Rekognition
│   │   │   ├── Image + video ML
│   │   │   ├── Uses → labeling, moderation, text detect, face detect/analysis, face search, celebrity, pathing
│   │   │   ├── Custom Labels → your logo/products w/ few hundred images
│   │   │   └── Custom Moderation Adaptors → enhance accuracy w/ labeled set
│   │   ├── Amazon Textract
│   │   │   ├── Extract text/handwriting/data from scanned docs
│   │   │   ├── Forms + tables
│   │   │   └── Uses → financial, healthcare, public sector
│   │   └── Amazon Transcribe → see [II]
│   │
│   ├── MANAGEMENT & GOVERNANCE
│   │   ├── AWS Auto Scaling
│   │   │   ├── Resources → EC2 ASG, Spot Fleet, ECS, DynamoDB, Aurora replicas
│   │   │   ├── Scaling Plans
│   │   │   │   ├── Dynamic → target tracking (40% avail, 50% balance, 70% cost, custom)
│   │   │   │   └── Predictive → forecast load + schedule
│   │   │   └── Options → disable scale-in, cooldown, warmup
│   │   ├── AWS Cost Anomaly Detection
│   │   │   ├── ML-based unusual spend detection
│   │   │   ├── Monitors services, accounts, tags, categories
│   │   │   └── SNS alerts (individual or summary)
│   │   ├── Cost Explorer
│   │   │   ├── Visualize cost/usage
│   │   │   ├── Monthly/hourly/resource granularity
│   │   │   ├── Savings Plan selection
│   │   │   └── Forecast up to 18 months
│   │   ├── Amazon Managed Grafana
│   │   │   ├── Managed Grafana
│   │   │   ├── IAM Identity Center / SAML auth
│   │   │   ├── Encrypted (KMS supported)
│   │   │   └── Sources → CloudWatch, OpenSearch, Timestream, Athena, Redshift, X-Ray, AMP, GitHub, Google, Azure, MySQL, Redis, JSON, OpenTelemetry
│   │   └── AWS Systems Manager (SSM)
│   │       ├── Manage EC2 + on-prem at scale (hybrid)
│   │       ├── Patching, run commands, parameter store
│   │       ├── Linux, Windows, macOS, Raspbian
│   │       ├── SSM Agent required (default on Amazon Linux)
│   │       ├── Session Manager → secure shell, no SSH/port 22 needed
│   │       │   └── Log to S3 or CloudWatch
│   │       └── Parameter Store
│   │           ├── Serverless secure config storage
│   │           ├── API keys, passwords, configs
│   │           ├── Version tracking + optional KMS
│   │           └── IAM-controlled
│   │
│   ├── MIGRATION & TRANSFER
│   │   ├── AWS DataSync
│   │   │   ├── Large data transfer
│   │   │   ├── On-prem/other cloud → AWS (needs agent)
│   │   │   ├── AWS↔AWS (no agent)
│   │   │   ├── Protocols → NFS, SMB, HDFS, S3 API
│   │   │   ├── Targets → S3 (any class), EFS, FSx (Win/Lustre/NetApp/OpenZFS)
│   │   │   ├── Scheduled (hourly/daily/weekly)
│   │   │   ├── Preserves POSIX/SMB permissions + metadata
│   │   │   └── 10 Gbps per task, bandwidth-limitable
│   │   └── AWS Transfer Family
│   │       ├── FTP/FTPS/SFTP → S3/EFS
│   │       ├── FTP = VPC ONLY
│   │       ├── Multi-AZ, scalable
│   │       ├── $ per endpoint-hour + data transfer
│   │       ├── Auth → built-in, AD, LDAP, Okta, Cognito, custom
│   │       └── Uses → file sharing, public data, CRM/ERP
│   │
│   ├── NETWORKING & CONTENT DELIVERY
│   │   ├── Amazon CloudFront
│   │   │   ├── CDN, 100s PoPs globally
│   │   │   ├── DDoS (Shield + WAF)
│   │   │   ├── Origins
│   │   │   │   ├── S3 (cache/upload) w/ OAC
│   │   │   │   ├── VPC Origin (ALB/NLB/EC2 private)
│   │   │   │   └── Custom HTTP (S3 site, any public HTTP)
│   │   │   └── vs S3 CRR
│   │   │       ├── CF → global edge, TTL, static content
│   │   │       └── CRR → region-specific, near real-time, dynamic
│   │   ├── Load Balancers
│   │   │   ├── Application LB → Layer 7, HTTP/S/gRPC
│   │   │   ├── Network LB → Layer 4, TCP/UDP, ultra-high perf, Elastic IP
│   │   │   ├── Gateway LB → Layer 3, GENEVE, security appliances
│   │   │   └── Classic LB → retired 2023
│   │   ├── AWS Global Accelerator
│   │   │   ├── 2 Anycast IPs
│   │   │   ├── Internal AWS network routing
│   │   │   ├── Works w/ EIP, EC2, ALB, NLB
│   │   │   ├── Health checks → <1min failover
│   │   │   ├── Shield DDoS
│   │   │   └── vs CloudFront
│   │   │       ├── CF → content caching at edge
│   │   │       └── GA → TCP/UDP proxy, static IPs, gaming/IoT/VoIP
│   │   └── Amazon Route 53
│   │       ├── Managed authoritative DNS + domain registrar
│   │       ├── 100% availability SLA
│   │       ├── Records → A, AAAA, CNAME, NS (+ advanced types)
│   │       │   └── CNAME → can't create for Zone Apex
│   │       ├── Hosted Zones
│   │       │   ├── Public → internet
│   │       │   └── Private → within VPC(s)
│   │       └── $0.50/month per hosted zone
│   │
│   └── STORAGE
│       ├── EBS
│       │   ├── Network drive, latency
│       │   ├── Locked to 1 AZ (snapshot to move)
│       │   ├── Provisioned capacity (GB + IOPS)
│       │   ├── Default → root EBS deleted on termination
│       │   └── Default → other EBS preserved
│       └── EFS
│           ├── Managed NFS, multi-AZ
│           ├── Linux only (POSIX)
│           ├── NFSv4.1 protocol
│           ├── Security Groups
│           ├── KMS at-rest encryption
│           ├── 1000s of concurrent clients, 10GB+/s
│           ├── Performance Modes → General Purpose (default), Max I/O
│           ├── Throughput Modes → Bursting, Provisioned, Elastic
│           ├── Storage Classes
│           │   ├── Standard → frequent
│           │   ├── IA → infrequent (retrieval cost)
│           │   ├── Archive → rarely accessed (50% cheaper)
│           │   └── Lifecycle policies for transitions
│           └── Availability
│               ├── Standard → Multi-AZ (prod)
│               └── One Zone → 1 AZ (dev, 90% cost savings)
│
├── [X] ARCHITECTURAL DECISIONS
│   │
│   ├── VECTOR STORE CHOICES
│   │   ├── OpenSearch managed → control + search features ($$-$$$, medium ops)
│   │   ├── OpenSearch Serverless → variable traffic, low-ops ($-$$)
│ │ ├── Kendra → enterprise doc search + ACL enforcement ($$$)
│   │   ├── Aurora + pgvector → SQL-first, compliance, GovCloud ($$)
│ │ ├── Neptune Analytics → graph relationships + vectors ($$-$$$)
│   │   └── S3 Vectors → massive scale, cost-first ($, metadata/filter limits, slow)
│ │
│ ├── DECISION KEYWORDS
│ │ ├── SharePoint/Confluence/ACLs → Kendra
│ │ ├── Graph/fraud/lineage/dependencies → Neptune Analytics
│ │ ├── Postgres + joins + vector → Aurora + pgvector
│ │ ├── Huge corpus + cost pressure → S3 Vectors
│ │ ├── Full search + tuning control → OpenSearch managed
│ │ └── Unpredictable traffic + minimize ops → OpenSearch Serverless
│ │
│ ├── OPENSEARCH vs SERVERLESS
│ │ ├── Billing → always-on vs per-request+storage
│ │ ├── Tuning → full control vs limited
│ │ ├── Latency → predictable vs variable
│ │ ├── Scaling → manual/auto vs automatic
│ │ └── Exam bias → "fine-grained control" vs "unpredictable traffic"
│ │
│ ├── STEP FUNCTIONS TRIGGERS
│ │ ├── Auditable state transitions
│ │ ├── Retry + failure isolation
│ │ ├── Explicit approval steps
│ │ └── Human approval
│ │
│ ├── INTERNAL Q&A CHATBOT PATTERN
│ │ ├── API Gateway → Lambda
│ │ ├── Cognito auth (user context → Kendra)
│ │ ├── Kendra for doc-level ACL (SharePoint)
│ │ └── Bedrock for retrieval + generation
│ │
│ └── CUSTOMER-FACING CHATBOT PATTERN
│ ├── WAF + CloudFront for external systems
│ ├── API Gateway → Lambda → Bedrock
│ ├── OpenSearch (Serverless) for RAG
│ ├── Cognito if PII/private
│ ├── Guardrails required
│ └── Ingestion → S3 → EventBridge → Lambda → Bedrock → OpenSearch
│
└── [XI] EXAM PREP
├── Duration → 3 hours (170 min); beta had 205 min
├── Questions → 75 (85 during beta)
├── Cost → $300 ($150 beta)
├── Question Types
│ ├── Multiple Choice (1 of 4)
│ ├── Multiple Response (2+ of 5+) → NO partial credit
│ ├── Ordering (3-5 in sequence) → NO partial credit; NEW
│ └── Matching (3-7 pairs) → NO partial credit; NEW
│ └── "Case Study" type DROPPED
├── Strategies
│ ├── 2-2.5 min/question pacing
│ ├── Flag + return
│ ├── Process of elimination
│ ├── Understand optimization target + requirements
│ └── Keep calm (100% not required)
└── Resources
├── AWS Skill Builder (Standard Exam Prep Plan, free)
├── Official Practice Question Set (20 Q)
├── Full-length practice exam
└── Amazon's Exam Guide
