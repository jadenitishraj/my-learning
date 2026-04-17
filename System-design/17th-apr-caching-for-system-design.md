```
CACHING FOR SYSTEM DESIGN INTERVIEWS
│
├── What is Caching
│   ├── Temporary storage for fast access
│   ├── Disk (SSD) → ~1ms access
│   ├── Memory (RAM) → ~100ns access
│   └── ~10,000x faster from memory
│
├── Where to Cache
│   ├── External Caching (most common)
│   │   ├── Dedicated service (Redis, Memcached)
│   │   ├── Runs on its own server
│   │   ├── Cache hit → return instantly
│   │   ├── Cache miss → fetch from DB, store in cache
│   │   └── Shared across all app servers
│   │
│   ├── In-Process Caching
│   │   ├── Cache inside app server memory
│   │   ├── Fastest (no network hop)
│   │   ├── Each server has its own cache
│   │   ├── Inconsistencies possible
│   │   └── Best for config data, small lookups
│   │
│   ├── CDN (Content Delivery Network)
│   │   ├── Geographically distributed servers
│   │   ├── Optimizes network latency
│   │   │   ├── Without CDN → 300-350ms (cross-continent)
│   │   │   └── With CDN → 20-40ms (nearby edge)
│   │   ├── Cache hit → return from edge server
│   │   ├── Cache miss → fetch from origin, cache at edge
│   │   ├── Can cache static media, API responses, HTML
│   │   └── Best for images, videos, static assets
│   │
│   └── Client-Side Caching
│       ├── Stored on user's device
│       ├── Browser: HTTP cache, local storage
│       ├── Mobile: in-memory or local disk
│       ├── Super fast (no network)
│       ├── Less control, data can go stale
│       └── Best for offline functionality
│
├── Cache Architectures
│   ├── Cache-Aside (DEFAULT — use this)
│   │   ├── App checks cache first
│   │   ├── Miss → fetch from DB → store in cache
│   │   ├── Keeps cache lean
│   │   ├── Only caches what's actually requested
│   │   └── Downside: cache miss adds latency
│   │
│   ├── Write-Through
│   │   ├── App writes to cache first
│   │   ├── Cache synchronously writes to DB
│   │   ├── Write not complete until both updated
│   │   ├── Needs special library (Spring Cache, Hazelcast)
│   │   ├── Downsides
│   │   │   ├── Slower writes
│   │   │   ├── Cache pollution (unread data)
│   │   │   └── Dual write problem
│   │   └── Use only when reads MUST be fresh
│   │
│   ├── Write-Behind (Write-Back)
│   │   ├── App writes to cache only
│   │   ├── Cache flushes to DB asynchronously
│   │   ├── Faster writes than write-through
│   │   ├── Use for analytics, metrics pipelines
│   │   └── Avoid unless strongly justified
│   │
│   └── Read-Through
│       ├── Like cache-aside but cache handles DB lookup
│       ├── Cache miss → cache fetches from DB
│       ├── Cache acts as proxy
│       ├── How CDNs work
│       └── Only bring up for CDN/edge caching
│
├── Eviction Policies
│   ├── LRU (Least Recently Used)
│   │   ├── Evicts least recently accessed items
│   │   └── Most common default
│   ├── LFU (Least Frequently Used)
│   │   ├── Evicts least accessed items
│   │   └── Good for highly skewed access patterns
│   ├── FIFO (First In, First Out)
│   │   ├── Oldest item removed first
│   │   └── Rarely the right choice
│   └── TTL (Time To Live)
│       ├── Each item has expiration time
│       ├── Auto-removed after time passes
│       └── Best when freshness matters most
│
├── Common Caching Issues
│   ├── Cache Stampede (Thundering Herd)
│   │   ├── Popular key expires via TTL
│   │   ├── Flood of requests all miss cache
│   │   ├── All hit DB simultaneously
│   │   ├── Can overwhelm and crash DB
│   │   └── Solutions
│   │       ├── Request Coalescing (Single Flight)
│   │       │   ├── Only first request rebuilds cache
│   │       │   └── Others wait for result
│   │       └── Cache Warming
│   │           ├── Proactively refresh before expiry
│   │           └── e.g., refresh at 55s of 60s TTL
│   │
│   ├── Cache Consistency
│   │   ├── Cache and DB return different values
│   │   ├── Reads from cache, writes to DB
│   │   ├── Creates stale data window
│   │   └── Strategies
│   │       ├── Invalidate on Write
│   │       │   ├── Delete cache key on DB write
│   │       │   └── Next read fetches fresh data
│   │       ├── Short TTLs
│   │       │   └── Accept brief staleness (e.g., 60s)
│   │       └── Accept Eventual Consistency
│   │           └── Fine for feeds, analytics, metrics
│   │
│   └── Hot Keys
│       ├── One cache key gets way more traffic
│       ├── Can overload single Redis node/shard
│       ├── e.g., Taylor Swift profile on Twitter
│       └── Solutions
│           ├── Replicate Hot Keys
│           │   ├── Copy to multiple cache shards
│           │   └── Load balance across them
│           └── Local Fallback Cache
│               ├── In-process cache for hot values
│               └── Avoids hitting Redis entirely
│
└── How to Discuss Caching in Interviews
    ├── When to Bring It Up
    │   ├── Read-heavy workload straining DB
    │   ├── Expensive queries (e.g., newsfeed joins)
    │   ├── Latency requirements (e.g., <100ms)
    │   └── Usually during deep dives on scale
    │
    ├── How to Introduce It (5 steps)
    │   ├── 1. Identify the bottleneck
    │   │   └── Quantify with rough numbers
    │   ├── 2. Decide what to cache
    │   │   ├── Frequently read data
    │   │   ├── Rarely changing data
    │   │   └── Expensive to fetch/compute
    │   ├── 3. Define cache keys explicitly
    │   │   └── Don't just say "add a cache"
    │   ├── 4. Choose cache architecture
    │   │   └── Default to cache-aside
    │   └── 5. Address potential downsides
    │       ├── Stampede risk?
    │       ├── Consistency issues?
    │       └── Hot key problems?
    │
    └── Key Advice
        ├── Don't add cache without justification
        ├── Don't memorize names, describe behavior
        └── Cache-aside is the only must-know
```
