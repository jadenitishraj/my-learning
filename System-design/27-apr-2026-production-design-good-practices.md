Youtube Link: https://www.youtube.com/watch?v=JLfd7he0UkI

PRODUCTION SYSTEM DESIGN COURSE 
│
├── Course Scope & Purpose
│   ├── Focus Area
│   │   ├── Post-deployment systems
│   │   ├── Operating at scale (millions of users)
│   │   └── Production incident handling
│   ├── Key Questions
│   │   ├── Schema evolution at billion-row scale
│   │   ├── Safe deployments under traffic
│   │   └── Debugging multi-service failures
│   └── Gap Addressed
│       ├── Interview design vs real production
│       └── Long-term system operation
│
├── Interview vs Production Reality
│   ├── Interview Model
│   │   ├── Linear process
│   │   │   ├── Requirements → Design → DB → APIs
│   │   │   └── Time-boxed (~45 min)
│   │   └── Snapshot design
│   │
│   ├── Production Model
│   │   ├── Continuous lifecycle
│   │   │   ├── Design
│   │   │   ├── Deploy
│   │   │   ├── Monitor
│   │   │   ├── Learn
│   │   │   └── Evolve
│   │   ├── Long time horizon (years)
│   │   └── Constant change
│   │       ├── Traffic growth
│   │       ├── Failures
│   │       ├── Team changes
│   │       └── Requirement shifts
│   │
│   └── Key Differences
│       ├── Schema → static vs evolving live
│       ├── Failures → assumed vs engineered
│       ├── Deployment → skipped vs critical
│       ├── Debugging → shallow vs deep tracing
│       ├── Cost → ignored vs major factor
│       └── On-call → none vs continuous
│
├── Course Structure
│   ├── Part 1: Foundations
│   │   ├── Architecture boundaries
│   │   └── Production requirements
│   │
│   ├── Part 2: Building Blocks
│   │   ├── Data in production
│   │   │   ├── Schema evolution
│   │   │   └── Migrations
│   │   ├── Caching
│   │   ├── Queues
│   │   └── Async workflows
│   │
│   ├── Part 3: Operations
│   │   ├── Reliability
│   │   │   ├── Timeouts
│   │   │   ├── Retries
│   │   │   └── Circuit breakers
│   │   ├── Observability
│   │   │   ├── Logs
│   │   │   ├── Metrics
│   │   │   └── Distributed tracing
│   │   └── Deployment
│   │       ├── Canary rollouts
│   │       ├── Feature flags
│   │       └── Safe migrations
│   │
│   ├── Part 4: Scale & Cost
│   │   ├── Security
│   │   ├── Cost optimization
│   │   └── Multi-region architecture
│   │
│   └── Part 5: Integration
│       ├── Incident management
│       ├── Case studies
│       └── Summary
│
├── Production Mindset
│   ├── Evolution of Thinking
│   │   ├── Early: "Does it work?"
│   │   └── Advanced:
│   │       ├── Is it observable?
│   │       ├── Is it recoverable?
│   │       └── Is it evolvable?
│   │
│   └── Key Properties
│       ├── Observability → detect issues
│       ├── Recoverability → fix failures quickly
│       └── Evolvability → change without breakage
│
├── Core Production Constraints
│   ├── Availability (SLA)
│   │   ├── 99% → 3.65 days/year
│   │   ├── 99.9% → 8.76 hours/year
│   │   ├── 99.99% → 52 minutes/year
│   │   ├── 99.999% → ~5 minutes/year
│   │   └── Insight
│   │       ├── Each “9” ≈ 10x improvement
│   │       └── Requires exponential effort
│   │
│   │   ├── Multi-component Availability
│   │   │   ├── Product of dependencies
│   │   │   └── Weakest link dominates
│   │   │
│   │   └── Production Design Responses
│   │       ├── Cache fallback to DB
│   │       ├── Read replicas
│   │       ├── Circuit breakers
│   │       └── Graceful degradation
│   │
│   ├── Latency Budget
│   │   ├── Example SLA: P99 < 500ms
│   │   ├── Budget Allocation
│   │   │   ├── Network → ~50ms
│   │   │   ├── Load balancer → ~5ms
│   │   │   ├── Auth / rate limiting → ~20ms
│   │   │   ├── Application → ~100ms
│   │   │   ├── Database → ~150ms
│   │   │   ├── Cache → ~10ms
│   │   │   ├── External API → ~150ms
│   │   │   └── Buffer → ~15ms
│   │   │
│   │   ├── Metrics
│   │   │   ├── P50 → median
│   │   │   ├── P95 → slow requests
│   │   │   └── P99 → worst 1%
│   │   │
│   │   └── Insight
│   │       ├── Average hides problems
│   │       └── P99 defines user experience
│   │
│   ├── Cost Constraints
│   │   ├── Compute
│   │   │   ├── $100–$500 per instance/month
│   │   │   └── Scales to $50k+ with redundancy
│   │   ├── Database
│   │   │   ├── $500–$2000 per instance
│   │   │   └── Replicas increase cost
│   │   ├── Cache
│   │   │   └── ~$30–50 per GB/month
│   │   ├── Storage
│   │   │   └── ~$23 per TB/month
│   │   ├── Bandwidth / CDN
│   │   │   ├── ~$85–90 per TB
│   │   │   └── Major hidden cost
│   │   └── Insight
│   │       ├── Egress dominates at scale
│   │       └── Trade-offs must be justified
│   │
│   ├── Team Structure (Conway’s Law)
│   │   ├── Architecture mirrors org structure
│   │   ├── Examples
│   │   │   ├── 5 engineers → monolith
│   │   │   ├── 15 engineers → 5–10 services
│   │   │   └── 50 engineers → microservices + platform team
│   │   ├── Ownership Definition
│   │   │   ├── Code
│   │   │   ├── On-call
│   │   │   ├── SLA
│   │   │   ├── Roadmap
│   │   │   └── Dependencies
│   │   └── Anti-pattern
│   │       └── Shared ownership → no ownership
│   │
│   └── Compliance
│       ├── GDPR
│       │   ├── Right to deletion
│       │   └── Data residency (EU)
│       ├── SOC 2
│       │   └── Audit logging
│       ├── HIPAA
│       │   └── Encryption at rest
│       ├── PCI-DSS
│       │   └── Network isolation
│       └── Architectural Impact
│           ├── Regional routing
│           ├── Data partitioning
│           ├── Restricted replication
│           └── Logging requirements
│
└── System Evolution
    ├── Day 1
    │   ├── ~100 users
    │   ├── Monolith
    │   └── Best-effort SLA
    ├── Day 100
    │   ├── ~10k users
    │   ├── Few microservices
    │   └── 99.9% SLA
    ├── Day 1000
    │   ├── ~1M users
    │   ├── 30+ services
    │   └── 99.99% SLA
    │
    ├── Design Principle
    │   └── Build for next 10x (not 100x)
    │
    └── Re-architecture Signals
        ├── Deployment delays (>2 days)
        ├── Frequent incidents (>2/month)
        ├── Latency near SLA limit (80%)
        ├── High cost concentration (>40%)
        └── Team ownership conflicts
