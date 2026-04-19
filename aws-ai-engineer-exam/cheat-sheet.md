AIP-C01
│
├── TARGET PROFILE
│ ├── 2+ yrs production AWS / open-source / AI-ML / data eng
│ ├── 1 yr hands-on GenAI solutions
│ └── Foundational: Compute, Storage, Networking, IAM, IaC, Monitoring
│
├── [I] GENERATIVE AI FUNDAMENTALS & BEDROCK
│ │
│ ├── FOUNDATION MODELS (FMs)
│ │ ├── Large pre-trained TRANSFORMER models
│ │ ├── AWS Nova — Amazon's own FM suite
│ │ ├── Jurassic-2 (AI21 Labs)
│ │ │ └── Multilingual LLM → Spanish, French, German, Portuguese, Italian, Dutch
│ │ ├── Claude (Anthropic)
│ │ │ └── Conversations, Q&A, workflow automation
│ │ ├── Stable Diffusion (stability.ai)
│ │ │ └── Image, art, logo, design generation
│ │ ├── Llama (Meta) — LLM
│ │ └── Amazon Titan
│ │ └── Summarization, Q&A, Embeddings, Personalization, Search
│ │
│ ├── FINE-TUNING (Custom Models)
│ │ ├── Purpose → adapt LLM to specific use case w/ proprietary data
│ │ ├── Benefits
│ │ │ ├── Eliminates extensive prompt engineering
│ │ │ └── Saves tokens long-term
│ │ ├── Bedrock-tunable models → Titan, Cohere, Meta
│ │ ├── Data formats
│ │ │ ├── Text → labeled pairs (prompt + completion)
│ │ │ └── Image → S3 paths linked to image descriptions
│ │ ├── Security → VPC + PrivateLink (sensitive training data)
│ │ └── Fine-tuned = usable like any other FM
│ │
│ ├── RAG (Retrieval-Augmented Generation)
│ │ ├── Analogy → "open-book exam" for LLMs
│ │ ├── Flow → query vector store → retrieve context → inject into prompt
│ │ ├── vs Fine-tuning → Faster + cheaper + easier updates (just update DB)
│ │ ├── Uses semantic search via vector stores
│ │ ├── Helps prevent HALLUCINATIONS
│ │ └── Performance sensitive to:
│ │ ├── Prompt templates
│ │ └── Relevancy of retrieved info
│ │
│ ├── KNOWLEDGE BASES / VECTOR DBs
│ │ ├── Bedrock Knowledge Bases (facilitate RAG)
│ │ ├── Sources
│ │ │ ├── S3
│ │ │ ├── Web crawlers
│ │ │ ├── Confluence
│ │ │ ├── Salesforce
│ │ │ └── SharePoint
│ │ ├── Required Components
│ │ │ ├── Embedding model → Cohere OR Amazon Titan
│ │ │ └── Vector store
│ │ │ ├── OpenSearch Service (can act as vector DB)
│ │ │ ├── Aurora
│ │ │ ├── MemoryDB w/ Valkey
│ │ │ ├── ElastiCache w/ Valkey
│ │ │ ├── MongoDB Atlas
│ │ │ ├── Pinecone
│ │ │ └── Redis Enterprise Cloud
│ │ └── Default for DEV → Serverless OpenSearch
│ │
│ ├── OPTIMIZING EMBEDDINGS & RETRIEVAL
│ │ ├── CHUNKING → splits data before storage; determines tokens/vector
│ │ │ ├── Hierarchical Chunking
│ │ │ │ ├── Small CHILD chunks → precision
│ │ │ │ └── Replaced w/ larger PARENT chunks → context
│ │ │ └── Semantic Chunking
│ │ │ └── FM breaks content by semantic meaning (NOT fixed length)
│ │ ├── VECTOR SIZE (dimensionality)
│ │ │ └── Balance cost vs retrieval performance
│ │ └── METADATA (stored alongside chunks)
│ │ ├── Document ID
│ │ ├── Topic
│ │ └── Access control
│ │ └── → improves relevance scoring + filtering
│ │
│ ├── BEDROCK GUARDRAILS
│ │ ├── Filters on INPUTS (prompts) + OUTPUTS (responses)
│ │ ├── Filter types
│ │ │ ├── Word filtering
│ │ │ ├── Topic filtering
│ │ │ ├── Profanities
│ │ │ └── PII removal / masking
│ │ ├── Contextual Grounding Check
│ │ │ └── Measures response alignment w/ retrieved context → prevents hallucinations
│ │ └── Attachable to → Agents + Knowledge Bases
│ │
│ ├── TOKEN-LEVEL REDACTION
│ │ ├── Beyond standard Guardrails
│ │ ├── Custom pre/post-processing handlers around inference endpoints
│ │ ├── Input filter OR output filter
│ │ └── Uses → Amazon Comprehend (NER + pattern matching)
│ │
│ └── PROMPT ENGINEERING & FLOWS
│ ├── Prompt Structure
│ │ ├── Instructions
│ │ ├── Context
│ │ ├── Input data
│ │ └── Output indicator
│ ├── Techniques
│ │ ├── Few-shot → examples of desired outputs
│ │ └── Chain of Thought (CoT) → "think step by step"
│ ├── Bedrock Prompt Management → store + version reusable prompts (w/ variables)
│ ├── Bedrock Flows → chain models/prompts/conditions (visual OR JSON)
│ └── Structured JSON output → describe schema in instructions
│
├── [II] MANAGING DATA FOR GENERATIVE AI
│ │
│ ├── DATA STRUCTURING
│ │ ├── Problem → raw unstructured text loses headings/tables
│ │ ├── Amazon Textract + Amazon Comprehend → extract structure
│ │ ├── Convert to HTML → preserve organization
│ │ └── Divider strings (e.g., <SECTION_BREAK>)
│ │ ├── Inserted via Lambda preprocessor
│ │ └── OR AWS Glue ETL pipeline
│ │ └── → improves chunking for vector stores
│ │
│ ├── BEDROCK DATA AUTOMATION (BDA)
│ │ ├── Extracts structured data from MULTIMODAL inputs
│ │ │ ├── Documents
│ │ │ ├── Images
│ │ │ ├── Videos
│ │ │ └── Audio
│ │ ├── Used for → IDP (Intelligent Document Processing) + KB prep
│ │ ├── BLUEPRINTS → specify exact fields to extract
│ │ ├── Output formats
│ │ │ ├── JSON
│ │ │ ├── JSON + files (CSV, markdown)
│ │ │ ├── HTML
│ │ │ └── CSV
│ │ ├── Video Processing
│ │ │ ├── Full summary
│ │ │ ├── Chapter summaries
│ │ │ └── Transcripts
│ │ └── Audio Processing
│ │ ├── Full transcript
│ │ ├── Speaker labeling
│ │ ├── Topic breakdown
│ │ └── Content moderation
│ │
│ ├── AMAZON TRANSCRIBE
│ │ ├── ASR (Automatic Speech Recognition) → speech → text
│ │ ├── PII Redaction
│ │ ├── Automatic Language Identification
│ │ ├── Accuracy Boosters
│ │ │ ├── Custom Vocabularies → domain words, brands, acronyms
│ │ │ └── Custom Language Models → trained on domain-specific text
│ │ └── Toxicity Detection (ML voice-based)
│ │ └── Hate speech, profanity categories
│ │
│ ├── AMAZON COMPREHEND
│ │ ├── Text analysis + NER + topic modeling
│ │ ├── Custom Classification → user-defined categories
│ │ ├── NER → predefined general entities (people, places, orgs)
│ │ ├── Custom Entity Recognition → business-specific (e.g., policy numbers)
│ │ └── Lambda integration → redact PII / classify / extract BEFORE Bedrock
│ │
│ └── VECTOR STORE OPTIMIZATION (OpenSearch)
│ ├── Binary vectors → bit sequences, 32x compression vs float32
│ ├── FP16 → 16-bit dim storage (scalar quantization used by HNSW)
│ ├── Hierarchical Indices → small top-level routes to detailed sub-indices
│ └── Neural Plugin → OpenSearch calls Bedrock for embeddings (ingest/search)
│
├── [III] AGENTIC AI
│ │
│ ├── BEDROCK AGENTS
│ │ ├── FMs + Tools + Planning + Memory
│ │ ├── Planning Module → breaks requests into sub-questions
│ │ └── Action Groups → define tools
│ │ └── OpenAPI (Swagger) schema in S3
│ │ └── Standardizes funcs, inputs, outputs → improves reliability
│ │
│ ├── AGENT WORKFLOWS
│ │ ├── Multi-agent
│ │ │ ├── Orchestrator → delegates subtasks
│ │ │ ├── Worker LLMs → execute
│ │ │ └── Synthesizer → combines results
│ │ ├── Chain of Sequence → sequential, output feeds next step
│ │ ├── Parallelization → concurrent (multi-guardrails, voting across models)
│ │ └── MCP (Model Context Protocol)
│ │ ├── Standardized agent-tool interface
│ │ ├── JSON-RPC 2.0 transport
│ │ ├── Over HTTP or stdio
│ │ └── "universal connector"
│ │
│ ├── AGENT MEMORY
│ │ ├── Short-term → chat history / immediate context
│ │ │ └── Sessions + Events
│ │ ├── Long-term → insights, summaries, preferences
│ │ │ └── Memory Records / Strategies
│ │ └── AgentCore Memory → scalable serverless storage
│ │
│ ├── AMAZON Q BUSINESS
│ │ ├── Managed GenAI assistant for employees
│ │ ├── Data Connectors
│ │ │ ├── S3
│ │ │ ├── SharePoint
│ │ │ ├── Slack
│ │ │ └── Salesforce
│ │ ├── Plugins
│ │ │ ├── Custom
│ │ │ └── Native → Jira, ServiceNow
│ │ ├── Auth → IAM Identity Center (respects user doc permissions)
│ │ └── Admin Controls (guardrails)
│ │ ├── Block words/topics
│ │ └── Restrict to internal knowledge only
│ │
│ ├── AMAZON Q APPS
│ │ └── Non-coders build GenAI productivity apps via natural language
│ │ └── Uses company data + plugins
│ │
│ ├── AMAZON Q DEVELOPER
│ │ ├── GenAI assistance based on AWS documentation
│ │ ├── CLI command suggestions
│ │ ├── Security scans
│ │ ├── Code gen/completion
│ │ ├── IDE Extensions
│ │ │ ├── Visual Studio Code
│ │ │ ├── Visual Studio
│ │ │ └── JetBrains
│ │ └── Project rules → ./amazon/rules directory
│ │
│ └── HUMANS IN THE LOOP (HITL)
│ ├── Human Augmentation → AI drafts, human refines
│ ├── Escalation Criteria → confidence-score routing to experts
│ └── Feedback Pipeline
│ ├── Front-end → API Gateway
│ └── Storage → DynamoDB (measure variant preference)
│
├── [IV] OPERATIONAL EFFICIENCY & OPTIMIZATION
│ │
│ ├── COST & TOKEN EFFICIENCY
│ │ ├── Bedrock CountTokens API → FREE, pre-invoke estimate
│ │ ├── CloudWatch metrics
│ │ │ ├── InputTokenCount
│ │ │ └── outputTokenCount
│ │ ├── Context Pruning
│ │ │ ├── Limit RAG chunks retrieved
│ │ │ ├── Filter via metadata
│ │ │ └── Summarize old chat history
│ │ ├── Response Size Controls
│ │ │ ├── maxTokens param
│ │ │ └── Prompt directive ("respond in 50 words or less")
│ │ └── Provisioned Throughput
│ │ ├── For consistent high-workload perf
│ │ └── Tied to SPECIFIC MODEL ARN
│ │
│ ├── MODEL SELECTION & ROUTING
│ │ ├── Cost/Capability Tradeoff → smaller model OK if RAG/tools handle "smarts"
│ │ ├── Dynamic Routing → Intelligent Prompt Routing (built into Bedrock)
│ │ │ ├── Complex query → larger model
│ │ │ └── Simple query → smaller cheaper model
│ │ └── Bedrock Evaluations → perf vs cost tradeoffs
│ │
│ ├── LATENCY & CACHING
│ │ ├── Prompt Caching (built-in Bedrock)
│ │ │ ├── Caches STATIC PREFIX (instructions, system prompt)
│ │ │ ├── Only dynamic content re-tokenized
│ │ │ ├── Cached reads DISCOUNTED; writes may cost more
│ │ │ └── Monitored in CloudWatch
│ │ └── TTFT (Time to First Token) → streaming latency metric in CloudWatch
│ │
│ ├── MODEL TUNING
│ │ ├── Evaluated via
│ │ │ ├── Bedrock Evaluations
│ │ │ └── CloudWatch Evidently (A/B testing)
│ │ └── Key Parameters
│ │ ├── Temperature → 0 deterministic … 1 creative/random
│ │ ├── Top_p → probability threshold / nucleus sampling
│ │ └── Top_k → sample size of token options
│ │
│ ├── SAGEMAKER SYSTEM OPTIMIZATION
│ │ ├── Large models up to 500GB
│ │ ├── Adjust → container health check + download timeout quotas
│ │ └── Instance types
│ │ ├── ml.p4d.24xlarge → GPU, large models
│ │ └── ml.c5.9xlarge → CPU, small tasks (e.g., NER)
│ │
│ └── SYSTEM RESILIENCY
│ ├── Chain of Thought → better reasoning on complex tasks
│ ├── Exponential Backoff → retry pattern
│ └── Circuit Breaker → often Step Functions + DynamoDB
│
├── [V] MANAGING MODELS WITH SAGEMAKER AI
│ │
│ ├── MODEL DEPLOYMENT
│ │ ├── Models stored in S3
│ │ ├── Persistent Endpoint → real-time inference
│ │ └── Batch Transform → offline prediction
│ │
│ ├── MODEL MONITORING (SageMaker Model Monitor)
│ │ ├── CloudWatch alerts on quality deviations
│ │ ├── Visualizes DATA DRIFT
│ │ │ ├── Missing input features
│ │ │ └── Shifting approval rates
│ │ └── Anomaly detection + new feature monitoring
│ │
│ ├── BIAS & EXPLAINABILITY (SageMaker Clarify)
│ │ ├── Integrated w/ Model Monitor
│ │ ├── Bias metrics
│ │ │ ├── CI → Class Imbalance
│ │ │ └── DPL → Difference in Proportions of Labels
│ │ └── Explainability → feature contribution to predictions
│ │
│ └── DATA LABELING
│ ├── Amazon Rekognition → image labels
│ └── Amazon Comprehend → text labels / topic modeling
│
├── [VI] MORE TOOLS FOR BUILDING AI APPS
│ │
│ ├── AWS LAMBDA
│ │ ├── Connect agents to external tools
│ │ ├── Param validation / error handling
│ │ ├── On-demand FM invocation (no provisioning)
│ │ ├── Webhook handling (API Gateway JSON events)
│ │ └── Custom aggregation (weighted avg, voting)
│ │
│ ├── AMAZON APPFLOW
│ │ ├── Data integration service
│ │ ├── Sources → S3, Redshift, Snowflake, Marketo
│ │ ├── SaaS → Salesforce, Zendesk
│ │ └── ETL pipelines to/from GenAI systems
│ │
│ ├── AWS CDK
│ │ ├── IaC in TypeScript, Python, Java
│ │ ├── Compiles to CloudFormation
│ │ └── Deploy infra + app together (ECS/Fargate, Lambda)
│ │
│ ├── AMAZON KENDRA
│ │ ├── ML-powered doc search w/ natural language
│ │ ├── Supports PDFs, HTML, MS Word
│ │ ├── Incremental Learning (from user interactions)
│ │ └── Manual fine-tuning of results
│ │
│ ├── API GATEWAY
│ │ ├── Secure API front-end
│ │ ├── Traffic management
│ │ └── Proxy for Lambda → FM / feedback collection
│ │
│ └── AWS TRANSFER FAMILY
│ ├── Managed file transfers → SFTP, FTPS, FTP
│ ├── FTP → VPC ONLY
│ └── Destinations → S3, EFS
│ └── Entry point for training/RAG ingestion
│
├── [VII] GOVERNANCE & QA
│ │
│ ├── RESPONSIBLE AI — Core Dimensions
│ │ ├── Fairness
│ │ ├── Explainability
│ │ ├── Privacy & Security
│ │ ├── Safety
│ │ ├── Controllability
│ │ ├── Veracity & Robustness
│ │ ├── Governance
│ │ └── Transparency
│ │ │
│ │ └── Tools
│ │ ├── SageMaker Clarify → bias + explainability
│ │ ├── Bedrock Model Evaluation
│ │ └── Amazon Augmented AI (A2I) → human review loops
│ │
│ ├── EVALUATION TECHNIQUES
│ │ ├── Human Evaluation → subjective (UX, creativity, complexity)
│ │ ├── Bedrock Evaluation Jobs → benchmarks or LLM judges
│ │ ├── RAG Metrics
│ │ │ ├── Correctness
│ │ │ ├── Completeness
│ │ │ ├── Helpfulness
│ │ │ ├── Logical coherence
│ │ │ └── Faithfulness → response ↔ retrieved text alignment
│ │ ├── Prompt Dataset
│ │ │ ├── Reference responses (optional ground truth)
│ │ │ └── Reference contexts (optional)
│ │ └── ROUGE → word/n-gram overlap vs ground truth
│ │ └── For summarization / translation
│ │
│ ├── AGENT TRACING (Bedrock Agent Tracing)
│ │ ├── Visibility into agent decisions
│ │ ├── Shows → reasoning, KBs hit, action groups invoked, errors
│ │ └── Trace Types
│ │ ├── PreProcessing
│ │ ├── Orchestration
│ │ ├── PostProcessing
│ │ └── Guardrail
│ │
│ └── OBSERVABILITY (CloudWatch Logs)
│ ├── Log groups + log streams
│ ├── KMS encryption supported
│ └── Export destinations → S3, Kinesis, Lambda, OpenSearch
│
├── [VIII] SECURITY, IDENTITY & COMPLIANCE
│ ├── IAM → roles + permissions
│ ├── AWS KMS → encryption keys
│ ├── Amazon Macie → data security + DLP (sensitive data discovery)
│ ├── AWS Secrets Manager → store + rotate creds, API keys
│ ├── Amazon Cognito → user auth/authz for web/mobile
│ ├── AWS WAF → protects from common web exploits
│ └── VPC + AWS PrivateLink
│ └── Private VPC↔AWS connectivity (critical for sensitive fine-tuning data)
│
├── [IX] OTHER SERVICES TO KNOW
│ │
│ ├── ANALYTICS
│ │ └── Amazon QuickSight → serverless BI
│ │ ├── Visualizations
│ │ ├── Paginated reports
│ │ ├── Ad-hoc analysis
│ │ └── Anomaly detection
│ │
│ ├── DATABASE
│ │ ├── Neptune Analytics
│ │ │ ├── Analytics engine on Neptune
│ │ │ ├── Vector DB querying
│ │ │ └── topKByEmbedding → top nodes + scores by vector
│ │ ├── RDS / Aurora
│ │ └── DynamoDB
│ │
│ ├── MANAGEMENT & GOVERNANCE
│ │ ├── AWS CloudTrail → API call logs
│ │ └── AWS Well-Architected Generative AI Lens
│ │ └── GenAI Lifecycle
│ │ ├── Scoping
│ │ ├── Model Selection
│ │ ├── Customization
│ │ ├── Integration
│ │ ├── Deployment
│ │ └── Continuous Improvement
│ │
│ ├── NETWORKING & CONTENT DELIVERY
│ │ └── Amazon CloudFront → CDN
│ │ ├── Edge caching (hundreds of locations)
│ │ └── Integrates w/ AWS Shield + WAF (DDoS protection)
│ │
│ └── COMPUTE / CONTAINERS
│ └── Amazon EMR → big data frameworks (Spark, Hadoop)
│
└── [X] EXAM PREPARATION
├── Traditional Types
│ ├── Multiple Choice
│ └── Multiple Response → NO partial credit
└── NEW Question Types (NOT in beta exam)
├── Ordering → place 3-5 responses in correct sequence
├── Matching → pair items from 2 lists
└── NO partial credit for new types
