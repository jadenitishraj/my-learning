```
SYSTEM DESIGN MASTERY ROADMAP
│
├── Course Overview
│   ├── Mid-level to Senior transition
│   ├── Focus on architectural design
│   ├── Covers real jobs & interviews
│   └── Pillars
│       ├── Foundations
│       ├── API Design
│       ├── Databases
│       ├── Caching & CDNs
│       ├── Big Data Processing
│       ├── Production Design
│       └── Interview Case Studies
│
├── Foundations
│   ├── Single Server Setup
│   │   ├── Everything on one server
│   │   │   ├── Web app
│   │   │   ├── Database
│   │   │   └── Cache
│   │   ├── Request Flow
│   │   │   ├── User types domain name
│   │   │   ├── DNS resolves to IP
│   │   │   ├── HTTP request sent
│   │   │   └── Server responds (HTML or JSON)
│   │   └── Traffic Sources
│   │       ├── Web browsers (HTML/CSS/JS)
│   │       └── Mobile apps (JSON over HTTP)
│   │
│   ├── Database Selection
│   │   ├── Relational (SQL)
│   │   │   ├── Examples
│   │   │   │   ├── PostgreSQL
│   │   │   │   ├── MySQL
│   │   │   │   ├── Oracle
│   │   │   │   └── SQLite
│   │   │   ├── Tables, columns, rows
│   │   │   ├── Join operations
│   │   │   ├── ACID Transactions
│   │   │   │   ├── Atomic
│   │   │   │   ├── Consistent
│   │   │   │   ├── Isolated
│   │   │   │   └── Durable
│   │   │   └── Best For
│   │   │       ├── Structured data
│   │   │       ├── Clear relationships
│   │   │       └── Financial/banking systems
│   │   └── Non-Relational (NoSQL)
│   │       ├── Document Stores (MongoDB)
│   │       ├── Wide Column Stores (Cassandra)
│   │       ├── Graph Databases (Neo4j)
│   │       ├── Key-Value Stores (Redis)
│   │       └── Best For
│   │           ├── Super low latency
│   │           ├── Unstructured data
│   │           └── Massive data volumes
│   │
│   ├── Scaling
│   │   ├── Vertical Scaling (Scale Up)
│   │   │   ├── Add more RAM/CPU
│   │   │   ├── Simple approach
│   │   │   ├── Resource limits exist
│   │   │   └── No redundancy
│   │   └── Horizontal Scaling (Scale Out)
│   │       ├── Add more servers
│   │       ├── Higher fault tolerance
│   │       ├── Better scalability
│   │       └── Requires load balancer
│   │
│   ├── Load Balancing
│   │   ├── Algorithms
│   │   │   ├── Round Robin
│   │   │   │   └── Sequential rotating order
│   │   │   ├── Least Connections
│   │   │   │   └── Fewest active connections
│   │   │   ├── Least Response Time
│   │   │   │   └── Fastest + fewest connections
│   │   │   ├── IP Hash
│   │   │   │   └── Consistent client-server mapping
│   │   │   ├── Weighted Algorithms
│   │   │   │   └── Based on server capacity
│   │   │   ├── Geographical
│   │   │   │   └── Closest server to user
│   │   │   └── Consistent Hashing
│   │   │       └── Hash ring distribution
│   │   ├── Health Checks
│   │   │   ├── Monitor server availability
│   │   │   └── Stop traffic to failed servers
│   │   └── Types
│   │       ├── Software (NGINX, HAProxy)
│   │       ├── Hardware (F5, Citrix)
│   │       └── Cloud (AWS ELB, Azure, GCP)
│   │
│   └── Single Point of Failure
│       ├── Problems
│       │   ├── Reliability risk
│       │   ├── Scalability issues
│       │   └── Security vulnerability
│       └── Solutions
│           ├── Add redundancy
│           ├── Health checks & monitoring
│           └── Self-healing systems
│
├── API Design
│   ├── What is an API
│   │   ├── Contract between client & server
│   │   ├── Abstraction mechanism
│   │   └── Defines service boundaries
│   │
│   ├── API Styles
│   │   ├── REST
│   │   │   ├── Resource-based (HTTP methods)
│   │   │   ├── Stateless
│   │   │   ├── Best for web & mobile apps
│   │   │   └── Fixed response structures
│   │   ├── GraphQL
│   │   │   ├── Single endpoint
│   │   │   ├── Client specifies response shape
│   │   │   ├── Query, Mutation, Subscription
│   │   │   ├── Minimal round trips
│   │   │   └── Best for complex UIs
│   │   └── gRPC
│   │       ├── Protocol buffers
│   │       ├── HTTP/2 transport
│   │       ├── Streaming support
│   │       └── Best for microservices
│   │
│   ├── Design Principles
│   │   ├── Consistency
│   │   │   └── Consistent naming & patterns
│   │   ├── Simplicity
│   │   │   └── Usable without docs
│   │   ├── Security
│   │   │   ├── Authentication
│   │   │   ├── Authorization
│   │   │   ├── Input validation
│   │   │   └── Rate limiting
│   │   └── Performance
│   │       ├── Caching strategies
│   │       ├── Pagination
│   │       ├── Minimal payloads
│   │       └── Reduce round trips
│   │
│   ├── API Protocols
│   │   ├── HTTP/HTTPS
│   │   │   ├── Foundation of web APIs
│   │   │   ├── Methods (GET, POST, PUT, DELETE)
│   │   │   ├── Status codes (2xx, 3xx, 4xx, 5xx)
│   │   │   └── HTTPS adds TLS/SSL encryption
│   │   ├── WebSockets
│   │   │   ├── Bidirectional communication
│   │   │   ├── Real-time data push
│   │   │   ├── Handshake then persistent
│   │   │   └── Best for chat, streaming
│   │   ├── AMQP
│   │   │   ├── Message queuing protocol
│   │   │   ├── Producer → Queue → Consumer
│   │   │   └── Guaranteed delivery
│   │   └── gRPC Protocol
│   │       ├── Uses HTTP/2
│   │       ├── Protocol buffers
│   │       └── Built-in streaming
│   │
│   ├── Transport Layer
│   │   ├── TCP
│   │   │   ├── Reliable delivery
│   │   │   ├── Three-way handshake
│   │   │   ├── Ordered packets
│   │   │   ├── Slower (overhead)
│   │   │   └── Best for payments, email
│   │   └── UDP
│   │       ├── Fast, lightweight
│   │       ├── No delivery guarantee
│   │       ├── No handshake
│   │       └── Best for video, gaming
│   │
│   ├── RESTful API Deep Dive
│   │   ├── Resource Modeling
│   │   │   ├── Use nouns, not verbs
│   │   │   ├── Plural resource names
│   │   │   └── Nested resources
│   │   ├── Filtering, Sorting, Pagination
│   │   │   ├── Query parameters
│   │   │   ├── Page + limit
│   │   │   ├── Offset-based
│   │   │   └── Cursor-based
│   │   ├── CRUD Operations
│   │   │   ├── GET → Read
│   │   │   ├── POST → Create
│   │   │   ├── PUT → Full replace
│   │   │   ├── PATCH → Partial update
│   │   │   └── DELETE → Remove
│   │   ├── Status Codes
│   │   │   ├── 200 OK
│   │   │   ├── 201 Created
│   │   │   ├── 204 No Content
│   │   │   ├── 400 Bad Request
│   │   │   ├── 401 Unauthorized
│   │   │   ├── 404 Not Found
│   │   │   └── 500 Server Error
│   │   └── Best Practices
│   │       ├── Plural nouns
│   │       ├── Proper HTTP methods
│   │       ├── Filtering + sorting + pagination
│   │       └── API versioning (v1, v2)
│   │
│   └── GraphQL Deep Dive
│       ├── Created by Facebook
│       ├── Single endpoint for all ops
│       ├── Schema Design
│       │   ├── Types define data shape
│       │   ├── Queries for reading
│       │   └── Mutations for writing
│       ├── Error Handling
│       │   ├── Always returns 200
│       │   └── Errors in response body
│       └── Best Practices
│           ├── Small modular schemas
│           ├── Limit query depth
│           ├── Meaningful naming
│           └── Input types for mutations
│
├── Authentication
│   ├── Purpose
│   │   └── Verify who the user is
│   │
│   ├── Basic Methods
│   │   ├── Basic Authentication
│   │   │   ├── Base64 encoded credentials
│   │   │   ├── Easily reversible
│   │   │   └── Insecure without HTTPS
│   │   ├── Digest Authentication
│   │   │   ├── MD5 hashing
│   │   │   └── Still outdated
│   │   ├── API Key Authentication
│   │   │   ├── Unique key per client
│   │   │   ├── Stored in database
│   │   │   ├── No built-in expiration
│   │   │   └── No embedded info (vs JWT)
│   │   └── Session-Based Authentication
│   │       ├── Server creates session
│   │       ├── Session storage options
│   │       │   ├── In-memory
│   │       │   ├── Redis (recommended)
│   │       │   └── Database
│   │       ├── Cookie sent to client
│   │       └── Stateful (hard to scale)
│   │
│   ├── Token-Based Authentication
│   │   ├── Bearer Token
│   │   │   └── Whoever has token gets access
│   │   ├── JWT (JSON Web Token)
│   │   │   ├── Signed JSON object
│   │   │   ├── Contains user ID, expiry, claims
│   │   │   ├── Stateless verification
│   │   │   └── No database lookup needed
│   │   └── Access + Refresh Tokens
│   │       ├── Access token: short-lived (15min–1hr)
│   │       ├── Refresh token: long-lived (days/weeks)
│   │       ├── Store refresh in HTTP-only cookies
│   │       └── Prevents XSS attacks
│   │
│   ├── OAuth 2.0
│   │   ├── Authorization framework (not auth)
│   │   ├── Delegated access
│   │   ├── Consent screen → Auth code → Token
│   │   └── Token proves app access, not identity
│   │
│   ├── OpenID Connect
│   │   ├── Adds authentication on top of OAuth2
│   │   ├── Returns access token + ID token
│   │   ├── ID token is JWT with identity
│   │   └── Used by Google, GitHub, Microsoft
│   │
│   └── Single Sign-On (SSO)
│       ├── UX pattern, not auth method
│       ├── Login once, access multiple services
│       ├── Identity Protocols
│       │   ├── SAML (XML-based, enterprise/legacy)
│       │   └── OpenID Connect (modern, JWT-based)
│       └── Example: Google services
│
├── Authorization
│   ├── Purpose
│   │   └── What can authenticated user do
│   │
│   ├── Models
│   │   ├── RBAC (Role-Based)
│   │   │   ├── Assign roles to users
│   │   │   ├── Admin → full access
│   │   │   ├── Editor → create/read/update
│   │   │   ├── Viewer → read only
│   │   │   └── Most common model
│   │   ├── ABAC (Attribute-Based)
│   │   │   ├── User attributes
│   │   │   ├── Resource attributes
│   │   │   ├── Environment conditions
│   │   │   └── More flexible but complex
│   │   └── ACL (Access Control Lists)
│   │       ├── Per-resource permission list
│   │       ├── User-centric
│   │       ├── Hard to scale
│   │       └── Example: Google Drive sharing
│   │
│   └── Enforcement
│       ├── OAuth2 delegated tokens
│       │   └── Example: Vercel accessing GitHub repos
│       └── JWT/Bearer tokens
│           ├── Carry identity + claims
│           └── Server applies permission logic
│
└── API Security (7 Techniques)
    ├── Rate Limiting
    │   ├── Per endpoint
    │   ├── Per user/IP
    │   └── Overall (anti-DDoS)
    ├── CORS
    │   └── Control allowed domains
    ├── SQL/NoSQL Injection Prevention
    │   ├── Parameterized queries
    │   └── ORM safeguards
    ├── Firewalls (WAF)
    │   └── Filter malicious traffic
    ├── VPNs
    │   └── Private network access only
    ├── CSRF Protection
    │   └── CSRF tokens + session cookies
    └── XSS Prevention
        └── Sanitize user inputs
```
