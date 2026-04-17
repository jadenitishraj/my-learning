LECTURE-ROOT
│
├── PART-1 :: MULTIMODAL RAG
│ │
│ ├── 1.1 WHAT-IS-RAG
│ │ │ └─ "Retrieval-Augmented Generation"
│ │ │ └─ Open-book exam for the LLM
│ │ │
│ │ ├── PROBLEM-IT-SOLVES
│ │ │ │
│ │ │ ├── stale-knowledge
│ │ │ │ └─ LLM frozen at training cutoff
│ │ │ │ └─ doesn't know yesterday's news
│ │ │ │
│ │ │ ├── private-data-blindness
│ │ │ │ └─ never saw your Jira, Confluence, manuals
│ │ │ │ └─ can't answer "error X-417"
│ │ │ │
│ │ │ ├── hallucination
│ │ │ │ └─ model invents confident wrong answers
│ │ │ │ └─ made-up books, fake citations
│ │ │ │
│ │ │ └── retrain-is-not-viable
│ │ │ └─ costs millions of dollars
│ │ │ └─ takes weeks of GPU time
│ │ │
│ │ ├── THE-TRICK
│ │ │ └─ don't teach the model, FEED it the answer at prompt-time
│ │ │
│ │ └── THE-3-WORDS
│ │ │
│ │ ├── Retrieval
│ │ │ └─ find relevant info from a database
│ │ │ └─ similarity search
│ │ │
│ │ ├── Augmented
│ │ │ └─ stuff info into the prompt as context
│ │ │ └─ prompt = question + chunks
│ │ │
│ │ └── Generation
│ │ └─ LLM reads context + question → answers
│ │ └─ grounded, not remembered
│ │
│ ├── 1.2 RAG-ARCHITECTURE
│ │ │ └─ two phases — spell them out clearly
│ │ │
│ │ ├── PHASE-1 :: OFFLINE (Ingestion / Indexing)
│ │ │ │ └─ runs once, or when new data arrives
│ │ │ │
│ │ │ ├── step-1 :: collect-raw-docs
│ │ │ │ └─ PDFs, wiki pages, product manuals, tickets
│ │ │ │
│ │ │ ├── step-2 :: chunk
│ │ │ │ │ └─ break docs into small pieces (~500 words)
│ │ │ │ │
│ │ │ │ ├── why-chunk
│ │ │ │ │ └─ LLM has context-window limits
│ │ │ │ │ └─ big docs are noisy
│ │ │ │ │
│ │ │ │ ├── too-small
│ │ │ │ │ └─ loses surrounding context
│ │ │ │ │
│ │ │ │ └── too-big
│ │ │ │ └─ dilutes signal, wastes tokens
│ │ │ │
│ │ │ ├── step-3 :: embed
│ │ │ │ │ └─ text → vector of 768 or 1536 numbers
│ │ │ │ │
│ │ │ │ ├── embedding-model
│ │ │ │ │ └─ BERT-family, OpenAI text-embedding-3, CLIP, etc.
│ │ │ │ │
│ │ │ │ └── semantic-magic
│ │ │ │ └─ similar meaning → similar numbers
│ │ │ │ └─ "King" ≈ "Queen", "King" ≠ "Pizza"
│ │ │ │
│ │ │ └── step-4 :: store
│ │ │ │ └─ push vectors into a vector DB
│ │ │ │
│ │ │ └── vector-db-options
│ │ │ └─ FAISS, Chroma, Pinecone, LanceDB, Weaviate, Milvus
│ │ │
│ │ └── PHASE-2 :: ONLINE (Query Time)
│ │ │ └─ runs every time a user asks something
│ │ │
│ │ ├── step-1 :: embed-query
│ │ │ └─ MUST use SAME embedding model as indexing
│ │ │ └─ else vector spaces mismatch → search breaks
│ │ │
│ │ ├── step-2 :: similarity-search
│ │ │ └─ find top-K closest chunks
│ │ │ └─ K usually 3-5
│ │ │ └─ cosine / dot-product / L2 distance
│ │ │
│ │ ├── step-3 :: build-prompt
│ │ │ └─ "Here is context: [chunks]. Answer: [question]"
│ │ │
│ │ └── step-4 :: generate
│ │ └─ LLM produces grounded answer
│ │
│ ├── 1.3 WHY-RAG-EXISTS
│ │ │
│ │ ├── BENEFITS
│ │ │ │
│ │ │ ├── fresh-knowledge
│ │ │ │ └─ update DB, system gets smarter instantly
│ │ │ │ └─ no GPU bill
│ │ │ │
│ │ │ ├── grounded-answers
│ │ │ │ └─ reading, not remembering
│ │ │ │ └─ fewer hallucinations
│ │ │ │
│ │ │ ├── citable
│ │ │ │ └─ "this came from doc X, page 4"
│ │ │ │ └─ critical for enterprise / legal / medical
│ │ │ │
│ │ │ └── cheap
│ │ │ └─ embedding << fine-tuning cost
│ │ │
│ │ └── CHALLENGES
│ │ │
│ │ ├── retrieval-is-everything
│ │ │ └─ wrong chunks → confidently wrong answer
│ │ │ └─ garbage in, garbage out
│ │ │
│ │ ├── chunking-strategy
│ │ │ └─ size, overlap, boundary-awareness
│ │ │
│ │ ├── latency
│ │ │ └─ every query = vector search + LLM call
│ │ │ └─ hundreds of ms minimum
│ │ │
│ │ └── scale
│ │ └─ 100M chunks → naive search dies
│ │ └─ need ANN index, sharding, caching
│ │
│ ├── 1.4 WHAT-IS-MULTIMODAL-RAG
│ │ │ └─ RAG where docs, query, or both span modalities
│ │ │ └─ text + images + audio + video
│ │ │
│ │ ├── WHY-IT-EXISTS
│ │ │ │ └─ real-world queries are rarely text-only
│ │ │ │
│ │ │ ├── customer-support
│ │ │ │ └─ user sends screenshot, not essay
│ │ │ │
│ │ │ ├── healthcare
│ │ │ │ └─ X-ray + clinical notes together
│ │ │ │
│ │ │ └── journalism
│ │ │ └─ articles quote video frames, charts
│ │ │
│ │ ├── WHAT-CHANGES-vs-PLAIN-RAG
│ │ │ │
│ │ │ ├── knowledge-base
│ │ │ │ └─ now holds text + images (+ audio/video)
│ │ │ │
│ │ │ ├── embedding-model
│ │ │ │ └─ must understand multiple modalities
│ │ │ │ └─ text "Lion" ≈ image of a lion
│ │ │ │
│ │ │ └── final-LLM
│ │ │ └─ must read images natively
│ │ │ └─ GPT-4V / GPT-4o / Gemini Vision / Claude
│ │ │
│ │ └── USE-CASES
│ │ │
│ │ ├── customer-support
│ │ │ └─ screenshot + text → fix suggestion
│ │ │
│ │ ├── healthcare
│ │ │ └─ X-ray + notes → similar-case retrieval
│ │ │
│ │ ├── media-journalism
│ │ │ └─ video frame + topic → article summary
│ │ │
│ │ ├── education
│ │ │ └─ diagram + question → explanation
│ │ │
│ │ └── e-commerce
│ │ └─ photo → similar products, reviews
│ │
│ ├── 1.5 MULTIMODAL-EMBEDDINGS
│ │ │ └─ THE heart of the system
│ │ │ └─ force all modalities into ONE vector space
│ │ │
│ │ ├── CORE-IDEA
│ │ │ │ └─ shared space: text + image + audio near each other
│ │ │ │
│ │ │ ├── matching-pairs
│ │ │ │ └─ (dog-photo, "a dog") → vectors PULLED close
│ │ │ │
│ │ │ └── non-matching-pairs
│ │ │ └─ (dog-photo, "a car") → vectors PUSHED apart
│ │ │
│ │ ├── CONTRASTIVE-LEARNING
│ │ │ │ └─ the training trick that makes this work
│ │ │ │
│ │ │ ├── positive-pairs
│ │ │ │ └─ same meaning → minimize distance
│ │ │ │
│ │ │ ├── negative-pairs
│ │ │ │ └─ different meaning → maximize distance
│ │ │ │
│ │ │ └── training-data
│ │ │ └─ millions of (image, caption) pairs from web
│ │ │ └─ weights adjust until alignment emerges
│ │ │
│ │ └── KEY-MODELS
│ │ │
│ │ ├── CLIP
│ │ │ └─ OpenAI, image + text
│ │ │ └─ the godfather of multimodal embeddings
│ │ │
│ │ ├── BLIP
│ │ │ └─ image + text + captioning
│ │ │
│ │ ├── Wav2Vec
│ │ │ └─ audio embeddings
│ │ │
│ │ ├── VideoCLIP
│ │ │ └─ video + text
│ │ │
│ │ ├── ImageBind
│ │ │ └─ Meta, SIX modalities at once
│ │ │ └─ text + image + audio + depth + thermal + motion
│ │ │
│ │ └── newer-upgrades
│ │ └─ SigLIP, OpenCLIP — better than CLIP today
│ │
│ ├── 1.6 MULTIMODAL-GENERATION
│ │ │ └─ how to produce the final answer
│ │ │ └─ two schools of thought
│ │ │
│ │ ├── APPROACH-1 :: convert-everything-to-text
│ │ │ │
│ │ │ ├── techniques
│ │ │ │ │
│ │ │ │ ├── OCR
│ │ │ │ │ └─ pull text out of images
│ │ │ │ │
│ │ │ │ ├── image-captioning
│ │ │ │ │ └─ BLIP describes pixels in words
│ │ │ │ │
│ │ │ │ └── speech-to-text
│ │ │ │ └─ Whisper for audio
│ │ │ │
│ │ │ ├── pros
│ │ │ │ └─ simple, works with any LLM, cheap
│ │ │ │
│ │ │ └── cons
│ │ │ └─ info lost in translation
│ │ │ └─ LLM never truly "sees"
│ │ │
│ │ └── APPROACH-2 :: true-multimodal-LLM
│ │ │ └─ pass image BYTES directly to model
│ │ │
│ │ ├── models
│ │ │ └─ GPT-4o, Gemini, Claude (vision)
│ │ │
│ │ ├── pros
│ │ │ └─ nothing lost, model sees pixels
│ │ │
│ │ └── cons
│ │ └─ expensive, vision-only models, slower
│ │
│ ├── 1.7 FRAMEWORKS-FOR-MULTIMODAL-RAG
│ │ │ └─ rule of thumb: LlamaIndex for DATA-IN, LangChain for LOGIC-OUT
│ │ │
│ │ ├── LlamaIndex
│ │ │ └─ best for data connectors + multimodal indexes
│ │ │ └─ cleanest for unstructured data (PDFs, videos, folders)
│ │ │
│ │ └── LangChain
│ │ └─ best for chains + agents + tool use
│ │ └─ huge ecosystem, better career signal
│ │
│ └── 1.8 NOTEBOOK-WALKTHROUGH (LlamaIndex + LanceDB + GPT-4o)
│ │ └─ end-to-end: YouTube → answers
│ │
│ ├── SECTION-A :: installs
│ │ │
│ │ ├── llama-index
│ │ │ └─ orchestrator: chunking, indexing, retrieval
│ │ │
│ │ ├── llama-index-vector-stores-lancedb
│ │ │ └─ LanceDB plug-in
│ │ │
│ │ ├── llama-index-embeddings-clip
│ │ │ └─ CLIP plug-in
│ │ │
│ │ ├── CLIP (from OpenAI repo)
│ │ │ └─ the multimodal embedder itself
│ │ │
│ │ ├── lancedb
│ │ │ └─ fast, local, multimodal-friendly vector DB
│ │ │
│ │ ├── moviepy
│ │ │ └─ Python video editor → frames + audio extraction
│ │ │
│ │ ├── yt_dlp
│ │ │ └─ YouTube downloader, modern pytube replacement
│ │ │
│ │ ├── whisper
│ │ │ └─ OpenAI speech-to-text
│ │ │
│ │ └── SpeechRecognition
│ │ └─ wrapper to call Whisper easily
│ │
│ ├── SECTION-B :: API-key-setup
│ │ │ └─ uses getpass — hides typed key
│ │ │
│ │ ├── never-hardcode
│ │ │ └─ bots scan GitHub every minute
│ │ │
│ │ └── never-commit
│ │ └─ keys drained in hours
│ │
│ ├── SECTION-C :: download-video
│ │ │ └─ yt_dlp grabs best MP4+M4A, merges to MP4
│ │ │
│ │ └── metadata-capture
│ │ └─ title, author, views
│ │ └─ used later for grounding attribution
│ │
│ ├── SECTION-D :: split-video
│ │ │
│ │ ├── video_to_images
│ │ │ │ └─ MoviePy write_images_sequence
│ │ │ │
│ │ │ └── fps=0.2
│ │ │ └─ 1 frame every 5 seconds
│ │ │ └─ balance between recall and cost
│ │ │ └─ tune higher for fast-action, lower for slides
│ │ │
│ │ ├── video_to_audio
│ │ │ └─ extracts audio track as .wav
│ │ │
│ │ └── audio_to_text
│ │ │ └─ SpeechRecognition + Whisper
│ │ │
│ │ └── result
│ │ └─ transcript text
│ │
│ ├── SECTION-E :: save-transcript-and-cleanup
│ │ │
│ │ ├── write-output_text.txt
│ │ │ └─ into mixed_data folder
│ │ │
│ │ └── delete-audio-wav
│ │ └─ info already extracted
│ │ └─ keep folder clean for indexer
│ │
│ ├── SECTION-F :: build-multimodal-index
│ │ │
│ │ ├── two-stores
│ │ │ │
│ │ │ ├── text_store :: LanceDB "text_collection"
│ │ │ │ └─ embedded by text encoder
│ │ │ │
│ │ │ └── image_store :: LanceDB "image_collection"
│ │ │ └─ embedded by CLIP
│ │ │
│ │ ├── StorageContext
│ │ │ └─ wires both stores together
│ │ │
│ │ ├── SimpleDirectoryReader
│ │ │ │ └─ auto-detects file types
│ │ │ │
│ │ │ ├── PNG → ImageDocument
│ │ │ │
│ │ │ └── TXT → TextDocument
│ │ │
│ │ └── MultiModalVectorStoreIndex.from_documents
│ │ │ └─ one call, three jobs
│ │ │
│ │ ├── chunks-text
│ │ │
│ │ ├── embeds-both-modalities
│ │ │
│ │ └── pushes-to-LanceDB
│ │
│ ├── SECTION-G :: retrieval
│ │ │
│ │ ├── similarity_top_k=1
│ │ │ └─ one best text chunk (text is dense)
│ │ │
│ │ ├── image_similarity_top_k=5
│ │ │ └─ five best frames (images are sparse)
│ │ │ └─ multiple angles on same moment
│ │ │
│ │ └── retrieve()
│ │ │ └─ splits results by type
│ │ │
│ │ ├── ImageNode → path list
│ │ │
│ │ └── else → text list
│ │
│ └── SECTION-H :: final-prompt-and-GPT-4o
│ │
│ ├── qa_tmpl_str
│ │ │ └─ prompt template
│ │ │
│ │ ├── instruction
│ │ │ └─ "without any additional prior knowledge"
│ │ │ └─ forces grounding, reduces hallucinations
│ │ │
│ │ ├── context_str
│ │ │ └─ retrieved text
│ │ │
│ │ ├── metadata_str
│ │ │ └─ video title/author/views (JSON)
│ │ │
│ │ └── query_str
│ │ └─ the user question
│ │
│ ├── OpenAIMultiModal(model="gpt-4o")
│ │ │ └─ the multimodal LLM call
│ │ │
│ │ ├── max_new_tokens=1500
│ │ │
│ │ └── image_documents
│ │ └─ actual frame pixels passed in
│ │
│ └── KEY-KNOBS-TO-TUNE
│ │
│ ├── fps
│ │ └─ frame sampling rate
│ │
│ ├── top_k
│ │ └─ retrieval budget
│ │
│ ├── chunk-size
│ │ └─ recall vs precision trade
│ │
│ ├── prompt-template
│ │ └─ huge impact on quality
│ │
│ └── embedding-model
│ └─ swap CLIP → SigLIP/OpenCLIP for better results
│
│
├── PART-2 :: AGENT ARCHITECTURES
│ │
│ ├── 2.1 FROM-RAG-TO-AGENTS
│ │ │ └─ the mindset shift
│ │ │
│ │ ├── RAG-LIMITATION
│ │ │ │
│ │ │ ├── single-shot
│ │ │ │ └─ one question → one answer
│ │ │ │
│ │ │ └── no-planning
│ │ │ └─ can't break task into steps
│ │ │
│ │ ├── AGENT-DEFINITION
│ │ │ │ └─ LLM wrapped in a loop
│ │ │ │ └─ can plan, use tools, remember, decide-done
│ │ │ │
│ │ │ ├── analogy
│ │ │ │ └─ RAG = asking Google
│ │ │ │ └─ Agent = hiring an intern
│ │ │ │
│ │ │ └── slogan
│ │ │ └─ "RAG is a function call. Agent is a worker."
│ │ │
│ │ └── THREE-THINGS-EVERY-AGENT-NEEDS
│ │ │
│ │ ├── memory
│ │ │ └─ remembers earlier steps
│ │ │
│ │ ├── tools
│ │ │ └─ acts on the world
│ │ │
│ │ └── planning-loop
│ │ └─ breaks task into steps
│ │ └─ decides when to stop
│ │
│ ├── 2.2 THE-FOUR-FRAMEWORKS
│ │ │ └─ same problem, four philosophies
│ │ │
│ │ ├── LangChain
│ │ │ │ └─ "everything is a chain"
│ │ │ │ └─ Lego-brick model
│ │ │ │
│ │ │ ├── building-blocks
│ │ │ │ └─ LLMs, tools, prompts, memory, parsers
│ │ │ │
│ │ │ ├── strengths
│ │ │ │ └─ biggest community
│ │ │ │ └─ most integrations
│ │ │ │ └─ most tutorials
│ │ │ │
│ │ │ └── weaknesses
│ │ │ └─ sprawling API, frequent breaks
│ │ │
│ │ ├── CrewAI
│ │ │ │ └─ "give each agent a job title"
│ │ │ │ └─ team-of-specialists model
│ │ │ │
│ │ │ ├── agent-attributes
│ │ │ │ │
│ │ │ │ ├── role
│ │ │ │ │ └─ Researcher, Writer, Critic
│ │ │ │ │
│ │ │ │ ├── goal
│ │ │ │ │ └─ what this agent aims to accomplish
│ │ │ │ │
│ │ │ │ └── backstory
│ │ │ │ └─ persona priming for the LLM
│ │ │ │
│ │ │ └── best-for
│ │ │ └─ beginners, human-like task division
│ │ │
│ │ ├── AutoGen (Microsoft)
│ │ │ │ └─ "agents talking to each other"
│ │ │ │ └─ conversation-first model
│ │ │ │
│ │ │ ├── AssistantAgent
│ │ │ │ └─ drafts / writes code
│ │ │ │
│ │ │ ├── UserProxyAgent
│ │ │ │ └─ executes code, gives feedback
│ │ │ │
│ │ │ └── best-for
│ │ │ └─ code generation, research workflows
│ │ │
│ │ └── LangGraph
│ │ │ └─ "agents as a state machine"
│ │ │ └─ most powerful, most complex
│ │ │
│ │ ├── nodes
│ │ │ └─ units of work
│ │ │
│ │ ├── edges
│ │ │ └─ transitions based on state
│ │ │
│ │ ├── capabilities
│ │ │ │
│ │ │ ├── loops
│ │ │ │
│ │ │ ├── retries
│ │ │ │
│ │ │ ├── conditional-paths
│ │ │ │
│ │ │ └── self-reflection
│ │ │
│ │ └── production-users
│ │ └─ Klarna, LinkedIn
│ │
│ ├── 2.3 MEMORY-BACKENDS
│ │ │ └─ how agents remember
│ │ │
│ │ ├── TWO-KINDS
│ │ │ │
│ │ │ ├── short-term
│ │ │ │ └─ current conversation, chat history
│ │ │ │ └─ "what was said 5 min ago"
│ │ │ │
│ │ │ └── long-term
│ │ │ └─ facts across sessions
│ │ │ └─ "user prefers concise answers"
│ │ │
│ │ ├── STORAGE-OPTIONS
│ │ │ │
│ │ │ ├── chat-history
│ │ │ │ │ └─ in RAM / a list
│ │ │ │ │
│ │ │ │ └── example
│ │ │ │ └─ LangChain ConversationBufferMemory
│ │ │ │
│ │ │ ├── vector-memory
│ │ │ │ │ └─ vector DB
│ │ │ │ │
│ │ │ │ └── examples
│ │ │ │ └─ FAISS, Chroma, Pinecone, Weaviate, LanceDB
│ │ │ │
│ │ │ ├── graph-memory
│ │ │ │ │ └─ graph DB for relationships
│ │ │ │ │
│ │ │ │ └── examples
│ │ │ │ └─ Neo4j, Memgraph
│ │ │ │
│ │ │ └── file-memory
│ │ │ │ └─ JSON / disk
│ │ │ │
│ │ │ └── examples
│ │ │ └─ custom agents with persisted state
│ │ │
│ │ ├── FRAMEWORK-DEFAULTS
│ │ │ │
│ │ │ ├── LangChain :: native
│ │ │ │
│ │ │ ├── CrewAI :: manual (inject via prompts)
│ │ │ │
│ │ │ ├── AutoGen :: built-in conversational
│ │ │ │
│ │ │ └── LangGraph :: partial (via LangChain)
│ │ │
│ │ └── BIG-INSIGHT
│ │ └─ infinite memory is BAD
│ │ └─ confuses model, costs tokens
│ │ └─ good memory = curated memory
│ │
│ ├── 2.4 TOOL-ABSTRACTION
│ │ │ └─ giving agents HANDS
│ │ │ └─ a tool = a function the LLM can call
│ │ │
│ │ ├── TOOL-EXAMPLES
│ │ │ │
│ │ │ ├── weather-API
│ │ │ │
│ │ │ ├── calculator
│ │ │ │
│ │ │ ├── database-query
│ │ │ │
│ │ │ ├── email-sender
│ │ │ │
│ │ │ └── web-search
│ │ │
│ │ ├── THE-LOOP
│ │ │ │
│ │ │ ├── step-1 :: LLM reads tool description
│ │ │ │
│ │ │ ├── step-2 :: LLM picks tool + writes arguments
│ │ │ │
│ │ │ ├── step-3 :: framework executes the tool
│ │ │ │
│ │ │ └── step-4 :: result fed back into LLM
│ │ │
│ │ ├── FORMULA
│ │ │ └─ Agent = LLM + Tools + Memory + Loop
│ │ │
│ │ ├── FRAMEWORK-PATTERNS
│ │ │ │
│ │ │ ├── LangChain
│ │ │ │ └─ Tool class: function + description
│ │ │ │
│ │ │ ├── CrewAI
│ │ │ │ └─ tasks assigned to roles
│ │ │ │
│ │ │ ├── AutoGen
│ │ │ │ └─ any Python function registered
│ │ │ │
│ │ │ └── LangGraph
│ │ │ └─ tools live inside nodes
│ │ │
│ │ └── TWO-GOLDEN-RULES
│ │ │
│ │ ├── declarative-descriptions
│ │ │ └─ tool description = what LLM reads to pick
│ │ │ └─ be specific: "solves 2+2 or 17\*43"
│ │ │ └─ NOT: "math tool"
│ │ │ └─ write it like a job posting
│ │ │
│ │ └── standardized-output
│ │ └─ return JSON or predictable text
│ │ └─ never random shapes
│ │
│ ├── 2.5 TRADE-OFFS-SUMMARY
│ │ │ └─ six dimensions across four frameworks
│ │ │
│ │ ├── setup-complexity
│ │ │ └─ LangChain: Medium | CrewAI: Low | AutoGen: Medium | LangGraph: High
│ │ │
│ │ ├── fine-control
│ │ │ └─ LangChain: Flexible | CrewAI: Limited | AutoGen: Yes | LangGraph: Full
│ │ │
│ │ ├── community
│ │ │ └─ LangChain: Huge | CrewAI: Growing | AutoGen: MS-backed | LangGraph: Niche
│ │ │
│ │ ├── debuggability
│ │ │ └─ LangChain: Average | CrewAI: High | AutoGen: Turn-based | LangGraph: Challenging
│ │ │
│ │ ├── scalability
│ │ │ └─ LangChain: Modular | CrewAI: Basic | AutoGen: Message-driven | LangGraph: Excellent
│ │ │
│ │ └── memory-support
│ │ └─ LangChain: Native | CrewAI: Manual | AutoGen: Built-in | LangGraph: Partial
│ │
│ ├── 2.6 THE-LAB :: Market-Research-Agent
│ │ │ └─ same task across frameworks
│ │ │ └─ task: pros/cons of top 3 LLMs
│ │ │
│ │ ├── step-1 :: CrewAI version
│ │ │ └─ Manager agent → Researcher agent
│ │ │ └─ introduces task delegation
│ │ │
│ │ ├── step-2 :: LangChain version
│ │ │ └─ single agent with SearchTool
│ │ │ └─ introduces modular tool use
│ │ │
│ │ ├── step-3 :: AutoGen version
│ │ │ └─ Assistant ↔ Critic
│ │ │ └─ introduces dialog coordination
│ │ │
│ │ ├── step-4 :: add memory
│ │ │ └─ applied to all three
│ │ │ └─ shows behavior change
│ │ │
│ │ └── step-5 :: LangGraph wrap (optional)
│ │ └─ retry loop if confidence < threshold
│ │ └─ shows self-correction
│ │
│ └── 2.7 DECISION-RULE
│ │
│ ├── modular-pipelines-with-tools
│ │ └─ → LangChain
│ │
│ ├── team-of-role-playing-specialists
│ │ └─ → CrewAI
│ │
│ ├── agents-debating-or-critiquing
│ │ └─ → AutoGen
│ │
│ ├── long-running-with-reflection-retries
│ │ └─ → LangGraph
│ │
│ └── slogan
│ └─ "Don't marry a framework. Marry the problem."
│
│
└── PART-3 :: CLOSING
│
├── THE-PATTERN (memorize this, not libraries)
│ │
│ ├── retrieve
│ │
│ ├── reason
│ │
│ ├── act
│ │
│ └── remember
│
├── HOMEWORK
│ │
│ ├── change-YouTube-URL, re-run notebook
│ │
│ ├── tune fps (0.2 → 1.0 → 0.05), observe quality/cost
│ │
│ ├── build CrewAI: Researcher + Writer
│ │
│ └── bonus :: wrap CrewAI in LangGraph retry-loop
│
└── CHEAT-SHEET
│
├── RAG
│ └─ find relevant docs, stuff into prompt, LLM answers
│
├── why-RAG
│ └─ fresh knowledge + grounding + fewer hallucinations (no retrain)
│
├── embedding
│ └─ vector that captures meaning; same meaning → close vectors
│
├── multimodal-embedding
│ └─ text + images in one vector space; search across modalities
│
├── CLIP
│ └─ aligned image ↔ text via contrastive training
│
├── vector-DB
│ └─ fast similarity search (LanceDB, FAISS, Pinecone, etc.)
│
├── multimodal-LLM
│ └─ GPT-4o, Gemini, Claude — reads images natively
│
├── agent
│ └─ LLM + memory + tools + loop
│
├── LangChain
│ └─ biggest ecosystem; chains, tools, memory
│
├── CrewAI
│ └─ role-based, easiest for specialist teams
│
├── AutoGen
│ └─ agents chatting; great for code-gen + critique
│
└── LangGraph
└─ agent as a graph; loops, retries, reflection
