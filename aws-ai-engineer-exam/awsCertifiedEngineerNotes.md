# AWS Certified Generative AI Developer - Professional (AIP-C01)
## Complete Hierarchical Course Outline
 
---
 
# 1. Course Introduction
 
## Table of Contents
- Generative AI Fundamentals and Bedrock
- Managing Data for Generative AI
- Agentic AI
- Operations Efficiency and Optimization
- Managing Models with SageMaker AI
- More Tools for Building AI Applications
- Governance and QA
- Security, Identity, and Compliance
- Other Services You Should Know (Analytics, Compute/Containers, Database, Dev Tools, ML, Management, Migration, Networking, Storage)
- Exam Preparation
## What We'll Cover: GenAI Fundamentals and Bedrock
- Foundation Models (FM's)
- Fine Tuning
- Retrieval-Augmented Generation
- Knowledge Bases / Vector DB's
- Optimizing embedding vectors
- Guardrails
- Prompt Engineering
- Bedrock Prompt Flows
- Enterprise Integration
## Managing Data for Generative AI
- Transforming and structuring your data
- Bedrock Data Manipulation
- SageMaker Data Wrangler
- AWS Transcribe, Amazon Comprehend
- AWS Glue
- CloudWatch
- Vector Storage with OpenSearch
- RDS / Aurora
- DynamoDB
- S3
## Agentic AI
- Agents in Bedrock
- Multi-agent workflows
- Strands Agents
- AgentCore
- Humans in the Loop
- Amazon Q
## Operational Efficiency and Optimization
- Context Management – Token Efficiency
- Model selection
- Resource utilization and throughput
- Caching
- Building responsive and resilient AI systems
- Optimizing Foundation Model system performance
- Resource allocation systems
- Bedrock Cross-Region Inference
## Managing Models with SageMaker AI
- Processing, Training, and Deployment
- Deployment Safeguards and Optimization
- Ground Truth
- Model Monitor
- Clarify
- Model Registry
- Lineage Tracking
- Edge Computing with Neo
- Pipelines
## More Tools for Building AI Apps
- AWS Lambda
- API Gateway
- AppConfig
- Step Functions
- EventBridge
- DevOps: CodeBuild, CodeDeploy, CodePipeline
- AppSync
- AWS Outposts
- AWS Wavelength
- SQS
- Amplify
## Governance and QA
- Bedrock Prompt Management
- Agent Tracing
- Evaluation Techniques
- Responsible AI
- CloudWatch
- CloudTrail
- X-Ray
- Lake Formation
## Security, Identity, and Compliance
- IAM
- KMS
- Macie
- Secrets Manager
- Cognito
- WAF (Web Application Firewall)
- VPC
- PrivateLink
## Target Candidate
- 2+ years experience with AWS and ML/AI
- 1+ year of hands-on experience implementing GenAI solutions
- AWS basics (storage, security, etc.)
- Should NOT be your first AWS certification
- NOT required: Model development and training, Advanced ML, Data/Feature Engineering
---
 
# 2. Generative AI Fundamentals and Bedrock
 
## Foundation Models
- Giant, pre-trained transformer models being fine-tuned for specific tasks
- Examples: GPT-n (OpenAI), Claude (Anthropic), DALL-E, LLaMa (Meta), DeepSeek, Nova
## AWS Foundation Models (Base Models)
- **Jurassic-2 (AI21labs)**: Multilingual LLMs (Spanish, French, German, Portuguese, Italian, Dutch)
- **Claude (Anthropic)**: Conversations, Q&A, workflow automation
- **Stable Diffusion (stability.ai)**: Image, art, logo, design generation
- **Llama (Meta)**: LLM
- **Amazon Titan**: Text summarization, generation, Q&A, embeddings, personalization, search
- **Amazon Nova Pro**: LLM portfolio
- **Amazon Nova Reels**: Video
## Amazon Bedrock
- API for generative AI Foundation Models
- Invoke chat, text, or image models
- Pre-built, fine-tuned, or your own models
- Third-party models bill you through AWS
- Support for RAG and LLM agents
- Serverless
- Integrates with SageMaker Canvas
## The Bedrock API Endpoints
- **bedrock**: Manage, deploy, train models
- **bedrock-runtime**: Perform inference (Converse, ConverseStream, InvokeModel, InvokeModelWithResponseStream)
- **bedrock-agent**: Manage, deploy, train LLM agents and knowledge bases
- **bedrock-agent-runtime**: Inference against agents/KBs (InvokeAgent, Retrieve, RetrieveAndGenerate)
## More on the Converse API
- Unified API for models that support messages
- Specify prompt in messages field (or ARN to prompt management)
- Specify modelId
- Optional: Model-specific fields, Guardrails, Config (max tokens, temperature), Prompt variables, Tools
## Bedrock IAM permissions
- Must use with IAM user (not root)
- Permissions: AmazonBedrockFullAccess, AmazonBedrockReadOnly
## Amazon Bedrock: Model Access
- AWS phasing out need to request access to specific models
- Check pricing at aws.amazon.com/bedrock/pricing
## Let's Play (Playgrounds)
- Chat, Text, Images playgrounds
- Must have model access first
- Useful for evaluating custom or imported models
## Fine-tuning
- Adapt existing LLM to specific use case
- Additional training using your own data
- Eliminates need for big conversation prompts
- Saves on tokens long term
- Can fine-tune a fine-tuned model
- Applications: chatbot personality, recent data training, proprietary data, specific applications
## Fine-tuning in Bedrock: "Custom Models"
- Titan, Cohere, Meta models can be fine-tuned
- Text models: labeled training pairs (prompts/completions) in S3
- Image models: pairs of image S3 paths to descriptions
- Use VPC and PrivateLink for sensitive data
- Can be expensive
## "Continued Pre-Training"
- Like fine-tuning but with unlabeled data
- Feed text to familiarize model
- Uses own business documents
- Includes extra data into model itself
## Low-Rank Adaptation (LoRA)
- Don't update entire model — add "low-rank matrices" to attention weights
- At inference, fine-tuned weights added into base model
- Base model remains unchanged
- Very efficient for storage, training, inference
- Different from "adapter layer" added to top
## Retrieval Augmented Generation (RAG)
- Like an open-book exam for LLMs
- Query external database for answers
- Work answers into LLM prompt
- Or use tools/functions to incorporate search
## RAG: Pros and Cons
- **Pros**: Faster/cheaper than fine-tuning, easy info updates, semantic search via vectors, prevents hallucinations, easy "AI search"
- **Cons**: Overcomplicated search engine, sensitive to prompt templates, non-deterministic, can still hallucinate, sensitive to retrieval relevancy
## RAG: Example Approach (Jeopardy!)
- Query Encoder → Retriever → Database → Generator
- Hands generator potential answers from external database
## Choosing a Database for RAG
- Graph database (Neo4j) for recommendations/relationships
- OpenSearch for traditional text search (TF/IDF)
- Most RAG examples use Vector database
- Elasticsearch/OpenSearch can function as vector DB
## Embeddings
- Big vector associated with data
- Point in multi-dimensional space (100s-1000s of dimensions)
- Similar items close together
- Use embedding base models (Titan) to compute en masse
## Vector Databases
- Stores data alongside computed embedding vectors
- Retrieval: compute embedding for search, query top items by K-Nearest Neighbor
- Examples: OpenSearch, SQL, Neptune, Redis, MongoDB, Cassandra
- Purpose-built: Pinecone, Weaviate (commercial); Chroma, Marqo, Vespa, Qdrant, LanceDB, Milvus (open source)
## RAG in Bedrock: Knowledge Bases
- Upload documents/structured data via S3
- Other sources: web crawler, Confluence, Salesforce, SharePoint
- Must use embedding model (Cohere or Amazon Titan)
- Vector store: serverless OpenSearch, MemoryDB, Aurora, MongoDB Atlas, Pinecone, Redis Enterprise
- Control chunking of data
## Using Knowledge Bases
- "Chat with your document" — automatic RAG
- Integrate into application directly
- Incorporate into agent ("Agentic RAG")
## Breaking up the R in RAG
- Pre-Retrieval: Indexing, Granularity/chunking, Data extraction, Query Rewriting
- Retrieval
- Post-Retrieval
## Pre-Retrieval (Chunking)
- What to store in your database
- Data granularity matters
- Process of splitting data = CHUNKING
## More on Chunking
- Stay within token limits
- Semantic Chunking ensures each chunk has independent info
- Embedding-based (LlamaIndex/Langchain)
- Model-based (BERT)
- LLM-based (costly)
## Chunking with Bedrock: Standard Chunking
- **Fixed Size**: specify tokens per chunk and overlap percentage
- **Default**: 300 tokens per chunk, honoring sentence boundaries
- **No chunking**: every document is a chunk
## Chunking with Bedrock: Hierarchical Chunking
- Nested parent/child chunks
- Initial search hits child chunks
- Replaces with parent chunks for context
- Better precision + comprehensiveness
## Chunking with Bedrock: Semantic Chunking
- FM breaks chunks based on semantic content
- Specify: Maximum tokens, Buffer size, Breakpoint percentile threshold
- Costs money (charged for FM used)
## Optimizing your Embeddings
- Smaller vector sizes reduce cost
- Smaller vectors = fewer dimensions = less cost
- Tradeoff with retrieval performance
- Titan default 1024+ dimensions
- Balance dimensionality with domain fit
## Sparse vs. Dense Embeddings
- **Sparse**: large mostly empty vectors (one-hot encoding)
- **Dense**: smaller vectors with semantic info (commonly used)
- Tradeoff: sparse give greater similarity factors; dense more efficient
- Cosine similarity common measure
## Optimizing Retrieval with Metadata
- Vector DB stores more than vectors and chunk text
- Bedrock KBs treat columns as content vs. metadata via metadata.json
- Add metadata tags for topics, sections for better retrieval
- Examples: Document ID, category, access control, data lineage
## Keeping Your KB Up to Date
- New/changed content triggers Lambda function
- Lambda generates new embeddings
- Batch-generate for efficiency
- Sync on schedule rather than every change
## Measuring your RAG System
- Bedrock RAG evaluation jobs measure:
  - Correctness, Completeness, Helpfulness
  - Logical coherence, Faithfulness
  - Citation precision and coverage
  - Harmfulness, Stereotyping, Refusal
## Subjective Evaluation Approach
- Provide "ground truth" of good responses
- Prompt dataset in JSON with prompts and reference responses
- Optional reference contexts
- LLM as a judge (Llama, Claude, Nova, Mistral)
## Multimodal Models and Pipelines
- Mixing different media types (text, images, audio, video, documents)
- Requires specialized encoders
- Bedrock multimodal models: Claude, Nova, Titan
- Multimodal embedding models convert types to compatible vectors
## Multimodal Input Data Preparation
- Titan Multimodal Embeddings G1 needs structured JSON
- Image data is base64-encoded
- Data pipeline performs conversion (SageMaker, Glue)
## Amazon Bedrock Guardrails
- Content filtering for prompts and responses
- Word filtering, Topic filtering, Profanities
- PII removal/masking
- **Contextual Grounding Check**: prevents hallucination, measures grounding and relevance
- Configure blocked message response
## Bedrock Guardrails – Automated Reasoning Checks
- Enforce complex policies (mortgage, medical)
- Detect hallucinations
- Provide policy as PDF document
- Use CreateAutomatedReasoningPolicy API
- Bedrock breaks policy into structured rules
## Token-Level Redaction
- Beyond Guardrails
- Filter sensitive tokens before request hits model
- Filter sensitive tokens on output
- Custom pre/post-processing handlers
- Pattern matching, Named Entity Recognition (NER)
- Amazon Comprehend can be used
## Prompt Management with Amazon Bedrock
- Reusable prompts stored
- Versioned
- Variables in double curly braces: {{genre}}, {{number}}
- Prompt Variants for different models/configs
- Prompt Builder tool in Bedrock console
- Associate Tools and Caching
- Deploy prompts within a Flow
## Amazon Bedrock Flows
- Mechanism for chaining prompts and models
- Flow = Nodes and Connections
- Connections may be conditional
- Generate visually with Flow Builder or via JSON
## Using Bedrock Flows with Prompts
- Stored prompts as flow components
- Chain together for complex tasks with conditions
- Enforce pre/post-processing
## Enforcing Structured Data Responses
- **Approach 1**: Specify in prompt with numbered instructions, schema, example output
- **Approach 2**: Tool Use in Bedrock's Converse API
- Modern FMs connect to external Tools (agentic AI)
- Make it look like calling a tool with given schema
- Called "response format template"
## Benefits of Effective Prompting
- Boost model abilities and improve safety
- Augment with domain knowledge and external tools without changing parameters
- Interact to grasp full capabilities
- Better quality outputs through better quality inputs
## Anatomy of a Prompt
- Instructions
- Context
- Input data
- Output indicator
## Prompt Best Practices
- Clear and concise
- Include context
- Specify desired response type
- Specify desired output at end of prompt
- Phrase input as a question
- Provide example response
- Break up complex tasks
- Experiment, be creative
## Types of Prompts
- **Zero-shot**: No examples, relies on large models
- **Few-shot**: Provide examples of desired responses
- **Chain of Thought (CoT)**: "Think step by step"
## Avoiding Prompt Mis-use
- **Prompt injection**: Influence response through specific instructions, bypass guardrails
- **System prompt** applies to whole conversation
- **Prompt leaking**: PII, "Tell me your initial instructions"
## Mitigating Bias
- Hidden biases in training data → biases in LLM
- **Disambiguation**: Make user specify race/gender/etc.
- TIED (Text-to-image disambiguation framework)
- TAB (Text-to-image ambiguity benchmark)
- Few-shot learning
- System prompt enforce diversity
- Fix/enhance training data
- Counterfactual data augmentation
- Detect/Segment/Augment
## Specific Points for Enterprise Integration
- Bedrock KBs integrate with S3, SharePoint, Confluence
- **Cross-account access**: OpenSearch has remote-inference connector
- Need IAM roles
- Bedrock account needs role for InvokeModel access from OpenSearch account
- **Event-Driven architecture**: SQS, Kafka, pub/sub for loose coupling
## AWS Well-Architected Generative AI Lens
- Overview of GenAI and best practices
- Aligns to six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability
- URL: docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens
## The Generative AI Lifecycle
- Scoping
- Model Selection
- Model Customization
- Development
- Integration
- Deployment
- Continuous Improvement
---
 
# 3. Managing Data for Generative AI
 
## Structured Data: Bedrock API Requests
- Bedrock expects JSON format payloads
- Native structure for models
## Structured Data for SageMaker AI Endpoints
- LLMs typically expect JSON
- Classical ML may use CSV
- SageMaker doesn't format input — your app/endpoint responsible
## Dealing with Unstructured Text
- Raw text loses structure (headings, sections, metadata, tables)
- Convert to HTML to preserve structure
- Tools: pandoc, Amazon Textract, Amazon Comprehend
- Ingestion pipeline on AWS Glue
- Newer: Bedrock Data Automation (BDA)
## Divider Strings for Segmenting Data
- Better chunking when ingesting to vector store
- Lambda Preprocessor in KB converts HTML tags to dividers
- AWS Glue ETL can do it as part of pipeline
## Formatting Data for Conversations
- Bedrock's Converse API requires JSON with:
  - Role (who is "talking")
  - Content
## What is Bedrock Data Automation (BDA)?
- Extracts structured data from anything
- Multi-modal: documents, images, videos, audio
- Used for: vector store prep, IDP, video analysis (scene summaries, explicit content, text in video, ads)
## BDA Concepts
- **Standard Output**: Auto-guesses format
- **Custom Output**: Customize via Blueprints (standard like US Driver License, or define your own)
- **Project**: Stores output configs, may include many Blueprints
- API: InvokeDataAutomationAsync
## BDA Document Processing
- Accepts: PDF, TIFF, JPEG, PNG, DOCX
- Outputs: JSON or JSON+files (CSV, markdown, HTML)
- Granularity: Page-level, element-level (default), word-level
- Bounding boxes and generative summaries
## BDA Image Processing
- Accepts: JPEG, PNG
- Generates: Image summary/caption, IAB Taxonomy, Logos, Text in images, Content moderation
## BDA Video Processing
- Accepts: MP4, MOV, AVI, MKV, WEBM
- Extracts: Full video summary, Chapter summaries, IAB Taxonomy, Transcript, Text in video, Logos, Content Moderation
## BDA Audio Processing
- Accepts: AMR, FLAC, M4A, MP3, Ogg, WAV
- Extracts: Summary, Full transcript, Speaker/Channel labeling, Topics, Content moderation
## BDA Blueprints for Custom Output
- Basic fields (explicit or implicit/transformed)
- Table fields
- Groups (for organizing fields)
- Custom types (e.g., "address" with city, street, zip)
- Create from prompt
- Pre-existing blueprints for common documents
## Uses of BDA Blueprints
- **Classification**: Auto-classify documents
- **Extraction**: Extract specific fields
- **Normalization**: Key Normalization, Value Normalization
- **Transformation**: Split/restructure data fields
- **Validation**: Ensure accuracy, ranges, sizes, types
## SageMaker Data Wrangler
- Visual interface in SageMaker Studio
- Prepare data for ML
- Import, Visualize, Transform (300+ transformations)
- Custom xforms with pandas, PySpark, PySpark SQL
- "Quick Model" to train and measure
## Data Wrangler: Notable Capabilities
- Transform image data (resize, enhance, corrupt)
- Balance data (oversampling, undersampling, SMOTE)
- Impute missing data
- Handle outliers
- Dimensionality reduction (PCA)
## Data Wrangler Sources
- S3, Athena, Redshift, Lake Formation
- SageMaker Feature Store
- SageMaker Processing/Pipelines/Feature Store notebook
- JDBC (Databricks, SaaS)
## Data Wrangler Troubleshooting
- Studio user needs IAM roles
- Permissions on data sources
- Add AmazonSageMakerFullAccess policy
- EC2 instance limit — request quota increase
## What is AWS Glue?
- Serverless discovery and definition of tables/schema
- S3 data lakes, RDS, Redshift, DynamoDB, SQL DBs
- Custom ETL jobs (trigger-driven, scheduled, on-demand)
- Fully managed
## Glue Crawler / Data Catalog
- Crawler scans data in S3, creates schema
- Runs periodically
- Populates Glue Data Catalog (only table definition)
- Original data stays in S3
- Treat unstructured data as structured (Redshift Spectrum, Athena, EMR, QuickSight)
## Glue and S3 Partitions
- Crawler extracts partitions based on S3 organization
- Time-based queries: yyyy/mm/dd/device
- Device-based queries: device/yyyy/mm/dd
## AWS Glue Studio
- Visual interface for ETL workflows
- Visual job editor, DAGs
- Sources: S3, Kinesis, Kafka, JDBC
- Transform/sample/join data
- Target S3 or Glue Data Catalog
- Visual job dashboard
## AWS Glue Data Quality
- Rules created manually or auto-recommended
- Integrates into Glue jobs
- Uses Data Quality Definition Language (DQDL)
- Fail job or report to CloudWatch
## Amazon CloudWatch Metrics
- Metrics for every AWS service
- Variables to monitor (CPUUtilization, NetworkIn)
- Belong to namespaces
- Dimensions (up to 30 per metric)
- Timestamps
- CloudWatch dashboards
- Custom Metrics
## CloudWatch Metric Streams
- Continually stream metrics to destination
- Near-real-time, low latency
- Targets: Kinesis Data Firehose, Datadog, Dynatrace, New Relic, Splunk, Sumo Logic
- Filter to subset of metrics
## Amazon Transcribe
- Converts speech to text
- Uses Automatic Speech Recognition (ASR) deep learning
- Auto-remove PII via Redaction
- Automatic Language Identification for multi-lingual
- Use cases: customer service calls, captioning, searchable archives
## Amazon Transcribe – Improving Accuracy
- **Custom Vocabularies (for words)**: specific words, phrases, brand names, acronyms
- **Custom Language Models (for context)**: train on your domain text
- Use both for highest accuracy
## Transcribe – Toxicity Detection
- ML-powered voice-based detection
- Speech cues (tone/pitch) and text cues
- Categories: sexual harassment, hate speech, threat, abuse, profanity, insult, graphic
## Amazon Comprehend
- Natural Language Processing (NLP)
- Fully managed, serverless
- Finds insights/relationships in text
- Detects: language, key phrases, places, people, brands, events
- Sentiment analysis
- Tokenization and parts of speech
- Topic modeling
## Comprehend – Custom Classification
- Organize documents into categories
- Categorize emails for guidance
- Supports text, PDF, Word, images
- Real-time (sync) or Async batch analysis
## Named Entity Recognition (NER)
- Extracts predefined general-purpose entities
- People, places, organizations, dates, standard categories
## Comprehend – Custom Entity Recognition
- Analyze for specific terms/noun phrases
- Extract policy numbers, escalation phrases
- Train with custom data
- Real-time or Async
## Using Comprehend and Lambda for Data Quality
- Lambda calls Comprehend before Bedrock
- Redact PII, Extract entities, Detect language, Classify
- Applications: clean transcripts, pre-screen content
## Amazon Comprehend Medical
- HIPAA-certified for medical use
- Pre-trained for prescriptions, procedures, diagnoses, PHI
- DetectPHI API (vs DetectEntities)
- Search medical ontologies
- VPC Endpoints/PrivateLink integration
## What is OpenSearch?
- Fork of Elasticsearch and Kibana
- Search engine, analysis tool, visualization (Dashboards = Kibana)
- Data pipeline (Kinesis replaces Beats & LogStash)
- Horizontally scalable
## OpenSearch Applications
- Full-text search
- Log analytics
- Application monitoring
- Security analytics
- Clickstream analytics
## OpenSearch Concepts
- **Documents**: JSON data being searched, unique ID and type
- **Indices**: Power search into all docs in a collection
- **Types**: Schema and mapping for documents
## Index Sharding
- Split into shards
- Documents hashed to shard
- Each shard on different node
- Each shard is self-contained Lucene index
## OpenSearch Redundancy
- Primary and replica shards
- Round-robin requests
- Writes routed to primary, replicated
- Reads from primary or any replica
## Amazon OpenSearch Service (Managed)
- Fully-managed (separate serverless option)
- Scale up/down without downtime (not automatic)
- Pay for use (instance-hours, storage, transfer)
- Network isolation
- AWS integration: S3, Kinesis Data Streams, DynamoDB Streams, CloudWatch/CloudTrail
- Zone awareness
## OpenSearch Options
- Dedicated master node(s)
- Choice of count and instance types
- "Domains"
- Snapshots to S3
- Zone Awareness
## Cold/Warm/UltraWarm/Hot Storage
- **Hot**: Standard nodes, instance stores or EBS, fastest
- **UltraWarm (warm)**: S3 + caching, few writes (logs), slower but cheaper, requires dedicated master
- **Cold**: S3, even cheaper, periodic research/forensic, requires UltraWarm and dedicated master, not compatible with T2/T3
- Map users to cold_manager role with fine-grained access
- Migration between storage types possible
## Index State Management
- Automates index policies
- Delete old indices
- Read-only state after time
- Move hot → UltraWarm → cold
- Reduce replica count
- Automate snapshots
- ISM policies run every 30-48 minutes (with jitter)
- Send notifications
## More Index Management
- **Index rollups**: Periodically summarize old data, save storage, fewer fields, coarser time buckets
- **Index transforms**: Different view to analyze differently, groupings/aggregations
## Cross-cluster Replication
- Replicate indices/mappings/metadata across domains
- High availability in outage
- Geographic replication for latency
- "Follower" pulls from "Leader"
- Requires fine-grained access control and node-to-node encryption
- "Remote Reindex" copies indices on demand
## OpenSearch Stability
- 3 dedicated master nodes (avoid split brain)
- Don't run out of disk space
- **Storage minimum**: Source Data * (1 + Replicas) * 1.45
- **Shard count**: (source data + growth) * (1 + indexing overhead) / desired shard size
- Limit shards per node in rare cases
- At least 3 nodes
- Instance types: m6g.large.search, i3.4xlarge.search, i3.16xlarge.search
## OpenSearch Security
- Resource-based policies
- Identity-based policies
- IP-based policies
- Request signing
- VPC
- Cognito
## Securing Dashboards
- Cognito
- Nginx reverse proxy on EC2 forwarding to ES domain
- SSH tunnel for port 5601
- VPC Direct Connect
- VPN
## OpenSearch Anti-patterns
- OLTP (no transactions) — use RDS or DynamoDB
- Ad-hoc data querying — use Athena
- OpenSearch primarily for search & analytics
## OpenSearch Performance
- Memory pressure in JVM if:
  - Unbalanced shard allocations
  - Too many shards
- Fewer shards yields better performance with JVMMemoryPressure errors
- Delete old/unused indices
## Amazon OpenSearch Serverless
- On-demand autoscaling
- Works against "collections" (search or time series)
- Always encrypted with KMS
- Data access policies
- Encryption at rest required
- Security policies across collections
- OpenSearch Compute Units (OCUs): minimum 2 indexing, 2 search
## OpenSearch as a Vector Store
- Serverless vector stores ("serverless" doesn't mean scales to zero)
- Shut down unused serverless instances
- Primary backing for Bedrock KBs (may be subsumed by S3 vectors)
- Integrates with SageMaker AI, HuggingFace, custom models
- **Semantic search**: vector search
- **Hybrid search**: combines vector and keyword, requires filterable keyword fields
## OpenSearch Vector Engines
- Engines: FAISS, NMSLib, Apache Lucene
- **Exact Nearest Neighbor**: slow
- **Approximate Nearest Neighbor (ANN)**:
  - HNSW: fast, high-quality, simple, lots of RAM
  - IVF: huge datasets, trade recall for speed/memory
- **Tuning**: M (edges per node), ef_construction (KNN graph list size), ef_search (graph exploration)
## OpenSearch Vector Store: Finer Points
- **Vector compression**: Different ANN methods (HNSW, IVF)
- **Binary vectors**: Bit sequences, 32x compression
- **FP16**: Scalar quantization, 16-bit instead of 32-bit
- Dense embeddings add up fast
## OpenSearch Sharding Strategies
- Balance shard size and CPU ratio
- Larger shards for semantic search (30-50 GB)
- Smaller for hybrid (10-30 GB)
- Vector search benefits from fewer, larger shards
- OpenSearch Serverless is automatic
- **Multi-index approaches**: Different doc types own indices, different embeddings per corpus, query routing needed
## OpenSearch Hierarchical Indices
- Top-level summary index (small, fast)
- Routes to detailed-data index per domain
- Specialized indices with own embeddings, shards, tuning
- FM can route to right index
## OpenSearch Neural Plugin
- Integrate embedding model into ingest pipeline
- "Neural queries" accept text, generate embeddings
- Alternative to built-in Bedrock KB integration
- OpenSearch calls Bedrock model for embeddings
## Amazon S3 Vectors
- Up to 90% cheaper, simpler
- Create S3 vector bucket
- Create vector index (specify dimensions, distance metric)
- Store embeddings with put_vectors
- Include metadata
- Query with query_vectors
## S3 Vectors Put Request Example
- s3vectors.put_vectors with bucket, index, vectors
- Each vector has key, data (float32 embeddings), metadata
## Alternative API: s3vectors-embed-cli
- Use boto3, AWS CLI, or dedicated S3 vectors CLI (open source GitHub)
- s3vectors-embed put: Convert text/images to embeddings via Bedrock, store
- s3vectors-embed query: Generate query embedding, query index
## S3 Vectors Integration
- Generate own vectors with embedding model
- Or fully integrated with Bedrock Knowledge Bases
- Integrates with Bedrock within SageMaker Unified Studio
## S3 Vectors: More Specifics
- Strongly consistent (immediately available)
- Auto-optimized over time
- Performance: 100ms-1s
- AWS recommends hybrid with OpenSearch for performance
- "Tiered search strategy": S3 for infrequently queried
- Connectivity with OpenSearch (copies/exports — pay for both)
- Or use OpenSearch with S3 Vectors engine (managed clusters only)
- **Limits**: Max 10,000 indices per bucket, 2B vectors per index
## S3 Vectors: Best Practices
- Insert/delete in large batches (500 per API call)
- Concurrent requests for smaller batches (up to 2500/sec)
- Retry mechanism (429 errors)
- Multiple indexes (per-index performance, multi-tenancy)
- Mark non-filtered metadata as non-filterable
## Amazon RDS Overview
- Relational Database Service
- Managed DB for SQL
- Engines: Postgres, MySQL, MariaDB, Oracle, SQL Server, IBM DB2, Aurora
## RDS vs EC2 DB Deployment
- Auto provisioning, OS patching
- Continuous backups, Point-in-Time Restore
- Monitoring dashboards
- Read replicas for performance
- Multi-AZ for DR
- Maintenance windows
- Vertical/horizontal scaling
- EBS storage
- Can't SSH into instances
## RDS – Storage Auto Scaling
- Dynamically increases storage
- Scales when running out of free DB storage
- Set Maximum Storage Threshold
- Triggers when:
  - Free storage < 10% allocated
  - Low-storage > 5 minutes
  - 6 hours since last modification
- All RDS engines
## Using RDS with S3 Document Repositories
- RDS as vector store (RDS SQL Server Vector Store)
- RDS for structured data, points to S3 for unstructured
- Common pattern: RAG vector store backed by RDS, returned data points to S3 content
## Amazon Aurora
- AWS proprietary (not open sourced)
- Postgres and MySQL supported
- "AWS cloud optimized" — 5x MySQL, 3x Postgres performance
- Storage grows in 10GB increments up to 256 TB
- Up to 15 replicas, sub 10ms lag
- Instantaneous failover, HA native
- Costs 20% more than RDS but more efficient
## Aurora High Availability and Read Scaling
- 6 copies across 3 AZ (4 for writes, 3 for reads)
- Self-healing peer-to-peer replication
- Storage striped across 100s of volumes
- One Aurora instance writes (master)
- Auto failover < 30 seconds
- Master + up to 15 read replicas
- Cross Region Replication
## Aurora Auto Scaling
- DB Cluster with shared storage volume (10GB-256TB)
- Reader Endpoint with Connection Load Balancing
- Writer Endpoint pointing to master
## Features of Aurora
- Automatic fail-over
- Backup and Recovery
- Isolation and security
- Industry compliance
- Push-button scaling
- Automated Patching with Zero Downtime
- Advanced Monitoring
- Routine Maintenance
- Backtrack: restore at any time without backups
## Amazon Aurora as a Vector Store
- pgvector extension (Trusted Language Extensions for PostgreSQL)
- New "vector" column type
- Compute cosine, L2, inner product distances
- Similarity search with IVF or HNSW
- SQL vector operators
- Advantage: complex filtering logic
- Store structured and vector together
- Good for small/medium RAG with mostly structured data
## Traditional Architecture
- RDBMS with SQL
- Strong data modeling requirements
- Joins, aggregations, complex computations
- Vertical scaling (CPU/RAM/IO)
- Horizontal scaling (Read Replicas)
## NoSQL Databases
- Non-relational, distributed
- MongoDB, DynamoDB
- No (or limited) joins
- All data in one row
- No aggregations (SUM, AVG)
- Horizontal scaling
- Different modeling, different query thinking
## Amazon DynamoDB
- Fully managed, highly available with multi-AZ replication
- NoSQL — not relational
- Massive workloads, distributed
- Millions of req/sec, trillions of rows, 100s TB
- Fast and consistent low latency
- IAM integration
- DynamoDB Streams for event-driven
- Low cost, auto-scaling
- Standard & Infrequent Access (IA) Table Class
## DynamoDB Basics
- Made of Tables
- Each table has Primary Key (decided at creation)
- Infinite items (rows)
- Attributes can be added (can be null)
- Item max size 400KB
- Data types: Scalar (String, Number, Binary, Boolean, Null), Document (List, Map), Set (String/Number/Binary Set)
## DynamoDB Primary Keys
- **Option 1: Partition Key (HASH)** — must be unique and diverse
- **Option 2: Partition Key + Sort Key (HASH+RANGE)** — combination unique, data grouped by partition
## DynamoDB Partition Keys (Best Practices)
- Highest cardinality is best candidate
- Don't use values that are skewed/limited
## DynamoDB Read/Write Capacity Modes
- **Provisioned**: Specify reads/writes per second, plan capacity, pay for provisioned
- **On-Demand (default)**: Auto scale, no planning, pay-as-you-go, more expensive
- Switch between modes once every 24 hours
## R/W Capacity – Provisioned
- Read Capacity Units (RCU)
- Write Capacity Units (WCU)
- Auto-scaling option
- Burst Capacity for temporary exceeds
- ProvisionedThroughputExceededException if exceeded
- Exponential backoff retry advised
## DynamoDB – Write Capacity Units (WCU)
- 1 WCU = 1 write/sec for item up to 1 KB
- Larger items consume more WCUs
- Examples: 10 items/sec at 2KB = 20 WCUs
## Strongly Consistent vs. Eventually Consistent Read
- **Eventually Consistent (default)**: Possible stale data after write
- **Strongly Consistent**: Correct data after write
- Set ConsistentRead=True (GetItem, BatchGetItem, Query, Scan)
- Consumes 2x RCU
## DynamoDB – Read Capacity Units (RCU)
- 1 RCU = 1 Strongly Consistent Read/sec or 2 Eventually/sec for item up to 4 KB
- Larger items consume more
- Examples: 10 SC reads at 4KB = 10 RCUs
## DynamoDB Partitions Internal
- Data in partitions
- Hash partition keys
- Compute partitions:
  - by capacity = (RCUs/3000) + (WCUs/1000)
  - by size = TotalSize/10GB
  - = ceil(max of both)
- WCUs/RCUs spread evenly
## DynamoDB Throttling
- ProvisionedThroughputExceededException
- Reasons: Hot Keys, Hot Partitions, Very large items
- Solutions: Exponential backoff, distribute partition keys, DAX for RCU issues
## R/W Capacity – On-Demand
- Auto scale, no planning
- Unlimited WCU & RCU, no throttle, more expensive
- Read Request Units (RRU), Write Request Units (WRU)
- 2.5x more expensive than provisioned
- Use cases: unknown/unpredictable workloads
## DynamoDB Writing Data
- **PutItem**: Create or fully replace, consumes WCUs
- **UpdateItem**: Edit existing, add new, Atomic Counters
- **Conditional Writes**: Accept if conditions met, concurrent access, no performance impact
## DynamoDB Reading Data – GetItem
- Read by Primary key (HASH or HASH+RANGE)
- Eventually Consistent (default)
- Strongly Consistent option (more RCU)
- ProjectionExpression for certain attributes
## DynamoDB Reading – Query
- Returns by:
  - KeyConditionExpression (Partition Key, Sort Key with =, <, >, BETWEEN, etc.)
  - FilterExpression (non-key attributes after Query)
- Returns Limit items or up to 1 MB
- Pagination
- Query table, LSI, or GSI
## DynamoDB Reading – Scan
- Scans entire table, filters out (inefficient)
- Up to 1 MB, use pagination
- Consumes lots of RCU
- Limit impact via Limit or smaller results
- **Parallel Scan**: Multiple workers, increases throughput and RCU
- ProjectionExpression & FilterExpression supported
## DynamoDB Deleting Data
- **DeleteItem**: Individual, conditional delete
- **DeleteTable**: Whole table, faster than DeleteItem on all
## DynamoDB Batch Operations
- Save latency, parallel execution
- **BatchWriteItem**: Up to 25 PutItem/DeleteItem, 16 MB, 400 KB per item, no UpdateItem, UnprocessedItems
- **BatchGetItem**: Up to 100 items, 16 MB, parallel, UnprocessedKeys
## DynamoDB PartiQL
- SQL-compatible query language
- Select/insert/update/delete with SQL
- Queries across multiple tables
- Run from: Console, NoSQL Workbench, APIs, CLI, SDK
## DynamoDB Accelerator (DAX)
- Fully-managed, highly available, in-memory cache
- Microseconds latency
- No app logic modification
- Solves "Hot Key" problem
- 5 minutes TTL default
- Up to 10 nodes in cluster
- Multi-AZ (3 nodes minimum prod)
- Secure (KMS, VPC, IAM, CloudTrail)
## DAX vs ElastiCache
- DAX: Individual objects cache, Query & Scan cache
- ElastiCache: Store Aggregation Result
## DynamoDB – Time To Live (TTL)
- Auto-delete items after expiry timestamp
- No WCUs consumed
- "Number" type, Unix Epoch timestamp
- Expired items deleted within few days
- Expired items appear in reads until deleted (filter out)
- Expired items deleted from LSIs/GSIs
- Delete enters DynamoDB Streams
- Use cases: reduce stored data, regulatory compliance
## DynamoDB with GenAI
- Not a vector store (can store but not search)
- Serves model with near real-time data
- Fast chat history storage/retrieval
- "Long term memory" for AI agents
- Context awareness in chatbots
## DynamoDB and OpenSearch
- Zero-ETL integration
- Pipeline DynamoDB → OpenSearch
- Use OpenSearch as vector store for Bedrock
- Incorporate DynamoDB data into KBs
## Keeping your Vector Store Up to Date
- Sync with new/changed data
- Incremental updates
- Real-time change detection
- Automated synchronization
- Scheduled refresh pipelines
- EventBridge support
## Vector Store Update Architecture
- S3 → EventBridge → Lambda (connector) → Bedrock
- Events, webhooks, polling
## Vector Index Maintenance
- Drift and fragmentation over time
- EventBridge schedule for periodic rebuild
- AWS Batch queues job
- Creates new embeddings, validates, swaps old → new
## Re-ranker Models in Amazon Bedrock
- Improves relevance of RAG results
- Calculates chunk relevance, orders accordingly
- Rerank operation in API
- Specify reranker model when hitting KB
- Amazon or Cohere models, limited regions
## S3 Storage Classes
- S3 Standard - General Purpose
- S3 Standard-Infrequent Access (IA)
- S3 One Zone-IA
- S3 Glacier Instant Retrieval
- S3 Glacier Flexible Retrieval
- S3 Glacier Deep Archive
- S3 Intelligent Tiering
- Move manually or via S3 Lifecycle
## S3 Durability and Availability
- **Durability**: 99.999999999% (11 9's) across multi-AZ — same all classes
- **Availability**: Varies by class (Standard 99.99% = 53 min/year unavailable)
## S3 Standard – General Purpose
- 99.99% Availability
- Frequently accessed
- Low latency, high throughput
- Sustain 2 concurrent facility failures
- Big Data analytics, mobile/gaming, content distribution
## S3 Storage – Infrequent Access
- Less frequent access, rapid when needed
- Lower cost than Standard
- **Standard-IA**: 99.9% availability, DR/backups
- **One Zone-IA**: 99.5% availability, single AZ, secondary backups
## Amazon S3 Glacier Storage Classes
- Low-cost archive/backup
- Pricing: storage + retrieval
- **Glacier Instant Retrieval**: ms retrieval, quarterly access, 90-day min
- **Glacier Flexible Retrieval**: Expedited (1-5 min), Standard (3-5 hr), Bulk (5-12 hr free), 90-day min
- **Glacier Deep Archive**: Standard (12 hr), Bulk (48 hr), 180-day min
## S3 Intelligent-Tiering
- Small monthly monitoring fee
- Auto-moves between Access Tiers
- No retrieval charges
- Tiers: Frequent, Infrequent (30d), Archive Instant (90d), Archive Access (90-700+d), Deep Archive (180-700+d)
## S3 Storage Classes Comparison
- Standard, IT, Std-IA, OZ-IA, Glacier IR, Glacier FR, Glacier DA
- All 11 9's durability
- Availability varies (99.99% to 99.5%)
- Different min storage durations and retrieval fees
## S3 – Moving between Storage Classes
- Transition objects between classes
- Move infrequent to Standard IA
- Archive to Glacier or Deep Archive
- Automate with Lifecycle Rules
## Amazon S3 – Lifecycle Rules
- **Transition Actions**: e.g., Standard IA after 60 days, Glacier after 6 months
- **Expiration Actions**: Delete after time, old versions, incomplete multi-part uploads
- Rules per prefix or tag
## S3 Lifecycle Rules Scenarios
- **Scenario 1**: Source images Standard → Glacier after 60 days; thumbnails One-Zone IA, expire after 60 days
- **Scenario 2**: Versioning enabled, transition noncurrent to Standard IA, then to Glacier Deep Archive
## S3 Analytics – Storage Class Analysis
- Help decide transitions
- Recommendations for Standard and Standard IA
- Doesn't work for One-Zone IA or Glacier
- Daily report
- 24-48 hours to start seeing data
## S3 Replication (CRR & SRR)
- Must enable Versioning in source and destination
- Cross-Region (CRR), Same-Region (SRR)
- Different AWS accounts possible
- Asynchronous
- IAM permissions to S3
- Use cases: CRR (compliance, latency, cross-account), SRR (log aggregation, prod/test)
## S3 Replication (Notes)
- Only new objects replicated after enable
- S3 Batch Replication for existing/failed
- DELETE: Optional delete marker replication
- Versioned deletes not replicated
- No "chaining" — bucket1→2→3 not transitive
## Amazon S3 – Object Encryption
- 4 methods:
- **Server-Side**: SSE-S3 (default), SSE-KMS, SSE-C
- **Client-Side**
## S3 Encryption – SSE-S3
- AWS-managed keys
- AES-256
- Header: x-amz-server-side-encryption: AES256
- Default for new buckets/objects
## S3 Encryption – SSE-KMS
- KMS keys
- User control + audit via CloudTrail
- Header: x-amz-server-side-encryption: aws:kms
## SSE-KMS Limitation
- Impacted by KMS limits
- Upload calls GenerateDataKey API
- Download calls Decrypt API
- KMS quota: 5500/10000/30000 req/sec by region
- Quota increase via Service Quotas
## S3 Encryption – SSE-C
- Customer-managed keys outside AWS
- S3 doesn't store key
- HTTPS required
- Key in HTTP headers every request
## S3 Encryption – Client-Side
- Amazon S3 Client-Side Encryption Library
- Clients encrypt before sending
- Clients decrypt on retrieve
- Customer fully manages keys/cycle
## S3 Encryption in Transit (SSL/TLS)
- HTTP (non-encrypted) and HTTPS endpoints
- HTTPS recommended
- HTTPS mandatory for SSE-C
- Most clients use HTTPS by default
## S3 – Force Encryption in Transit
- aws:SecureTransport
- Bucket Policy denies non-HTTPS
## S3 Default Encryption vs. Bucket Policies
- SSE-S3 auto-applied to new objects
- "Force encryption" via bucket policy
- Bucket Policies evaluated before Default Encryption
## S3 Access Logs
- Audit access to buckets
- Logs into another bucket
- Same AWS region as target
- Log format documented
## S3 Access Logs Warning
- Don't set logging bucket = monitored bucket
- Creates exponential growth loop
## S3 – Access Points
- Simplify security management
- Each has DNS name (Internet/VPC Origin)
- Access point policy
- Manage security at scale
- Examples: Finance/Sales/Analytics access points with prefix policies
## S3 Access Points – VPC Origin
- Accessible only from within VPC
- VPC Endpoint required (Gateway or Interface)
- VPC Endpoint Policy must allow bucket and Access Point
---
 
# 4. Agentic AI
 
## LLM Agents
- Giving tools to LLM
- LLM has discretion on tools
- Memory, planning, tools
- "Memory" = chat history + external stores
- "Planning module" = guidance for breakdown
- Prompts guide tool use
## LLM Agents: A More Practical Approach
- "Tools" are functions provided to tools API
- In Bedrock, can be Lambda function
- Prompts guide LLM
- Tools may access outside info, retrievers, modules, services
## How do Agents Know Which Tools to Use?
- Foundational model
- **Action Groups** define tools in Bedrock
- Prompt informs FM when to use
- Define parameters (Lambda function expects)
- Description used for parameter extraction
- FM can ask user for missing info
- OpenAI-style schemas or visual table
- Knowledge bases with prompts ("Agentic RAG")
- Optional Code Interpreter
## Deploying Bedrock Agents
- Create "alias" for agent (deployed snapshot)
- **On-Demand throughput (ODT)**: account-level quotas
- **Provisioned throughput (PT)**: increased rate/tokens
- App uses InvokeAgent with alias ID and Bedrock Agents Runtime Endpoint
## Multi-agent Systems Example
- Many tools used at once
- Coding agents on multiple files
- Complex decision making workflows
- **Orchestrator** breaks down/delegates
- **Synthesizer** combines results
## Why Use Multiple Agents?
- **Too many tools**: One agent struggles, specialized agents work better
- **Complex logic**: Prompts too complicated, define flow with specialized agents
## Manager (Orchestrator – Workers)
- Like multi-agent
- Many tools used at once
- Complex decision making
- Orchestrator breaks/delegates
- Synthesizer combines
## Routing
- "Router" LLM picks one specialized agent
- Use for complex tasks needing classification
- Examples: model size needed, customer service query type
## Parallelization
- Independent subtasks in parallel
- **Sectioning**: multiple guardrails/evaluations at once
- **Voting**: same thing different models/prompts, vote on result
## Prompt Chaining
- Discrete sequence of known steps
- Each LLM processes previous output
- "Gates" to keep on track or exit early
- Examples: write document then translate, outline then slides
## Evaluator – Optimizer
- One LLM generates response
- Another evaluates
- Feedback loop, try again
- Examples: code reviewing, multi-round search
## Adding Memory
- **Short-term**: Chat history within session, immediate context, conversations, in-memory or distributed cache (Elasticache, MemoryDB, DynamoDB)
- **Long-term**: Extracted insights, summaries, preferences, facts, "Memory Records", "Strategies"
- Storage: DynamoDB, SQLLite, RDS, Aurora, AgentCore Memory, Mem0 (Strands)
- KBs as long-term memory
## Strands Agents
- Open source Agents Python SDK from Amazon
- Like OpenAI Agents SDK, CrewAI, LangGraph, Google ADK
- Specialized agents, multi-agent systems
- Complex task decomposition
- Collaborative problem solving
- AWS integration (Bedrock, Lambda, Step Functions)
- Not tied to AWS
- Multimodal (text, speech, images, video)
- MCP support
## Strands Built-in Tools
- AWS Services / boto3
- RAG and memory in Bedrock KBs
- Mem0 agent memory and personalization
- Run Python code
- http (call external)
- Run shell commands
- Manipulate files
- Coordinate agent swarms
- Speak (Amazon Polly)
- Custom Python tools
## The Strands Agent Loop
- Input, context
- Tool selection
- LLM/Reasoning
- Tool execution
- Response
## AWS Agent Squad
- Open source multi-agent framework
- github.com/awslabs/agent-squad
- Intelligent intent classification
- Routes queries to right agent
- Python and TypeScript
- Shared contexts
- Pre-built agents and classifiers
- Integrates with Bedrock Agents
- Extends Bedrock Flows
- Conversation memory, orchestration
- **Supervisor Agent**: coordinates specialized agents
- Agent Squad routing-focused, Strands tool-use focused
## Amazon Bedrock AgentCore
- Deployment/operation of AI agents at scale
- No Docker, ECR, ECS hassle
- Serverless
- Works with ANY agent framework
- Not tied to Bedrock or Strands
- OpenAI Agent SDK, LangGraph/LangChain, CrewAI
- Strands gets better support
- "Starter toolkit" for easy deployment
- Tools and capabilities included
## AgentCore Capabilities
- Agent Identity
- Tools
- Memory
- Gateways
- Agent Runtime
- Observability
## AgentCore Agent Runtime
- Serverless endpoints
- Deploy to ECR with AgentCore capabilities
- Starter toolkit uses CodeBuild
- Build own Docker if desired
- Multiple endpoints
- Observability via "GenAI Observability" in CloudWatch
## Adding AgentCore Memory
- **Short-term**: Session objects with Events, conversations
- **Long-term**: Memory Records, Strategies (preferences, semantic facts, summaries)
- OpenAI Agents SDK gives SQLLite
- AgentCore Memory: serverless scalable
## AgentCore Built-In Tools
- **Browser Tool**: Control browser to interact with web
- **Code Interpreter**: Run code in isolated container (Python, JavaScript, TypeScript)
## Importing Bedrock Agents
- Bedrock has own endpoint system
- agentcore import-agent
- Generates Strands code (or LangChain/LangGraph)
- Test or deploy like any AgentCore agent
## AgentCore Gateway
- External tools at scale
- Convert APIs, Lambda, services to MCP tools
- Targets: OpenAPI (REST), Smithy models, Lambda
- Agents access via Gateway endpoints
- OAuth security/credentials
- Semantic tool selection
## AgentCore Identity
- Different from user OAuth
- Agent identity/identities
- Secure access to external tools/AWS
- Central repository (like Cognito user pool)
- Secure credential storage
- OAuth 2.0 support
- Built-in: Google, GitHub, Slack, Salesforce, Atlassian
## Policy in AgentCore
- Integrates with Gateways
- Intercepts tool calls
- Defined in Cedar language
- NLP or form-based construction
- Fine-grained control
- Evaluated outside agent code
## Policy Enforcement
- **Deny by default**: All denied unless permitted
- **Contextual validation**: Full context, OAuth claims, tool arguments
- **Dual modes**: Enforce mode (block), Log-only mode (test)
## AgentCore Evaluations
- Assess agent: tasks, edge cases, consistency
- Integrates with Strands, LangGraph, OpenTelemetry, OpenInference
- Visualize in CloudWatch
- AgentCore Observability Insights
- Cross-region inference (optimal region selection)
- Data may be transmitted encrypted to other regions
## Some Built-In Evaluations
- Correctness (factual)
- Helpfulness
- Conciseness
- Instruction following
- Faithfulness (supported by sources)
- Response relevance
- Coherence
- Refusal (evasive)
- Goal success rate
- Tool selection/parameter accuracy
- Harmfulness, Stereotyping
- Limited by filters and sampling rate
## Custom Evaluators
- Specify judge model and configure
- Define with prompt
- Start with built-in
- Define scales (ranges to labels)
- Evaluation level (session, trace, tool call)
## Lab: Strands Agents, AgentCore, Agent Squad
- Python environment
- AWS CLI configured (admin perms)
- Bedrock API Key (AWS_BEARER_TOKEN_BEDROCK)
- Agent Squad fragile ATM
- Cleanup: agentcore destroy, check Bedrock AgentCore console
- Build: Strands agent (calculator, clock, count keywords), AgentCore deployment, Agent Squad orchestration
## Model Context Protocol (MCP)
- Standardized agent-tool interactions
- "USB-C port for AI Applications" – Anthropic
- Data layer: JSON-RPC 2.0
- Transport: stdio or HTTP streaming
- External tools, consistent patterns
- Apps provide context to LLMs
- Most agent SDKs can call MCP servers (including Strands)
- Servers expose tools, resources, prompts
- Popular: GitHub, Atlassian, PostgreSQL, Slack, Google Maps, Udemy
## Deploying Your Own MCP Server
- **Stateless/lightweight**: AWS Lambda
- **Complex tools**: ECS or Fargate
- **API Gateway** can expose MCP endpoints
- Use MCP client libraries
- Deploy via AgentCore
## OpenAPI and GenAI
- Originally Swagger
- Web service interface spec
- Define interfaces between FMs and tools
- Reliable tool operations
- Standardize function definitions
- Used with Bedrock action groups
- Upload OpenAPI schema to S3 or edit in console
## Humans in the Loop
- "Human augmentation pattern": AI drafts, humans refine
- Escalation criteria for complex/uncertain cases
- Confidence scores or risk assessments
- Continuous improvement via feedback
- API Gateway for feedback
- Store in DynamoDB with indexing
- Measure model/variant preference
## Amazon Q Business
- Fully managed Gen-AI assistant for employees
- Based on company knowledge/data
- Q&A, summaries, content, automate tasks
- Routine actions (time-off, meeting invites)
- Built on Bedrock (can't choose FM)
## Amazon Q Business Capabilities
- **Data Connectors (managed RAG)**: 40+ enterprise sources (S3, RDS, Aurora, WorkDocs, MS 365, Salesforce, GDrive, Gmail, Slack, SharePoint)
- **Plugins**: 3rd party services (Jira, ServiceNow, Zendesk, Salesforce)
- **Custom Plugins**: Connect to any 3rd party via APIs
## Amazon Q Business + IAM Identity Center
- Authenticate via IAM Identity Center
- Responses only from accessible documents
- IDP integration: Google Login, MS Active Directory
## Amazon Q Business – Admin Controls
- Customize responses for organization
- Admin controls = Guardrails
- Block words/topics
- Internal info only
- Global and topic-level controls
## Amazon Q Apps (Q Business)
- Gen AI-powered apps without coding
- Natural language
- Internal data
- Plugins (Jira, etc.)
## Amazon Q Developer
- AWS docs and service selection
- Account resource questions
- CLI suggestions
- Bill analysis, errors, troubleshooting
- AI code companion (like GitHub Copilot)
- Languages: Java, JavaScript, Python, TypeScript, C#
- Real-time suggestions, security scans
- Software agent: features, docs, projects
## Amazon Q Developer – IDE Extensions
- Visual Studio Code, Visual Studio
- AWS dev questions
- Code completions/generation
- Security vulnerability scans
- Debugging, optimizations
## Amazon Q Developer - Rules
- Coding standards, workflow preferences
- Consistent AI guidance
- Markdown format (.md)
- Place in .amazon/rules directory
- Like claude.md in Claude Code
---
 
# 5. Operational Efficiency and Optimization
 
## Token Efficiency
- **Token Estimation and Tracking**:
  - Bedrock CountTokens API
  - Returns count without running
  - Costs nothing
  - Estimate costs prior to inference
  - Optimize prompts for limits
- CloudWatch tracks input/output tokens
## Other Stuff CloudWatch Monitors
- Count, time for requests
- TTFT (Time to First Token, streaming)
- Throttles/server errors/client errors
- Model latency, invocation count, throttles
- Input/output token counts
## More Token Efficiency Techniques
- **Context Window Optimization/Pruning**: Chunking RAG, limiting chunks, metadata filtering, summarize/toss old chats
- **Response Size Controls**: maxTokens, prompt instructions, few-shot examples, JSON output
- **Prompt Compression**: Small model summarizes, KBs instead of full docs
## Cost-Effective Model Selection
- **Cost/Capability Tradeoff**: Smaller models for RAG/tool-heavy, pre-processing
- **Tiered usage based on complexity (Dynamic Routing)**:
  - AKA Intelligent Prompt Routing
  - Bedrock feature
  - Conditional Flow, Lambda, Agent Squad, Strands
  - Tool to score "complexity"
## Measuring Price : Performance Ratio
- Bedrock Evaluations measure FM performance
- Compare feature visualizes models
- Token counting estimates costs
- Informed tradeoffs
## Maximizing Resource Utilization
- **Batching strategies**: Batch embeddings, Bedrock Batch Inference (S3 prompts/responses)
- **Capacity planning**: TPM/RPM, AWS Service Quotas, request increase or provisioned throughput
- AWS CloudFormation templates
- **Tensor parallelism**: Shards LLM weights across GPUs
## Maximizing Resource Utilization (continued)
- **Provisioned throughput**: Tokens or Model Units (MUs), required for customized models, consistent high-volume performance, ARN as modelID
- **Utilization monitoring**: CloudWatch dashboards, Cost Explorer
- **Auto-scaling**: Lambda, Bedrock, OpenSearch serverless, AgentCore
## Intelligent Caching: Semantic Caching
- Cache embeddings of prompts/responses (not text)
- In-memory vector store (ElastiCache for Valkey, MemoryDB)
- OpenSearch possible
- New prompts: embedding, nearest neighbors, threshold check
- Tune similarity threshold
- Balance hits with relevance
- Overhead vs benefits
- Improves latency
## Intelligent Caching: Prompt Caching
- Improves latency for supported models
- Built into Bedrock
- Cache prompt prefix (static content, instructions, few-shot)
- Dynamic content at end
- Cache checkpoint separates
- No re-tokenizing prefix
- Cache documents queried repeatedly
- Discounted per token (writes more expensive)
- CloudWatch monitoring
- Option in Bedrock Prompt Management
## Intelligent Caching: Edge Caching
- Use CloudFront when possible
- Reduces latency, backend requests
- Common prompts/responses cached
- Deterministic request hash → fingerprint in GET → CloudFront cache
- Fingerprint results based on model config
- Aggressive TTL if changes
- Cache more than just LLM piece
## Building Responsive AI Systems
- **Parallel requests** for complex workflows
- Multi-agent in parallel
- Step Functions
- **Cache/pre-compute** predictable queries
- **Response streaming**
- **Latency-optimized inference**: Bedrock feature, performanceConfig={'latency':'optimized'}, optimizes TTFT, OTPS, E2E
## More Responsive AI Systems
- Bedrock Intelligent Prompt Routing (model selection by complexity)
- Concise prompts, important first
- Context pruning (ditch irrelevant RAG)
- Limit response sizes
- Break complex tasks
## Optimizing Retrieval Performance
- Optimize indices
- Hybrid search improves relevancy
- Custom hybrid scoring
- **Query pre-processing**:
  - Normalize style
  - Break multi-part questions
  - Filter irrelevant
  - Reduce ambiguity
  - Keyword extraction for hybrid
## Optimizing for Specific Use Cases
- Different models, different parameters
- A/B testing (Bedrock Evaluations, CloudWatch Evidently)
- **Common parameters**:
  - **Temperature**: randomness (0=not, 1=creative)
  - **Top_p**: Nucleus sampling threshold (use OR temperature)
  - **Top_k**: How many tokens to sample
## Optimizing FM System Performance
- API call profiling (find patterns)
- Identify caching, batching, RAG opportunities
- Structured input/output (JSON, XML)
- Chain of Thought instruction patterns ("Reasoning")
- Feedback loops on satisfaction & behavior
## Optimizing FM System Performance: SageMaker
- Up to 500GB models
- Adjust container health check and download timeouts
- 3rd party model parallelization: Triton, FasterTransformer, DeepSpeed
- **Instance types**:
  - Large models: ml.p4d.24xlarge (GPU)
  - Small (NER): ml.c5.9xlarge (CPU)
## More FM System Performance
- **UltraServers (Trn2, P6e-GB200)**: Connect EC2, low-latency high-bandwidth interconnects
- **Lambda endpoint lifecycle management**: Auto-init endpoints, download from S3 on demand
## Exponential Backoff
- Retry failed API calls
- Custom retry policies in SDK
- Start 100ms, factor 2, max 3-5 retries, jitter ±100ms
- Prevent synchronized retries
## Connection Pooling
- HTTP clients
- Maintain pool of open connections
- 10-20 per instance
- TTL 60-300 seconds
- Balance utilization and re-use
## Bedrock Cross-Region Inference
- Distributes during interruptions/restrictions
- Inference profiles:
  - **Specific geography**: optimal region within geography
  - **Global**: optimal commercial region
- Doesn't work with provisioned throughput
- AWS Organizations SCPs can block regions
- SCP must allow all regions enabled
## Cross-Region Inference Types
- **Geographic**: Data residency, standard pricing
- **Global**: Maximized throughput, 10% cost savings, pricing based on call origin
- Don't need to enable regions in account
- Encrypted in transit, logged in CloudTrail
---
 
# 6. Managing Models with SageMaker AI
 
## SageMaker Built for Whole ML Workflow
- Fetch, clean, prepare data
- Train and evaluate model
- Deploy model, evaluate in production
## SageMaker Training & Deployment
- Endpoint, Client app
- Model deployment/hosting
- Model training
- S3 model artifacts, training data
- Inference code image, Training code image
- SageMaker ECR
## SageMaker Notebooks
- Notebook Instances on EC2
- Spun up from console
- S3 data access
- Scikit_learn, Spark, Tensorflow
- Built-in models
- Spin up training instances
- Deploy trained models
## Data Prep on SageMaker
- Data from S3
- Format varies (often RecordIO/Protobuf)
- Athena, EMR, Redshift, Keyspaces
- Apache Spark integration
- Scikit_learn, numpy, pandas in notebook
## SageMaker Processing
- Processing jobs
- Copy data from S3
- Spin up processing container (built-in or user)
- Output to S3
## Deploying Trained Models
- Save to S3
- **Persistent endpoint** for individual predictions
- **SageMaker Batch Transform** for entire dataset
- **Inference Pipelines**: complex processing
- **SageMaker Neo**: edge devices
- **Elastic Inference**: deep learning acceleration
- **Auto-scaling**: increase endpoints
- **Shadow Testing**: evaluate new vs current
## Deployment Safeguards
- For async or real-time inference endpoints
- Controls traffic shifting
- "Blue/Green Deployments":
  - All at once
  - Canary (small portion)
  - Linear (linearly spaced)
- Auto-rollbacks
- **Shadow Tests**: Compare shadow to production, monitor and promote
## Putting It Together
- SageMaker Studio
- SageMaker Autopilot
- SageMaker Model Monitor
- SageMaker Notebooks
- SageMaker Experiments
- SageMaker Debugger
- Automatic Model Tuning
## SageMaker: More Features
- **JumpStart**: One-click models, 150+ open source
- **Data Wrangler**: Import/transform/analyze/export
- **Feature Store**: Find, share features, online (low-latency) or offline modes, Feature Groups
- **Edge Manager**: Software agent for edge, models with Neo
- **Asynchronous Inference endpoints**
## Optimizing FM Deployments
- **Single and multi-model endpoints** (multi-container)
- Deployment guardrails, VPC, network isolation
- Train/tune in SageMaker, deploy through Bedrock (Custom Model Import)
- Serverless inference
- **SageMaker AI Inference Components**: each model own scaling policy
## More Deployment Optimization
- **Cross-region inference profiles** (Bedrock endpoints)
- **EC2 Auto Scaling Groups**: Load balancing in front
- **Model servers**:
  - TorchServe
  - DJL Serving (Deep Java Library, Amazon-created)
  - Deep Learning Containers
  - Triton Inference Server
## More Optimization
- **Asynchronous inference** if latency unimportant
- SageMaker async endpoints
- Own queue with SNS/SQS
- **Model compression**: Quantization, Pruning, Knowledge distillation (smaller from larger)
- Avoid premature optimization
## What is Ground Truth?
- Generate training labels via humans
- Image classification needs tagged images
- Manages humans for labeling
## More Than That
- Creates own model as labeling progresses
- Only ambiguous images sent to humans
- Reduces labeling cost 70%
## Who are Human Labelers?
- Mechanical Turk
- Internal team
- Professional labeling companies
## Ground Truth Plus
- Turnkey solution
- AWS Experts manage workflow/labelers
- Intake form → contact → pricing
- Track via Project Portal
- Get labeled data from S3
## Other Ways to Generate Labels
- **Rekognition**: Image classification
- **Comprehend**: Text analysis, topic modeling
- Pre-trained or unsupervised techniques
## SageMaker Model Monitor
- Quality deviation alerts (CloudWatch)
- Visualize data drift
- Detect anomalies/outliers
- Detect new features
- No code needed
## Model Monitor + Clarify
- **SageMaker Clarify** detects bias
- Imbalances across groups/ages/income
- Alerted to new bias via CloudWatch
- Clarify explains model behavior
- Identifies feature contributions
## Pre-training Bias Metrics in Clarify
- **Class Imbalance (CI)**
- **Difference in Proportions of Labels (DPL)**
- **Kullback-Leibler/Jensen-Shannon Divergence (KL/JS)**
- **Lp-norm (LP)**
- **Total Variation Distance (TVD)**
- **Kolmogorov-Smirnov (KS)**
- **Conditional Demographic Disparity (CDD)**
## Model Monitor Implementation
- Data in S3, secured
- Monitoring jobs scheduled
- Metrics to CloudWatch
- Notifications trigger alarms
- Take corrective action
- Tensorboard, QuickSight, Tableau, Studio
## Model Monitor Types
- **Data quality drift**: vs baseline, statistical properties
- **Model quality drift**: accuracy, with quality baseline, Ground Truth labels
- **Bias drift**
- **Feature attribution drift**: NDCG (Normalized Discounted Cumulative Gain), training vs live ranking
## SageMaker Model Registry
- Catalog, version models
- Metadata
- Approval status
- Deploy production
- CI/CD automation
- Share models
- Integrate with Collections
- **Workflow**: Create Model Group → Pipeline → Register versions → Add to Registry
## SageMaker ML Lineage Tracking
- ML workflow store (MLOps)
- Model history
- Audit/compliance
- Auto/manual entities
- AWS Resource Access Manager for cross-account
## Lineage Tracking Entities
- **Trial component** (processing/training/transform)
- **Trial** (model from components)
- **Experiment** (group of Trials)
- **Context** (logical grouping)
- **Action** (workflow step, deployment)
- **Artifact** (S3 bucket, ECR image)
- **Association**: ContributedTo, AssociatedWith, DerivedFrom, Produced, SameAs
## Querying Lineage Entities
- LineageQuery API in Python (SageMaker SDK)
- Find all models/endpoints using artifact
- Visualization (external Visualizer helper class)
## Cross-Account Lineage Tracking
- Trace across organizational boundaries
- SageMaker AddAssociation API
- IAM roles & permissions
## SageMaker Neo
- Train once, run anywhere
- Edge devices: ARM, Intel, Nvidia
- Embedded (e.g., car)
- Optimizes code per device
- Tensorflow, MXNet, PyTorch, ONNX, XGBoost, DarkNet, Keras
- Compiler and runtime
## Neo + AWS IoT Greengrass
- Neo-compiled to HTTPS endpoint
- C5, M5, M4, P3, P2 instances (same as compilation)
- Or deploy to IoT Greengrass
- Inference at edge with local data
- Lambda inference applications
## SageMaker Unified Studio
- Single interface: data, analytics, AI, ML
- Bedrock, Q, QuickSight
- Notebooks, all old SageMaker Studio
- Single build/deploy/execute/monitor
- Built for teams
- Domain connects assets/users/projects
- Connect from Visual Studio Code
## SageMaker Pipelines
- Directed Acyclic Graph (DAG) for ML workflows
- Visual designer or JSON
- Integrated with Unified Studio and SageMaker AI
---
 
# 7. More Tools for Building AI Applications
 
## What is Lambda?
- Run code snippets in cloud
- Serverless
- Continuous scaling
- Process data as moved
## Lambda Examples
- Serverless website
- Order history app (Kinesis → Lambda → DynamoDB → Mobile)
- Transaction rate alarm (Kinesis → Analytics → Lambda → SNS)
## Why Not a Server?
- Server management overhead
- Scaling expensive
- No charge for unused processing
- Easier dev split
## Main Uses of Lambda
- Real-time file processing
- Real-time stream processing
- ETL
- Cron replacement
- Process AWS events
## Supported Languages
- Node.js, Python, Java, C#, Go, Powershell, Ruby
## Lambda Triggers
- Various AWS service triggers
## Lambda and OpenSearch
- Integration patterns
## Lambda and Data Pipeline
- Integration
## Lambda and Redshift
- Best practice: COPY command
- Lambda for new data anytime
- DynamoDB tracks loaded
- Batch and load with COPY
## Lambda + Kinesis
- Receives event with batch
- Specify batch size (up to 10,000)
- Too large = timeouts
- Batches split beyond 6 MB
- Retries until success or expiry
- Handle errors to avoid stalling
- More shards for error isolation
- Synchronous processing per shard
## Using Lambda with Bedrock/GenAI
- Connect agents with tools
- Parameter validation, error handling
- On-demand FM invocation (no provisioning)
- Webhook handling (JSON from API Gateway)
- Custom aggregation logic (weighted, voting)
## Building a Serverless API
- REST API → Proxy Requests → CRUD
- Client → API Gateway → Lambda → DynamoDB
## AWS API Gateway
- Lambda + API Gateway: no infra
- WebSocket Protocol
- API versioning (v1, v2)
- Environments (dev/test/prod)
- Auth/Authorization
- API keys, throttling
- Swagger/Open API import
- Transform/validate
- Generate SDK
- Cache responses
## API Gateway – Integrations
- **Lambda Function**: Easy REST API
- **HTTP**: Backend HTTP endpoints, internal APIs, ALB
- **AWS Service**: Any AWS API, Step Functions, SQS
## API Gateway – AWS Service Integration
- Kinesis Data Streams example
- API Gateway → Streams → Firehose → S3
## API Gateway Endpoint Types
- **Edge-Optimized (default)**: Global, CloudFront Edge, single region
- **Regional**: Same region clients, manual CloudFront combine
- **Private**: VPC interface endpoint (ENI), resource policy
## API Gateway Security
- IAM Roles (internal)
- Cognito (external mobile)
- Custom Authorizer
- Custom Domain HTTPS via ACM
- Edge: cert in us-east-1
- Regional: cert in API Gateway region
- Route 53 CNAME or A-alias
## API Gateway and GenAI
- Front for feedback collection
- Front for models
- **Usage plans**: throttling (~10-50 rps), burst (~2-3X)
- Response filtering
- Retry strategies
- Request validator + JSON schema for token limits
- Routing logic with transformations
- Validate required fields
## AWS AppConfig
- Configure/validate/deploy dynamic configs
- Independent of code deployments
- No app restart
- Feature flags, tuning, allow/block listing
- EC2, Lambda, ECS, EKS
- Gradual deployment, rollback
- **Validation**: JSON Schema (syntactic), Lambda (semantic)
## AppConfig and GenAI
- Dynamic FM selection
- No code changes for model switch
- Feature flags, configuration profiles
- Configuration in S3
- Tool for rolling out, A/B testing, rollbacks
- SageMaker also does this
- Bedrock Evaluations and CloudWatch Evidently for A/B
## AWS Step Functions
- Design workflows
- Easy visualizations
- Advanced error/retry outside code
- Audit history
- "Wait" arbitrary time
- Max execution: 1 year
## Step Functions Examples
- Train ML Model
- Tune ML Model
- Manage Batch Job
## AWS Step Functions Concepts
- **State machine** = workflow
- **State** = step
- Types:
  - **Task**: Lambda, AWS services, third party
  - **Choice**: Conditional logic
  - **Wait**: Delay
  - **Parallel**: Separate branches
  - **Map**: Run for each item in dataset (JSON, S3, CSV)
  - Pass, Succeed, Fail
## Step Functions: Circuit Breakers
- Pattern to prevent calling failing service
- Detects functional again
- With Step Functions, Lambda, DynamoDB
- Safeguards AI workflows
- Fallback models, degraded service
## More Step Functions + GenAI
- **ReAct patterns** (Reasoning and Acting): Reasoning Traces, FM, Environment, Observations, Actions
- Chain of thought reasoning
- Dynamic routing to specialized FMs
- Orchestrate model review/approval
## Even More Step Functions
- 256KB limit between steps (use DynamoDB or S3)
- Integrated with Bedrock (InvokeModel, CreateModelCustomizationJob)
- Chain multiple FM calls
- InvokeModel with guardrails
- Chain those too
## AWS CodePipeline
- Visual CICD orchestration
- **Source**: CodeCommit, ECR, S3, Bitbucket, GitHub
- **Build**: CodeBuild, Jenkins, CloudBees, TeamCity
- **Test**: CodeBuild, Device Farm, 3rd party
- **Deploy**: CodeDeploy, Elastic Beanstalk, CloudFormation, ECS, S3
- **Invoke**: Lambda, Step Functions
- Stages with sequential/parallel actions
- Manual approval at any stage
## Technology Stack for CICD
- Code → Build → Test → Deploy → Provision
- CodeCommit, CodeBuild, CodePipeline, CodeDeploy, Elastic Beanstalk
- GitHub, Jenkins CI, 3rd party
- EC2, On-prem, Lambda, ECS
## CodePipeline Artifacts
- Each stage creates artifacts
- Stored in S3, passed to next stage
## CodePipeline Troubleshooting
- CloudWatch Events (EventBridge) for state changes
- Failed pipeline events
- Cancelled stage events
- Failed stage info in console
- IAM Service Role permissions
- CloudTrail for AWS API audit
## AWS CodeBuild
- Fully managed CI service
- Continuous scaling
- Compile, test, package
- Alternative to Jenkins
- Per-minute compute charges
- Docker for reproducible builds
- Pre-packaged or custom images
- KMS encryption, IAM, VPC, CloudTrail
## AWS CodeBuild Sources/Output
- **Source**: CodeCommit, S3, Bitbucket, GitHub
- buildspec.yml or console
- Logs in S3 or CloudWatch Logs
- CloudWatch Metrics for stats
- EventBridge for failed builds
- CloudWatch Alarms for thresholds
- Build Projects in CodePipeline or CodeBuild
## CodeBuild Supported Environments
- Java, Ruby, Python, Go, Node.js, Android, .NET Core, PHP, Docker
## CodeBuild How It Works
- CodeCommit (Source) + buildspec.yml
- CodeBuild Container runs instructions
- Docker Image (prepackaged or custom)
- S3 for artifacts and cache
- CloudWatch Logs
## CodeBuild – buildspec.yml
- Root of code
- **env**: variables (parameter-store, secrets-manager)
- **phases**: install, pre_build, build, post_build
- **artifacts**: upload to S3 (KMS encrypted)
- **cache**: dependencies for speedup
## AWS CodeDeploy
- Automate deployment
- EC2, On-prem, Lambda, ECS
- Auto rollback, CloudWatch Alarm trigger
- Gradual deployment
- appspec.yml
## CodeDeploy – EC2/On-premises
- In-place or blue/green
- CodeDeploy Agent on instances
- Speed: AllAtOnce, HalfAtATime, OneAtATime, Custom %
## CodeDeploy – In-Place Deployment
- Half At A Time visualization
## CodeDeploy – Blue-Green Deployment
- New ASG, ALB switches
## CodeDeploy Agent
- Pre-requisite on EC2
- Systems Manager auto-install/update
- IAM permissions for S3 deployment bundles
## CodeDeploy – Lambda Platform
- Automate alias traffic shift
- SAM framework integrated
- **Linear**: 10% every N minutes (3 or 10)
- **Canary**: 10% then 100% (5 or 30 min)
- **AllAtOnce**: immediate
## CodeDeploy – ECS Platform
- New ECS Task Definition
- Only Blue/Green
- ALB required
- Linear, Canary, AllAtOnce options
## MLFlow
- Open-source ML/GenAI workflows
- Observability, evaluations, tracking, tracing, AI gateway
- Model management/deployment
- Integrated with SageMaker AI
- Managed service
- Integration: SageMaker Studio, Model Registry, AI Inference, IAM, CloudTrail, EventBridge
## AWS AppSync GraphQL and GenAI
- Connects apps/services to data and events
- GraphQL and Pub/Sub APIs
- GraphQL = Graph query language (Facebook)
- Retrieves from different sources as graph
- Serverless
- JavaScript/TypeScript for logic
- **GenAI**:
  - Lambda + AppSync resolvers for real-time inference
  - Transform GraphQL via Apache Velocity Template Language (VTL)
  - VTL translates GraphQL to data source
## AWS Outposts
- Hybrid Cloud
- Server racks with same AWS infra/services/APIs
- AWS sets up, manages "Outposts Racks" on-premises
- You're responsible for physical security
## AWS Outposts Benefits
- Low-latency on-prem access
- Local data processing
- Data residency
- Easier migration
- Fully managed
- Services: EC2, EBS, S3, EKS, ECS, RDS, EMR
## AWS Outposts and GenAI
- Data compliance across jurisdictions
- Different country AI laws
- Data privacy
- On-premise data integration
- Sufficient compute/storage for inference
- Local caching minimizes data movement
## AWS WaveLength
- Infra in 5G telecom datacenters at edge
- AWS services to 5G edge
- EC2, EBS, VPC
- Ultra-low latency via 5G
- Traffic stays in CSP network
- High-bandwidth secure to parent Region
- No additional charges
- Use cases: Smart Cities, ML diagnostics, Connected Vehicles, Live Video, AR/VR, Gaming
## AWS WaveLength and GenAI
- Edge deployments
- Secure routing cloud/on-prem
- Mobile foundation model apps
- Distribute between Wavelength Zones and parent regions
- Low-latency lighter at edge
- Heavier in Region
## Amazon SQS – Queue Concept
- Producers send messages
- Consumers poll messages
## Amazon SQS – Standard Queue
- Oldest offering (10+ years)
- Fully managed, decouples apps
- **Attributes**:
  - Unlimited throughput, messages
  - 4 days retention default (max 14)
  - Low latency (<10ms)
  - 1024 KB per message
  - Duplicate possible (at least once)
  - Out of order possible (best effort)
## SQS – Producing Messages
- SDK SendMessage
- Persisted until consumer deletes
- Retention 4-14 days
- Up to 1024 KB
- Standard: unlimited throughput
## SQS – Consuming Messages
- Consumers on EC2/Lambda
- Poll (up to 10 messages)
- Process
- Delete via DeleteMessage API
## SQS – Multiple EC2 Consumers
- Receive/process in parallel
- At least once delivery
- Best-effort ordering
- Delete after processing
- Scale horizontally
## SQS with Auto Scaling Group
- CloudWatch Metric – ApproximateNumberOfMessages
- Alarm triggers ASG scale
## SQS Decoupling Tiers
- Infinitely scalable queue
- Front-end SendMessage
- Back-end ReceiveMessages
## Amazon SQS Security
- **Encryption**: HTTPS in-flight, KMS at-rest, client-side
- **Access Controls**: IAM policies, SQS Access Policies (cross-account, allow other services)
## AWS Amplify
- Develop/deploy scalable full-stack web/mobile
- Auth, Storage, API (REST/GraphQL), CI/CD, PubSub, Analytics, AI/ML, Monitoring
- Source: GitHub, CodeCommit, Bitbucket, GitLab, upload
- Frontend libraries connect to backend (S3, Cognito, AppSync, API Gateway, Lambda, DynamoDB, SageMaker, Lex)
- Amplify Console build/deploy with CloudFront
## Amazon EventBridge
- Schedule (cron jobs)
- Event Pattern (react to service)
- Trigger Lambda, SQS/SNS
## EventBridge Rules
- **Sources**: EC2, CodeBuild, S3 Event, Trusted Advisor, CloudTrail, Schedule
- **Destinations**: Lambda, AWS Batch, ECS Task, SQS, SNS, Kinesis, Step Functions, CodePipeline, CodeBuild, SSM, EC2 Actions
## EventBridge Buses
- **Default**: AWS Services
- **Partner**: AWS SaaS Partners
- **Custom**: Custom Apps
- Resource-based Policies for cross-account
- Archive events (filter, indefinite/period)
- Replay archived
## EventBridge Schema Registry
- Analyzes events, infers schema
- Generate code
- Versioned
## EventBridge Resource-based Policy
- Permissions for Event Bus
- Allow/deny from another account/region
- Aggregate events from Organization
## Amazon SNS
- Send one message to many receivers
- Pub/Sub Topic vs Direct Integration
## Amazon SNS Architecture
- Producer → SNS Topic
- Many subscriptions
- All messages to all subscribers (filter optionally)
- Up to 12,500,000 subscriptions per topic
- 100,000 topics limit
- Subscribers: SQS, Lambda, Kinesis Firehose, HTTP(S), SMS/Mobile, Emails
## SNS AWS Service Integration
- CloudWatch Alarms, S3 Events, ASG Notifications, CloudFormation, AWS Budgets, Lambda, AWS DMS, DynamoDB, RDS Events
## Amazon SNS Publishing
- **Topic Publish (SDK)**: Create topic → subscriptions → publish
- **Direct Publish (mobile SDK)**: Platform application → endpoint → publish
- Google GCM, Apple APNS, Amazon ADM
## Amazon SNS Security
- **Encryption**: HTTPS, KMS, client-side
- **Access Controls**: IAM, SNS Access Policies (cross-account, S3)
## Amazon AppFlow
- Integration SaaS apps and AWS
- **Sources**: Salesforce, SAP, Zendesk, Slack, ServiceNow
- **Destinations**: S3, Redshift, SnowFlake, Salesforce
- Schedule, event, on demand
- Filtering and validation
- Public internet or AWS PrivateLink
- No coding integrations
---
 
# 8. Governance and QA
 
## Bedrock Agent Tracing
- Trace per Agent response
- Reasoning process
- KBs hit, results
- Action group usage
- Error details
- **Trace types**:
  - PreProcessing (categorize input)
  - Orchestration (action groups, KBs)
  - PostProcessing (final response)
  - CustomOrchestration (action order)
  - RoutingClassifier (request routing)
  - Failure (step fail reason)
  - Guardrail (guardrail behavior)
## Foundation Model Evaluation Criteria
- Multiple criteria
## Human Evaluation
- Best feedback source
- UX, contextual relevancy, creativity, complex problem handling
## Evaluation against Benchmark Datasets
- SME-generated prompts/answers
- Specific application or problem types
- Initial metrics before human feedback
- "Leaderboards"
- Measurable: Accuracy, Speed/Efficiency, Scalability, Context retrieval
- Only as good as test data — flawed
## Using Another Model as Judge
- "Trusted" model evaluates
- Assumes trust
- Shared problems = problem
- Better for "small" language models
## Hybrid Approaches
- Combine human and benchmark
- Reveal limitations of both
## ROUGE
- Text summarization, machine translation
- Overlapping units between output and ground-truth
- Words, n-grams, fragments
- **ROUGE-N**: n-grams overlap
  - ROUGE-1: unigrams
  - ROUGE-2: bigrams
- **ROUGE-L**: longest common subsequence, coherence/order
## BLEU
- Machine translation evaluation
- Compares to human translation
- N-gram PRECISION (vs ROUGE recall)
- Sentence level
- Brevity penalty (overly short)
- Limited fluency/grammar assessment
## BERTscore
- Embedding vectors compare semantic similarity
- BERT predated GPT
- Less sensitive to synonyms/paraphrasing
## Testing Strategy Selection
- Choose strategy based on need
## Bedrock Model Evaluations
- **Automatic**: Built-in tasks, datasets, metrics (text generation, summarization, Q&A, classification)
- **Human-based**: Compare two models, prompt dataset, work team in Cognito/Ground Truth/A2I
## More Bedrock Model Evaluations
- **LLM as a judge**: Evaluator and generator models, prompt dataset, many metrics
- **RAG evaluation jobs**:
  - Retrieve only (relevance, coverage)
  - Retrieve and generate (correctness, completeness, helpfulness, coherence)
  - JSON line format in S3
  - Custom metrics with judge prompts
## Considerations for Deployment Validation
- **Synthetic user workflows**: Unit testing inadequate (non-deterministic), simulate end-to-end, before/after
- Tools: CloudWatch synthetic monitoring (canaries), Step Functions, EventBridge, Lambda
- Store in S3/Athena, analyze in QuickSight
- **AI-Specific output validation**: hallucination rate, semantic drift, faithfulness, compliance
- Bedrock Model Evaluations or Lambda + Step Functions
- **Response consistency**: style, similar test answers, variability range
## Responsible AI: Core Dimensions
- Fairness
- Explainability
- Privacy and Security
- Safety
- Controllability
- Veracity and Robustness
- Governance
- Transparency
## AWS Tools for Responsible AI
- **Amazon Bedrock**: Model evaluation tools
- **SageMaker Clarify**: Bias detection, evaluation, explainability
- **SageMaker Model Monitor**: Inaccurate response alerts
- **Amazon Augmented AI**: Humans correct results
- **SageMaker ML Governance**: Role Manager, Model Cards, Model Dashboard
## CloudWatch Logs
- Log groups (apps), Log streams (instances)
- Expiration policies (1d-10y, never)
- **Send to**: S3, Kinesis Streams, Firehose, Lambda, OpenSearch
- Encrypted by default, KMS option
## CloudWatch Logs Sources
- SDK, CloudWatch Logs Agent, Unified Agent
- Elastic Beanstalk, ECS, Lambda
- VPC Flow Logs, API Gateway
- CloudTrail filtered
- Route53 DNS queries
## CloudWatch Logs Insights
- Search and analyze CloudWatch Logs
- Find IPs, count "ERROR"
- Purpose-built query language
- Auto-discovers fields (AWS, JSON)
- Fetch fields, filter, aggregate, sort, limit
- Save queries, add to dashboards
- Multiple Log Groups, accounts
- Query engine, not real-time
## CloudWatch Logs S3 Export
- Up to 12 hours to become available
- API: CreateExportTask
- Not near-real time — use Subscriptions
## CloudWatch Logs Subscriptions
- Real-time events for processing
- To Kinesis Streams, Firehose, Lambda
- **Subscription Filter**: filter delivered events
- Real-time to Lambda/Streams
- Near real-time to Firehose
## CloudWatch Alarms
- Trigger notifications for any metric
- Sampling, %, max, min options
- **States**: OK, INSUFFICIENT_DATA, ALARM
- **Period**: time in seconds, high-res 10/30s or multiples of 60
## CloudWatch Alarm Targets
- EC2: Stop, Terminate, Reboot, Recover
- Auto Scaling Action
- SNS notification
## CloudWatch Alarms – Composite Alarms
- Single metric alarms vs composite (multiple alarms)
- AND/OR conditions
- Reduce alarm noise
## EC2 Instance Recovery
- **Status Check**: Instance, System, EBS attached
- **Recovery**: Same Private/Public/Elastic IP, metadata, placement group
## CloudWatch Alarm Tips
- Based on CloudWatch Logs Metrics Filters
- Test via CLI: aws cloudwatch set-alarm-state
## CloudWatch and GenAI
- **Test prompt regression**: Logs prompt inputs and responses, foundational for monitoring
- **Monitor KPIs**: prompt effectiveness/quality, latency, error rates
## Other Things to Monitor
- Foundation model interaction tracing
- Business impact metrics
- Prompt effectiveness, hallucination rates
- Anomaly detection
- Token burst patterns, response drift
- Bedrock model invocation logs
- Cost anomaly detection
## CloudWatch Real User Monitoring (RUM)
- Mobile apps testing (iOS/Android)
- Page load times, errors, app launch
- Real user session
- Application Signals integration
- View in X-Ray traces
- End-to-end mobile GenAI performance
## AWS CloudTrail
- Governance, compliance, audit
- Enabled by default
- API call history (Console, SDK, CLI, AWS Services)
- Logs to CloudWatch Logs or S3
- Trail to All Regions or single
- Investigate deleted resources first
## CloudTrail Diagram
- Sources: SDK, CLI, Console
- IAM Users & Roles
- Console Inspect & Audit
- CloudWatch Logs, S3 Bucket
## CloudTrail Events
- **Management Events**: Operations on resources, Read or Write events, default logged
- **Data Events**: Default not logged (high volume), S3 object-level (Get/Delete/Put), Lambda Invoke
- **CloudTrail Insights Events**: Detect unusual activity
## CloudTrail Insights
- Detect unusual activity
- Inaccurate provisioning, service limits, IAM bursts, maintenance gaps
- Analyzes management events for baseline
- Continuously analyzes write events
- Insights Events generated
- S3 storage, EventBridge event
## CloudTrail Events Retention
- 90 days in CloudTrail
- S3 + Athena for longer
- Analysis tools
## CloudTrail and GenAI
- Track all Bedrock API calls
- Audit of prompt resources used
- When and by who
- Compliance requirement
## AWS X-Ray
- Old way: log statements, redeploy
- Distributed services hard
- No common architecture views
## AWS X-Ray Visual
- Visual app analysis
## AWS X-Ray Advantages
- Performance troubleshooting (bottlenecks)
- Microservice dependencies
- Pinpoint service issues
- Review request behavior
- Find errors/exceptions
- SLA compliance
- Throttling
- Identify impacted users
## X-Ray Compatibility
- Lambda, Elastic Beanstalk, ECS, ELB, API Gateway, EC2, on-premise
## AWS X-Ray Tracing
- End-to-end request following
- Each component adds trace
- Made of segments + sub segments
- Annotations for extra info
- Trace every request, sample %, rate per minute
- **Security**: IAM auth, KMS encryption
## AWS X-Ray Setup
- Import AWS X-Ray SDK (Java, Python, Go, Node.js, .NET)
- Captures: AWS calls, HTTP, DB (MySQL, Postgres, DynamoDB), Queue (SQS)
- Install X-Ray daemon or AWS Integration
- UDP packet interceptor
- Lambda runs daemon
- IAM rights to write to X-Ray
## The X-Ray Magic
- Service collects from all services
- Service map computed from segments/traces
- Graphical for non-technical troubleshooting
## AWS X-Ray Troubleshooting
- **EC2**: IAM Role, daemon running
- **Lambda**: AWSX-RayWriteOnlyAccess, X-Ray imported, Active Tracing enabled
## AWS Lake Formation
- Easy secure data lake setup
- Loading data, monitoring flows
- Setting partitions
- Encryption, key management
- Define transformation jobs
- Access control
- Auditing
- Built on Glue
## AWS Lake Formation Architecture
- S3 Data Lake (S3, RDBMS, NoSQL)
- Crawlers, ETL, catalog, security, ACL, cleaning, transforms (Parquet/ORC)
- Athena, Redshift, EMR
- On-premises or AWS
## AWS Lake Formation Pricing
- No cost for Lake Formation itself
- Underlying services (Glue, S3, EMR, Athena, Redshift) charged
## AWS Lake Formation Building Steps
- Create IAM user (Data Analyst)
- AWS Glue connection to data sources
- S3 bucket for lake
- Register S3 path, grant permissions
- Create database in Lake Formation, grant permissions
- Use blueprint for workflow (DB snapshot)
- Run workflow
- Grant SELECT permissions
## AWS Lake Formation Finer Points
- Cross-account permission, recipient as data lake admin
- AWS Resource Access Manager for external accounts
- IAM permissions for cross-account
- Doesn't support manifests in Athena/Redshift queries
- IAM permissions on KMS keys for encrypted catalogs
- IAM for blueprints/workflows
## Lake Formation: Governed Tables and Security
- **Governed Tables**: ACID transactions across tables, S3 table type, can't change choice, streaming (Kinesis)
- Query with Athena
- Storage Optimization, Automatic Compaction
- Granular Access Control: Row and Cell-Level Security (governed and S3 tables)
- Additional charges based on usage
## Data Permissions in Lake Formation
- IAM users/roles, SAML, external AWS accounts
- Policy tags on databases/tables/columns
- Specific permissions for tables/columns
## Data Filters in Lake Formation
- Column, row, or cell-level security
- Apply with SELECT permission grants
- All columns + row filter = row-level
- All rows + specific columns = column-level
- Specific columns + rows = cell-level
- Console or CreateDataCellsFilter API
---
 
# 9. Security, Identity, and Compliance
 
## Principle of Least Privilege
- Grant only required permissions
- Start broad while developing
- Lock down with knowledge of services/operations
- IAM Access Analyzer generates least-privilege based on activity
## Data Masking and Anonymization
- PII or sensitive data
- **Masking** obfuscates: credit card last 4, social security, passwords
- Glue DataBrew and Redshift support
## Anonymization Techniques
- Replace with random
- Shuffle
- Encrypt (deterministic or probabilistic)
- Hashing
- Delete or don't import
## Key Salting
- Append/prepend random "salt" before hashing
- Prevents rainbow table attacks
- Same data ≠ same hash with unique salt
- **Best practices**: Strong cryptographically secure values, rotate periodically, unique per user, salt and hash before storing
## Key Salting Example
- Different salt values produce different hashes for same password
## IAM: Users & Groups
- Identity and Access Management
- Global service
- Root account default (don't use/share)
- Users in organization, groupable
- Groups only contain users
- User can belong to multiple groups (or none)
## IAM: Permissions
- Users/Groups assigned JSON policies
- Define permissions
- Least privilege principle
## IAM Policies Inheritance
- Group → users
- Inline policies
## IAM Policies Structure
- **Version**: "2012-10-17" always
- **Id**: optional identifier
- **Statement**: required, one or more
  - Sid: optional identifier
  - Effect: Allow/Deny
  - Principal: account/user/role
  - Action: list of allowed/denied actions
  - Resource: list of resources
  - Condition: optional condition
## IAM Password Policy
- Minimum length
- Character types (upper, lower, numbers, non-alphanumeric)
- Allow self-change
- Expiration
- Prevent re-use
## Multi Factor Authentication (MFA)
- Protect Root and IAM users
- Password + security device
- If password stolen, account not compromised
## MFA Devices Options
- **Virtual MFA**: Google Authenticator, Authy
- **Universal 2nd Factor (U2F)**: YubiKey
- **Hardware Key Fob**: Gemalto
- **GovCloud Hardware Key Fob**: SurePassID
## IAM Roles for Services
- AWS services need permissions
- Common roles: EC2 Instance, Lambda Function, CloudFormation
## AWS IAM Identity Center (formerly SSO)
- One login for AWS accounts in Organizations
- Business cloud apps (Salesforce, Box, MS 365)
- SAML2.0 apps
- EC2 Windows Instances
- Identity providers: built-in store, Active Directory, OneLogin, Okta
## IAM Identity Center Login Flow
- Browser → IAM Identity Center → User auth → Access
## IAM Identity Center Architecture
- AWS Organization
- Business Cloud Apps, SAML2.0 Apps
- Permission Sets
- Browser Interface
- Windows EC2 login
- Identity Store: built-in or Active Directory
## IAM Identity Center with Organizations
- Management Account, OU (Dev/Prod)
- Group (Developers) with permission sets
- ReadOnlyAccess, FullAccess
## IAM Identity Center Fine-grained
- **Multi-Account Permissions**: Across Organization accounts
- **Permission Sets**: Collection of IAM Policies
- **Application Assignments**: SSO to SAML 2.0 apps
- **Attribute-Based Access Control (ABAC)**: User attributes (cost center, title, locale)
## AWS Control Tower
- Set up and govern multi-account environment
- Best practices
- Uses AWS Organizations
- **Benefits**: Automate setup, policy management with guardrails, detect/remediate violations, monitor compliance
## AWS Control Tower – Guardrails
- Ongoing governance
- **Preventive**: SCPs (restrict regions)
- **Detective**: AWS Config (untagged resources)
- SNS notify, Lambda invoke, remediate
## Why Encryption?
- **Encryption in Flight (TLS/SSL)**: Encrypt before send, decrypt after receive, TLS certs (HTTPS), no MITM
## Server-side Encryption at Rest
- Encrypted after received by server
- Decrypted before sent
- Stored encrypted with key (data key)
- Server has key access
## Client-side Encryption
- Client encrypts, server never decrypts
- Receiving client decrypts
- Server can't decrypt
- Envelope Encryption possible
## AWS KMS (Key Management Service)
- "Encryption" in AWS = mostly KMS
- AWS manages encryption keys
- IAM integration
- CloudTrail audit
- Integrated into most services (EBS, S3, RDS, SSM)
- API calls (SDK, CLI)
- Encrypted secrets in code/env vars
## KMS Keys Types
- New name for KMS Customer Master Key
- **Symmetric (AES-256)**: Single key encrypt/decrypt, AWS services use, never get unencrypted, must call API
- **Asymmetric (RSA & ECC pairs)**: Public encrypt/Private decrypt, Sign/Verify, public downloadable, private encrypted, encrypt outside AWS
## AWS KMS Key Types
- **AWS Owned Keys** (free): SSE-S3, SSE-SQS, SSE-DDB
- **AWS Managed Key** (free): aws/service-name
- **Customer managed keys created in KMS**: $1/month
- **Customer managed keys imported**: $1/month
- API calls: $0.03/10000
- **Auto rotation**: AWS-managed (1 year), Customer-managed (must enable, on-demand), Imported (manual via alias)
## Copying Snapshots Across Regions
- ReEncrypt with new region's KMS key
## AWS Macie
- Fully managed data security/privacy
- ML and pattern matching
- Discover and protect sensitive data
- Identify PII alerts
- S3 Buckets → Macie → EventBridge → notify integrations
## AWS Secrets Manager
- Storing secrets
- Force rotation every X days
- Auto-generate on rotation (Lambda)
- Amazon RDS integration (MySQL, Postgres, Aurora)
- KMS encryption
- Mostly RDS integration
## Secrets Manager – Multi-Region Secrets
- Replicate across Regions
- Read replicas in sync with primary
- Promote replica to standalone
- Multi-region apps, DR, multi-region DBs
## Amazon Cognito
- Identity for web/mobile apps
- **User Pools (CUP)**: Sign-in for users, integrates with API Gateway and ALB
- **Identity Pools (Federated)**: AWS credentials, integrates with User Pools as identity provider
- Cognito vs IAM: hundreds of users, mobile users, SAML auth
## Cognito User Pools – User Features
- Serverless user database
- Username/email + password
- Password reset
- Email/Phone verification
- MFA
- Federated Identities (Facebook, Google, SAML)
## Cognito User Pools – Integrations
- API Gateway: REST API + Pass Token, evaluate token, authenticate
- Application Load Balancer: Listeners & Rules, authenticate, target group, backend
## Cognito Identity Pools
- Get identities for "users", temporary AWS credentials
- Sources: User Pools, 3rd party, etc.
- Direct AWS access or via API Gateway
- IAM policies in Cognito
- Custom by user_id
- Default IAM roles for auth and guest
## Cognito Identity Pools Diagram
- Web/Mobile → Identity Pools
- Social Identity Provider, User Pools
- Login → Token → Temporary AWS creds
- Direct access (S3, DynamoDB)
## Cognito Identity Pools Row-Level Security
- DynamoDB row-level
## AWS WAF – Web Application Firewall
- Common web exploits (Layer 7 = HTTP)
- Deploy on: ALB, API Gateway, CloudFront, AppSync GraphQL, Cognito User Pool
## AWS WAF Rules
- Web ACL Rules:
  - IP Set (10,000 IPs)
  - HTTP headers/body/URI strings
  - SQL injection and XSS
  - Size constraints, geo-match
  - Rate-based (DDoS protection)
- Web ACL Regional except CloudFront
- Rule group reusable
## VPC – Crash Course
- Important for SAA and SOA exams
- AWS Certified Developer level: VPC, Subnets, IGW, NAT, SG, NACL, VPC Flow Logs, Peering, Endpoints, Site-to-Site VPN, Direct Connect
## VPC & Subnets Primer
- **VPC**: Private network for resources (regional)
- **Subnets**: Partition VPC (AZ resource)
- **Public Subnet**: Internet accessible
- **Private Subnet**: Not internet accessible
- Route Tables define access
## VPC Diagram
- VPC across AZs with public/private subnets
- CIDR Range example: 10.0.0.0/16
## Internet Gateway & NAT Gateways
- **IGW**: VPC instances connect to internet, public subnets route to IGW
- **NAT Gateways (managed) & NAT Instances (self-managed)**: Private subnets access internet privately
## Network ACL & Security Groups
- **NACL**: Subnet firewall, ALLOW/DENY rules, attached at subnet level, IP addresses only
- **Security Groups**: ENI/EC2 firewall, ALLOW only, IPs and other security groups
## Network ACLs vs Security Groups
- Comparison details
## VPC Flow Logs
- Capture IP traffic
- VPC, Subnet, ENI Flow Logs
- Monitor connectivity issues
- AWS managed interfaces (ELB, ElastiCache, RDS, Aurora)
- Send to S3, CloudWatch Logs, Kinesis Firehose
## VPC Peering
- Connect two VPCs privately
- AWS network
- Same network behavior
- No overlapping CIDRs
- Not transitive (must establish each)
## VPC Endpoints
- Connect to AWS Services privately
- Enhanced security, lower latency
- **Gateway**: S3 & DynamoDB
- **Interface**: Most services (including S3 & DynamoDB)
- Only within VPC
## Site to Site VPN & Direct Connect
- **Site to Site VPN**: On-prem VPN to AWS, auto-encrypted, public internet
- **Direct Connect (DX)**: Physical connection, private/secure/fast, private network, 1+ month to establish
## VPC Closing Comments
- VPC, Subnets, IGW, NAT, NACL, SG, Peering, Endpoints, Flow Logs, Site-to-Site VPN, Direct Connect summary
## AWS PrivateLink (VPC Endpoint Services)
- Most secure/scalable to expose service to 1000s of VPCs
- No peering, IGW, NAT, route tables
- Network load balancer (Service VPC) and ENI (Customer VPC)
---
 
# 10. Other Services You Should Know
 
## What is Athena?
- Interactive S3 query service (SQL)
- No data loading
- Presto under hood
- Serverless
- **Formats**: CSV, TSV, JSON, ORC, Parquet, Avro
- **Compression**: Snappy, Zlib, LZO, Gzip
- Unstructured/semi-structured/structured
## Athena Examples
- Ad-hoc web logs
- Staging before Redshift
- Analyze CloudTrail/CloudFront/VPC/ELB logs
- Jupyter, Zeppelin, RStudio
- QuickSight integration
- ODBC/JDBC visualization tools
## What is EMR?
- Elastic MapReduce
- Managed Hadoop on EC2
- Spark, HBase, Presto, Flink, Hive, more
- EMR Notebooks
- AWS integration
## An EMR Cluster
- **Master node**: manages cluster, single EC2, "leader node"
- **Core node**: HDFS data, runs tasks, scaleable, multi-node has 1+
- **Task node**: Tasks only, no data, optional, no risk on remove, good for spot
## EMR Usage
- **Transient**: Terminate after steps, save money
- **Long-running**: Manual termination, data warehouse
- Spot instances for task nodes
- Reserved instances for long-running savings
- Termination protection on, auto-termination off
## EMR Usage (Continued)
- Frameworks specified at launch
- Connect directly to master or submit ordered steps
- Process S3 or HDFS data
- Output to S3 or wherever
- Steps invoked via console
## What is QuickSight?
- Cloud-powered business analytics
- Build visualizations
- Paginated reports
- Ad-hoc analysis
- Anomaly alerts
- Insights anytime/device
- Serverless
## QuickSight Data Sources
- Redshift, Aurora/RDS, Athena, OpenSearch, IoT Analytics
- EC2-hosted databases
- Files (S3, on-prem)
- Excel, CSV/TSV, log formats
- Limited ETL
## SPICE
- Super-fast, Parallel, In-memory Calculation Engine
- Columnar in-memory, machine code generation
- Accelerate large datasets queries
- 10GB per user
- Highly available/durable
- Hundreds of thousands of users
- Accelerate large queries (timeout >30 min import)
## QuickSight Use Cases
- Interactive ad-hoc exploration
- Dashboards/KPIs
- Logs, on-prem DB, AWS, SaaS, JDBC/ODBC
## QuickSight Anti-Patterns
- ETL — use Glue (some transforms in QuickSight OK)
## QuickSight Security
- MFA on account
- VPC connectivity (whitelist IPs)
- Row-level security
- Column-level security (CLS, Enterprise)
- Private VPC access (ENI, Direct Connect)
## QuickSight Resource Access
- Authorize QuickSight for Athena/S3/buckets
- Manage in console
- IAM policies for data restrictions
## Quicksight + Redshift: Security
- Same region by default
- Cross-region: new SG with inbound from QuickSight IPs
- Documented at AWS
## QuickSight Cross-Region (Enterprise)
- Private subnet in VPC
- ENI to put QuickSight in subnet
- Cross-account access
## QuickSight Cross-Region Connectivity
- Peering connection between subnets
- Cross-account works
## QuickSight Cross-Account
- AWS Transit Gateway (same org & region)
- Peer Transit Gateways across regions
- AWS PrivateLink
- VPC sharing
## QuickSight User Management
- IAM or email signup
- Active Directory connector (Enterprise)
- AWS-managed keys (CANNOT use customer-provided)
- Enterprise edition only
- IAM tweaks
## Amazon Kinesis Data Streams
- Real-time streaming collect/store
- Producers: Click streams, IoT, metrics/logs, agent
- Consumers: Lambda, applications, Firehose, Managed Service for Apache Flink
## Kinesis Data Streams
- Up to 365 days retention
- Replay
- Can't delete (until expire)
- 1MB data
- Ordering with same Partition ID
- KMS at-rest, HTTPS in-flight
- KPL (Kinesis Producer Library)
- KCL (Kinesis Client Library)
## Kinesis Data Streams Capacity Modes
- **Provisioned**: Choose shards, 1MB/s in (1000 records/sec), 2MB/s out, manual scaling, pay per shard hour
- **On-demand**: No provisioning, 4MB/s in default (4000 records/sec), auto-scale based on 30-day peak, pay per stream/hour + GB
## Amazon MSK
- Managed Streaming for Apache Kafka
- Alternative to Kinesis
- Fully managed Apache Kafka
- Create/update/delete clusters
- Brokers and Zookeeper nodes managed
- VPC, multi-AZ (up to 3)
- Auto-recovery
- EBS volumes
- **MSK Serverless**: No capacity management, auto-provisions
## Apache Kafka Architecture
- Producers (Kinesis, IoT, RDS) → MSK Cluster (Brokers) → Consumers (EMR, S3, SageMaker, Kinesis, RDS)
- Write to topic, Poll from topic
## Kinesis vs MSK Comparison
- **Kinesis**: 1 MB limit, Shards, Splitting/Merging, TLS, KMS
- **MSK**: 1 MB default (configurable to 10MB), Topics with Partitions, only add partitions, PLAINTEXT or TLS, KMS
## Amazon MSK Consumers
- Kinesis Data Analytics for Apache Flink
- AWS Glue Streaming ETL Jobs (Apache Spark)
- Lambda
- EC2 applications on ECS, EKS
## AWS App Runner
- Managed web app/API deploy at scale
- No infra experience
- Source code or container image
- Auto build/deploy
- Auto scaling, HA, load balancer, encryption
- VPC access (DB, cache, queue)
- Use cases: web apps, APIs, microservices, rapid prod
## Amazon EC2
- Most popular AWS offering
- Elastic Compute Cloud
- IaaS
- Renting VMs (EC2)
- Storing data on virtual drives (EBS)
- Distributing load (ELB)
- Auto-scaling (ASG)
## EC2 Sizing & Configuration
- OS (Linux, Windows, Mac OS)
- Compute (CPU)
- RAM
- Storage (EBS & EFS network, EC2 Instance Store hardware)
- Network card (speed, Public IP)
- Firewall (security group)
- Bootstrap (EC2 User Data)
## EC2 User Data
- Bootstrap script
- Run commands at start
- Once at first start
- Automate boot tasks (updates, software, downloads)
- Runs as root user
## Docker Containers Management
- **Amazon ECS**: AWS container platform
- **Amazon EKS**: Managed Kubernetes
- **AWS Fargate**: Serverless container platform (with ECS/EKS)
- **Amazon ECR**: Store container images
## Amazon ECS – EC2 Launch Type
- Elastic Container Service
- Launch Docker on AWS
- Launch ECS Tasks on Clusters
- Provision EC2 infrastructure
- ECS Agent registers in cluster
- AWS starts/stops containers
## Amazon ECS – Fargate Launch Type
- Launch Docker on AWS
- No infrastructure to provision
- Serverless
- Create task definitions
- AWS runs based on CPU/RAM
- Scale by increasing tasks
## Amazon ECS – IAM Roles
- **EC2 Instance Profile** (EC2 Launch): ECS agent, API calls, CloudWatch Logs, ECR, Secrets/SSM
- **ECS Task Role**: Per-task role, defined in task definition
## Amazon ECS – Load Balancer Integrations
- **ALB**: Most use cases
- **NLB**: High throughput/performance, AWS Private Link pairing
- **Classic**: Supported but not recommended (no Fargate)
## Amazon ECS – Data Volumes (EFS)
- Mount EFS on tasks
- EC2 and Fargate launch types
- Multi-AZ shared data
- Fargate + EFS = Serverless
- S3 cannot be mounted as filesystem
## Amazon EKS Overview
- Elastic Kubernetes Service
- Managed Kubernetes clusters
- Open-source for containerized apps
- Alternative to ECS
- Supports EC2 worker nodes or Fargate serverless
- Use case: K8s migration to AWS
- Cloud-agnostic
- Multi-region: one EKS per region
- CloudWatch Container Insights
## Amazon EKS Diagram
- AWS Cloud, VPC, AZs
- Public/Private subnets, ELB, NGW
- EKS Service LBs (public/private)
- ASG, EKS nodes with Pods
## Amazon EKS Node Types
- **Managed Node Groups**: Creates/manages EC2, ASG managed by EKS, On-Demand or Spot
- **Self-Managed Nodes**: You create and register, prebuilt AMI (EKS Optimized AMI), On-Demand or Spot
- **AWS Fargate**: No maintenance, no nodes
## Amazon EKS Data Volumes
- StorageClass manifest on cluster
- Container Storage Interface (CSI) compliant driver
- **Support**: EBS, EFS (Fargate), FSx for Lustre, FSx for NetApp ONTAP
## Amazon Lex & Connect
- **Amazon Lex** (powers Alexa): Automatic Speech Recognition (ASR), NLU intent recognition, build chatbots/call center bots
- **Amazon Connect**: Receive calls, contact flows, virtual contact center, integrate with CRM/AWS, 80% cheaper, no upfront
## DocumentDB
- Aurora-like for MongoDB (NoSQL)
- Store/query/index JSON
- Same deployment as Aurora
- Fully Managed, multi-AZ replication
- 10GB increments
- Auto-scales millions req/sec
## Amazon ElastiCache Overview
- Managed Redis or Memcached
- In-memory DBs, high performance, low latency
- Reduce DB load (read-intensive)
- Stateless apps
- AWS managed (OS, optimization, setup, monitoring, recovery, backups)
- Heavy app code changes
## ElastiCache: DB Cache Architecture
- Apps query cache first
- Get from RDS if not available
- Store in ElastiCache
- Reduces RDS load
- Cache invalidation strategy
## ElastiCache: User Session Store
- User logs in
- Session data written to cache
- Other instance retrieves
- User auto-logged in
## ElastiCache – Redis vs Memcached
- **Redis**: Multi-AZ Auto-Failover, Read Replicas, Data Durability (AOF), Backup/restore, Sets/Sorted Sets
- **Memcached**: Multi-node sharding, no HA, non-persistent, backup/restore (Serverless), multi-threaded
## ElastiCache for Valkey
- Full Valkey compatibility (open source, fork of Redis)
- Alternative to Redis OSS
- **Vector search support** (important for GenAI/RAG/semantic caching)
- Billions of high-dimensional vectors
- Microsecond latency
- Recall > 99%
## Amazon MemoryDB
- Valkey and Redis OSS vector search
- All in-memory (super fast)
- Multi-AZ
- **Vector index algorithms**:
  - Flat: brute force linear
  - HNSW: faster execution approximation
## Amazon Neptune
- Fully managed graph database
- Social network example
- Multi-AZ, up to 15 read replicas
- Highly connected datasets
- Billions of relations, ms latency
- HA replications across AZs
- Knowledge graphs (Wikipedia), fraud detection, recommendations, social
## Neptune and GenAI
- **Neptune Analytics**: Engine on top of Neptune database
- **vectors.topKByEmbedding**: Query vectors with explicit values, filter by attributes, returns top nodes/scores
## AWS Cloud Development Kit (CDK)
- Define infra in familiar language
- JavaScript/TypeScript, Python, Java, .NET
- High level "constructs"
- Compiled to CloudFormation
- Deploy infra + runtime together
- Lambda, Docker (ECS/EKS)
## CDK in a Diagram
- CDK Application + Constructs + Programming Languages
- cdk synth → CDK CLI → CloudFormation Template
## CDK vs SAM
- **SAM**: Serverless focused, JSON/YAML, quick Lambda start, leverages CloudFormation
- **CDK**: All AWS services, programming languages, leverages CloudFormation
## CDK + SAM
- SAM CLI to test CDK apps locally
- Run cdk synth first
- sam local invoke -t template.json function
## CDK Hands-On
- Upload to S3 → trigger Lambda → Rekognition → DynamoDB save
## How Users Access AWS
- AWS Management Console (password + MFA)
- AWS CLI (access keys)
- AWS SDK (access keys)
- Access Keys generated via console
- Users manage own keys
- Keys are secret (don't share)
- Access Key ID = username, Secret = password
## Example Access Keys
- Don't share
## What's the AWS CLI?
- Interact via commands
- Direct public API access
- Scripts to manage resources
- Open source
- Alternative to console
## What's the AWS SDK?
- Language-specific APIs
- Access AWS programmatically
- Embedded in app
- SDKs: JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++
- Mobile SDKs: Android, iOS
- IoT Device SDKs: Embedded C, Arduino
- AWS CLI built on SDK for Python
## What is CloudFormation
- Declarative AWS infra outline
- Most resources supported
- Example: SG → 2 EC2 → S3 → ELB
- Creates in right order with config
## Benefits of CloudFormation (1/2)
- **Infrastructure as code**: No manual creation, code review changes
- **Cost**: Tagged resources, estimate costs, save by deleting/recreating
## Benefits of CloudFormation (2/2)
- **Productivity**: Destroy/recreate, auto diagrams, declarative, leverage templates
- Documentation
- Almost all AWS resources
- Custom resources for unsupported
## CloudFormation + Infrastructure Composer
- Visualize stacks
- WordPress example
- See resources and relations
## AWS CodeArtifact
- Software package management
- Code dependencies
- Artifact management traditional setup
- Secure, scalable, cost-effective
- Maven, Gradle, npm, yarn, twine, pip, NuGet
- Devs and CodeBuild retrieve dependencies
## AWS CodeArtifact Architecture
- Public Repos: NuGet, Java/.NET/Python/JavaScript
- AWS CodeArtifact Domain
- Repository A/B with packages
- VPC
- CodeBuild fetches
- IT Leader publish/approve
- Proxy
## CodeArtifact – EventBridge Integration
- CodeArtifact → EventBridge events
- Lambda, Step Functions, SNS, SQS
- CodePipeline (CodeCommit → CodeBuild → CodeDeploy)
- Rebuild & Redeploy with security fixes
- Events on package version create/modify/delete
## CodeArtifact – Resource Policy
- Authorize cross-account access
- Principal reads all packages or none
- Repository Resource Policy
## Amazon Augmented AI (A2I)
- Human ML prediction oversight
- Employees, 500,000+ AWS contractors, Mechanical Turk
- Pre-screened vendors
- ML on AWS or elsewhere (SageMaker, Rekognition)
- High-confidence → returned, Low-confidence → human review
- Reviews consolidated with weighted scores in S3
- Reviewed data → training set
## Amazon Kendra
- Managed document search service ML
- Extract answers from text/PDF/HTML/PowerPoint/Word/FAQs
- Natural language search
- Learn from user feedback (Incremental Learning)
- Manual fine-tuning (importance, freshness, custom)
- Sources: S3, RDS, Google Drive, SharePoint, OneDrive, 3rd party, APN, Custom
- Knowledge Index powered by ML
## Amazon Lex
- Build chatbots quickly (voice/text)
- Order pizzas, book hotel
- Multiple languages
- Lambda, Connect, Comprehend, Kendra
- Auto-understand intent → invoke Lambda
- Asks for "Slots" if needed
## Amazon Rekognition
- Find objects/people/text/scenes in images/videos
- Facial analysis, search, verification, counting
- Familiar faces or celebrities
- Use cases: Labeling, Content Moderation, Text Detection, Face Detection/Analysis, Face Search/Verification, Celebrity Recognition, Pathing
## Amazon Rekognition – Custom Labels
- Custom: logos in social media, products on shelves
- NFL uses for logos
- Label and upload to Rekognition
- Few hundred images
- Custom model trained
- Subsequent images categorized
## Amazon Rekognition – Content Moderation
- Auto-detect inappropriate content
- Filter harmful images in social/broadcast/ads
- Reduce human review to 1-5%
- Integrated with A2I
- **Custom Moderation Adaptors**: Your labeled images, enhance accuracy or specific use cases
## Content Moderation API – Diagram
- User → Chatbot → Image → Rekognition DetectModerationLabels → Pass
## Amazon Textract
- Extract text/handwriting/data from scanned documents
- Forms and tables
- Any document type (PDFs, images)
- Use cases: Financial (invoices, reports), Healthcare (records, claims), Public Sector (tax, IDs, passports)
## AWS Auto Scaling
- Backbone for scalable resources:
- EC2 Auto Scaling groups
- EC2 Spot Fleet requests
- ECS service desired count
- DynamoDB (table or GSI): WCU/RCU
- Aurora: Dynamic Read Replicas
## AWS Auto Scaling Plans
- **Dynamic scaling** (target tracking):
  - Optimize for availability (40% utilization)
  - Balance availability and cost (50%)
  - Optimize for cost (70%)
  - Custom (own metric)
  - Disable scale-in, cooldown, warmup
- **Predictive scaling**: Continuously forecast and schedule
## AWS Cost Anomaly Detection
- ML monitor cost/usage
- Detect unusual spends
- Historic patterns, no thresholds
- Monitor services, accounts, tags, categories
- Anomaly report with root-cause
- Individual alerts or summary (SNS)
## Cost Explorer
- Visualize/understand/manage costs/usage
- Custom reports
- High-level: total across accounts
- Monthly, hourly, resource granularity
- Optimal Savings Plan
- Forecast 18 months
## Cost Explorer – Various Views
- Monthly Cost by AWS Service
- Hourly & Resource Level
- Savings Plan (alternative to Reserved)
- Forecast Usage
## Amazon Managed Grafana
- Open-source platform for monitor/visualize/alert metrics/logs
- IAM Identity Center and SAML for users/permissions
- Grafana plugins and alerts
- Fully managed, auto-scale
- Encrypted, KMS
## Managed Grafana Data Sources
- AWS: CloudWatch, OpenSearch, Timestream, Athena, Redshift, X-Ray
- Amazon Managed Service for Prometheus (AMP)
- Other Grafana integrations: GitHub, Google, Azure, MySQL, Redis, JSON, OpenTelemetry
## AWS Systems Manager (SSM)
- Manage EC2 and on-prem at scale
- Hybrid AWS service
- Operational insights
- 10+ products
- **Features**: Patching automation, Run commands across fleet, SSM Parameter Store
- Linux, Windows, MacOS, Raspberry Pi OS
## How Systems Manager works
- Install SSM agent
- Default on Amazon Linux AMI and some Ubuntu
- SSM control issues = SSM agent issues
- Run commands, patch, configure
## SSM Session Manager
- Secure shell on EC2 and on-prem
- No SSH/bastion/keys
- No port 22
- Linux, macOS, Windows
- Logs to S3 or CloudWatch Logs
## SSM Parameter Store
- Secure storage configs/secrets
- API Keys, passwords, configurations
- Serverless, scalable, durable
- IAM access
- Version tracking, encryption optional (KMS)
## AWS DataSync
- Move large data
- On-prem/other cloud to AWS (NFS, SMB, HDFS, S3 API) — needs agent
- AWS to AWS — no agent
- **Sync to**: S3 (any class including Glacier), EFS, FSx (Windows, Lustre, NetApp, OpenZFS)
- Hourly, daily, weekly schedule
- Permissions/metadata preserved (NFS POSIX, SMB)
- 10 Gbps per task, bandwidth limit
## DataSync NFS/SMB to AWS
- On-prem NFS/SMB → DataSync Agent → AWS DataSync → S3, EFS, FSx
- TLS
- AWS Snowcone (agent pre-installed)
## DataSync AWS-to-AWS Transfer
- Copy between FSx, EFS, S3 services
## AWS Transfer Family
- Managed FTP for S3 or EFS
- **Protocols**: AWS Transfer for FTP, FTPS, SFTP
- Managed infra, scalable, reliable, multi-AZ
- Pay per provisioned endpoint hour + GB transfers
- Store credentials or integrate (AD, LDAP, Okta, Cognito, custom)
- Sharing files, public datasets, CRM, ERP
## AWS Transfer Family Architecture
- Users (FTP client) → Route 53 → Transfer Family → S3, EFS
- MS AD, LDAP authenticate
- IAM Role
## Amazon CloudFront
- Content Delivery Network (CDN)
- Improve read performance
- Edge caching
- Better UX
- Hundreds of POPs globally
- DDoS protection (Shield, WAF)
## CloudFront Origins
- **S3 bucket**: Distribute/cache files, upload through CloudFront, secured with Origin Access Control (OAC)
- **VPC Origin**: Apps in private subnets, ALB/NLB/EC2
- **Custom Origin (HTTP)**: S3 website, public HTTP backend
## CloudFront High Level
- Edge Location → Local Cache → Forward to Origin
- HTTP/HTTPS
## CloudFront S3 as Origin
- Edges in LA, Mumbai, Melbourne, São Paulo
- Public www to edges
- OAC + S3 bucket policy
- Private AWS internal
## CloudFront vs S3 Cross-Region Replication
- **CloudFront**: Global Edge, TTL cache (day), static content everywhere
- **S3 CRR**: Per-region setup, near real-time, read-only, dynamic content low-latency in few regions
## What is Load Balancing?
- Forward internet traffic to multiple servers (EC2)
## Why Load Balancer?
- Spread load
- Single DNS
- Handle failures
- Health checks
- SSL termination
- HA across zones
## Why Elastic Load Balancer?
- Managed
- AWS guarantees
- Upgrades/maintenance/HA
- Few config knobs
- Cheaper but more effort to roll your own
- 4 types: Application LB (Layer 7), Network LB (Layer 4), Gateway LB (Layer 3), Classic LB (retired 2023)
## Load Balancer Types
- **Network LB (NLB)**: TCP/UDP Layer 4, millions req/sec, Static IP via Elastic IP
- **Application LB (ALB)**: HTTP/HTTPS/gRPC Layer 7, HTTP routing, Static DNS (URL)
- **Gateway LB (GWLB)**: GENEVE Protocol Layer 3, Route to firewalls, Intrusion detection
## AWS Global Accelerator
- AWS internal network routing
- 2 Anycast IPs
- Send traffic to Edge Locations
- Edges to application
## AWS Global Accelerator Features
- EIP, EC2, ALB, NLB, public/private
- **Consistent Performance**: Lowest latency routing, fast failover
- No client cache issue (IP doesn't change)
- Internal AWS network
- **Health Checks**: App health, global, < 1 minute failover, DR
- **Security**: 2 external IPs whitelisted, AWS Shield DDoS
## Global Accelerator vs CloudFront
- Both: AWS global network/edges, AWS Shield
- **CloudFront**: Cacheable + dynamic content, content at edge
- **Global Accelerator**: TCP/UDP apps, proxies packets at edge, non-HTTP (gaming UDP, IoT MQTT, VoIP), HTTP needing static IPs, deterministic failover
## Amazon Route 53
- HA, scalable, fully managed Authoritative DNS
- You can update records
- Domain Registrar
- Health checks
- 100% availability SLA
- Port 53 reference
## Route 53 Records
- Route traffic for domain
- Contains: Domain/subdomain, Type, Value, Routing Policy, TTL
- Types: A, AAAA, CNAME, NS (must know), CAA, DS, MX, NAPTR, PTR, SOA, TXT, SPF, SRV (advanced)
## Route 53 Record Types
- **A**: hostname → IPv4
- **AAAA**: hostname → IPv6
- **CNAME**: hostname → another hostname (target needs A or AAAA, can't be Zone Apex)
- **NS**: Name Servers for Hosted Zone, traffic routing
## Route 53 Hosted Zones
- Container for records
- **Public**: Internet records (public domains)
- **Private**: VPC records (private domains)
- $0.50/month/zone
## Route 53 Public vs Private Zones
- Public: example.com → 54.22.33.44 from client
- Private: db.example.internal → 10.0.0.35 within VPC
## What's an EBS Volume?
- Elastic Block Store
- Network drive attached to instances
- Persist data after termination
- One instance at a time (CCP level)
- Bound to AZ
- "Network USB stick"
## EBS Volume Details
- Network drive (some latency)
- Detach/attach quickly
- Locked to AZ
- Move via snapshot
- Provisioned capacity (GB, IOPS)
- Billed for provisioned
- Increase capacity over time
## EBS Volume Example
- US-EAST-1A: 10 GB, 100 GB, 50 GB volumes
- US-EAST-1B: 50 GB, 10 GB volumes
- Unattached possible
## EBS Delete on Termination
- Controls behavior on EC2 terminate
- Root EBS deleted by default
- Other attached EBS not deleted by default
- AWS console / CLI control
- Preserve root on termination
## Amazon EFS
- Elastic File System
- Managed NFS, mount on many EC2
- Multi-AZ
- HA, scalable, expensive (3x gp2), pay per use
## Amazon EFS Use Cases
- Content management, web serving, data sharing, WordPress
- NFSv4.1
- Security group access
- Linux only (not Windows)
- KMS encryption
- POSIX (~Linux), standard file API
- Auto scaling, no capacity planning
## EFS Performance & Storage Classes
- **Scale**: 1000s NFS clients, 10 GB+/s throughput, Petabyte-scale
- **Performance Mode** (set at creation):
  - General Purpose (default): latency-sensitive
  - Max I/O: higher latency, throughput, parallel
- **Throughput Mode**:
  - Bursting: 1 TB = 50MiB/s + burst 100MiB/s
  - Provisioned: Set throughput regardless of size
  - Elastic: Auto scale, up to 3GiB/s read, 1GiB/s write, unpredictable workloads
## EFS Storage Classes
- **Storage Tiers** (lifecycle):
  - Standard: frequent
  - Infrequent (EFS-IA): retrieval cost, lower storage
  - Archive: rarely (few/year), 50% cheaper
- Lifecycle policies move files
- **Availability/Durability**:
  - Standard: Multi-AZ, prod
  - One Zone: One AZ, dev, backup default, IA compatible (90% cost savings)
## EBS vs EFS – EBS
- One instance (except multi-attach io1/io2)
- Locked to AZ
- gp2: IO with disk size
- gp3 & io1: Independent IO
- Migrate via snapshot to another AZ
- Backups use IO (avoid heavy traffic)
- Root EBS deleted by default (configurable)
## EBS vs EFS – EFS
- 100s instances across AZ
- Share website files (WordPress)
- Linux only (POSIX)
- Higher price than EBS
- Storage Tiers for savings
- Remember: EFS vs EBS vs Instance Store
---
 
# 11. Making GenAI Architectural Decisions
 
## Production Systems Are More Than Bedrock
- Generative AI Application Builder reference architecture
## Choosing a Vector Store
- **OpenSearch (managed)**: Custom RAG at scale, mature, control, $$-$$$, medium ops, VPC patterns, pay for capacity, tuning matters
- **OpenSearch Serverless**: Spiky traffic, low-ops, $-$$ usage, low ops, IAM-centric, less control
- **Amazon Kendra**: Enterprise document search with permissions, $$$, very low ops, strong enterprise security, less tinkering
- **Aurora PostgreSQL + pgvector**: RAG + relational, $$, medium ops, compliance + governance, GovCloud, needs pgvector, scaling/ANN tuning
- **Neptune Analytics**: RAG + graph relationships, $$-$$$, medium ops, regulated industries, analytics engine, vector loading constraints
- **Amazon S3 Vectors**: Massive-scale cost-optimized, $ very cost-driven, very low ops, S3 IAM, metadata limits, can be slow
## Vector Store Decision Heuristics
- SharePoint/Confluence/document permissions/ACLs → Kendra
- Graph relationships (fraud rings, lineage) → Neptune Analytics
- Already on Postgres + joins/transactions + vector → Aurora + pgvector
- Huge corpus + cost pressure + S3-tied → S3 Vectors
- Full search + tuning control → OpenSearch managed
- Unpredictable traffic + minimize ops → OpenSearch Serverless
## Vector Store Decision (First Principles)
- Cost-first: S3 Vectors (massive corpora, infrequent queries)
- Permissions-first: Kendra
- Relationship-first: Neptune Analytics
- SQL-first: Aurora + pgvector
- Search-first: OpenSearch (managed/serverless)
## OpenSearch vs OpenSearch Serverless
- **Billing**: Always-on nodes vs Per-request + storage
- **Tuning**: Full control (HNSW, shards) vs Limited
- **Latency**: Predictable vs Variable
- **Scaling**: Manual/Auto vs Automatic
- **Exam Bias**: "Need fine-grained control" vs "Unpredictable traffic"
## Orchestration: When Step Functions?
- Auditable state transitions
- Retry & failure isolation
- Explicit approval steps
- Human approval
- Serverless nice, but not the only choice
## Example: Internal Legal Q&A Chatbot
- Internal use, no CloudFront/WAF needed
- Kendra for document-level access control + SharePoint
- Cognito authenticates, user context to Kendra
- Bedrock retrieval and generation
- Architecture: API Gateway → Lambda → Bedrock + Kendra (S3 + Sharepoint), Cognito
## Example: Customer-facing Chatbot
- External-facing: WAF, CloudFront, API Gateway
- Lambda calls Bedrock with OpenSearch data
- Lambda may do other DB queries
- Cognito for personal/private info
- Guardrails consideration
- Ingestion: S3 → EventBridge → Lambda → Bedrock embeddings → OpenSearch
- Architecture: WAF → CloudFront → API Gateway → Lambda → Bedrock + OpenSearch (Serverless)
---
 
# 12. Exam Preparation
 
## More Prep Resources
- Various preparation materials
## AWS Skill Builder
- Free resources likely sufficient
- Standard Exam Prep Plan with Amazon training
- Official Practice Question Set (20 questions)
- URL: skillbuilder.aws/learning-plan/9VXVGYT38G
## Practice Exams
- Includes Amazon's
- Full-length practice exam in subscription materials
- Practice exam in this course
## Amazon's Exam Guide
- d1.awsstatic.com link to exam guide PDF
## Consider Certified AI Practitioner First
- Take AI Practitioner exam first
## New Question Types
- Old: Multiple choice (1 of 4), Multiple response (2+ of 5+)
- **New**: 
  - **Ordering**: Choose 3-5 in correct order, no partial credit
  - **Matching**: Match to 3-7 prompts, no partial credit
- Case study type dropped
## Ordering
- Place items in order
## Matching
- Match items to prompts
## What to Expect
- Exam expectations
## Sitting for the Exam
- 3 hours (170 min)
- Probably need ~2 hours
- 75 questions (85 beta with 205 min)
- Take time to fully understand
- Use flag capability
- Time to double-check
- Can't bring anything (paper, earplugs given)
- Empty room for at-home
- Schedule smartly (high-energy time)
- Different testing providers different availability
- Testing center can be better (no environment validation, no glitches)
## Prepare
- Bathroom before
- Eat (not right before)
- Good night's sleep
- Review memorization (evaluation metrics, new services)
- Be alert
- $300 on the line ($150 beta)
- Take practice exams repeatedly
## Strategies
- Don't rush
- Per question understand: optimization goal, requirements, system as whole
- Pace 2-2.5 minutes/question
- Longer → guess, flag, return
- Process of elimination
- Keep calm, don't need 100%
## Your AWS Certification Journey
- **Foundational**: Knowledge-based, foundational AWS Cloud, no prior experience
- **Professional**: Role-based advanced skills, secure/optimized/modern apps, 2+ years AWS
- **Associate**: Role-based, knowledge/skills, prior cloud or strong on-prem
- **Specialty**: Trusted advisor in strategic areas
## AWS Certification Paths – Architecture
- Solutions Architect: Design/develop/manage cloud, work with DevOps for migration
- Application Architect: Design app architecture (UI, middleware, infra), enterprise scalable
## AWS Certification Paths – Operations
- Systems Administrator: Install/upgrade/maintain components, automation
- Cloud Engineer: Implement/operate networked computing, security systems
## AWS Certification Paths – DevOps
- Test Engineer: Embed testing/quality from design to release
- Cloud DevOps Engineer: Design/deploy/operate large-scale hybrid, CI/CD pipelines
- DevSecOps Engineer: Accelerate cloud adoption with stable CI/CD principles
## AWS Certification Paths – Security
- Cloud Security Engineer: Security architecture, cyber security designs, measures to protect
- Cloud Security Architect: Enterprise cloud governance, identify/communicate/minimize risks
## AWS Certification Paths – Development & Networking
- Software Development Engineer: Develop/construct/maintain software
- Network Engineer: Design/implement networks (LAN, WAN, intranets)
## AWS Certification Paths – Data Analytics & AI/ML
- Cloud Data Engineer: Automate data collection/processing, monitor pipelines
- Machine Learning Engineer: Research/build/design AI systems, automate predictive models
## AWS Certification Paths – AI/ML
- Prompt Engineer: Design/test/refine text prompts
- Machine Learning Ops Engineer: Build/maintain AI/ML platforms and infra
- Data Scientist: Develop/maintain AI/ML models, train/fine-tune, evaluate
---
 
# Congratulations!
