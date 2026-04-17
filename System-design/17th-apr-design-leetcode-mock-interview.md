```
DESIGN LEETCODE — SYSTEM DESIGN MOCK INTERVIEW
│
├── Functional Requirements
│   ├── View list of coding problems
│   ├── View a given problem
│   │   └── Code solution in any language
│   ├── Submit solution
│   │   └── Get instant feedback
│   └── Live leaderboard
│       └── For bi-weekly/weekly contests
│
├── Out of Scope
│   ├── Authentication & authorization
│   ├── User profiles
│   ├── Payment gateway
│   └── User analytics
│
├── Non-Functional Requirements
│   ├── High Availability
│   │   ├── Prioritize over consistency
│   │   └── Eventual consistency acceptable
│   │       └── e.g., problem count ±10 across regions
│   ├── Code Isolation & Security
│   │   ├── User code must not affect system
│   │   └── Prevent malware & DDoS
│   ├── Low Latency
│   │   └── Submission results < X seconds
│   ├── Scalability
│   │   ├── Millions of daily active users
│   │   └── 100K concurrent during contests
│   └── Fault Tolerance
│       ├── No single point of failure
│       └── Distributed system architecture
│
├── Core Entities
│   ├── Problem
│   ├── User
│   ├── Submission
│   └── Leaderboard
│
├── API Design (RESTful)
│   ├── GET /problems
│   │   ├── Paginated (page=1, limit=100)
│   │   └── Filters (difficulty, category)
│   ├── GET /problems/:id
│   │   └── Language filter
│   │       └── Returns template + compiler info
│   ├── POST /problems/:id/submission
│   │   ├── Code as string
│   │   └── Language as string
│   └── GET /leaderboard/:competitionId
│       └── Paginated (limit=100)
│
├── Database Design
│   ├── Choice: DynamoDB (NoSQL)
│   │   ├── No complex joins needed
│   │   ├── Flexible schema
│   │   └── Nested test cases as single document
│   ├── Problem Schema
│   │   ├── ID
│   │   ├── Description
│   │   ├── Submission stats
│   │   ├── Test cases
│   │   └── Metadata
│   └── Submission Schema
│       ├── ID
│       ├── User ID
│       ├── Competition ID (partition key)
│       ├── Submitted at (timestamp)
│       ├── Test case result (pass/fail)
│       ├── Runtime
│       └── Error status
│
├── High-Level Design
│   ├── Client → API Server → Database
│   │
│   ├── Code Execution (3 approaches discussed)
│   │   ├── ❌ Run on API Server
│   │   │   ├── Security risk (malware)
│   │   │   ├── CPU/memory hog
│   │   │   └── No isolation or fault tolerance
│   │   ├── ⚠️ VM-Based Execution
│   │   │   ├── Good isolation
│   │   │   ├── Heavy resource usage
│   │   │   ├── Each VM has own OS
│   │   │   └── Costly to maintain
│   │   └── ✅ Container-Based Execution
│   │       ├── Lightweight (Docker)
│   │       ├── Process-level isolation
│   │       ├── Better resource utilization
│   │       ├── Easy scale up/down
│   │       ├── One container per language runtime
│   │       └── Services: ECS, EKS, Kubernetes
│   │
│   └── Alternative: Serverless (Lambda/Cloud Functions)
│       └── Mentioned but not explored
│
├── Leaderboard Design
│   ├── Query submissions by competition ID
│   ├── Group by user ID
│   ├── Rank by time + test results
│   └── Client polls periodically
│
├── Scaling Strategy
│   ├── Vertical Scaling
│   │   └── Bigger machines (short-term)
│   ├── Horizontal Scaling
│   │   ├── Multiple API servers
│   │   └── Multiple runtime containers per language
│   ├── Message Queue
│   │   ├── Between API server & containers
│   │   ├── Workers pull jobs & execute
│   │   └── Smoothens traffic spikes
│   ├── Caching (Redis)
│   │   ├── Cache leaderboard results
│   │   ├── Reduce database load
│   │   └── In-memory for fast reads
│   └── Retry Mechanism
│       └── Exponential backoff on container failures
│
├── Security & Isolation
│   ├── Write output to temp directory
│   ├── Clean periodically
│   ├── Timeout cap (TLE enforcement)
│   └── Stops infinite loops
│
├── Test Cases Across Languages
│   ├── Standard test case definition per problem
│   ├── Input/output stored as JSON
│   ├── Serialization/deserialization per language
│   │   ├── C++ → hashmap
│   │   └── Python → dictionary
│   └── Core problem remains same
│
└── Database Reliability
    ├── Master-Slave Architecture
    │   ├── Primary + replicas
    │   └── Promote replica if primary fails
    ├── Submissions DB → Replicas needed
    └── Problems DB → Not needed (only ~4000 problems)
```
