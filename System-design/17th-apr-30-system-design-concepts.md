```
30 SYSTEM DESIGN CONCEPTS EVERY DEVELOPER SHOULD KNOW
│
├── Client-Server Architecture
│   ├── Client (browser, mobile app)
│   ├── Server (handles requests)
│   └── Request → Process → Response
│
├── IP Addresses & DNS
│   ├── Every server has unique IP address
│   ├── DNS maps domain names to IPs
│   └── Browser queries DNS → gets IP → connects
│
├── Proxy & Reverse Proxy
│   ├── Proxy
│   │   ├── Middleman between client & internet
│   │   └── Hides client IP address
│   └── Reverse Proxy
│       ├── Intercepts client requests
│       └── Forwards to backend servers
│
├── Latency
│   ├── Delay caused by physical distance
│   ├── Roundtrip delay = latency
│   └── Reduce by deploying across data centers
│
├── HTTP & HTTPS
│   ├── HTTP
│   │   ├── Rules for client-server communication
│   │   ├── Request: header + body
│   │   └── Response: data or error
│   └── HTTPS
│       ├── Encrypted via SSL/TLS
│       └── Prevents interception
│
├── APIs (Application Programming Interfaces)
│   ├── Middleman for client-server communication
│   ├── Structured responses (JSON/XML)
│   ├── REST API
│   │   ├── Resource-based
│   │   ├── Stateless
│   │   ├── Uses HTTP methods (GET, POST, PUT, DELETE)
│   │   ├── Simple, scalable, easy to cache
│   │   └── Can over-fetch data
│   └── GraphQL
│       ├── Client asks for exactly what it needs
│       ├── Single query for multiple resources
│       ├── Introduced by Facebook (2015)
│       └── More server-side processing
│
├── Databases
│   ├── SQL (Relational)
│   │   ├── Tables with strict schema
│   │   ├── ACID properties
│   │   └── Best for structured data, banking
│   ├── NoSQL
│   │   ├── Flexible schema
│   │   ├── Key-value, document, graph, wide column
│   │   └── Best for high scalability
│   └── Many apps use both together
│
├── Scaling
│   ├── Vertical Scaling (Scale Up)
│   │   ├── Add more CPU/RAM/storage
│   │   ├── Has maximum capacity
│   │   └── Single point of failure
│   └── Horizontal Scaling (Scale Out)
│       ├── Add more servers
│       ├── More capacity & reliability
│       └── Requires load balancer
│
├── Load Balancer
│   ├── Distributes requests across servers
│   ├── Redirects if server crashes
│   └── Algorithms
│       ├── Round Robin
│       ├── Least Connections
│       └── IP Hashing
│
├── Database Scaling Techniques
│   ├── Indexing
│   │   ├── Lookup table for fast reads
│   │   ├── Index frequently queried columns
│   │   └── Speeds reads, slows writes
│   │
│   ├── Replication
│   │   ├── One primary (writes)
│   │   ├── Multiple read replicas
│   │   ├── Data synced from primary
│   │   └── Improves read performance & availability
│   │
│   ├── Sharding (Horizontal Partitioning)
│   │   ├── Split database into smaller shards
│   │   ├── Distributed by shard key (e.g., user ID)
│   │   └── Reduces load per server
│   │
│   ├── Vertical Partitioning
│   │   ├── Split table by columns
│   │   ├── Queries scan only relevant columns
│   │   └── Reduces unnecessary disk I/O
│   │
│   ├── Caching
│   │   ├── Store frequent data in memory
│   │   ├── Cache-aside pattern
│   │   │   ├── Check cache first
│   │   │   ├── Miss → fetch from DB → store in cache
│   │   │   └── Use TTL to prevent stale data
│   │   └── Much faster than disk
│   │
│   └── Denormalization
│       ├── Combine related tables into one
│       ├── Reduces joins
│       ├── Faster reads
│       └── Tradeoff: more storage, complex updates
│
├── CAP Theorem
│   ├── No distributed system has all three
│   │   ├── Consistency
│   │   ├── Availability
│   │   └── Partition Tolerance
│   └── Must choose: CP or AP
│
├── Blob Storage
│   ├── For images, videos, PDFs, large files
│   ├── Example: Amazon S3
│   ├── Stored in buckets with unique URLs
│   └── Scalable, pay-as-you-go
│
├── CDN (Content Delivery Network)
│   ├── Global distributed servers
│   ├── Serves content from nearest server
│   └── Faster load times, minimal buffering
│
├── WebSockets
│   ├── Persistent two-way connection
│   ├── Server pushes updates without request
│   ├── Replaces polling
│   └── Best for chat, stock tickers, games
│
├── WebHooks
│   ├── Server-to-server event notifications
│   ├── Receiver registers webhook URL
│   ├── Provider sends HTTP POST on event
│   └── Saves resources vs polling
│
├── Microservices
│   ├── Break monolith into small services
│   ├── Each has own database & logic
│   ├── Scale independently
│   └── Communicate via APIs or message queues
│
├── Message Queues
│   ├── Async communication between services
│   ├── Producer → Queue → Consumer
│   ├── Decouples services
│   └── Prevents overload
│
├── Rate Limiting
│   ├── Restrict requests per time frame
│   ├── e.g., 100 requests/minute per IP
│   ├── Prevents bot attacks & server crashes
│   └── Algorithms
│       ├── Fixed Window
│       ├── Sliding Window
│       └── Token Bucket
│
├── API Gateway
│   ├── Single entry point for all requests
│   ├── Handles
│   │   ├── Authentication
│   │   ├── Rate limiting
│   │   ├── Logging & monitoring
│   │   └── Request routing
│   └── Routes to appropriate microservice
│
└── Idempotency
    ├── Repeated requests produce same result
    ├── Each request gets unique ID
    ├── System checks for duplicates
    └── Critical for payments & sensitive ops
```
