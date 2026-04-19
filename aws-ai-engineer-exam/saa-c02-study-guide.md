SAA-C02 ULTIMATE COURSE SYNOPSIS
│
├── [I] AWS FUNDAMENTALS & GLOBAL INFRASTRUCTURE
│   │
│   ├── WHAT IS AWS?
│   │   ├── Cloud Provider → infrastructure as a service
│   │   ├── Servers/Services → on-demand, scalable
│   │   └── Giants powered → Amazon.com, Netflix
│   │
│   ├── GLOBAL INFRASTRUCTURE
│   │   ├── Regions → Cluster of data centers (e.g., us-east-1, eu-west-3)
│   │   │   ├── Most services are Region-scoped
│   │   │   └── Choice criteria → Compliance, Latency, Service availability, Pricing
│   │   ├── Availability Zones (AZ) → 1+ discrete data centers in a region
│   │   │   ├── Min 2, usually 3, Max 6 per region
│   │   │   ├── Redundant power, networking, connectivity
│   │   │   └── Isolated from disasters; high bandwidth/low-latency link
│   │   └── Points of Presence (Edge Locations) → 216+ locations, 84 cities, 42 countries
│   │       └── Content delivery with lower latency (CloudFront)
│   │
│   ├── AWS CLOUD HISTORY
│   │   ├── 2002: Internal launch
│   │   ├── 2004: Public launch (SQS)
│   │   ├── 2006: Re-launch (SQS, S3, EC2)
│   │   └── 2019: $35B revenue, 47% market share (leader for 9+ years)
│   │
│   └── CONSOLE SERVICE SCOPE
│       ├── Global → IAM, Route 53, CloudFront, WAF
│       └── Regional → EC2, Beanstalk, Lambda, Rekognition
│
├── [II] IAM (IDENTITY & ACCESS MANAGEMENT)
│   │
│   ├── USERS & GROUPS
│   │   ├── Root Account → created by default; do NOT share or use for daily tasks
│   │   ├── Users → physical people in organization
│   │   └── Groups → contain users only (no nested groups); users can be in multiple
│   │
│   ├── PERMISSIONS (POLICIES)
│   │   ├── JSON Documents → define "what" is allowed
│   │   ├── Least Privilege Principle → only give necessary permissions
│   │   └── Policy Structure:
│   │       ├── Version → language version ("2012-10-17")
│   │       ├── Id → policy identifier (optional)
│   │       └── Statement (Required):
│   │           ├── Sid → statement ID (optional)
│   │           ├── Effect → Allow / Deny
│   │           ├── Principal → account/user/role applied to
│   │           ├── Action → list of API actions (e.g., ec2:Describe*)
│   │           ├── Resource → list of resources actions apply to
│   │           └── Condition → when policy is in effect (optional)
│   │
│   ├── SECURITY & MFA
│   │   ├── Password Policy → length, complexity, expiration, prevent re-use
│   │   └── MFA (Multi-Factor Auth) → "Something you know + Something you have"
│   │       ├── Virtual MFA → Google Authenticator (phone), Authy (multi-device)
│   │       ├── U2F Security Key → YubiKey (support multiple users/root)
│   │       └── Hardware Fob → Gemalto, SurePassID (GovCloud)
│   │
│   ├── ACCESSING AWS
│   │   ├── Management Console → Password + MFA
│   │   ├── CLI (Line Interface) → Access Keys ($Id + $Secret); scripts/automation
│   │   └── SDK (Software Dev Kit) → Language-specific APIs (JS, Py, PHP, .NET, etc.)
│   │
│   ├── IAM ROLES
│   │   ├── Assigned to Services (not people) to perform actions
│   │   └── Examples → EC2 Instance Roles, Lambda Roles, CloudFormation Roles
│   │
│   ├── AUDIT TOOLS
│   │   ├── Credentials Report → Account-level; list of all users & credential status
│   │   └── Access Advisor → User-level; shows service permissions vs. last accessed time
│   │
│   └── SHARED RESPONSIBILITY
│       ├── AWS → Infrastructure, global network security, vuln analysis
│       └── USER → Users, Groups, Roles, Policies, MFA, Key rotation, Access analysis
│
├── [III] EC2 (ELASTIC COMPUTE CLOUD) BASICS
│   │
│   ├── EC2 SIZING & CONFIG
│   │   ├── OS → Linux, Windows, Mac OS
│   │   ├── Compute → CPU cores & power
│   │   ├── RAM → random-access memory
│   │   ├── Storage → EBS/EFS (Network) vs. Instance Store (Hardware)
│   │   ├── Network → Card speed, Public IP
│   │   └── Firewall → Security Groups
│   │
│   ├── BOOTSTRAPPING (USER DATA)
│   │   ├── Script runs ONCE at first launch
│   │   ├── Automates tasks → updates, software install, file downloads
│   │   └── Runs as ROOT user
│   │
│   ├── INSTANCE TYPES (Naming: m5.2xlarge)
│   │   ├── m: instance class
│   │   ├── 5: generation
│   │   ├── 2xlarge: size within class
│   │   ├── General Purpose (t2.micro) → balance of Compute/Memory/Network
│   │   ├── Compute Optimized (c5) → Batch, Media transcoding, HPC, ML, Gaming
│   │   ├── Memory Optimized (r5) → DBs, Cache stores, BI, Big Data real-time
│   │   └── Storage Optimized (i3) → OLTP, NoSQL, Redis, Data Warehouse, DFS
│   │
│   ├── SECURITY GROUPS
│   │   ├── Firewall "outside" the EC2
│   │   ├── Controls Inbound (blocked by default) & Outbound (auth by default)
│   │   ├── Attributes → Port access, IP ranges (v4/v6), Rules (IP or SG-ref)
│   │   ├── Ports to Know:
│   │   │   ├── 22 → SSH (Linux) / SFTP
│   │   │   ├── 80 → HTTP (unsecured)
│   │   │   ├── 443 → HTTPS (secured)
│   │   │   ├── 3389 → RDP (Windows)
│   │   │   └── 21 → FTP
│   │   └── Troubleshooting → Time out = SG issue; Conn Refused = App issue
│   │
│   ├── SSH & CONNECTIVITY
│   │   ├── Mac/Linux → native Terminal (`ssh -i key.pem`)
│   │   ├── Windows → Putty (convert pem to ppk) or native SSH (Win10+)
│   │   └── EC2 Instance Connect → Browser-based; temporary key upload; Port 22 must open
│   │
│   ├── PURCHASING OPTIONS
│   │   ├── On-Demand → Short workload, predictable, highest cost, no commitment
│   │   ├── Reserved (1-3 yr) → Up to 72% discount; long workloads (DBs)
│   │   │   ├── Convertible → can change instance type (45% disc)
│   │   │   └── Scheduled → specific time windows (fraction of day/week)
│   │   ├── Spot → Up to 90% discount; risk of loss if spot price > max bid
│   │   │   └── Use case: Batch, Data analysis, Image processing (resilient jobs)
│   │   ├── Dedicated Hosts → physical server; BYOL; compliance (3 yr commit)
│   │   └── Dedicated Instances → dedicated hardware; shared within your account
│   │
│   └── SPOT INSTANCE STRATEGY
│       ├── Spot Block → "block" for 1-6 hours without interruption (mostly)
│       ├── Terminating → 2 min grace period; must cancel Spot Request BEFORE instance
│       └── Spot Fleets → Set of Spot + (optional) On-Demand instances
│           ├── lowestPrice / diversified / capacityOptimized strategies
│           └── Tries to meet target capacity within price constraints
│
├── [IV] EC2 ASSOCIATE (NETWORKING & PLACEMENT)
│   │
│   ├── IP ADDRESSING (IPv4)
│   │   ├── Public IP → unique on web; geo-located info; changes on stop/start
│   │   ├── Private IP → internal network only; persistent across restart
│   │   └── Elastic IP → fixed public IPv4; max 5 per account; avoid (use DNS/LB)
│   │
│   ├── PLACEMENT GROUPS
│   │   ├── Cluster → single AZ; low-latency; 10 Gbps (HPC, Big Data)
│   │   ├── Spread → across diff hardware; max 7 per AZ per group (High Availability)
│   │   └── Partition → across multiple partitions/racks; 100s of EC2s (HDFS, Kafka, Cassandra)
│   │
│   ├── ENI (ELASTIC NETWORK INTERFACE)
│   │   ├── Virtual network card; Public/Private IP, MAC, Security Group
│   │   └── Bound to specific AZ; can move between instances for failover
│   │
│   ├── EC2 HIBERNATE
│   │   ├── Preservation of RAM state (written to root EBS volume)
│   │   ├── Fast boot (app already initialized/cached)
│   │   └── Requirements → less than 150GB RAM; encrypted root EBS; On-Demand/Reserved
│   │
│   ├── EC2 NITRO & vCPU
│   │   ├── Nitro → next-gen virtual (A1, C5, M5); 64K IOPS EBS; enhanced networking
│   │   ├── Bare Metal → direct hardware access (e.g., c5.metal)
│   │   ├── vCPU → each thread on CPU = 1 vCPU (m5.2xlarge = 4 cores * 2 threads = 8 vCPU)
│   │   └── Optimization → can decrease cores for licensing or disable multithreading for HPC
│   │
│   └── CAPACITY RESERVATIONS
│       ├── Immediate capacity access in specific AZ; no 1-3 yr commit
│       └── Billed from start; no cost saving (unless combined with Savings Plans)
│
├── [V] EC2 STORAGE & INSTANCE STORE
│   │
│   ├── EBS (ELASTIC BLOCK STORE)
│   │   ├── Network drive; AZ-locked; Snapshot to move; Persistent on termination (optional)
│   │   ├── Delete on Termination → enabled for root by default
│   │   └── Snapshots → point-in-time backup; copy across AZ/Region; encrypts on copy if needed
│   │
│   ├── AMI (AMAZON MACHINE IMAGE)
│   │   ├── Customization (OS, Software, Config); built for specific region
│   │   └── Sources → Public (AWS), Own (Private), Marketplace (3rd party)
│   │
│   ├── INSTANCE STORE
│   │   ├── Hardware attached disk; highest I/O (caches, buffers, temp data)
│   │   └── Ephemeral → data lost if instance is STOPPED (Stop/Restart moves hardware)
│   │
│   ├── EBS VOLUME TYPES
│   │   ├── gp2/gp3 (SSD) → General Purpose; balances price/perf; Boot volumes
│   │   ├── io1/io2 (SSD) → Provisioned IOPS; mission-critical; DBs; Multi-Attach support
│   │   ├── st1 (HDD) → Throughput Optimized; Big Data; Log processing (no boot)
│   │   └── sc1 (HDD) → Cold HDD; lowest cost; infrequent access (no boot)
│   │
│   ├── EBS MULTI-ATTACH (io1/io2 ONLY)
│   │   ├── Attach to multiple EC2s in same AZ (Read/Write)
│   │   └── Application must be cluster-aware (Teradata)
│   │
│   ├── EBS ENCRYPTION
│   │   ├── KMS (AES-256); Data at rest, in-flight, snapshots are all encrypted
│   │   └── Unencrypted vol → Snapshot → Copy (with Enc) → Create Vol from Enc Snapshot
│   │
│   └── EFS (ELASTIC FILE SYSTEM)
│       ├── Managed NFS; 100s of EC2 instances across Multi-AZ; Linux only (POSIX)
│       ├── Grow to Petabyte scale; Scalable throughput; 3x price of gp2
│       ├── Performance Modes → General Purpose vs. Max I/O
│       ├── Throughput Modes → Bursting vs. Provisioned
│       └── Storage Tiers → Standard vs. Infrequent Access (EFS-IA)
│
├── [VI] HIGH AVAILABILITY & SCALABILITY
│   │
│   ├── SCALABILITY TYPES
│   │   ├── Vertical → increase instance size (t2.nano to u-12tb1); limit is hardware
│   │   └── Horizontal (Elasticity) → increase number of instances (distributed systems)
│   │
│   ├── SCALABILITY vs. HA
│   │   ├── High Availability → run in at least 2 AZs (survive data center loss)
│   │   └── Active (horiz scaling) vs. Passive (RDS standby)
│   │
│   ├── ELB (ELASTIC LOAD BALANCER)
│   │   ├── Managed service; DNS exposure; Health checks; SSL termination; Stickiness
│   │   ├── ALB (v2 - Layer 7) → HTTP/HTTPS/WebSocket; Path/Host/Query routing
│   │   │   ├── Target Groups → EC2, ECS, Lambda, IP
│   │   │   └── Client IP → Header "X-Forwarded-For"
│   │   ├── NLB (v2 - Layer 4) → TCP/UDP/TLS; static IP; Elastic IP; 100ms latency
│   │   ├── GWLB (Layer 3) → IP Protocol; single entry path for security appliances
│   │   └── CLB (v1) → HTTP/HTTPS/TCP/SSL (legacy)
│   │
│   ├── ELB FEATURES
│   │   ├── Sticky Sessions → cookie (AWSALB/AWSELB) forces same client to same instance
│   │   ├── Cross-Zone LB → distributes evenly across ALL AZs (always on for ALB)
│   │   ├── SNI (Server Name Indication) → multiple SSL certs on one LB (ALB/NLB only)
│   │   └── Connection Draining → Time to finish in-flight requests during deregistration
│   │
│   └── SSL/TLS BASICS
│       ├── Encrypts traffic in transit; ACM (AWS Certificate Manager) management
│       ├── HTTPS Listeners require X.509 cert; security policies for legacy clients
│       └── SNI vs. Multi-CLB → Use SNI for cost efficiency on newer LBs
│
├── [VII] AUTO SCALING GROUPS (ASG)
│   │
│   ├── ASG GOALS
│   │   ├── Scale out/in based on load; maintain min/max capacity
│   │   └── Automatically register to ELB; replace unhealthy instances
│   │
│   ├── SCALING ALARMS & POLICIES
│   │   ├── CloudWatch Alarms → trigger based on Average CPU, Network, etc.
│   │   ├── Target Tracking → keep Avg CPU at 40% (simplest)
│   │   ├── Simple / Step scaling → e.g., CPU > 70% + 2 units; < 30% - 1 unit
│   │   ├── Scheduled Actions → increase min capacity Friday 5pm
│   │   └── Predictive Scaling → forecast load and schedule ahead
│   │
│   ├── METRICS TO SCALE ON
│   │   ├── CPUUtilization
│   │   ├── RequestCountPerTarget (ALB)
│   │   └── Average Network In / Out
│   │
│   ├── TERMINATION POLICY
│   │   ├── Find AZ with most instances → Delete oldest Launch Config/Template
│   │   └── Goal → balance instances across AZs
│   │
│   ├── ASG LIFECYCLE HOOKS
│   │   ├── Pending state steps before In-Service
│   │   └── Terminating state steps before Instance stops
│   │
│   └── LAUNCH TEMPLATE vs. CONFIG
│       ├── Template (Newer) → Versions; Parameter subsets; Spot+On-Demand mix; T2 unlimited
│       └── Config (Legacy) → must re-create every time
│
├── [VIII] DATABASES (RDS, AURORA, ELASTICACHE)
│   │
│   ├── AMAZON RDS (RELATIONAL DB SERVICE)
│   │   ├── Managed Engines → MySQL, Postgres, MariaDB, Oracle, SQL Server, Aurora
│   │   ├── Managed Features → Provisioning, OS Patching, PITR (Point in Time Restore)
│   │   ├── Backups → Daily full + Transaction logs (every 5 min); 7-35 day retention
│   │   ├── Storage Auto Scaling → dynamically increase storage if free space < 10%
│   │   ├── Read Replicas → scale reads (Async); Multi-AZ/Region; Promo to master
│   │   ├── Multi-AZ (Sync) → Failover/DR (AZ loss, storage fail); Multi-AZ RR supported
│   │   ├── Security → KMS at rest; SSL in-flight; IAM Auth (MySQL/Postgres)
│   │   └── Shared Resp USER → SG rules, In-DB users, Public access setting, SSL config
│   │
│   ├── AMAZON AURORA (Cloud Optimized)
│   │   ├── 5x MySQL perf, 3x Postgres perf; Auto-expand storage (10GB-128TB)
│   │   ├── High Availability → 6 copies across 3 AZs (4 for write, 3 for read)
│   │   ├── Self-Healing → peer-to-peer replication; 15 replicas; instantaneous failover
│   │   ├── Endpoints → Writer Endpoint vs. Reader Endpoint (Load Balancer connection)
│   │   ├── Replicas Auto Scaling → add replicas based on CPU usage
│   │   ├── Custom Endpoints → subset of instances for specific queries (Analytical)
│   │   ├── Serverless → intermittent/interrupted workloads; proxy fleet
│   │   ├── Global Database → 1 Primary (R/W), 5 Secondary (R/O); < 1s lag; 1 min RTO
│   │   └── Machine Learning → SQL integration with SageMaker/Comprehend
│   │
│   ├── AMAZON ELASTICACHE
│   │   ├── Managed Redis/Memcached; in-memory; low latency; reduce DB load
│   │   ├── Redis → Auth support; Multi-AZ (Auto-failover); Read replicas; AOF; Snapshots
│   │   ├── Memcached → Multi-node sharding; Multi-threaded; No-HA; Non-persistent
│   │   ├── Security → No IAM Auth (Redis AUTH/tokens instead); SSL in-flight; SGs
│   │   └── Patterns:
│   │       ├── Lazy Loading → Cache miss app gets from DB and writes to cache
│   │       ├── Write Through → update cache whenever DB is written
│   │       └── Session Store → store temp data via TTL
│   │
│   └── GAMING USE CASE (REDIS)
│       └── Sorted Sets → guarantee uniqueness + elemental ordering for real-time leaderboards
│
├── [IX] ROUTE 53 (DNS)
│   │
│   ├── DNS BASICS
│   │   ├── Registrar → buys domain name (e.g., Godaddy, Route 53)
│   │   ├── Record Type → A (host to IPv4), AAAA (IPv6), CNAME (host to host - non root)
│   │   ├── NS → Name Servers for hosted zone
│   │   ├── TTL (Time To Live) → cache duration (High = less traffic; Low = fast changes)
│   │   └── Alias Records → AWS Specific; points to ALB/CF/S3 (Free, Zone Apex support)
│   │
│   ├── HOSTED ZONES
│   │   ├── Public → route traffic on Internet
│   │   └── Private → route traffic WITHIN VPCs (webapp.company.internal)
│   │
│   ├── ROUTING POLICIES
│   │   ├── Simple → single resource; random choice if multiple values
│   │   ├── Weighted → % traffic distribution; testing new versions; weight 0 stops traffic
│   │   ├── Latency-based → region with least latency to user
│   │   ├── Failover (Active-Passive) → secondary DR site if primary health fails
│   │   ├── Geolocation → based on user Continent/Country/US-State
│   │   ├── Geoproximity → location + bias (expand/shrink regions); uses Traffic Flow
│   │   └── Multi-Value → returns up to 8 healthy records
│   │
│   ├── HEALTH CHECKS
│   │   ├── Endpoint checks → 15 checkers; Healthy if > 18% success; 2xx/3xx response
│   │   ├── Calculated checks → OR/AND/NOT logic on up to 256 child checks
│   │   └── CloudWatch Alarm checks → for private resources (throttles, metrics)
│   │
│   └── TRAFFIC FLOW
│       ├── Visual editor for complex routing decision trees
│       └── Traffic Flow Policy → supports versioning/re-use across Hosted Zones
│
├── [X] SOLUTIONS ARCHITECTURE (SAA JOURNEYS)
│   │
│   ├── STATELESS APP: WhatIsTheTime.com
│   │   ├── Single EC2 + EIP (downtime on upgrade)
│   │   ├── Vertical (M5 upgrade) vs. Horizontal (more t2.micro) scaling
│   │   ├── Multi-AZ + ASG + ELB + Health Checks
│   │   └── Reserved capacity for cost savings on base load
│   │
│   ├── STATEFUL APP: MyClothes.com
│   │   ├── Scaling Cart → Stickiness (ELB) vs. Client Cookies (Risk: Security/Size)
│   │   ├── Server Session → ElastiCache / DynamoDB (Session Store)
│   │   ├── User DB → RDS Multi-AZ + Read Replicas
│   │   └── Tight Security → SGs referencing SGs (LB -> EC2 -> DB/Cache)
│   │
│   ├── CMS APP: MyWordPress.com
│   │   ├── DB → Aurora Multi-AZ
│   │   ├── Images → EFS (distributed/NFS) vs. EBS (locked to single instance)
│   │   └── S3 (Alternative) → scale images globally
│   │
│   └── INSTANTIATING QUICKLY
│       ├── Golden AMI → pre-installed software/OS deps
│       ├── User Data → dynamic boot configuration
│       └── Snapshot Restore → DB/Volumes ready with data on boot
│
├── [XI] ELASTIC BEANSTALK
│   │
│   ├── DEVELOPER CENTRIC PaaS
│   │   ├── Handles Capacity, LB, Config, Scaling, Monitoring
│   │   └── Developer responsibility → just code
│   │
│   ├── COMPONENTS
│   │   ├── Application → collection of environments/versions
│   │   ├── App Version → iteration of code
│   │   └── Environment → collection of AWS resources (Web vs. Worker tiers)
│   │
│   ├── TIERS
│   │   ├── Web Server Tier → ALB + ASG (myapp.us-east-1.elasticbeanstalk.com)
│   │   └── Worker Tier → SQS Queue + ASG (processes background tasks/scaling on SQS depth)
│   │
│   └── PLATFORMS
│       └── Go, Java, Node, PHP, Python, Ruby, Docker (Single/Multi/Preconfig)
│
└── [XII] AMAZON S3 (SIMPLE STORAGE SERVICE)
    │
    ├── BUCKETS vs. OBJECTS
    │   ├── Buckets → Region-level; Globally Unique Name; No uppercase/underscore
    │   └── Objects → Key (full path including slash); Value (body); Max 5TB
    │
    ├── VERSIONING
    │   ├── Enabled at bucket level; protect against accidental delete
    │   └── Delete Marker → hides object instead of deleting
    │
    ├── S3 ENCRYPTION
    │   ├── SSE-S3 → keys managed by S3 (AES-256 header)
    │   ├── SSE-KMS → keys managed by KMS (user control + audit trail)
    │   ├── SSE-C → user manages keys OUTSIDE AWS (must provide in every HTTPS header)
    │   └── Client Side ENCRYPTION → encrypt before send; decrypt after retrieve
    │
    └── S3 SECURITY
        ├── User Based → IAM Policies
        ├── Resource Based → Bucket Policies (cross-account); Object ACLs; Bucket ACLs
        └── Transport → SSL/TLS mandatory for SSE-C; HTTPS recommended
