```
GRAPHRAG VS TRADITIONAL RAG — HIGHER ACCURACY & INSIGHT WITH LLM
│
├── Use case example
│   ├── Healthcare support line
│   ├── Complex multi-step questions
│   └── Accuracy and speed matter
│
├── Traditional RAG
│   ├── Start with private dataset
│   │   ├── Structured and unstructured
│   │   └── Break into text chunks
│   ├── Store embeddings in vector database
│   ├── Query vector database for context
│   ├── Send context to LLM
│   └── LLM provides answer
│
├── GraphRAG
│   ├── Builds on top of traditional RAG
│   ├── Same text chunks
│   ├── Also extracts entities
│   ├── Maps information in knowledge graph
│   ├── Doesn't retrieve isolated answers
│   └── Connects related information
│       └── Enhances quality, accuracy, insight
│
├── Example: immunologist + CEO sentence
│   ├── Traditional text analysis
│   │   └── Detects "immunologist" and "CEO" as named entities
│   ├── GraphRAG goes further
│   │   ├── Identifies relationships between entities
│   │   ├── Maps connections
│   │   └── Deeper context into their interaction
│   ├── Immunologist
│   │   └── Deeply connected to immunology and medical research
│   ├── CEO
│   │   └── Indirect connection through healthcare company leadership
│   └── LLM quantifies
│       ├── Strength of relationships
│       ├── Nature of relationships
│       └── Constructs weighted graphs
│
├── Knowledge graph capabilities
│   ├── Network of connected linked entities
│   ├── Linked multilayered knowledge graph
│   ├── Supports wide range of applications
│   ├── Generating targeted questions
│   ├── Crafting contextually relevant summaries
│   └── Depth of insights traditional RAG cannot achieve
│
└── GraphRAG benefits
    ├── Production
    │   ├── Higher accuracy
    │   └── More complete answers at runtime
    ├── Development
    │   └── Once graph is built, easier to maintain than traditional RAG
    └── Governance
        ├── Better explainability
        ├── Traceability
        └── Access controls
```
