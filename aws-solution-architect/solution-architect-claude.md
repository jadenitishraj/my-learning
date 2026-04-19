AWS Certified Solutions Architect Associate (SAA-C02)

# COMPLETE ASCII TREE REFERENCE — EXAM READY

```
SAA-C02
│
├── [0] AWS GLOBAL INFRASTRUCTURE
│   │
│   ├── REGIONS
│   │   ├── Cluster of data centers (e.g., us-east-1, eu-west-3)
│   │   ├── Most AWS services are region-scoped
│   │   └── How to choose
│   │       ├── Compliance → data stays in region unless you say so
│   │       ├── Proximity → reduced latency
│   │       ├── Service availability → new features roll out per region
│   │       └── Pricing → varies per region
│   │
│   ├── AVAILABILITY ZONES (AZs)
│   │   ├── Usually 3 per region (min 2, max 6)
│   │   ├── Each AZ = 1+ discrete data centers (redundant power/networking)
│   │   ├── Isolated from disasters
│   │   └── Connected via high-bandwidth, ultra-low latency networking
│   │
│   ├── EDGE LOCATIONS / POINTS OF PRESENCE
│   │   └── 216 PoPs (205 Edge + 11 Regional Caches), 84 cities, 42 countries
│   │
│   └── GLOBAL vs REGIONAL SERVICES
│       ├── Global → IAM, Route 53, CloudFront, WAF
│       └── Region-scoped → EC2, Beanstalk, Lambda, Rekognition (most)
│
├── [I] IAM (Identity & Access Management)
│   │
│   ├── CORE CONCEPTS
│   │   ├── Global service
│   │   ├── Root account → created by default, NEVER use/share
│   │   ├── Users → people, can be grouped
│   │   ├── Groups → contain users ONLY (not other groups)
│   │   └── Users can belong to 0 or multiple groups
│   │
│   ├── POLICIES
│   │   ├── JSON documents
│   │   ├── Assigned to users/groups
│   │   ├── Principle of Least Privilege
│   │   └── Structure
│   │       ├── Version (always "2012-10-17")
│   │       ├── Id (optional)
│   │       ├── Statement (required, 1+)
│   │       │   ├── Sid (optional)
│   │       │   ├── Effect → Allow/Deny
│   │       │   ├── Principal → account/user/role
│   │       │   ├── Action → list of actions
│   │       │   ├── Resource → list of resources
│   │       │   └── Condition (optional)
│   │       └── Inheritance → inline + group + direct policies
│   │
│   ├── PASSWORD POLICY
│   │   ├── Min length
│   │   ├── Character type requirements (upper/lower/numbers/symbols)
│   │   ├── Allow users to change own password
│   │   ├── Password expiration
│   │   └── Prevent re-use
│   │
│   ├── MFA (Multi-Factor Auth)
│   │   ├── Password (know) + security device (own)
│   │   └── Device Options
│   │       ├── Virtual → Google Authenticator, Authy
│   │       ├── U2F Security Key → YubiKey
│   │       ├── Hardware Key Fob → Gemalto
│   │       └── GovCloud → SurePassID
│   │
│   ├── ACCESS METHODS
│   │   ├── AWS Management Console → password + MFA
│   │   ├── AWS CLI → access keys
│   │   ├── AWS SDK → access keys
│   │   └── Access Keys = Access Key ID (username) + Secret (password)
│   │
│   ├── IAM ROLES FOR SERVICES
│   │   ├── Let AWS services perform actions on your behalf
│   │   ├── EC2 Instance Roles
│   │   ├── Lambda Function Roles
│   │   └── CloudFormation Roles
│   │
│   ├── SECURITY TOOLS
│   │   ├── IAM Credentials Report (account-level)
│   │   └── IAM Access Advisor (user-level) → last accessed timestamps
│   │
│   ├── BEST PRACTICES
│   │   ├── Don't use root (only setup)
│   │   ├── 1 physical user = 1 AWS user
│   │   ├── Assign users → groups → permissions
│   │   ├── Strong password policy + MFA
│   │   ├── Roles for services
│   │   ├── Access Keys for programmatic access
│   │   └── Audit with Credentials Report
│   │
│   └── SHARED RESPONSIBILITY MODEL (IAM)
│       ├── AWS → infra, config/vulnerability analysis, compliance validation
│       └── YOU → users/groups/roles/policies, MFA, key rotation, permission analysis
│
├── [II] EC2 BASICS
│   │
│   ├── EC2 OVERVIEW
│   │   ├── Elastic Compute Cloud = IaaS
│   │   ├── Capabilities
│   │   │   ├── Rent VMs (EC2)
│   │   │   ├── Store data on virtual drives (EBS)
│   │   │   ├── Distribute load (ELB)
│   │   │   └── Auto-scale (ASG)
│   │   └── Knowing EC2 = understanding the cloud
│   │
│   ├── EC2 CONFIGURATION
│   │   ├── OS → Linux / Windows / macOS
│   │   ├── CPU (compute power, cores)
│   │   ├── RAM
│   │   ├── Storage → EBS & EFS (network) + Instance Store (hardware)
│   │   ├── Network card → speed, Public IP
│   │   ├── Firewall → Security Group
│   │   └── Bootstrap → EC2 User Data (runs as root, once at first start)
│   │
│   ├── INSTANCE TYPES (naming: m5.2xlarge)
│   │   ├── m → instance class
│   │   ├── 5 → generation
│   │   ├── 2xlarge → size
│   │   ├── General Purpose → t2.micro (free tier), balanced
│   │   ├── Compute Optimized → C-series, HPC, media transcoding, gaming
│   │   ├── Memory Optimized → R-series, in-memory DBs, BI analytics
│   │   └── Storage Optimized → I/D-series, OLTP, NoSQL, data warehouses
│   │
│   ├── SECURITY GROUPS
│   │   ├── Firewall on EC2
│   │   ├── Regulate → ports, IP ranges (v4/v6), inbound/outbound
│   │   ├── Rules ONLY (no deny rules)
│   │   ├── Attach to multiple instances
│   │   ├── Locked to region/VPC
│   │   ├── Lives OUTSIDE EC2
│   │   ├── Can reference other Security Groups
│   │   ├── Defaults
│   │   │   ├── Inbound → ALL BLOCKED
│   │   │   └── Outbound → ALL ALLOWED
│   │   └── Troubleshooting
│   │       ├── Timeout → security group issue
│   │       └── Connection refused → app error
│   │
│   ├── CLASSIC PORTS
│   │   ├── 22 → SSH / SFTP
│   │   ├── 21 → FTP
│   │   ├── 80 → HTTP
│   │   ├── 443 → HTTPS
│   │   └── 3389 → RDP (Windows)
│   │
│   ├── EC2 INSTANCE CONNECT
│   │   ├── SSH in browser
│   │   ├── No key file needed (temp key uploaded)
│   │   ├── Only out-of-box for Amazon Linux 2
│   │   └── Port 22 must be open
│   │
│   └── PURCHASING OPTIONS
│       ├── On-Demand
│       │   ├── Linux → per second (after first minute)
│       │   ├── Others → per hour
│       │   ├── Highest cost, no commitment
│       │   └── Short-term, unpredictable workloads
│       ├── Reserved (min 1 year)
│       │   ├── Up to 72% discount vs on-demand
│       │   ├── 1 year (+) or 3 years (+++)
│       │   ├── No upfront | Partial upfront (+) | All upfront (++)
│       │   ├── Reserved → specific instance type, steady-state
│       │   ├── Convertible → change instance type, up to 45% off
│       │   └── Scheduled → launch in time window, 1 year only
│       ├── Spot
│       │   ├── Up to 90% discount
│       │   ├── Can LOSE at any time (max price < current spot price)
│       │   ├── Most cost-efficient
│       │   ├── Best for → batch, data analysis, resilient workloads
│       │   └── NOT for critical jobs or databases
│       ├── Dedicated Hosts
│       │   ├── Physical server fully dedicated
│       │   ├── 3-year reservation
│       │   ├── Compliance / BYOL licensing
│       │   └── Most expensive
│       └── Dedicated Instances
│           ├── Hardware dedicated to you
│           ├── May share with other instances in your account
│           └── No control over instance placement
│
├── [III] EC2 ADVANCED (Associate-level)
│   │
│   ├── PRIVATE vs PUBLIC IP (IPv4)
│   │   ├── IPv4: [0-255].[0-255].[0-255].[0-255]
│   │   ├── Public → unique worldwide, geo-locatable
│   │   ├── Private → unique within network, machines use NAT+IGW for internet
│   │   └── Private IP ranges
│   │       ├── 10.0.0.0/8 → big networks
│   │       ├── 172.16.0.0/12 → default AWS
│   │       └── 192.168.0.0/16 → home networks
│   │
│   ├── ELASTIC IP (EIP)
│   │   ├── Fixed public IPv4
│   │   ├── 5 EIP per account (can request more)
│   │   ├── One instance at a time
│   │   ├── Mask instance/software failure via remapping
│   │   └── AVOID → use DNS/ALB instead (poor architecture sign)
│   │
│   ├── PLACEMENT GROUPS
│   │   ├── Cluster
│   │   │   ├── Same rack, same AZ
│   │   │   ├── 10 Gbps bandwidth between instances (Enhanced Networking)
│   │   │   ├── Rack failure → all instances fail
│   │   │   └── Use → big data fast, low-latency high-throughput apps
│   │   ├── Spread
│   │   │   ├── Across hardware, can span AZs
│   │   │   ├── Max 7 instances/AZ/group
│   │   │   └── Use → critical apps needing max availability, isolation
│   │   └── Partition
│   │       ├── Up to 7 partitions per AZ
│   │       ├── Can span multiple AZs same region
│   │       ├── Up to 100s of EC2 instances
│   │       ├── Partitions don't share racks
│   │       ├── Partition failure doesn't affect others
│   │       ├── Metadata accessible on instances
│   │       └── Use → HDFS, HBase, Cassandra, Kafka
│   │
│   ├── ELASTIC NETWORK INTERFACES (ENI)
│   │   ├── Logical VPC component = virtual network card
│   │   ├── Attributes
│   │   │   ├── Primary private IPv4 + secondary
│   │   │   ├── 1 EIP per private IPv4
│   │   │   ├── 1 public IPv4
│   │   │   ├── 1+ security groups
│   │   │   └── MAC address
│   │   ├── Create independently, attach on fly (failover)
│   │   └── Bound to specific AZ
│   │
│   ├── EC2 HIBERNATE
│   │   ├── Preserves in-memory RAM state
│   │   ├── Faster boot (OS not stopped/restarted)
│   │   ├── RAM → written to root EBS
│   │   ├── Root EBS must be encrypted
│   │   ├── Requirements
│   │   │   ├── Families → C3, C4, C5, M3, M4, M5, R3, R4, R5
│   │   │   ├── RAM < 150 GB
│   │   │   ├── NOT bare metal
│   │   │   ├── AMIs → Amazon Linux 2, Linux AMI, Ubuntu, Windows
│   │   │   ├── Root → EBS, encrypted, not instance store, large
│   │   │   ├── On-Demand + Reserved
│   │   │   └── Max 60 days hibernated
│   │   └── Use → long-running processes, save RAM, slow init services
│   │
│   ├── EC2 NITRO
│   │   ├── Next-gen underlying platform
│   │   ├── Virtualized → A1, C5, C5a, C5ad, C5d, C5n, C6g, etc.
│   │   ├── Bare metal → a1.metal, c5.metal, etc.
│   │   └── Benefits
│   │       ├── Enhanced networking, HPC, IPv6
│   │       ├── Higher EBS speed (64,000 IOPS vs 32,000)
│   │       └── Better underlying security
│   │
│   ├── vCPU
│   │   ├── Multiple threads per CPU = multithreading
│   │   ├── Each thread = 1 vCPU
│   │   └── Example → m5.2xlarge = 4 CPU × 2 threads = 8 vCPU
│   │
│   ├── CPU OPTIMIZATION
│   │   ├── # of cores → can decrease (reduce licensing)
│   │   ├── Threads/core → disable MT for HPC
│   │   └── Only at instance launch
│   │
│   └── CAPACITY RESERVATIONS
│       ├── Ensure capacity when needed
│       ├── Manual/planned end date
│       ├── No 1/3-year commitment
│       ├── Immediate access, billed on start
│       ├── Specify → AZ, # instances, type/tenancy/platform
│       └── Combine with RI + Savings Plans for cost savings
│
├── [IV] EC2 INSTANCE STORAGE
│   │
│   ├── EBS (Elastic Block Store)
│   │   ├── Network drive attached to instances
│   │   ├── Persists after termination
│   │   ├── One instance at a time (except multi-attach io1/io2)
│   │   ├── Bound to AZ (snapshot to move across AZs)
│   │   ├── Provisioned capacity (size + IOPS)
│   │   ├── Free tier → 30 GB GP or Magnetic
│   │   ├── Delete on Termination
│   │   │   ├── Root → deleted (default)
│   │   │   └── Other → preserved (default)
│   │   └── Volume Types (6)
│   │       ├── GP2/GP3 (SSD) → General Purpose, boot volumes
│   │       ├── IO1/IO2 (SSD) → Highest perf, boot volumes
│   │       ├── ST1 (HDD) → Throughput Optimized
│   │       └── SC1 (HDD) → Cold, cheapest
│   │
│   ├── GP2/GP3 DETAILS
│   │   ├── 1 GiB - 16 TiB
│   │   ├── GP3 → 3000 IOPS baseline, 125 MiB/s
│   │   │   └── Max 16,000 IOPS, 1000 MiB/s (independent)
│   │   └── GP2 → burst to 3000 IOPS
│   │       ├── Size + IOPS linked, max 16,000
│   │       ├── 3 IOPS/GB, max at 5,334 GB
│   │       └── Uses → boot, virtual desktops, dev/test
│   │
│   ├── IO1/IO2 DETAILS (PIOPS SSD)
│   │   ├── 4 GiB - 16 TiB
│   │   ├── Max PIOPS → 64,000 (Nitro), 32,000 (others)
│   │   ├── PIOPS independent from size
│   │   ├── IO2 → better durability + more IOPS/GiB (same price)
│   │   └── Use → critical business, >16,000 IOPS, databases
│   │
│   ├── IO2 BLOCK EXPRESS
│   │   ├── 4 GiB - 64 TiB
│   │   ├── Sub-millisecond latency
│   │   ├── Max 256,000 PIOPS (1000:1 IOPS:GiB ratio)
│   │   └── Supports EBS Multi-Attach
│   │
│   ├── ST1/SC1 DETAILS (HDD)
│   │   ├── Cannot be boot volume
│   │   ├── 125 MiB - 16 TiB
│   │   ├── ST1 → Throughput Optimized
│   │   │   ├── Max 500 MiB/s, 500 IOPS
│   │   │   └── Big data, warehouses, logs
│   │   └── SC1 → Cold
│   │       ├── Max 250 MiB/s, 250 IOPS
│   │       └── Infrequent, lowest cost
│   │
│   ├── EBS MULTI-ATTACH (io1/io2)
│   │   ├── Same EBS → multiple EC2 in SAME AZ
│   │   ├── Full read/write on all
│   │   ├── Use → clustered Linux apps (Teradata)
│   │   ├── Apps manage concurrent writes
│   │   └── Cluster-aware filesystem (NOT XFS/EX4)
│   │
│   ├── EBS SNAPSHOTS
│   │   ├── Point-in-time backup
│   │   ├── Detach not required (but recommended)
│   │   └── Copy across AZ/Region
│   │
│   ├── EBS ENCRYPTION
│   │   ├── Data at rest + in flight (to instance) + snapshots + derived volumes
│   │   ├── Transparent (nothing to do)
│   │   ├── Uses KMS (AES-256)
│   │   ├── Minimal latency impact
│   │   ├── Copy unencrypted → encrypt during copy
│   │   └── To encrypt existing: snapshot → copy encrypted → new volume → attach
│   │
│   ├── AMI (Amazon Machine Image)
│   │   ├── EC2 customization (software, config, OS, monitoring)
│   │   ├── Faster boot vs raw OS
│   │   ├── Region-specific (copy across regions)
│   │   ├── Sources → Public, Your own, Marketplace
│   │   └── Process → start instance → stop → create AMI (+ EBS snapshots)
│   │
│   ├── EC2 INSTANCE STORE
│   │   ├── High-performance HARDWARE disk
│   │   ├── Better I/O than EBS
│   │   ├── EPHEMERAL → lost when stopped
│   │   ├── Use → buffer/cache/scratch/temporary
│   │   ├── Data loss risk on hardware failure
│   │   └── YOUR responsibility → backups/replication
│   │
│   ├── EFS (Elastic File System)
│   │   ├── Managed NFS for multiple EC2
│   │   ├── Multi-AZ works
│   │   ├── Highly available, scalable, 3x gp2 price, pay-per-use
│   │   ├── Linux only (POSIX, NFSv4.1)
│   │   ├── Uses Security Groups
│   │   ├── KMS encryption at rest
│   │   ├── No capacity planning
│   │   ├── Use → CMS, web serving, data sharing, WordPress
│   │   ├── Performance Modes
│   │   │   ├── General Purpose (default) → latency-sensitive
│   │   │   └── Max I/O → higher latency/throughput, parallel, big data
│   │   ├── Throughput Modes
│   │   │   ├── Bursting → 1 TB = 50 MiB/s + burst 100 MiB/s
│   │   │   └── Provisioned → set regardless of size
│   │   └── Storage Tiers
│   │       ├── Standard → frequent access
│   │       └── Infrequent Access (EFS-IA) → retrieval cost, cheaper storage
│   │
│   └── EBS vs EFS
│       ├── EBS → single instance, AZ-locked
│       │   ├── GP2 → IO grows with size
│       │   ├── IO1 → IO independent
│       │   └── Migrate via snapshot → restore
│       └── EFS → multiple instances across AZs, Linux only
│
├── [V] LOAD BALANCING, ASG, HIGH AVAILABILITY
│   │
│   ├── SCALABILITY CONCEPTS
│   │   ├── Vertical → increase instance size (RDS, ElastiCache)
│   │   │   └── t2.nano (0.5G/1vCPU) → u-12tb1.metal (12.3TB/448 vCPU)
│   │   ├── Horizontal → increase # instances (web apps)
│   │   │   └── ASG + Load Balancer
│   │   └── High Availability → multi-AZ, passive or active
│   │
│   ├── LOAD BALANCER BASICS
│   │   ├── Purposes
│   │   │   ├── Spread load
│   │   │   ├── Single DNS access
│   │   │   ├── Handle failures
│   │   │   ├── Health checks
│   │   │   ├── SSL termination
│   │   │   ├── Stickiness (cookies)
│   │   │   ├── Multi-AZ HA
│   │   │   └── Separate public/private traffic
│   │   ├── Health Checks → port + route (/health common), 200=OK
│   │   └── Integrations → EC2, ASG, ECS, ACM, CloudWatch, R53, WAF, Global Accelerator
│   │
│   ├── ELB TYPES (4)
│   │   ├── CLB (Classic) → 2009, v1, HTTP/HTTPS/TCP/SSL, Layer 4/7
│   │   ├── ALB (Application) → 2016, v2, HTTP/HTTPS/WebSocket, Layer 7
│   │   ├── NLB (Network) → 2017, v2, TCP/TLS/UDP, Layer 4
│   │   └── GWLB (Gateway) → 2020, IP Protocol, Layer 3
│   │
│   ├── APPLICATION LOAD BALANCER (ALB)
│   │   ├── Layer 7, multi-app/container balance
│   │   ├── HTTP/2 + WebSocket + redirects
│   │   ├── Routing
│   │   │   ├── URL path (/users, /posts)
│   │   │   ├── Hostname (one.ex.com vs two.ex.com)
│   │   │   └── Query string/headers
│   │   ├── Great for microservices + containers (ECS dynamic port)
│   │   ├── Target Groups → EC2, ECS, Lambda, IP (private)
│   │   ├── Routes to multiple target groups
│   │   ├── Health checks at target group level
│   │   ├── Fixed hostname → XXX.region.elb.amazonaws.com
│   │   └── Client IP → X-Forwarded-For header (+ Port, Proto)
│   │
│   ├── NETWORK LOAD BALANCER (NLB)
│   │   ├── Layer 4, TCP/UDP
│   │   ├── Millions req/sec, ~100ms latency (vs 400ms ALB)
│   │   ├── 1 static IP per AZ, supports EIP
│   │   ├── Not in free tier
│   │   └── Use → extreme perf, TCP/UDP
│   │
│   ├── STICKY SESSIONS
│   │   ├── Same client → same instance
│   │   ├── CLB + ALB only
│   │   ├── Cookie expiration controllable
│   │   ├── Use → preserve session data
│   │   ├── Can cause imbalance
│   │   └── Cookie Names
│   │       ├── Application-based
│   │       │   ├── Custom cookie (from target)
│   │       │   │   └── Reserved names → AWSALB, AWSALBAPP, AWSALBTG
│   │       │   └── Application cookie → AWSALBAPP (ALB-generated)
│   │       └── Duration-based (ALB-generated)
│   │           ├── ALB → AWSALB
│   │           └── CLB → AWSELB
│   │
│   ├── CROSS-ZONE LOAD BALANCING
│   │   ├── ALB → always on, no inter-AZ charges
│   │   ├── NLB → disabled by default, $ inter-AZ
│   │   └── CLB → Console:on, CLI/API:off, no charges if enabled
│   │
│   ├── SSL/TLS
│   │   ├── ACM manages certs
│   │   ├── HTTPS listener → default cert + optional list
│   │   ├── SNI → multiple certs per ALB/NLB/CloudFront
│   │   │   └── CLB does NOT support SNI
│   │   ├── CLB → 1 SSL cert
│   │   ├── ALB → multi-listener, multi-cert (SNI)
│   │   └── NLB → multi-listener, multi-cert (SNI)
│   │
│   └── CONNECTION DRAINING / DEREGISTRATION DELAY
│       ├── CLB → "Connection Draining"
│       ├── ALB/NLB → "Deregistration Delay"
│       ├── 1-3600s, default 300s
│       ├── 0 = disabled
│       └── Stop sending NEW requests during deregister
│
├── [VI] AUTO SCALING GROUPS (ASG)
│   │
│   ├── PURPOSE
│   │   ├── Scale out/in to match load
│   │   ├── Min/max machines
│   │   └── Auto-register with LB
│   │
│   ├── ATTRIBUTES
│   │   ├── Launch Configuration/Template
│   │   │   ├── AMI + Instance Type
│   │   │   ├── User Data, EBS, Security Groups
│   │   │   └── SSH Key Pair
│   │   ├── Min / Max / Desired capacity
│   │   ├── Network + Subnets
│   │   ├── Load Balancer info
│   │   └── Scaling Policies
│   │
│   ├── SCALING POLICIES
│   │   ├── Dynamic
│   │   │   ├── Target Tracking → e.g., avg CPU 40%
│   │   │   ├── Simple/Step → CloudWatch alarm-based
│   │   │   └── Scheduled → known patterns (Fri 5pm)
│   │   ├── Predictive → ML forecasts load
│   │   └── Alarm-based (CloudWatch)
│   │       ├── Monitor metric
│   │       ├── Scale-out + Scale-in policies
│   │       └── Custom Metrics via PutMetric
│   │
│   ├── GOOD METRICS TO SCALE ON
│   │   ├── CPUUtilization
│   │   ├── RequestCountPerTarget
│   │   ├── Network In/Out
│   │   └── Custom CloudWatch
│   │
│   ├── SCALING COOLDOWNS
│   │   ├── Default 300s after scaling
│   │   ├── Prevents launch/terminate for metrics to stabilize
│   │   └── Use ready-made AMI → reduce cooldown
│   │
│   ├── DEFAULT TERMINATION POLICY
│   │   1. AZ with most instances
│   │   2. Oldest Launch Configuration
│   │   └── Tries to balance across AZs
│   │
│   ├── LIFECYCLE HOOKS
│   │   ├── Pending state → extra setup before in-service
│   │   └── Terminating state → actions before terminate
│   │
│   └── LAUNCH TEMPLATE vs CONFIGURATION
│       ├── Both → AMI, type, key pair, SGs, etc.
│       ├── Launch Configuration (legacy)
│       │   └── Recreate every time
│       └── Launch Template (NEW, recommended)
│           ├── Multiple versions
│           ├── Parameter subsets (reuse/inheritance)
│           ├── On-Demand + Spot mix
│           ├── T2 unlimited burst
│           └── AWS recommends going forward
│
├── [VII] RDS, AURORA & ELASTICACHE
│   │
│   ├── RDS OVERVIEW
│   │   ├── Engines → Postgres, MySQL, MariaDB, Oracle, MS SQL, Aurora
│   │   ├── Managed benefits
│   │   │   ├── Auto provisioning, OS patching
│   │   │   ├── Continuous backups + PITR
│   │   │   ├── Monitoring dashboards
│   │   │   ├── Read Replicas + Multi-AZ DR
│   │   │   ├── Maintenance windows
│   │   │   ├── Vertical + horizontal scaling
│   │   │   └── Storage → EBS (gp2/io1)
│   │   └── NO SSH access
│   │
│   ├── RDS BACKUPS
│   │   ├── Auto-enabled
│   │   ├── Automated
│   │   │   ├── Daily full backup (maintenance window)
│   │   │   ├── Tx logs every 5 min
│   │   │   ├── Retention 7 days (up to 35)
│   │   │   └── PITR to any point
│   │   └── DB Snapshots → manual, any retention
│   │
│   ├── RDS STORAGE AUTO SCALING
│   │   ├── Auto-increase storage
│   │   ├── Triggers
│   │   │   ├── <10% free storage
│   │   │   ├── 5 min low-storage
│   │   │   └── 6 hr since last mod
│   │   ├── Set Maximum Storage Threshold
│   │   └── All engines supported
│   │
│   ├── RDS READ REPLICAS
│   │   ├── Up to 5 Read Replicas
│   │   ├── Same AZ / Cross AZ / Cross Region
│   │   ├── ASYNC replication (eventually consistent)
│   │   ├── Can promote to own DB
│   │   ├── App must update connection string
│   │   ├── Use → SELECT queries only (no INSERT/UPDATE/DELETE)
│   │   └── Network Cost
│   │       ├── Same region → FREE
│   │       └── Cross region → $$$
│   │
│   ├── RDS MULTI-AZ (DR)
│   │   ├── SYNC replication
│   │   ├── One DNS name → auto failover
│   │   ├── Increases availability
│   │   ├── Failover on AZ/network/instance/storage failure
│   │   ├── No manual app intervention
│   │   ├── NOT for scaling
│   │   ├── FREE
│   │   ├── Read Replicas can also be Multi-AZ
│   │   └── Single-AZ → Multi-AZ
│   │       ├── Zero downtime
│   │       ├── Click "modify"
│   │       └── Internal: snapshot → restore → sync
│   │
│   ├── RDS SECURITY
│   │   ├── At rest encryption
│   │   │   ├── KMS AES-256 master + read replicas
│   │   │   ├── Defined at launch
│   │   │   ├── Unencrypted master → no encrypted replicas
│   │   │   └── TDE for Oracle + SQL Server
│   │   ├── In-flight
│   │   │   ├── SSL certificates
│   │   │   ├── Enforce SSL
│   │   │   │   ├── PostgreSQL → rds.force_ssl=1
│   │   │   │   └── MySQL → GRANT USAGE ... REQUIRE SSL
│   │   │   └── Trust certificate when connecting
│   │   ├── Encryption Ops
│   │   │   ├── Snapshot of unencrypted → unencrypted
│   │   │   ├── Snapshot of encrypted → encrypted
│   │   │   ├── Copy snapshot → can enable encryption
│   │   │   └── Encrypt existing → snapshot → copy encrypted → restore
│   │   ├── Network → private subnet, security groups
│   │   ├── Access Mgmt → IAM for API, traditional user/pass
│   │   └── IAM Auth (MySQL + PostgreSQL)
│   │       ├── Token instead of password
│   │       ├── 15 min lifetime
│   │       ├── Network in/out must be SSL
│   │       └── EC2 role for easy integration
│   │
│   ├── RDS SHARED RESPONSIBILITY
│   │   ├── YOURS
│   │   │   ├── Check ports/IP/SG rules
│   │   │   ├── DB user creation + permissions (or IAM)
│   │   │   ├── Public/private access
│   │   │   └── SSL config, parameter groups
│   │   └── AWS
│   │       ├── No SSH
│   │       ├── No manual DB patching
│   │       ├── No manual OS patching
│   │       └── Can't audit underlying instance
│   │
│   ├── AURORA OVERVIEW
│   │   ├── AWS-proprietary (not open source)
│   │   ├── Postgres + MySQL compatible
│   │   ├── Performance
│   │   │   ├── 5x over MySQL on RDS
│   │   │   └── 3x over Postgres on RDS
│   │   ├── Storage → auto-grow 10GB increments, up to 128 TB
│   │   ├── Up to 15 read replicas (vs 5 on MySQL), sub-10ms lag
│   │   ├── Instantaneous failover, HA native
│   │   └── 20% more expensive than RDS, more efficient
│   │
│   ├── AURORA HIGH AVAILABILITY
│   │   ├── 6 copies across 3 AZs
│   │   │   ├── 4/6 for writes
│   │   │   └── 3/6 for reads
│   │   ├── Self-healing peer-to-peer replication
│   │   ├── 100s of volumes (striped)
│   │   ├── One master (writes)
│   │   ├── Auto failover <30s
│   │   ├── Master + up to 15 replicas for reads
│   │   └── Cross-region replication supported
│   │
│   ├── AURORA ENDPOINTS
│   │   ├── Writer Endpoint → master
│   │   ├── Reader Endpoint → load balance reads
│   │   └── Custom Endpoints → subset for specific workloads
│   │       └── Example → analytics on bigger replicas
│   │
│   ├── AURORA FEATURES
│   │   ├── Auto failover
│   │   ├── Backup & Recovery
│   │   ├── Isolation + Security
│   │   ├── Industry compliance
│   │   ├── Push-button scaling
│   │   ├── Zero-downtime patching
│   │   ├── Advanced Monitoring
│   │   ├── Routine Maintenance
│   │   └── Backtrack → restore any point w/o backups
│   │
│   ├── AURORA SECURITY
│   │   ├── Same as RDS (same engines)
│   │   ├── KMS at rest (backups/snapshots/replicas too)
│   │   ├── SSL in flight
│   │   ├── IAM token auth
│   │   └── SG protection, no SSH
│   │
│   ├── AURORA SERVERLESS
│   │   ├── Auto instantiation + scaling
│   │   ├── Good for intermittent/unpredictable workloads
│   │   ├── No capacity planning
│   │   └── Pay per second
│   │
│   ├── AURORA MULTI-MASTER
│   │   ├── Immediate write-node failover (HA)
│   │   └── Every node does R/W (vs promoting replica)
│   │
│   ├── AURORA GLOBAL DATABASE
│   │   ├── Cross-region read replicas → for DR
│   │   └── Global Database (recommended)
│   │       ├── 1 primary region (R/W)
│   │       ├── Up to 5 secondary (RO) regions, <1s lag
│   │       ├── 16 read replicas/secondary region
│   │       ├── Lower latency
│   │       └── DR promotion RTO <1 min
│   │
│   ├── AURORA MACHINE LEARNING
│   │   ├── ML predictions via SQL
│   │   ├── Supported → SageMaker + Comprehend
│   │   └── Uses → fraud detection, ad targeting, sentiment, recommendations
│   │
│   ├── ELASTICACHE OVERVIEW
│   │   ├── Managed Redis/Memcached
│   │   ├── In-memory, sub-ms latency
│   │   ├── Clustering (Redis), Multi-AZ, Read Replicas (sharding)
│   │   ├── IAM/SG/KMS/Redis Auth security
│   │   ├── Backup/Snapshot/PITR
│   │   ├── Heavy app code changes required
│   │   └── Use cases
│   │       ├── DB Cache (cache-aside)
│   │       └── User Session Store
│   │
│   ├── REDIS vs MEMCACHED
│   │   ├── REDIS
│   │   │   ├── Multi-AZ + auto-failover
│   │   │   ├── Read Replicas → scale reads + HA
│   │   │   ├── Data durability (AOF persistence)
│   │   │   └── Backup/restore
│   │   └── MEMCACHED
│   │       ├── Multi-node sharding
│   │       ├── NO HA (replication)
│   │       ├── Non-persistent
│   │       ├── No backup/restore
│   │       └── Multi-threaded
│   │
│   ├── ELASTICACHE SECURITY
│   │   ├── NO IAM auth (IAM only for API)
│   │   ├── Redis AUTH → password/token + SSL
│   │   └── Memcached → SASL auth
│   │
│   └── CACHING PATTERNS
│       ├── Lazy Loading → cache on read, can be stale
│       ├── Write Through → cache on DB write, never stale
│       ├── Session Store → temp data with TTL
│       └── Redis Use Case → Gaming leaderboards (sorted sets)
│
├── [VIII] ROUTE 53 (DNS)
│   │
│   ├── DNS BASICS
│   │   ├── Translates hostnames to IPs
│   │   ├── FQDN → http://api.www.example.com.
│   │   │   ├── Protocol → http://
│   │   │   ├── Root → .
│   │   │   ├── TLD → .com
│   │   │   ├── SLD → example.com
│   │   │   ├── Subdomain → www
│   │   │   └── Domain Name → api.www.example.com
│   │   ├── Terminologies
│   │   │   ├── Domain Registrar → R53, GoDaddy
│   │   │   ├── DNS Records → A/AAAA/CNAME/NS
│   │   │   ├── Zone File → contains records
│   │   │   ├── Name Server → resolves queries
│   │   │   ├── TLD → .com/.us
│   │   │   └── SLD → amazon.com
│   │   └── Resolution Flow
│   │       ├── Browser → Local DNS → Root → TLD → SLD → IP
│   │       └── ICANN manages root, IANA manages domain roots
│   │
│   ├── ROUTE 53 OVERVIEW
│   │   ├── Highly available, scalable, managed, authoritative DNS
│   │   ├── Domain registrar
│   │   ├── Health checks
│   │   ├── 100% availability SLA (only AWS service)
│   │   └── Port 53 reference
│   │
│   ├── RECORDS
│   │   ├── Contain
│   │   │   ├── Domain/subdomain name
│   │   │   ├── Record type
│   │   │   ├── Value
│   │   │   ├── Routing Policy
│   │   │   └── TTL
│   │   └── Types
│   │       ├── Must know → A / AAAA / CNAME / NS
│   │       └── Advanced → CAA/DS/MX/NAPTR/PTR/SOA/TXT/SPF/SRV
│   │
│   ├── RECORD TYPES DETAIL
│   │   ├── A → hostname → IPv4
│   │   ├── AAAA → hostname → IPv6
│   │   ├── CNAME → hostname → hostname
│   │   │   └── CANNOT do Zone Apex (top of domain)
│   │   └── NS → Name Servers for hosted zone
│   │
│   ├── HOSTED ZONES
│   │   ├── Public → internet routing
│   │   ├── Private → VPC-only routing
│   │   └── $0.50/month/zone
│   │
│   ├── TTL (Time To Live)
│   │   ├── High TTL (24h) → less traffic, possibly outdated
│   │   ├── Low TTL (60s) → more traffic ($), fresh, easy change
│   │   └── Mandatory EXCEPT for Alias
│   │
│   ├── CNAME vs ALIAS
│   │   ├── CNAME
│   │   │   ├── hostname → any hostname
│   │   │   └── NON-ROOT domain only
│   │   └── ALIAS
│   │       ├── hostname → AWS resource
│   │       ├── Works on ROOT + non-root
│   │       ├── FREE
│   │       ├── Native health check
│   │       ├── Always A/AAAA type
│   │       ├── No TTL setting
│   │       └── Auto-recognizes IP changes
│   │
│   ├── ALIAS TARGETS
│   │   ├── Elastic Load Balancers
│   │   ├── CloudFront Distributions
│   │   ├── API Gateway
│   │   ├── Elastic Beanstalk
│   │   ├── S3 Websites
│   │   ├── VPC Interface Endpoints
│   │   ├── Global Accelerator
│   │   ├── Route 53 record (same hosted zone)
│   │   └── CANNOT be EC2 DNS name
│   │
│   ├── ROUTING POLICIES (7)
│   │   ├── Simple
│   │   │   ├── Single resource (or multiple values, random choice)
│   │   │   ├── Alias = one resource only
│   │   │   └── NO health checks
│   │   ├── Weighted
│   │   │   ├── % of requests per resource
│   │   │   ├── Weight 0 = stop
│   │   │   ├── All 0 = return all equally
│   │   │   └── Health checks supported
│   │   ├── Latency-based
│   │   │   ├── Lowest latency to AWS Region
│   │   │   └── Health checks supported
│   │   ├── Failover (Active-Passive)
│   │   │   ├── Primary → mandatory health check
│   │   │   └── Secondary → DR
│   │   ├── Geolocation
│   │   │   ├── User LOCATION (vs latency)
│   │   │   ├── Continent/Country/US State
│   │   │   ├── Create "Default" record
│   │   │   └── Use → localization, content restriction
│   │   ├── Geoproximity
│   │   │   ├── Geo of users + resources
│   │   │   ├── Bias: 1-99 (expand) / -1 to -99 (shrink)
│   │   │   ├── AWS region OR lat/long
│   │   │   └── REQUIRES Route 53 Traffic Flow
│   │   └── Multi-Value
│   │       ├── Up to 8 healthy records returned
│   │       ├── Not a substitute for ELB
│   │       └── Health checks supported
│   │
│   ├── HEALTH CHECKS
│   │   ├── HTTP Health Checks → public only
│   │   ├── Types
│   │   │   ├── Endpoint (app, server, resource)
│   │   │   ├── Calculated (monitor other checks)
│   │   │   └── CloudWatch Alarm (private resources!)
│   │   ├── CW metrics integrated
│   │   ├── Endpoint Checks
│   │   │   ├── ~15 global checkers
│   │   │   ├── Threshold → 3 default
│   │   │   ├── Interval → 30s (or 10s higher cost)
│   │   │   ├── Protocols → HTTP/HTTPS/TCP
│   │   │   ├── >18% healthy = healthy
│   │   │   ├── 2xx/3xx = pass
│   │   │   ├── Text matching in first 5120 bytes
│   │   │   └── Firewall must allow R53 IPs
│   │   ├── Calculated Health Checks
│   │   │   ├── Combine with OR/AND/NOT
│   │   │   ├── Up to 256 child checks
│   │   │   └── Use → maintenance without all failing
│   │   └── Private Hosted Zones
│   │       ├── R53 checkers outside VPC
│   │       └── Use CloudWatch Metric + Alarm
│   │
│   ├── TRAFFIC FLOW
│   │   ├── Visual editor for complex decision trees
│   │   ├── Traffic Flow Policies (versioned)
│   │   └── Apply across hosted zones
│   │
│   └── DOMAIN REGISTRAR vs DNS
│       ├── Registrar (GoDaddy, R53) → buy domain
│       ├── DNS Service → manage records
│       ├── 3rd party registrar + R53 DNS
│       │   ├── Create R53 hosted zone
│       │   └── Update NS records on 3rd party
│       └── Registrar ≠ DNS Service
│
├── [IX] CLASSIC SOLUTIONS ARCHITECTURES
│   │
│   ├── STATELESS WEB APP (WhatIsTheTime.com)
│   │   ├── Progression
│   │   │   ├── Start simple → Public EC2 + EIP
│   │   │   ├── Vertical scale → downtime
│   │   │   ├── Horizontal scale → multiple EC2 + DNS
│   │   │   ├── Add LB → multi-AZ health checks
│   │   │   ├── Add ASG → auto-scaling
│   │   │   ├── Multi-AZ resilience
│   │   │   └── Reserve capacity for min → cost savings
│   │   └── Key lessons → 5 pillars (cost, perf, reliability, security, ops)
│   │
│   ├── STATEFUL WEB APP (MyClothes.com)
│   │   ├── Challenge → shopping cart + user details
│   │   ├── Progression
│   │   │   ├── Multi-AZ ASG
│   │   │   ├── Sticky Sessions (ELB)
│   │   │   ├── Web Cookies (stateless) → risk: tampered, 4KB limit
│   │   │   ├── Server Sessions → ElastiCache / DynamoDB
│   │   │   ├── RDS for user data
│   │   │   ├── Scale Reads → Read Replicas
│   │   │   ├── Alternative → Write Through cache
│   │   │   ├── Multi-AZ ElastiCache + RDS
│   │   │   └── Tight SGs → LB→EC2→RDS/Cache
│   │   └── Components
│   │       ├── ELB stickiness
│   │       ├── Web clients + cookies
│   │       ├── ElastiCache (sessions/caching)
│   │       └── RDS (user data, Read Replicas, Multi-AZ)
│   │
│   ├── STATEFUL WEB APP (MyWordPress.com)
│   │   ├── Aurora Multi-AZ + Read Replicas
│   │   ├── EBS (single instance storage)
│   │   └── EFS (distributed storage for images)
│   │
│   ├── FAST INSTANTIATION
│   │   ├── EC2
│   │   │   ├── Golden AMI
│   │   │   ├── User Data bootstrap
│   │   │   └── Hybrid (Beanstalk)
│   │   ├── RDS → restore snapshot
│   │   └── EBS → restore snapshot
│   │
│   ├── TYPICAL 3-TIER WEB APP
│   │   ├── Route 53
│   │   ├── ELB (public subnet)
│   │   ├── ASG (private subnet)
│   │   ├── ElastiCache + RDS (data subnet)
│   │   └── All Multi-AZ
│   │
│   └── ELASTIC BEANSTALK
│       ├── Developer-centric app deployment
│       ├── Uses EC2/ASG/ELB/RDS under hood
│       ├── Managed → capacity, LB, scaling, health
│       ├── Full config control
│       ├── FREE (pay for underlying)
│       ├── Components
│       │   ├── Application → collection of components
│       │   ├── Application Version → iteration
│       │   └── Environment → resources running a version
│       │       ├── Tiers → Web Server vs Worker
│       │       └── Multiple (dev/test/prod)
│       ├── Supported Platforms
│       │   ├── Go, Java SE, Java w/ Tomcat
│       │   ├── .NET Core Linux / .NET Windows
│       │   ├── Node.js, PHP, Python, Ruby
│       │   ├── Packer Builder
│       │   ├── Single Container Docker
│       │   ├── Multi-container Docker
│       │   ├── Preconfigured Docker
│       │   └── Custom Platform
│       └── Worker Tier
│           ├── Scales on SQS queue size
│           └── Push from Web Server Tier
│
├── [X] S3 STORAGE & DATA MANAGEMENT
│   │
│   ├── S3 BUCKETS
│   │   ├── Globally unique name
│   │   ├── Region-level
│   │   └── Naming → no uppercase/underscore, 3-63 chars, no IP, start with lower/number
│   │
│   ├── S3 OBJECTS
│   │   ├── Key = FULL path (prefix + object name)
│   │   ├── NO "directories" really (just slashes)
│   │   ├── Max size → 5 TB
│   │   ├── >5 GB → multi-part upload required
│   │   ├── Metadata (system or user)
│   │   ├── Tags (up to 10, Unicode)
│   │   └── Version ID (if versioning enabled)
│   │
│   ├── VERSIONING
│   │   ├── Bucket level
│   │   ├── Protect against unintended deletes
│   │   ├── Easy rollback
│   │   ├── Pre-versioning files → "null" version
│   │   └── Suspending doesn't delete previous versions
│   │
│   ├── ENCRYPTION (4 METHODS)
│   │   ├── SSE-S3
│   │   │   ├── AWS-managed keys
│   │   │   ├── AES-256
│   │   │   ├── Header → "x-amz-server-side-encryption: AES256"
│   │   │   └── Default for new buckets/objects
│   │   ├── SSE-KMS
│   │   │   ├── KMS-managed keys
│   │   │   ├── User control + CloudTrail audit
│   │   │   └── Header → "aws:kms"
│   │   ├── SSE-C
│   │   │   ├── Customer-managed keys (outside AWS)
│   │   │   ├── S3 never stores the key
│   │   │   ├── HTTPS mandatory
│   │   │   └── Key in headers for every request
│   │   └── Client-Side
│   │       ├── Amazon S3 Encryption Client
│   │       ├── Client encrypts/decrypts
│   │       └── Customer fully manages keys + cycle
│   │
│   ├── ENCRYPTION IN TRANSIT
│   │   ├── HTTP endpoint (non-encrypted)
│   │   ├── HTTPS endpoint (recommended)
│   │   └── HTTPS MANDATORY for SSE-C
│   │
│   ├── S3 SECURITY
│   │   ├── User-based → IAM policies
│   │   ├── Resource-based
│   │   │   ├── Bucket Policies (cross-account)
│   │   │   ├── Object ACL (finer grain)
│   │   │   └── Bucket ACL (less common)
│   │   └── Access if → IAM allows OR Resource policy allows, AND no explicit DENY
│   │
│   ├── BUCKET POLICIES
│   │   ├── JSON-based
│   │   ├── Use cases
│   │   │   ├── Public access
│   │   │   ├── Force encrypted uploads
│   │   │   └── Cross-account access
│   │   └── Components → Resources, Actions, Effect, Principal
│   │
│   ├── BLOCK PUBLIC ACCESS
│   │   ├── Block via new ACLs
│   │   ├── Block via any ACLs
│   │   ├── Block via new bucket policies
│   │   ├── Block cross-account + public via policies
│   │   ├── Prevents company data leaks
│   │   └── Can be set at account level
│   │
│   ├── MFA DELETE
│   │   ├── Requires versioning
│   │   ├── Needed for → permanent version delete, suspend versioning
│   │   ├── NOT needed for → enable versioning, list deleted
│   │   ├── Only root account can enable/disable
│   │   └── Enable via CLI only
│   │
│   ├── OTHER SECURITY
│   │   ├── VPC Endpoints (private access)
│   │   ├── S3 Access Logs → other S3 bucket
│   │   ├── CloudTrail API logs
│   │   └── Pre-Signed URLs → temporary access
│   │
│   ├── S3 WEBSITES
│   │   ├── URL → bucket.s3-website-region.amazonaws.com (or .s3-website.)
│   │   └── 403 → bucket policy not allowing public reads
│   │
│   ├── CORS (Cross-Origin Resource Sharing)
│   │   ├── Origin = scheme + host + port
│   │   ├── Browser mechanism
│   │   ├── Same origin → same host+port+proto
│   │   ├── Preflight → OPTIONS request
│   │   ├── Headers → Access-Control-Allow-Origin, -Methods
│   │   └── S3 CORS → enable on bucket
│   │       ├── Specific origin OR *
│   │       └── Popular exam question
│   │
│   ├── CONSISTENCY MODEL
│   │   ├── Strong Consistency (Dec 2020+)
│   │   ├── After successful PUT/DELETE
│   │   ├── Read-after-write consistency
│   │   ├── List consistency
│   │   └── No additional cost / perf impact
│   │
│   └── DEFAULT ENCRYPTION
│       ├── Option 1 → bucket policy (deny unencrypted PUT)
│       ├── Option 2 → default encryption option
│       └── Bucket Policies evaluated BEFORE default encryption
│
├── [XI] DEVELOPING ON AWS
│   │
│   ├── EC2 INSTANCE METADATA
│   │   ├── Learn about itself without IAM role
│   │   ├── URL → http://169.254.169.254/latest/meta-data
│   │   ├── Can retrieve IAM Role name, NOT policy
│   │   ├── Metadata = info about instance
│   │   └── Userdata = launch script
│   │
│   ├── AWS SDK
│   │   ├── Languages → Java, .NET, Node.js, PHP, Python (boto3), Go, Ruby, C++
│   │   ├── Default region if unspecified → us-east-1
│   │   └── AWS CLI uses Python SDK (boto3)
│   │
│   ├── SDK CREDENTIALS SECURITY
│   │   ├── NEVER hardcode
│   │   ├── Default credential provider chain
│   │   │   ├── ~/.aws/credentials
│   │   │   ├── Instance Profile (IAM roles for EC2)
│   │   │   └── Env variables (AWS_ACCESS_KEY_ID, etc.)
│   │   └── 100% IAM Roles within AWS
│   │
│   └── EXPONENTIAL BACKOFF
│       ├── Retry rate-limited APIs
│       └── Built into SDK
│
├── [XII] ADVANCED S3
│   │
│   ├── S3 REPLICATION (CRR & SRR)
│   │   ├── Versioning required source + destination
│   │   ├── CRR → Cross-Region
│   │   ├── SRR → Same-Region
│   │   ├── Can be different accounts
│   │   ├── Asynchronous copying
│   │   ├── Proper IAM permissions for S3
│   │   ├── Use cases
│   │   │   ├── CRR → compliance, latency, cross-account
│   │   │   └── SRR → log aggregation, prod/test
│   │   ├── Only NEW objects replicated (not retroactive)
│   │   ├── DELETE → optional delete marker replication
│   │   ├── NO delete by version ID (prevents malicious)
│   │   └── NO chaining (A→B→C, A not replicated to C)
│   │
│   ├── PRE-SIGNED URLs
│   │   ├── Downloads → CLI
│   │   ├── Uploads → SDK only
│   │   ├── Default 3600s expiration (--expires-in to change)
│   │   ├── Inherit permissions of signer
│   │   └── Use cases
│   │       ├── Premium content
│   │       ├── Dynamic URL lists
│   │       └── Temporary upload access
│   │
│   ├── S3 STORAGE CLASSES
│   │   ├── S3 Standard
│   │   │   ├── General Purpose, 11 9s durability, 99.99% availability
│   │   │   └── 2 facility failures sustained
│   │   ├── S3 Standard-IA
│   │   │   ├── 99.9% availability
│   │   │   ├── Disaster recovery, backups
│   │   │   └── 30 day min duration
│   │   ├── S3 One Zone-IA
│   │   │   ├── Single AZ
│   │   │   ├── 99.5% availability
│   │   │   ├── Secondary backups, recreatable data
│   │   │   └── 30 day min
│   │   ├── S3 Intelligent-Tiering
│   │   │   ├── Auto moves between Access Tiers
│   │   │   ├── Small monitoring fee
│   │   │   └── Multi-AZ
│   │   ├── Glacier
│   │   │   ├── Archive/backup
│   │   │   ├── $0.004/GB/month + retrieval
│   │   │   ├── Archive items (up to 40TB)
│   │   │   ├── Stored in Vaults
│   │   │   └── Retrieval options
│   │   │       ├── Expedited (1-5 min)
│   │   │       ├── Standard (3-5 hr)
│   │   │       └── Bulk (5-12 hr)
│   │   │   └── 90 day min
│   │   └── Glacier Deep Archive
│   │       ├── Standard (12 hr)
│   │       ├── Bulk (48 hr)
│   │       └── 180 day min
│   │
│   ├── LIFECYCLE RULES
│   │   ├── Transition Actions
│   │   │   ├── Move to Standard-IA after N days
│   │   │   └── Move to Glacier for archive
│   │   ├── Expiration Actions
│   │   │   ├── Delete logs after 365 days
│   │   │   ├── Delete old versions
│   │   │   └── Delete incomplete multi-part uploads
│   │   ├── Rules by prefix (s3://mybucket/mp3/*)
│   │   ├── Rules by tags (Department:Finance)
│   │   ├── Scenario 1 → thumbnails + source images
│   │   └── Scenario 2 → versioning + IA + Deep Archive
│   │
│   ├── S3 ANALYTICS
│   │   ├── Storage Class Analysis
│   │   ├── Standard → Standard-IA recommendations
│   │   ├── Does NOT work for One Zone-IA or Glacier
│   │   ├── Daily updates, 24-48 hr to start
│   │   └── First step for Lifecycle Rules
│   │
│   ├── S3 PERFORMANCE
│   │   ├── Baseline → 3,500 PUT/COPY/POST/DELETE per prefix
│   │   ├── Baseline → 5,500 GET/HEAD per prefix
│   │   ├── No prefix limit
│   │   ├── 100-200ms latency
│   │   ├── Spread across 4 prefixes → 22,000 req/sec
│   │   ├── Multi-Part Upload
│   │   │   ├── Recommended >100 MB
│   │   │   ├── Required >5 GB
│   │   │   └── Parallel uploads
│   │   ├── Transfer Acceleration
│   │   │   ├── Via edge location
│   │   │   ├── Compatible with multi-part
│   │   │   └── Fast public www → fast private AWS
│   │   └── Byte-Range Fetches
│   │       ├── Parallelize GETs
│   │       ├── Resilient to failures
│   │       └── Partial data (e.g., file head)
│   │
│   ├── S3 KMS LIMITATION
│   │   ├── Upload → GenerateDataKey API
│   │   ├── Download → Decrypt API
│   │   ├── KMS quota per second (5500/10000/30000)
│   │   └── Request quota increase via Service Quotas
│   │
│   ├── S3 SELECT & GLACIER SELECT
│   │   ├── Server-side SQL filtering
│   │   ├── Filter by rows + columns
│   │   └── Less network/CPU client-side
│   │
│   ├── S3 EVENT NOTIFICATIONS
│   │   ├── Events → ObjectCreated, ObjectRemoved, Restore, Replication
│   │   ├── Filtering (e.g., *.jpg)
│   │   ├── Targets → Lambda, SNS, SQS
│   │   ├── Typically seconds (sometimes minute+)
│   │   ├── Concurrent writes → may only get 1 notification
│   │   └── Enable versioning for guaranteed per-write notifications
│   │
│   ├── S3 REQUESTER PAYS
│   │   ├── Owner pays storage, requester pays request + download
│   │   ├── Use → share large datasets
│   │   └── Requester must be authenticated (not anonymous)
│   │
│   ├── ATHENA
│   │   ├── Serverless SQL on S3
│   │   ├── No loading (queries in place)
│   │   ├── Presto under hood
│   │   ├── Per-query pricing
│   │   ├── Formats → CSV, TSV, JSON, ORC, Avro, Parquet
│   │   └── Use → BI, logs analysis (VPC Flow/ELB/CloudTrail)
│   │
│   ├── GLACIER VAULT LOCK
│   │   ├── WORM (Write Once Read Many)
│   │   ├── Lock policy for future edits
│   │   └── Compliance + retention
│   │
│   ├── S3 OBJECT LOCK (versioning required)
│   │   ├── WORM model
│   │   ├── Block version delete for period
│   │   ├── Retention
│   │   │   ├── Retention Period → fixed
│   │   │   └── Legal Hold → no expiry
│   │   └── Modes
│   │       ├── Governance → users can't override w/o special perms
│   │       └── Compliance → NOBODY can override (even root)
│   │
│   ├── CLOUDFRONT
│   │   ├── CDN, 216 PoPs globally
│   │   ├── Shield + WAF DDoS protection
│   │   ├── HTTPS expose + internal HTTPS backends
│   │   ├── Origins
│   │   │   ├── S3 bucket (+ OAI for security)
│   │   │   ├── Custom Origin (HTTP)
│   │   │   │   ├── ALB, EC2, S3 website
│   │   │   │   └── Any HTTP backend
│   │   │   └── Ingress (upload to S3)
│   │   ├── ALB/EC2 as Origin
│   │   │   ├── ALB → must be PUBLIC
│   │   │   ├── EC2 direct → must be PUBLIC
│   │   │   └── SG → allow CloudFront Edge IPs
│   │   ├── Geo Restriction
│   │   │   ├── Whitelist/Blacklist countries
│   │   │   ├── 3rd party Geo-IP DB
│   │   │   └── Use → copyright laws
│   │   └── vs S3 CRR
│   │       ├── CF → Global Edge, TTL cached, static
│   │       └── CRR → per region setup, near real-time, dynamic
│   │
│   ├── CLOUDFRONT SIGNED URLs / COOKIES
│   │   ├── URL Expiration
│   │   ├── IP ranges
│   │   ├── Trusted signers (accounts)
│   │   ├── Duration
│   │   │   ├── Shared content → short (minutes)
│   │   │   └── Private content → long (years)
│   │   ├── Signed URL → single file
│   │   ├── Signed Cookie → multiple files
│   │   └── vs S3 Pre-Signed URL
│   │       ├── CloudFront → path-based, account-wide key, caching
│   │       └── S3 → IAM key-based, limited lifetime
│   │
│   ├── CLOUDFRONT PRICING
│   │   ├── Edge cost varies globally
│   │   └── Price Classes
│   │       ├── All → best performance
│   │       ├── 200 → excludes most expensive
│   │       └── 100 → only least expensive
│   │
│   ├── CLOUDFRONT MULTIPLE ORIGIN
│   │   ├── Path pattern routing (/api/*, /images/*)
│   │   └── Different origins per content type
│   │
│   ├── CLOUDFRONT ORIGIN GROUPS
│   │   ├── High availability + failover
│   │   ├── Primary + secondary origin
│   │   └── S3 Region-level HA w/ Replication
│   │
│   ├── CLOUDFRONT FIELD-LEVEL ENCRYPTION
│   │   ├── Protect sensitive info through stack
│   │   ├── Extra HTTPS layer
│   │   ├── Edge encryption (close to user)
│   │   ├── Asymmetric encryption
│   │   └── Up to 10 fields in POST requests
│   │
│   ├── AWS GLOBAL ACCELERATOR
│   │   ├── Internal AWS network routing
│   │   ├── 2 Anycast IPs
│   │   ├── Anycast vs Unicast
│   │   │   ├── Unicast → 1 IP per server
│   │   │   └── Anycast → same IP, routed to nearest
│   │   ├── Works with EIP, EC2, ALB, NLB, public/private
│   │   ├── Consistent performance, smart routing
│   │   ├── No client cache issue (IP stable)
│   │   ├── Health Checks <1min failover
│   │   ├── DR friendly
│   │   └── Security → 2 IPs whitelisted, Shield DDoS
│   │
│   ├── GLOBAL ACCELERATOR vs CLOUDFRONT
│   │   ├── Both → edge network + Shield
│   │   ├── CloudFront
│   │   │   ├── Cacheable + dynamic content
│   │   │   ├── Served at edge
│   │   │   └── HTTP-centric
│   │   └── Global Accelerator
│   │       ├── TCP/UDP proxy at edge → Regions
│   │       ├── Non-HTTP (gaming, IoT, VoIP)
│   │       ├── HTTP w/ static IPs
│   │       └── Deterministic fast regional failover
│   │
│   ├── AWS SNOW FAMILY
│   │   ├── Highly secure portable devices
│   │   ├── Data migration
│   │   │   ├── Snowcone, Snowball Edge, Snowmobile
│   │   │   └── Use when network transfer > 1 week
│   │   ├── Edge computing
│   │   │   ├── Snowcone, Snowball Edge
│   │   │   └── Limited/no connectivity
│   │   ├── Snowball Edge (80 TB)
│   │   │   ├── Storage Optimized → 80 TB HDD
│   │   │   ├── Compute Optimized → 42 TB HDD
│   │   │   ├── Per transfer job
│   │   │   └── S3-compatible object + block
│   │   ├── Snowcone (8 TB)
│   │   │   ├── 4.5 lbs, portable
│   │   │   ├── Edge computing + storage + transfer
│   │   │   ├── Provide own battery/cables
│   │   │   └── Ship back OR AWS DataSync online
│   │   ├── Snowmobile (100 PB each)
│   │   │   ├── Exabyte-scale
│   │   │   ├── Temp-controlled, GPS, 24/7 video
│   │   │   └── Better than Snowball >10 PB
│   │   ├── Process
│   │   │   ├── Request → console
│   │   │   ├── Install Snowball client / OpsHub
│   │   │   ├── Connect + copy
│   │   │   ├── Ship back
│   │   │   ├── Data loaded into S3
│   │   │   └── Device wiped
│   │   └── Edge Computing
│   │       ├── Snowcone → 2 CPUs, 4 GB RAM
│   │       ├── Snowball Edge Compute → 52 vCPU, 208 GiB RAM, opt. GPU, 42 TB
│   │       ├── Snowball Edge Storage → 40 vCPU, 80 GiB, 80 TB, clustering
│   │       ├── All → Run EC2 + Lambda (IoT Greengrass)
│   │       └── 1/3 year discounted pricing
│   │
│   ├── AWS OPSHUB
│   │   ├── GUI for Snow Family (replaces CLI)
│   │   ├── Unlock/configure single/cluster
│   │   ├── Transfer files
│   │   ├── Manage EC2 on devices
│   │   ├── Monitor metrics
│   │   └── Launch AWS services (EC2, DataSync, NFS)
│   │
│   ├── SNOWBALL INTO GLACIER
│   │   ├── Snowball CANNOT import to Glacier directly
│   │   └── Must → S3 first → Lifecycle Policy to Glacier
│   │
│   └── HYBRID CLOUD FOR STORAGE
│       ├── AWS Storage Gateway (S3 proprietary → on-prem)
│       ├── Cloud Native Storage
│       │   ├── Block → EBS, EC2 Instance Store
│       │   ├── File → EFS, FSx
│       │   └── Object → S3, Glacier
│       ├── 3 Types of Storage Gateway
│       │   ├── File Gateway
│       │   │   ├── S3 via NFS/SMB
│       │   │   ├── Supports Standard, IA, One Zone-IA
│       │   │   ├── IAM roles per gateway
│       │   │   ├── MRU cached
│       │   │   ├── Multi-server mount
│       │   │   └── Active Directory integration
│       │   ├── Volume Gateway
│       │   │   ├── Block storage via iSCSI backed by S3
│       │   │   ├── EBS snapshots for restore
│       │   │   ├── Cached → low-latency recent data
│       │   │   └── Stored → entire dataset on-prem, scheduled S3 backup
│       │   └── Tape Gateway
│       │       ├── Virtual Tape Library backed by S3+Glacier
│       │       ├── Use existing tape backup processes
│       │       └── iSCSI interface, tape software compatible
│       └── Hardware Appliance
│           ├── For no on-prem virtualization
│           ├── Buy on amazon.com
│           ├── Works with all 3 gateways
│           └── Small DC daily NFS backups
│
├── [XII-b] AMAZON FSx
│   │
│   ├── FSx FOR WINDOWS (File Server)
│   │   ├── Managed Windows file share drive
│   │   ├── SMB + NTFS
│   │   ├── Active Directory + ACLs + user quotas
│   │   ├── SSD, 10s GB/s, millions IOPS, 100s PB
│   │   ├── On-prem accessible
│   │   ├── Multi-AZ optional
│   │   └── Daily S3 backups
│   │
│   ├── FSx FOR LUSTRE
│   │   ├── Parallel distributed FS, large-scale compute
│   │   ├── "Linux" + "cluster"
│   │   ├── Use → ML, HPC, video, financial, EDA
│   │   ├── 100s GB/s, millions IOPS, sub-ms latency
│   │   ├── S3 seamless integration (read + write)
│   │   └── On-prem accessible
│   │
│   └── DEPLOYMENT OPTIONS
│       ├── Scratch File System
│       │   ├── Temporary
│       │   ├── No replication (data lost on fail)
│       │   ├── 6x faster (200MBps per TiB burst)
│       │   └── Short-term, cost-optimized
│       └── Persistent File System
│           ├── Long-term
│           ├── Same-AZ replicated
│           ├── Failed files replaced within minutes
│           └── Long-term, sensitive data
│
├── [XII-c] AWS TRANSFER FAMILY
│   ├── Fully managed FTP transfers → S3 / EFS
│   ├── Protocols
│   │   ├── SFTP
│   │   ├── FTPS
│   │   └── FTP (VPC ONLY)
│   ├── Multi-AZ, scalable
│   ├── Per endpoint-hour + data transfer pricing
│   ├── Auth → built-in OR AD, LDAP, Okta, Cognito, custom
│   └── Use → file sharing, public datasets, CRM, ERP
│
├── [XII-d] STORAGE COMPARISON
│   ├── S3 → object
│   ├── Glacier → object archival
│   ├── EFS → NFS for Linux, POSIX
│   ├── FSx Windows → NFS for Windows
│   ├── FSx Lustre → HPC Linux
│   ├── EBS → single EC2 network storage
│   ├── Instance Store → physical, high IOPS
│   ├── Storage Gateway → File/Volume/Tape
│   ├── Snowball/Snowmobile → physical migration
│   └── Database → indexed/queried
│
├── [XIII] INTEGRATION & MESSAGING (SQS/SNS/Kinesis)
│   │
│   ├── COMMUNICATION PATTERNS
│   │   ├── Synchronous (app → app)
│   │   └── Asynchronous (app → queue → app)
│   │       └── Decouple for spikes + independent scaling
│   │
│   ├── SQS OVERVIEW
│   │   ├── Oldest offering (10+ years)
│   │   ├── Managed, decoupling
│   │   ├── Standard Queue
│   │   │   ├── Unlimited throughput + messages
│   │   │   ├── Retention → default 4 days, max 14
│   │   │   ├── Low latency (<10ms)
│   │   │   ├── Max 256KB/message
│   │   │   ├── Duplicates possible (at-least-once)
│   │   │   └── Best-effort ordering
│   │   ├── Producing → SendMessage API
│   │   ├── Consuming → poll (up to 10), DeleteMessage
│   │   └── Scale → horizontal consumers
│   │
│   ├── SQS + ASG
│   │   ├── Metric → ApproximateNumberOfMessages
│   │   ├── CW Alarm on metric
│   │   └── ASG scales
│   │
│   ├── SQS SECURITY
│   │   ├── In-flight → HTTPS
│   │   ├── At-rest → KMS
│   │   ├── Client-side encryption
│   │   ├── IAM for API
│   │   └── SQS Access Policies (S3-like)
│   │       ├── Cross-account
│   │       └── Allow other services (SNS, S3) to write
│   │
│   ├── SQS VISIBILITY TIMEOUT
│   │   ├── Default 30 seconds
│   │   ├── Message invisible to others during timeout
│   │   ├── Not processed in time → reappears
│   │   ├── ChangeMessageVisibility API → more time
│   │   ├── High → long reprocess on crash
│   │   └── Low → duplicates likely
│   │
│   ├── SQS DEAD LETTER QUEUE (DLQ)
│   │   ├── MaximumReceives threshold
│   │   ├── Failed messages → DLQ
│   │   ├── Debugging
│   │   └── Set 14-day DLQ retention
│   │
│   ├── SQS DELAY QUEUE
│   │   ├── Delay up to 15 min
│   │   ├── Default 0 seconds
│   │   ├── Queue-level default OR per-message DelaySeconds
│   │
│   ├── SQS REQUEST-RESPONSE
│   │   ├── SQS Temporary Queue Client
│   │   └── Virtual queues (cost-effective)
│   │
│   ├── SQS FIFO QUEUE
│   │   ├── First In First Out ordering
│   │   ├── 300 msg/s without batch, 3000 w/ batch
│   │   ├── Exactly-once send (deduplication)
│   │   └── In-order processing
│   │
│   ├── SNS OVERVIEW
│   │   ├── One message → many receivers (pub/sub)
│   │   ├── Producer → topic only
│   │   ├── Subscribers → SQS, HTTP(S), Lambda, Email, SMS, Mobile
│   │   ├── Up to 10M subs/topic, 100K topics
│   │   └── Integrated → CloudWatch, ASG, S3, CloudFormation
│   │
│   ├── SNS PUBLISH
│   │   ├── Topic Publish (SDK) → topic → subscriptions
│   │   └── Direct Publish (mobile) → platform app → endpoint
│   │       └── GCM, APNS, ADM
│   │
│   ├── SNS SECURITY → same as SQS (HTTPS, KMS, IAM, Access Policies)
│   │
│   ├── SNS + SQS FAN OUT
│   │   ├── Push to SNS → receive in all SQS
│   │   ├── Fully decoupled, no data loss
│   │   ├── SQS persistence, delayed processing, retries
│   │   └── Make sure SQS policy allows SNS writes
│   │
│   ├── S3 EVENTS TO MULTIPLE QUEUES
│   │   ├── Same event type + prefix → only 1 S3 rule
│   │   └── Use SNS fan-out to many SQS
│   │
│   ├── SNS FIFO TOPIC
│   │   ├── Ordering by Message Group ID
│   │   ├── Deduplication ID or Content-Based
│   │   ├── ONLY SQS FIFO subscribers
│   │   └── Limited throughput (same as SQS FIFO)
│   │
│   ├── SNS MESSAGE FILTERING
│   │   ├── JSON policy per subscription
│   │   └── Without policy → receive every message
│   │
│   ├── KINESIS OVERVIEW
│   │   ├── Real-time streaming
│   │   ├── Use → app logs, metrics, clickstream, IoT
│   │   ├── Kinesis Data Streams → capture/process/store
│   │   ├── Kinesis Data Firehose → load to stores
│   │   ├── Kinesis Data Analytics → SQL/Flink analysis
│   │   └── Kinesis Video Streams → video streams
│   │
│   ├── KINESIS DATA STREAMS
│   │   ├── Shards architecture
│   │   ├── Billing → per shard provisioned
│   │   ├── Retention 1-365 days
│   │   ├── Replay capability
│   │   ├── Immutable
│   │   ├── Same partition → same shard (ordering)
│   │   ├── Producers → SDK, KPL, Kinesis Agent
│   │   ├── Consumers → KCL+SDK, Lambda, Firehose, Analytics
│   │   ├── Per shard
│   │   │   ├── 1 MB/s in OR 1000 msg/s
│   │   │   ├── 2 MB/s out (shared) all consumers
│   │   │   └── 2 MB/s out (enhanced) per consumer
│   │   └── Message size up to 1 MB
│   │
│   ├── KINESIS DATA FIREHOSE
│   │   ├── Fully managed, auto-scaling, serverless
│   │   ├── Destinations
│   │   │   ├── AWS → S3, Redshift (via S3), ElasticSearch
│   │   │   ├── 3rd party → Splunk, MongoDB, DataDog, NewRelic
│   │   │   └── Custom HTTP
│   │   ├── Pay per data through
│   │   ├── Near real-time → 60s min non-full, or 32 MB
│   │   ├── Formats/conversions/transforms/compression
│   │   ├── Lambda transforms
│   │   └── Failed/all → backup S3 bucket
│   │
│   ├── DATA STREAMS vs FIREHOSE
│   │   ├── Data Streams
│   │   │   ├── Custom consumer/producer
│   │   │   ├── Real-time (~200ms)
│   │   │   ├── Manual scaling (shards)
│   │   │   ├── 1-365 day storage
│   │   │   └── Replay support
│   │   └── Firehose
│   │       ├── Load to S3/Redshift/ES/3rd party/HTTP
│   │       ├── Near real-time (60s+ buffer)
│   │       ├── Auto-scaling
│   │       ├── No storage
│   │       └── No replay
│   │
│   ├── KINESIS DATA ANALYTICS (SQL)
│   │   ├── Real-time SQL on streams
│   │   ├── Fully managed, serverless
│   │   ├── Auto-scaling
│   │   ├── Pay per consumption
│   │   ├── Create streams from queries
│   │   └── Use → time-series, dashboards, metrics
│   │
│   ├── ORDERING IN KINESIS
│   │   ├── Use Partition Key (e.g., truck_id)
│   │   ├── Same key → same shard
│   │   └── Order preserved per shard
│   │
│   ├── ORDERING IN SQS
│   │   ├── Standard → no order
│   │   ├── FIFO without Group ID → single consumer, in-order
│   │   └── FIFO with Group ID → parallel with related grouping
│   │
│   ├── KINESIS vs SQS ORDERING
│   │   ├── Kinesis 5 shards, 100 trucks → 5 parallel consumers, 5 MB/s
│   │   └── SQS FIFO with 100 group IDs → 100 consumers, 300/3000 msg/s
│   │
│   ├── SQS vs SNS vs KINESIS
│   │   ├── SQS
│   │   │   ├── Pull data, consumer deletes
│   │   │   ├── Unlimited workers
│   │   │   ├── No throughput provisioning
│   │   │   ├── Only FIFO orders
│   │   │   └── Individual delay
│   │   ├── SNS
│   │   │   ├── Push data
│   │   │   ├── Up to 12.5M subs, 100K topics
│   │   │   ├── Not persisted (if not delivered)
│   │   │   ├── Pub/Sub
│   │   │   ├── No throughput provisioning
│   │   │   ├── Fan-out w/ SQS
│   │   │   └── FIFO via SQS FIFO
│   │   └── Kinesis
│   │       ├── Standard: pull, 2 MB/shard
│   │       ├── Enhanced-fanout: push, 2 MB/shard/consumer
│   │       ├── Replay possible
│   │       ├── Real-time big data/analytics/ETL
│   │       ├── Shard-level ordering
│   │       ├── X-day expiry
│   │       └── Must provision throughput
│   │
│   └── AMAZON MQ
│       ├── Managed Apache ActiveMQ
│       ├── For traditional protocols → MQTT, AMQP, STOMP, Openwire, WSS
│       ├── Doesn't scale like SQS/SNS
│       ├── Dedicated machine, HA + failover
│       ├── Has queue (~SQS) + topic (~SNS)
│       └── HA → Active/Standby via EFS storage
│
├── [XIV] CONTAINERS (ECS, EKS, Fargate)
│   │
│   ├── DOCKER OVERVIEW
│   │   ├── Software platform to deploy apps in containers
│   │   ├── Benefits
│   │   │   ├── Run on any OS/machine
│   │   │   ├── No compatibility issues
│   │   │   ├── Predictable behavior
│   │   │   ├── Easier maintenance + deployment
│   │   │   └── Any language/OS/tech
│   │   └── Docker Repositories
│   │       ├── Public → Docker Hub (hub.docker.com)
│   │       ├── Private → Amazon ECR
│   │       └── Public → Amazon ECR Public
│   │
│   ├── DOCKER vs VMs
│   │   ├── Docker → shared host OS, many containers on one server
│   │   └── VMs → guest OS per VM via hypervisor
│   │
│   ├── DOCKER PRIMER FLOW
│   │   ├── Dockerfile → build → Docker Image
│   │   ├── Push/Pull to Docker Repository
│   │   └── Run Image → Docker Container
│   │
│   ├── CONTAINER MANAGEMENT CHOICES
│   │   ├── ECS → AWS container platform
│   │   ├── Fargate → AWS Serverless container platform
│   │   └── EKS → AWS managed Kubernetes
│   │
│   ├── ECS (Elastic Container Service)
│   │   ├── Launch Docker containers on AWS
│   │   ├── YOU provision + maintain EC2 infra
│   │   ├── AWS starts/stops containers
│   │   └── ALB integrations
│   │
│   ├── EC2 LAUNCH TYPE (ECS)
│   │   ├── ECS Agent on EC2 (container instance)
│   │   ├── ASG of container instances
│   │   └── Mix instance types (m5.xlarge, t2.small)
│   │
│   ├── FARGATE
│   │   ├── Launch containers, NO EC2 management
│   │   ├── Serverless
│   │   └── Pay per CPU/RAM needed
│   │
│   ├── FARGATE LAUNCH TYPE (ECS)
│   │   ├── Task → ENI (has IP)
│   │   └── Runs across AZs
│   │
│   ├── IAM ROLES FOR ECS TASKS
│   │   ├── EC2 Instance Profile (for ECS agent)
│   │   │   ├── ECS API calls
│   │   │   ├── CloudWatch Logs
│   │   │   ├── Pull from ECR
│   │   │   └── Secrets Manager / SSM
│   │   └── ECS Task Role
│   │       ├── Per-task role
│   │       ├── Different roles per service
│   │       └── Defined in task definition
│   │
│   ├── ECS DATA VOLUMES – EFS
│   │   ├── Works for EC2 + Fargate tasks
│   │   ├── Mount EFS onto tasks
│   │   ├── Tasks in any AZ share data
│   │   ├── Fargate + EFS = serverless + persistent storage
│   │   └── Use → multi-AZ shared storage for containers
│   │
│   ├── ECS SERVICES & TASKS
│   │   ├── Service runs tasks on container instances
│   │   └── ALB fronts services
│   │
│   ├── LOAD BALANCING FOR EC2 LAUNCH
│   │   ├── Dynamic port mapping
│   │   ├── ALB finds correct port
│   │   └── SG → allow any port from ALB SG
│   │
│   ├── LOAD BALANCING FOR FARGATE
│   │   ├── Each task → unique IP
│   │   └── SG on ENI → allow task port from ALB SG
│   │
│   ├── ECS TASK INVOCATION
│   │   └── EventBridge rule → Run ECS Task (e.g., S3 upload → process → DynamoDB)
│   │
│   ├── ECS SCALING
│   │   ├── Service CPU Usage
│   │   │   ├── CW Metric → Alarm → ECS Capacity Providers
│   │   │   └── ASG scales
│   │   └── SQS Queue Example
│   │       ├── Queue Length metric → Alarm
│   │       └── Scale ECS + ASG
│   │
│   ├── ECS ROLLING UPDATES
│   │   ├── Minimum Healthy Percent (0-100%)
│   │   ├── Maximum Percent (100-200%)
│   │   ├── Min 50%, Max 100% → terminate first
│   │   └── Min 100%, Max 150% → create first, then terminate
│   │
│   ├── AMAZON ECR
│   │   ├── Store/manage/deploy containers
│   │   ├── Pay for what you use
│   │   ├── Integrated with ECS + IAM
│   │   ├── Backed by S3
│   │   └── Image vulnerability scanning + versioning + tags + lifecycle
│   │
│   └── AMAZON EKS
│       ├── Managed Kubernetes on AWS
│       ├── Alternative to ECS (K8s API)
│       ├── Workers → EC2 or Fargate
│       ├── Use → existing K8s workloads migrating to AWS
│       └── Cloud-agnostic (Azure, GCP)
│
├── [XV] SERVERLESS OVERVIEW
│   │
│   ├── WHAT IS SERVERLESS
│   │   ├── Developers don't manage servers
│   │   ├── Initially → FaaS (Lambda pioneered)
│   │   ├── Now includes → DBs, messaging, storage
│   │   └── Servers exist, you just don't manage them
│   │
│   ├── SERVERLESS IN AWS
│   │   ├── AWS Lambda
│   │   ├── DynamoDB
│   │   ├── AWS Cognito
│   │   ├── API Gateway
│   │   ├── S3
│   │   ├── SNS & SQS
│   │   ├── Kinesis Data Firehose
│   │   ├── Aurora Serverless
│   │   ├── Step Functions
│   │   └── Fargate
│   │
│   ├── LAMBDA vs EC2
│   │   ├── EC2 → virtual servers, RAM/CPU limited, continuous, manual scaling
│   │   └── Lambda → virtual functions, short executions, on-demand, auto-scaled
│   │
│   ├── LAMBDA BENEFITS
│   │   ├── Pay per request + compute time
│   │   ├── Free tier → 1M requests + 400K GB-seconds
│   │   ├── Integrated with AWS services
│   │   ├── Many languages supported
│   │   ├── CloudWatch monitoring
│   │   ├── Up to 10GB RAM per function
│   │   └── More RAM → better CPU + network
│   │
│   ├── LAMBDA LANGUAGES
│   │   ├── Node.js (JavaScript)
│   │   ├── Python
│   │   ├── Java (Java 8)
│   │   ├── C# (.NET Core)
│   │   ├── Golang
│   │   ├── C# / PowerShell
│   │   ├── Ruby
│   │   ├── Custom Runtime API (e.g., Rust)
│   │   └── Lambda Container Image
│   │       ├── Must implement Lambda Runtime API
│   │       └── ECS/Fargate preferred for arbitrary Docker
│   │
│   ├── LAMBDA INTEGRATIONS
│   │   ├── API Gateway
│   │   ├── Kinesis
│   │   ├── DynamoDB
│   │   ├── S3
│   │   ├── CloudFront
│   │   ├── CloudWatch Events / EventBridge
│   │   ├── CloudWatch Logs
│   │   ├── SNS
│   │   ├── SQS
│   │   └── Cognito
│   │
│   ├── EXAMPLES
│   │   ├── Serverless Thumbnail → S3 → Lambda → Thumbnail + DynamoDB
│   │   └── Serverless CRON → EventBridge every hour → Lambda
│   │
│   ├── LAMBDA PRICING
│   │   ├── Per calls → first 1M free, $0.20/1M after
│   │   ├── Per duration (1ms increments)
│   │   ├── 400,000 GB-seconds free
│   │   │   ├── 400K seconds @ 1 GB
│   │   │   └── 3.2M seconds @ 128 MB
│   │   └── $1.00 / 600K GB-seconds after
│   │
│   ├── LAMBDA LIMITS (per region)
│   │   ├── Execution
│   │   │   ├── RAM → 128 MB - 10 GB (1 MB increments)
│   │   │   ├── Max execution → 900s (15 min)
│   │   │   ├── Env variables → 4 KB
│   │   │   ├── /tmp disk → 512 MB
│   │   │   └── Concurrency → 1000 (expandable)
│   │   └── Deployment
│   │       ├── Compressed .zip → 50 MB
│   │       ├── Uncompressed → 250 MB
│   │       ├── /tmp for startup loads
│   │       └── Env vars → 4 KB
│   │
│   ├── LAMBDA@EDGE
│   │   ├── Lambda alongside CloudFront CDN
│   │   ├── Global deployment
│   │   ├── Customize CDN content
│   │   ├── Request filtering
│   │   ├── 4 event points
│   │   │   ├── Viewer Request (before CF receives)
│   │   │   ├── Origin Request (before CF forwards)
│   │   │   ├── Origin Response (after CF receives from origin)
│   │   │   └── Viewer Response (before CF forwards to viewer)
│   │   ├── Can generate responses without hitting origin
│   │   └── Use Cases
│   │       ├── Website security + privacy
│   │       ├── Dynamic web app at edge
│   │       ├── SEO
│   │       ├── Route across origins/DCs
│   │       ├── Bot mitigation
│   │       ├── Real-time image transformation
│   │       ├── A/B testing
│   │       ├── Auth & authorization
│   │       ├── User prioritization
│   │       └── User tracking + analytics
│   │
│   ├── DYNAMODB
│   │   ├── Fully managed, HA (multi-AZ replication)
│   │   ├── NoSQL (not relational)
│   │   ├── Massive scale → millions req/s, trillions rows, 100s TB
│   │   ├── Fast + consistent low-latency
│   │   ├── IAM integrated
│   │   ├── DynamoDB Streams → event-driven
│   │   └── Low cost + auto-scaling
│   │
│   ├── DYNAMODB BASICS
│   │   ├── Tables with Primary Key (at creation)
│   │   ├── Infinite items (rows)
│   │   ├── Attributes (columns) can be added over time (can be null)
│   │   ├── Max item size → 400 KB
│   │   └── Data types
│   │       ├── Scalar → String, Number, Binary, Boolean, Null
│   │       ├── Document → List, Map
│   │       └── Set → String Set, Number Set, Binary Set
│   │
│   ├── DYNAMODB TABLE EXAMPLE
│   │   ├── Partition Key (e.g., User_ID)
│   │   ├── Sort Key (e.g., Game_ID)
│   │   └── Attributes (Score, Result)
│   │
│   ├── READ/WRITE CAPACITY MODES
│   │   ├── Provisioned (default)
│   │   │   ├── Specify RCU + WCU per sec
│   │   │   ├── Plan capacity
│   │   │   └── Optional auto-scaling
│   │   └── On-Demand
│   │       ├── Auto-scale with workload
│   │       ├── No planning
│   │       ├── More expensive ($$$)
│   │       └── Unpredictable workloads
│   │
│   ├── DYNAMODB ACCELERATOR (DAX)
│   │   ├── Fully-managed in-memory cache
│   │   ├── Solve read congestion
│   │   ├── Microseconds latency for cached
│   │   ├── No app logic changes (DynamoDB API compatible)
│   │   └── 5 min TTL default
│   │
│   ├── DAX vs ELASTICACHE
│   │   ├── DAX → individual objects cache, query/scan cache
│   │   └── ElastiCache → store aggregation results
│   │
│   ├── DYNAMODB STREAMS
│   │   ├── Ordered item-level modifications (create/update/delete)
│   │   ├── Stream records → Kinesis Data Streams, Lambda, KCL apps
│   │   ├── Retention → 24 hours
│   │   └── Use Cases
│   │       ├── React in real-time (welcome emails)
│   │       ├── Analytics
│   │       ├── Derivative tables
│   │       ├── ElasticSearch insert
│   │       └── Cross-region replication
│   │
│   ├── DYNAMODB GLOBAL TABLES
│   │   ├── Multi-region low latency access
│   │   ├── Active-Active replication
│   │   ├── Read + write in any region
│   │   └── DynamoDB Streams prerequisite
│   │
│   ├── DYNAMODB TTL
│   │   ├── Auto-delete items after expiry timestamp
│   │   └── Use → reduce data, regulatory compliance
│   │
│   ├── DYNAMODB INDEXES
│   │   ├── Global Secondary Indexes (GSI)
│   │   ├── Local Secondary Indexes (LSI)
│   │   └── Query on attributes other than Primary Key
│   │
│   ├── DYNAMODB TRANSACTIONS
│   │   └── All-or-none writes across tables
│   │
│   ├── API GATEWAY
│   │   ├── Lambda + API Gateway = no infra
│   │   ├── WebSocket support
│   │   ├── API versioning (v1, v2)
│   │   ├── Multiple environments (dev, test, prod)
│   │   ├── Security → auth + authorization
│   │   ├── API keys + throttling
│   │   ├── Swagger / Open API import
│   │   ├── Transform + validate req/resp
│   │   ├── Generate SDK + specs
│   │   └── Cache API responses
│   │
│   ├── API GATEWAY INTEGRATIONS
│   │   ├── Lambda Function → REST API backed by Lambda
│   │   ├── HTTP → ALB, on-prem HTTP API
│   │   │   └── Add rate limiting, caching, auth, API keys
│   │   └── AWS Service → Step Functions, SQS
│   │       └── Add auth, deploy publicly, rate control
│   │
│   ├── API GATEWAY ENDPOINT TYPES
│   │   ├── Edge-Optimized (default)
│   │   │   ├── Global clients
│   │   │   ├── Via CloudFront Edge locations
│   │   │   └── API Gateway in one region
│   │   ├── Regional
│   │   │   ├── Same-region clients
│   │   │   └── Combine with CloudFront manually
│   │   └── Private
│   │       ├── VPC only via Interface VPC Endpoint (ENI)
│   │       └── Resource policy for access
│   │
│   ├── API GATEWAY SECURITY
│   │   ├── IAM Permissions
│   │   │   ├── IAM policy on User/Role
│   │   │   ├── Sig v4 in headers
│   │   │   └── Good for internal infra
│   │   ├── Lambda Authorizer (Custom)
│   │   │   ├── Lambda validates token
│   │   │   ├── Cacheable
│   │   │   ├── OAuth/SAML/3rd party
│   │   │   └── Returns IAM policy
│   │   └── Cognito User Pools
│   │       ├── Cognito manages user lifecycle
│   │       ├── API Gateway auto-verifies
│   │       ├── No custom code
│   │       └── Only auth (not authz)
│   │
│   ├── API GATEWAY SECURITY SUMMARY
│   │   ├── IAM → internal users/roles, auth+authz, Sig v4
│   │   ├── Custom Authorizer → 3rd party tokens, flexible IAM policy
│   │   └── Cognito → own user pool, no custom code, backend does authz
│   │
│   ├── AWS COGNITO
│   │   ├── User Pools (CUP)
│   │   │   ├── Sign in for app users
│   │   │   ├── API Gateway integration
│   │   │   ├── Username/email + password
│   │   │   ├── Email/phone verification + MFA
│   │   │   ├── Federated Identities (Facebook, Google, SAML)
│   │   │   └── Returns JWT
│   │   ├── Identity Pools (Federated)
│   │   │   ├── AWS credentials for direct resource access
│   │   │   ├── Integrates with CUP
│   │   │   ├── Login → federated provider OR anonymous
│   │   │   ├── Get temp AWS creds
│   │   │   ├── Pre-defined IAM policy
│   │   │   └── Example → S3 write via Facebook login
│   │   └── Cognito Sync
│   │       ├── Sync data device → Cognito
│   │       ├── May be deprecated (AppSync replacement)
│   │       ├── Cross-device sync
│   │       ├── Offline capability
│   │       ├── Requires Federated Identity Pool
│   │       ├── Datasets up to 1 MB
│   │       └── Up to 20 datasets
│   │
│   └── AWS SAM
│       ├── Serverless Application Model
│       ├── YAML config for serverless apps
│       │   ├── Lambda Functions
│       │   ├── DynamoDB tables
│       │   ├── API Gateway
│       │   └── Cognito User Pools
│       ├── Run Lambda/API GW/DynamoDB locally
│       └── CodeDeploy for Lambda deployment
│
├── [XVI] SERVERLESS ARCHITECTURES
│   │
│   ├── MOBILE APP (MyTodoList)
│   │   ├── REST API → API Gateway + Lambda + DynamoDB
│   │   ├── Auth → Cognito
│   │   ├── S3 access via temp creds (STS)
│   │   ├── High read throughput → DAX
│   │   └── API caching → API Gateway level
│   │
│   ├── SERVERLESS WEBSITE (MyBlog.com)
│   │   ├── Static content → CloudFront + S3 + OAI
│   │   ├── REST API → API Gateway + Lambda + DynamoDB + DAX
│   │   ├── Global Tables for multi-region
│   │   ├── Welcome email flow
│   │   │   └── DynamoDB Stream → Lambda → SES
│   │   └── Thumbnail generation
│   │       └── S3 → SNS → SQS → Lambda → thumbnails
│   │
│   ├── MICRO SERVICES ARCHITECTURE
│   │   ├── Many services interact via REST API
│   │   ├── Each service has own architecture
│   │   ├── Leaner dev lifecycle
│   │   ├── Synchronous → API Gateway, LB
│   │   ├── Asynchronous → SQS, Kinesis, SNS, Lambda
│   │   └── Challenges (solved by serverless)
│   │       ├── Overhead per service
│   │       ├── Server density optimization
│   │       ├── Multiple versions
│   │       └── Client SDK complexity
│   │
│   ├── DISTRIBUTING PAID CONTENT
│   │   ├── Serverless → Cognito + DynamoDB (premium users) + CloudFront + S3
│   │   ├── CloudFront Signed URL for premium content
│   │   ├── S3 Pre-Signed not efficient globally
│   │   └── Flow
│   │       ├── Cognito auth
│   │       ├── Check premium status
│   │       └── Generate CloudFront Signed URL (5 min)
│   │
│   ├── SOFTWARE UPDATES OFFLOADING
│   │   ├── Problem → EC2 distributing updates costly
│   │   ├── Solution → CloudFront in front
│   │   ├── Benefits
│   │   │   ├── No architecture changes
│   │   │   ├── Files cached at edge
│   │   │   ├── ASG doesn't need to scale as much
│   │   │   └── Save on EC2, bandwidth, availability
│   │
│   └── BIG DATA INGESTION PIPELINE
│       ├── Requirements → fully serverless, real-time, SQL queries, S3 reports, warehouse
│       ├── Flow
│       │   ├── IoT Core → Kinesis Data Streams
│       │   ├── Firehose → S3 (Ingestion Bucket)
│       │   ├── Lambda transforms data
│       │   ├── S3 → SQS (optional)
│       │   ├── Lambda → Athena (SQL)
│       │   ├── Athena outputs → S3 (Reporting Bucket)
│       │   └── QuickSight or Redshift for dashboards
│       └── Components
│           ├── IoT Core → harvest IoT data
│           ├── Kinesis → real-time collection
│           ├── Firehose → near real-time delivery (1 min)
│           ├── Lambda → transforms + triggers
│           ├── S3 → event notifications
│           ├── Athena → serverless SQL
│           └── QuickSight/Redshift → BI
│
├── [XVII] DATABASES
│   │
│   ├── CHOOSING THE RIGHT DATABASE
│   │   ├── Read-heavy / write-heavy / balanced?
│   │   ├── Data volume + growth + object size?
│   │   ├── Durability + source of truth?
│   │   ├── Latency + concurrent users?
│   │   ├── Data model + joins + schema?
│   │   ├── Reporting + search + RDBMS/NoSQL?
│   │   └── License costs + Cloud Native migration?
│   │
│   ├── DATABASE TYPES
│   │   ├── RDBMS (SQL/OLTP) → RDS, Aurora → joins
│   │   ├── NoSQL → DynamoDB, ElastiCache, Neptune → no joins/SQL
│   │   ├── Object Store → S3, Glacier
│   │   ├── Data Warehouse (SQL/BI) → Redshift (OLAP), Athena
│   │   ├── Search → ElasticSearch (JSON)
│   │   └── Graphs → Neptune
│   │
│   ├── RDS (for SA perspective)
│   │   ├── Ops → small downtime (failover, maint), manual scaling
│   │   ├── Security → AWS=OS, YOU=KMS/SG/IAM/SSL
│   │   ├── Reliability → Multi-AZ
│   │   ├── Performance → depends on EC2+EBS, Read Replicas, storage auto-scale
│   │   └── Cost → per hour EC2+EBS
│   │
│   ├── AURORA (for SA)
│   │   ├── Ops → less ops, auto-scaling storage
│   │   ├── Security → same as RDS
│   │   ├── Reliability → Multi-AZ, Serverless, Multi-Master options
│   │   ├── Performance → 5x, up to 15 Read Replicas
│   │   └── Cost → per hour EC2+storage, cheaper than enterprise DBs
│   │
│   ├── ELASTICACHE (for SA)
│   │   ├── Ops → similar to RDS
│   │   ├── Security → KMS, SG, IAM, Redis Auth, SSL
│   │   ├── Reliability → Clustering, Multi-AZ
│   │   ├── Performance → sub-ms, in-memory, read replica sharding
│   │   └── Cost → per hour EC2+storage
│   │
│   ├── DYNAMODB (for SA)
│   │   ├── Ops → no ops, serverless, auto-scaling
│   │   ├── Security → IAM policies, KMS, SSL
│   │   ├── Reliability → Multi-AZ, backups
│   │   ├── Performance → single-digit ms, DAX caching
│   │   └── Cost → per provisioned capacity + storage
│   │
│   ├── S3 (for SA)
│   │   ├── Key/value object store
│   │   ├── Big objects, not small
│   │   ├── Serverless, infinite scale, max 5 TB
│   │   ├── Strong consistency
│   │   ├── Tiers + features
│   │   └── Security → IAM, Bucket Policy, ACL, encryption
│   │
│   ├── ATHENA (for SA)
│   │   ├── Fully serverless SQL
│   │   ├── Query S3 data
│   │   ├── Pay per query, output to S3
│   │   ├── IAM security
│   │   └── Use → one-time SQL, serverless S3 queries, log analytics
│   │
│   ├── REDSHIFT OVERVIEW
│   │   ├── Based on PostgreSQL
│   │   ├── NOT OLTP → OLAP (analytics + warehousing)
│   │   ├── 10x better perf vs others
│   │   ├── Scales to PBs
│   │   ├── Columnar storage
│   │   ├── Massively Parallel Query (MPP)
│   │   ├── Pay per provisioned instance
│   │   ├── SQL interface
│   │   ├── BI tools → QuickSight, Tableau
│   │   ├── Data sources → S3, DynamoDB, DMS, other DBs
│   │   ├── 1-128 nodes, up to 128 TB/node
│   │   ├── Leader node → plans queries
│   │   ├── Compute nodes → perform queries
│   │   ├── Redshift Spectrum → query S3 directly
│   │   ├── Backup + Restore, VPC/IAM/KMS security, monitoring
│   │   └── Enhanced VPC Routing → COPY/UNLOAD via VPC
│   │
│   ├── REDSHIFT SNAPSHOTS & DR
│   │   ├── NO Multi-AZ mode
│   │   ├── Snapshots → PIT backups in S3
│   │   ├── Incremental
│   │   ├── Restore → new cluster
│   │   ├── Automated → every 8 hrs / 5 GB / schedule
│   │   ├── Manual → retained until deleted
│   │   └── Cross-region snapshot copy
│   │
│   ├── LOADING DATA INTO REDSHIFT
│   │   ├── Firehose → Redshift (via S3 COPY)
│   │   ├── S3 COPY command
│   │   ├── EC2 JDBC driver (batch)
│   │   └── Enhanced VPC Routing → through VPC
│   │
│   ├── REDSHIFT SPECTRUM
│   │   ├── Query S3 without loading
│   │   ├── Must have Redshift cluster
│   │   └── Query → thousands of Spectrum nodes
│   │
│   ├── REDSHIFT (for SA)
│   │   ├── Ops → like RDS
│   │   ├── Security → IAM, VPC, KMS, SSL
│   │   ├── Reliability → auto-healing, cross-region snapshot
│   │   ├── Performance → 10x, compression
│   │   ├── Cost → per node, 1/10 vs other warehouses
│   │   ├── vs Athena → faster joins/aggregations (indexes)
│   │   └── Redshift = Analytics/BI/Warehouse
│   │
│   ├── AWS GLUE
│   │   ├── Managed ETL
│   │   ├── Prep + transform data for analytics
│   │   └── Fully serverless
│   │
│   ├── GLUE DATA CATALOG
│   │   ├── Catalog of datasets
│   │   ├── Crawler writes metadata
│   │   └── Used by Athena, Redshift Spectrum, EMR
│   │
│   ├── NEPTUNE
│   │   ├── Fully managed graph database
│   │   ├── Use → high-relationship data
│   │   │   ├── Social networking
│   │   │   └── Knowledge graphs (Wikipedia)
│   │   ├── HA across 3 AZ, up to 15 read replicas
│   │   ├── PITR + continuous S3 backup
│   │   └── KMS + HTTPS
│   │
│   ├── NEPTUNE (for SA)
│   │   ├── Ops → similar to RDS
│   │   ├── Security → IAM, VPC, KMS, SSL, IAM Auth
│   │   ├── Reliability → Multi-AZ, clustering
│   │   ├── Performance → graph-optimized, clustering
│   │   ├── Cost → per node (like RDS)
│   │   └── Neptune = Graphs
│   │
│   ├── ELASTICSEARCH
│   │   ├── Search any field (vs DynamoDB PK/indexes only)
│   │   ├── Complement to other DBs
│   │   ├── Big data applications
│   │   ├── Cluster of instances
│   │   ├── Built-in integrations → Firehose, IoT, CloudWatch Logs
│   │   ├── Security → Cognito, IAM, KMS, SSL, VPC
│   │   └── ELK Stack → ElasticSearch + Kibana (viz) + Logstash (ingest)
│   │
│   └── ELASTICSEARCH (for SA)
│       ├── Ops → similar to RDS
│       ├── Security → Cognito, IAM, VPC, KMS, SSL
│       ├── Reliability → Multi-AZ, clustering
│       ├── Performance → PB scale
│       ├── Cost → per node (like RDS)
│       └── ElasticSearch = Search/Indexing
│
├── [XVIII] MONITORING, AUDIT & PERFORMANCE
│   │
│   ├── CLOUDWATCH METRICS
│   │   ├── Metrics for every AWS service
│   │   ├── Variables to monitor (CPU, Network)
│   │   ├── Belong to namespaces
│   │   ├── Dimensions (instance id, env) → up to 10
│   │   ├── Timestamps
│   │   └── CloudWatch Dashboards
│   │
│   ├── EC2 DETAILED MONITORING
│   │   ├── Default → 5 min intervals
│   │   ├── Detailed → 1 min intervals (cost)
│   │   ├── Use → faster ASG scaling
│   │   ├── Free tier → 10 detailed metrics
│   │   └── RAM → NOT pushed by default (custom metric)
│   │
│   ├── CUSTOM METRICS
│   │   ├── PutMetricData API
│   │   ├── Examples → RAM, disk, logged-in users
│   │   ├── Dimensions (segment metrics)
│   │   ├── StorageResolution
│   │   │   ├── Standard → 60s
│   │   │   └── High → 1/5/10/30s (higher cost)
│   │   └── Accepts data points 2 weeks back, 2 hours forward
│   │
│   ├── CW DASHBOARDS
│   │   ├── Quick key metric + alarm access
│   │   ├── Global
│   │   ├── Cross-account + cross-region
│   │   ├── Change time zone + range
│   │   ├── Auto-refresh (10s, 1m, 2m, 5m, 15m)
│   │   ├── Share → public/email/SSO
│   │   └── Pricing → 3 free (50 metrics), $3/dashboard after
│   │
│   ├── CLOUDWATCH LOGS
│   │   ├── Apps send logs via SDK
│   │   ├── Collect from
│   │   │   ├── Elastic Beanstalk
│   │   │   ├── ECS
│   │   │   ├── Lambda
│   │   │   ├── VPC Flow Logs
│   │   │   ├── API Gateway
│   │   │   ├── CloudTrail (filtered)
│   │   │   ├── CW log agents (on EC2)
│   │   │   └── Route 53
│   │   ├── Destinations
│   │   │   ├── S3 (batch export)
│   │   │   └── ElasticSearch (stream)
│   │   ├── Storage
│   │   │   ├── Log Groups → app name
│   │   │   └── Log Streams → instances/files/containers
│   │   ├── Expiration policies
│   │   ├── AWS CLI tail logs
│   │   ├── IAM permissions needed
│   │   └── KMS encryption at group level
│   │
│   ├── CW LOGS METRIC FILTER & INSIGHTS
│   │   ├── Filter expressions (find IP)
│   │   ├── Trigger alarms
│   │   └── CloudWatch Logs Insights → query + dashboards
│   │
│   ├── CW LOGS FOR EC2
│   │   ├── No default logs
│   │   ├── Run CW agent on EC2
│   │   ├── IAM permissions
│   │   └── Works on-premises too
│   │
│   ├── CW LOGS AGENT vs UNIFIED AGENT
│   │   ├── Logs Agent (old) → Logs only
│   │   └── Unified Agent (new)
│   │       ├── System metrics (RAM, processes)
│   │       ├── Logs to CW Logs
│   │       └── Centralized config via SSM Parameter Store
│   │
│   ├── UNIFIED AGENT METRICS
│   │   ├── CPU (active/guest/idle/system/user/steal)
│   │   ├── Disk (free/used/total, IO writes/reads/bytes/iops)
│   │   ├── RAM (free/inactive/used/total/cached)
│   │   ├── Netstat (TCP/UDP connections, packets, bytes)
│   │   ├── Processes (total/dead/blocked/idle/running/sleep)
│   │   └── Swap (free/used/percent)
│   │
│   ├── CLOUDWATCH ALARMS
│   │   ├── Trigger notifications
│   │   ├── Options → sampling, %, max, min
│   │   ├── States → OK, INSUFFICIENT_DATA, ALARM
│   │   └── Period
│   │       ├── Length in seconds
│   │       └── High-res → 10s, 30s, or 60s multiples
│   │
│   ├── CW ALARM TARGETS
│   │   ├── EC2 stop/terminate/reboot/recover
│   │   ├── ASG action
│   │   └── SNS notifications
│   │
│   ├── EC2 INSTANCE RECOVERY
│   │   ├── Status Checks
│   │   │   ├── Instance status → VM check
│   │   │   └── System status → hardware check
│   │   └── Recovery → same Private/Public/EIP/metadata/placement
│   │
│   ├── CLOUDWATCH EVENTS
│   │   ├── Event Pattern → intercept events (EC2 start, S3, CodeBuild)
│   │   ├── CloudTrail API call interception
│   │   ├── Schedule or Cron
│   │   └── Targets
│   │       ├── Compute → Lambda, Batch, ECS task
│   │       ├── Integration → SQS, SNS, Kinesis Streams/Firehose
│   │       ├── Orchestration → Step Functions, CodePipeline, CodeBuild
│   │       └── Maintenance → SSM, EC2 Actions
│   │
│   ├── EVENTBRIDGE
│   │   ├── Next evolution of CW Events
│   │   ├── Default bus → AWS services (CW Events)
│   │   ├── Partner bus → SaaS (Zendesk, DataDog, Segment, Auth0)
│   │   ├── Custom bus → your apps
│   │   ├── Cross-account accessible
│   │   └── Rules → process events
│   │
│   ├── EVENTBRIDGE SCHEMA REGISTRY
│   │   ├── Analyzes bus events
│   │   ├── Infers schema
│   │   ├── Generates code for apps
│   │   └── Versioned schemas
│   │
│   ├── EVENTBRIDGE vs CW EVENTS
│   │   ├── Builds upon CW Events
│   │   ├── Same API + endpoint + infra
│   │   ├── Adds custom buses + 3rd party
│   │   ├── Schema Registry capability
│   │   └── Over time → CW Events name replaced with EventBridge
│   │
│   ├── CLOUDTRAIL
│   │   ├── Governance, compliance, audit
│   │   ├── Enabled by default
│   │   ├── History of events/API calls via
│   │   │   ├── Console
│   │   │   ├── SDK
│   │   │   ├── CLI
│   │   │   └── AWS Services
│   │   ├── Logs → CloudWatch Logs or S3
│   │   ├── Trail → all regions (default) or single
│   │   └── If resource deleted → investigate CloudTrail first
│   │
│   ├── CLOUDTRAIL EVENTS
│   │   ├── Management Events
│   │   │   ├── Operations on resources
│   │   │   ├── Examples → IAM AttachRolePolicy, EC2 CreateSubnet, CreateTrail
│   │   │   ├── Default logged
│   │   │   └── Separate Read vs Write
│   │   ├── Data Events
│   │   │   ├── NOT default (high volume)
│   │   │   ├── S3 object-level (Get/Delete/PutObject)
│   │   │   └── Lambda Invoke API
│   │   └── Insights Events
│   │       ├── Detect unusual activity
│   │       │   ├── Inaccurate provisioning
│   │       │   ├── Service limits
│   │       │   ├── IAM action bursts
│   │       │   └── Maintenance gaps
│   │       ├── Baseline from normal management events
│   │       ├── Anomalies in console
│   │       ├── Event → S3
│   │       └── EventBridge event
│   │
│   ├── CLOUDTRAIL RETENTION
│   │   ├── 90 days in CloudTrail
│   │   └── Beyond → log to S3 + Athena
│   │
│   ├── AWS CONFIG
│   │   ├── Auditing + compliance recording
│   │   ├── Config + changes over time
│   │   ├── Answers
│   │   │   ├── Unrestricted SSH SGs?
│   │   │   ├── Buckets public?
│   │   │   └── ALB config history?
│   │   ├── SNS alerts on changes
│   │   ├── Per-region service
│   │   ├── Aggregate cross-region + cross-account
│   │   └── Data → S3 + Athena
│   │
│   ├── CONFIG RULES
│   │   ├── AWS-managed (75+) or Custom (Lambda)
│   │   ├── Examples
│   │   │   ├── EBS = gp2?
│   │   │   └── EC2 = t2.micro?
│   │   ├── Triggers
│   │   │   ├── Per config change
│   │   │   └── Scheduled intervals
│   │   ├── Does NOT prevent actions (no deny)
│   │   └── Pricing → no free tier, $0.003/config item, $0.001/evaluation
│   │
│   ├── CONFIG RESOURCE VIEW
│   │   ├── Compliance over time
│   │   ├── Configuration over time
│   │   └── CloudTrail API calls over time
│   │
│   ├── CONFIG REMEDIATIONS
│   │   ├── SSM Automation Documents
│   │   ├── AWS-Managed or custom
│   │   ├── Custom docs can invoke Lambda
│   │   └── Remediation Retries if still non-compliant
│   │
│   ├── CONFIG NOTIFICATIONS
│   │   ├── EventBridge → Lambda/SNS/SQS on non-compliance
│   │   └── SNS → all events (filter client-side)
│   │
│   ├── CW vs CLOUDTRAIL vs CONFIG
│   │   ├── CloudWatch
│   │   │   ├── Performance monitoring + dashboards
│   │   │   ├── Events + Alerting
│   │   │   └── Log aggregation + analysis
│   │   ├── CloudTrail
│   │   │   ├── API calls by everyone
│   │   │   ├── Trails for specific resources
│   │   │   └── Global service
│   │   └── Config
│   │       ├── Config changes recorded
│   │       ├── Evaluate against rules
│   │       └── Timeline of changes + compliance
│   │
│   └── FOR AN ELB (EXAMPLE)
│       ├── CloudWatch → incoming connections, error codes, dashboards
│       ├── Config → SG rules, config changes, SSL cert compliance
│       └── CloudTrail → who made changes
│
├── [XIX] IDENTITY & FEDERATION
│   │
│   ├── STS (Security Token Service)
│   │   ├── Temp AWS resource access
│   │   ├── Token valid up to 1 hour (refresh)
│   │   ├── Actions
│   │   │   ├── AssumeRole (own or cross-account)
│   │   │   ├── AssumeRoleWithSAML (SAML logins)
│   │   │   ├── AssumeRoleWithWebIdentity (IdP) - use Cognito instead
│   │   │   └── GetSessionToken (MFA)
│   │   └── Process
│   │       ├── Define IAM Role + principals
│   │       ├── STS AssumeRole → creds
│   │       └── Temp creds 15 min - 1 hr
│   │
│   ├── CROSS-ACCOUNT STS
│   │   └── Trust relationship + assume role
│   │
│   ├── IDENTITY FEDERATION
│   │   ├── External users → temp role → AWS resources
│   │   ├── No IAM user per person
│   │   ├── Types
│   │   │   ├── SAML 2.0
│   │   │   ├── Custom Identity Broker
│   │   │   ├── Web Identity (Cognito)
│   │   │   ├── Web Identity (no Cognito)
│   │   │   ├── Single Sign-On
│   │   │   └── Non-SAML with AWS Microsoft AD
│   │
│   ├── SAML 2.0 FEDERATION
│   │   ├── Active Directory / ADFS / any SAML 2.0
│   │   ├── Console + CLI via temp creds
│   │   ├── No IAM user per employee
│   │   ├── Trust setup both ways
│   │   ├── Web-based cross-domain SSO
│   │   ├── Uses AssumeRoleWithSAML
│   │   └── Old way → Single Sign-On Federation now preferred
│   │
│   ├── CUSTOM IDENTITY BROKER
│   │   ├── If IdP not SAML 2.0 compatible
│   │   ├── Broker determines IAM policy
│   │   └── Uses AssumeRole or GetFederationToken
│   │
│   ├── WEB IDENTITY FEDERATION
│   │   ├── AssumeRoleWithWebIdentity
│   │   └── NOT recommended → use Cognito instead
│   │       └── Cognito allows → anonymous, sync, MFA
│   │
│   ├── COGNITO FOR RESOURCE ACCESS
│   │   ├── Direct access to AWS resources client-side
│   │   ├── Providers → CUP, Google, Facebook, Twitter, SAML, OpenID
│   │   ├── No IAM users for app users
│   │   └── Pre-defined IAM policy on temp creds
│   │
│   ├── MICROSOFT ACTIVE DIRECTORY (AD)
│   │   ├── Windows Server with AD DS
│   │   ├── Database of objects (users, computers, printers, shares, groups)
│   │   ├── Centralized security
│   │   ├── Objects in trees, group of trees = forest
│   │   └── Domain Controller
│   │
│   ├── AWS DIRECTORY SERVICES
│   │   ├── AWS Managed Microsoft AD
│   │   │   ├── Your own AD in AWS
│   │   │   ├── Local user management + MFA
│   │   │   └── Trust with on-prem AD
│   │   ├── AD Connector
│   │   │   ├── Proxy to on-prem AD
│   │   │   └── Users managed on-prem
│   │   └── Simple AD
│   │       ├── AD-compatible in AWS
│   │       └── No on-prem join
│   │
│   ├── AWS ORGANIZATIONS
│   │   ├── Global service
│   │   ├── Manage multiple accounts
│   │   ├── Master account (can't change)
│   │   ├── Member accounts
│   │   │   ├── Only one org per account
│   │   │   └── Consolidated billing
│   │   ├── Volume discount (EC2, S3)
│   │   └── API for auto account creation
│   │
│   ├── MULTI-ACCOUNT STRATEGIES
│   │   ├── Per department / cost center / dev-test-prod / regulatory (SCP)
│   │   ├── Better resource isolation (VPC)
│   │   ├── Separate service limits
│   │   ├── Isolated logging
│   │   ├── Multi-Account vs Multi-VPC
│   │   ├── Tagging standards for billing
│   │   ├── Enable CloudTrail on all → central S3
│   │   ├── CW Logs → central account
│   │   └── Cross-Account Roles for admin
│   │
│   ├── ORGANIZATIONAL UNITS (OU)
│   │   ├── Business Unit
│   │   ├── Environmental Lifecycle
│   │   └── Project-based
│   │
│   ├── SERVICE CONTROL POLICIES (SCP)
│   │   ├── Whitelist/blacklist IAM actions
│   │   ├── OU or Account level
│   │   ├── Does NOT apply to Master Account
│   │   ├── Applies to ALL Users + Roles (incl. Root)
│   │   ├── Does NOT affect service-linked roles
│   │   ├── Must have explicit Allow (no default)
│   │   └── Use cases
│   │       ├── Restrict services (no EMR)
│   │       └── PCI compliance enforcement
│   │
│   ├── SCP HIERARCHY (example)
│   │   ├── Master Account → no SCP applies (do anything)
│   │   ├── Account A → all except Redshift (OU deny)
│   │   ├── Account B → all except Redshift + Lambda (OU denies)
│   │   └── Account C → all except Redshift (Prod OU deny)
│   │
│   ├── MOVING ACCOUNTS BETWEEN ORGS
│   │   ├── Remove from old
│   │   ├── Invite to new
│   │   ├── Accept invite
│   │   └── Master to new org → remove all members, delete old, invite master
│   │
│   ├── IAM CONDITIONS
│   │   ├── aws:SourceIP → restrict client IP
│   │   ├── aws:RequestedRegion → restrict region
│   │   ├── Tag-based restrictions
│   │   └── Force MFA
│   │
│   ├── IAM FOR S3
│   │   ├── ListBucket → arn:aws:s3:::test (bucket level)
│   │   └── GetObject/PutObject/DeleteObject → arn:aws:s3:::test/* (object level)
│   │
│   ├── IAM ROLES vs RESOURCE-BASED POLICIES
│   │   ├── Resource-based → attached to resource (S3 bucket policy)
│   │   ├── Role assumption → give up original, take role permissions
│   │   ├── Resource-based → principal keeps permissions
│   │   ├── Example → Account A user scans DDB in A, dumps to S3 in B
│   │   └── Supported → S3, SNS, SQS, etc.
│   │
│   ├── IAM PERMISSION BOUNDARIES
│   │   ├── Users + Roles (not groups)
│   │   ├── Max permissions an entity can get
│   │   ├── Combines with IAM Policy → intersection
│   │   ├── Use with SCPs
│   │   └── Use cases
│   │       ├── Delegate user creation to non-admins
│   │       ├── Dev self-assign policies (no privilege escalation)
│   │       └── Restrict specific user (vs whole account)
│   │
│   ├── IAM POLICY EVALUATION LOGIC
│   │   ├── Explicit Deny → always wins
│   │   ├── Explicit Allow needed
│   │   └── Default → Implicit Deny
│   │
│   ├── AWS RAM (Resource Access Manager)
│   │   ├── Share resources with other accounts
│   │   ├── Any account or within Org
│   │   ├── Avoid duplication
│   │   ├── Shareable
│   │   │   ├── VPC Subnets (same Org)
│   │   │   │   ├── NOT SGs + default VPC
│   │   │   │   └── Participants manage own resources
│   │   │   ├── Transit Gateway
│   │   │   ├── Route53 Resolver Rules
│   │   │   └── License Manager Configs
│   │   └── VPC Sharing example
│   │       ├── Each account → own resources
│   │       ├── Network shared → talk via VPC
│   │       ├── Private IP access
│   │       └── Reference SGs from other accounts
│   │
│   ├── AWS SINGLE SIGN-ON (SSO)
│   │   ├── Central SSO to many accounts + 3rd party
│   │   ├── Integrated with Organizations
│   │   ├── SAML 2.0 markup
│   │   ├── On-prem AD integration
│   │   ├── Centralized permission mgmt
│   │   └── Centralized CloudTrail auditing
│   │
│   └── SSO vs AssumeRoleWithSAML
│       ├── AssumeRoleWithSAML → 3rd party IdP → SAML → AWS
│       └── AWS SSO → AWS SSO login portal + identity store (integrated)
│
├── [XX] SECURITY & ENCRYPTION
│   │
│   ├── WHY ENCRYPTION
│   │   ├── In-flight (SSL) → encrypt before send, decrypt after receive
│   │   │   ├── SSL certs for HTTPS
│   │   │   └── Prevents MITM
│   │   ├── Server-side at rest
│   │   │   ├── Encrypted after server receives
│   │   │   ├── Decrypted before send
│   │   │   └── Keys managed somewhere, server needs access
│   │   └── Client-side
│   │       ├── Client encrypts, server never decrypts
│   │       ├── Receiving client decrypts
│   │       └── Envelope Encryption possible
│   │
│   ├── AWS KMS (Key Management Service)
│   │   ├── "Encryption" = KMS
│   │   ├── AWS manages keys, you control access
│   │   ├── IAM for authorization
│   │   ├── Integrated with
│   │   │   ├── EBS, S3, Redshift, RDS, SSM
│   │   │   └── Many more
│   │   └── Can also use CLI/SDK
│   │
│   ├── KMS CMK TYPES
│   │   ├── Symmetric (AES-256)
│   │   │   ├── First offering, single key encrypt+decrypt
│   │   │   ├── AWS services integrated use these
│   │   │   ├── Necessary for envelope encryption
│   │   │   └── Never get unencrypted access (must call KMS API)
│   │   └── Asymmetric (RSA & ECC)
│   │       ├── Public (Encrypt) + Private (Decrypt)
│   │       ├── Encrypt/Decrypt or Sign/Verify
│   │       ├── Public key downloadable
│   │       ├── Private key no unencrypted access
│   │       └── Use → encryption outside AWS by non-KMS callers
│   │
│   ├── KMS MANAGEMENT
│   │   ├── Create, rotate, disable, enable
│   │   ├── Audit via CloudTrail
│   │   ├── 3 CMK types
│   │   │   ├── AWS Managed Service Default CMK → free
│   │   │   ├── User Keys created in KMS → $1/month
│   │   │   └── User Keys imported (256-bit symmetric) → $1/month
│   │   └── API call → $0.03 / 10,000 calls
│   │
│   ├── KMS USE
│   │   ├── Sensitive info → DB passwords, credentials, SSL private keys
│   │   ├── CMK never retrievable by user
│   │   ├── CMK rotatable for extra security
│   │   ├── Never store plaintext secrets in code
│   │   ├── Encrypted secrets OK in code/env vars
│   │   ├── KMS encrypts up to 4 KB per call
│   │   ├── >4 KB → envelope encryption
│   │   └── Access → Key Policy + IAM Policy
│   │
│   ├── COPYING SNAPSHOTS ACROSS REGIONS
│   │   └── KMS ReEncrypt with target region KMS Key B
│   │
│   ├── KMS KEY POLICIES
│   │   ├── Like S3 bucket policies
│   │   ├── Can't control access without them
│   │   ├── Default Policy
│   │   │   ├── Created if no custom
│   │   │   ├── Root user complete access
│   │   │   └── IAM policies get access
│   │   └── Custom Policy
│   │       ├── Define users/roles
│   │       ├── Define admins
│   │       └── Cross-account access
│   │
│   ├── COPYING SNAPSHOTS ACROSS ACCOUNTS
│   │   ├── Create snapshot encrypted with own CMK
│   │   ├── Attach KMS Key Policy for cross-account
│   │   ├── Share encrypted snapshot
│   │   ├── Target → copy snapshot, encrypt with own KMS
│   │   └── Create volume from snapshot
│   │
│   ├── KMS AUTOMATIC KEY ROTATION
│   │   ├── Customer-managed CMK (not AWS-managed)
│   │   ├── Enabled → every 1 year
│   │   ├── Previous key active for old data decrypt
│   │   └── Same CMK ID (backing key changes)
│   │
│   ├── KMS MANUAL KEY ROTATION
│   │   ├── Every 90/180 days
│   │   ├── New Key → different CMK ID
│   │   ├── Keep previous active for decryption
│   │   ├── Use aliases to hide key change
│   │   └── Good for CMKs not eligible for auto-rotation (asymmetric)
│   │
│   ├── KMS ALIAS UPDATING
│   │   └── UpdateAlias API → point alias to new CMK ID
│   │
│   ├── SSM PARAMETER STORE
│   │   ├── Secure storage for config + secrets
│   │   ├── Optional KMS encryption
│   │   ├── Serverless, scalable, durable
│   │   ├── Version tracking
│   │   ├── Path + IAM config mgmt
│   │   ├── CloudWatch Events notifications
│   │   └── CloudFormation integration
│   │
│   ├── PARAMETER STORE HIERARCHY
│   │   ├── /my-department/my-app/dev/db-url
│   │   ├── /aws/reference/secretsmanager/SECRET_ID
│   │   └── /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
│   │
│   ├── STANDARD vs ADVANCED PARAMETER TIERS
│   │   ├── Standard → 10K params, 4 KB, free, no policies
│   │   └── Advanced → 100K, 8 KB, policies, $0.05/param/month
│   │
│   ├── PARAMETER POLICIES (advanced)
│   │   ├── TTL for params (force update/delete)
│   │   ├── Multiple policies simultaneously
│   │   └── Types → Expiration, ExpirationNotification, NoChangeNotification
│   │
│   ├── AWS SECRETS MANAGER
│   │   ├── Newer, secrets-focused
│   │   ├── Force rotation every X days
│   │   ├── Auto-generate on rotation (Lambda)
│   │   ├── RDS integration (MySQL/PostgreSQL/Aurora)
│   │   ├── KMS encryption
│   │   └── Mainly RDS integration
│   │
│   ├── AWS SHIELD
│   │   ├── Standard
│   │   │   ├── Free, activated for all
│   │   │   └── SYN/UDP Floods, Reflection, L3/L4 attacks
│   │   └── Advanced
│   │       ├── $3,000/month/org
│   │       ├── EC2, ELB, CloudFront, Global Accelerator, Route 53
│   │       ├── 24/7 DRP (DDoS response team)
│   │       └── Protects against spike fees during DDoS
│   │
│   ├── CLOUDHSM
│   │   ├── KMS → AWS manages software encryption
│   │   ├── CloudHSM → AWS provisions encryption hardware
│   │   ├── HSM = Hardware Security Module
│   │   ├── YOU manage keys entirely
│   │   ├── Tamper-resistant, FIPS 140-2 Level 3
│   │   ├── Symmetric + Asymmetric (SSL/TLS)
│   │   ├── NO free tier
│   │   ├── Must use CloudHSM Client Software
│   │   ├── Redshift supports CloudHSM
│   │   └── Good for SSE-C encryption
│   │
│   ├── CLOUDHSM HA
│   │   ├── Multi-AZ cluster
│   │   └── HA + durability
│   │
│   ├── CLOUDHSM vs KMS
│   │   ├── Tenancy → Multi vs Single
│   │   ├── Standard → FIPS L2 vs L3
│   │   ├── Master Keys
│   │   │   ├── KMS → AWS Owned/Managed/Customer
│   │   │   └── CloudHSM → Customer only
│   │   ├── Key Types
│   │   │   ├── KMS → Symmetric/Asymmetric/Signing
│   │   │   └── CloudHSM → All + Hashing
│   │   ├── Accessibility
│   │   │   ├── KMS → Multi-region
│   │   │   └── CloudHSM → VPC-deployed, shareable via VPC Peering
│   │   ├── Crypto Acceleration
│   │   │   ├── KMS → None
│   │   │   └── CloudHSM → SSL/TLS + Oracle TDE
│   │   ├── Auth
│   │   │   ├── KMS → IAM
│   │   │   └── CloudHSM → Customer-managed users
│   │   ├── HA → AWS Managed vs Multi-AZ HSMs
│   │   └── Free Tier → Yes vs No
│   │
│   ├── AWS WAF (Web Application Firewall)
│   │   ├── Layer 7 (HTTP) protection
│   │   ├── Deploy on → ALB, API Gateway, CloudFront
│   │   ├── Web ACL (Access Control List)
│   │   ├── Rules
│   │   │   ├── IP addresses
│   │   │   ├── HTTP headers/body/URI
│   │   │   ├── SQL injection + XSS
│   │   │   ├── Size constraints + geo-match
│   │   │   └── Rate-based (DDoS)
│   │
│   ├── AWS FIREWALL MANAGER
│   │   ├── Rules across AWS Organization accounts
│   │   ├── Common security rules
│   │   │   ├── WAF rules (ALB, API Gateway, CloudFront)
│   │   │   ├── Shield Advanced (ALB, CLB, EIP, CloudFront)
│   │   │   └── SGs for EC2 + ENI in VPC
│   │
│   ├── AMAZON GUARDDUTY
│   │   ├── Intelligent threat discovery
│   │   ├── ML + anomaly detection + 3rd party data
│   │   ├── 30-day trial, no install
│   │   ├── Input data
│   │   │   ├── CloudTrail Logs (unusual API, unauth deploys)
│   │   │   ├── VPC Flow Logs (unusual traffic/IPs)
│   │   │   └── DNS Logs (compromised EC2)
│   │   ├── CW Event rules → Lambda/SNS
│   │   └── CryptoCurrency attack dedicated finding
│   │
│   ├── AMAZON INSPECTOR
│   │   ├── EC2 security assessments
│   │   ├── OS vulnerabilities
│   │   ├── Unintended network accessibility
│   │   ├── Inspector Agent must be installed
│   │   ├── Report of vulnerabilities
│   │   └── Optional SNS notifications
│   │
│   ├── INSPECTOR EVALUATES
│   │   ├── ONLY EC2 instances
│   │   ├── Network (agentless)
│   │   │   └── Network Reachability
│   │   └── Host (with agent)
│   │       ├── CVE
│   │       ├── CIS Benchmarks
│   │       └── Security Best Practices
│   │
│   ├── AMAZON MACIE
│   │   ├── Managed data security + privacy
│   │   ├── ML + pattern matching
│   │   ├── Discover sensitive data (PII)
│   │   └── Alerts via CW Events/EventBridge
│   │
│   └── SHARED RESPONSIBILITY MODEL
│       ├── AWS → Security OF the Cloud
│       │   ├── Infra (HW/SW/facilities/network)
│       │   └── Managed services (S3, DDB, RDS)
│       ├── Customer → Security IN the Cloud
│       │   ├── EC2 → OS mgmt, patches, firewall, IAM
│       │   └── Encrypt app data
│       ├── Shared → Patch Mgmt, Config Mgmt, Training
│       ├── RDS Example
│       │   ├── AWS → EC2 mgmt, disable SSH, auto DB/OS patching, audit
│       │   └── You → SG ports, DB users, public/private, SSL config, encryption
│       └── S3 Example
│           ├── AWS → unlimited storage, encryption, data separation, employee access
│           └── You → bucket config, policy/public setting, IAM, enable encryption
│
├── [XXI] VPC (Networking)
│   │
│   ├── VPC DIAGRAM COMPONENTS
│   │   ├── VPC
│   │   ├── Subnets (Public + Private)
│   │   ├── Internet Gateway (IGW)
│   │   ├── NAT Gateway
│   │   ├── Route Tables
│   │   ├── Security Groups
│   │   ├── Network ACLs
│   │   ├── VPC Peering
│   │   ├── VPC Endpoints
│   │   ├── VPC Flow Logs
│   │   ├── VPN Gateway
│   │   ├── Site-to-Site VPN
│   │   └── Customer Gateway
│   │
│   ├── CIDR (IPv4)
│   │   ├── Classless Inter-Domain Routing
│   │   ├── Base IP + Subnet Mask
│   │   │   ├── 192.168.0.0 = base
│   │   │   └── /26 = mask
│   │   └── Masks
│   │       ├── /32 = 1 IP (2^0)
│   │       ├── /31 = 2 IPs
│   │       ├── /30 = 4 IPs
│   │       ├── /29 = 8 IPs
│   │       ├── /28 = 16 IPs (MIN VPC)
│   │       ├── /27 = 32 IPs
│   │       ├── /26 = 64 IPs
│   │       ├── /25 = 128 IPs
│   │       ├── /24 = 256 IPs
│   │       ├── /16 = 65,536 IPs (MAX VPC)
│   │       ├── /8 = 16.7M IPs
│   │       └── /0 = all IPs (2^32)
│   │
│   ├── CIDR QUICK MEMO
│   │   ├── /32 → no change
│   │   ├── /24 → last octet
│   │   ├── /16 → last 2 octets
│   │   ├── /8 → last 3 octets
│   │   └── /0 → all
│   │
│   ├── PRIVATE IP RANGES (IANA)
│   │   ├── 10.0.0.0/8 → big networks
│   │   ├── 172.16.0.0/12 → default AWS
│   │   └── 192.168.0.0/16 → home
│   │
│   ├── DEFAULT VPC
│   │   ├── All accounts have default
│   │   ├── Instances without subnet → default VPC
│   │   ├── Internet connectivity + public IP
│   │   └── Public + private DNS names
│   │
│   ├── VPC RULES
│   │   ├── Max 5 VPCs per region (soft limit)
│   │   ├── Max 5 CIDR per VPC
│   │   ├── CIDR min /28 (16 IPs)
│   │   ├── CIDR max /16 (65,536 IPs)
│   │   ├── Only private IP ranges allowed
│   │   └── Don't overlap with other networks
│   │
│   ├── SUBNETS
│   │   ├── AWS reserves 5 IPs per subnet
│   │   │   ├── .0 → Network address
│   │   │   ├── .1 → VPC router
│   │   │   ├── .2 → DNS mapping
│   │   │   ├── .3 → future use
│   │   │   └── .255 → Broadcast
│   │   └── Exam Tip
│   │       ├── Need 29 IPs → /27 (32 IPs) NOT ENOUGH (32-5=27)
│   │       └── Need /26 (64 IPs, 59 usable)
│   │
│   ├── INTERNET GATEWAYS (IGW)
│   │   ├── Connect VPC to internet
│   │   ├── Horizontally scalable, HA, redundant
│   │   ├── Created separately from VPC
│   │   ├── 1 VPC ↔ 1 IGW
│   │   ├── NAT for public IPv4 instances
│   │   └── Route tables must be edited
│   │
│   ├── NAT INSTANCES (outdated, at exam)
│   │   ├── Internet for private subnets
│   │   ├── Launched in public subnet
│   │   ├── Disable Source/Destination Check
│   │   ├── Must have EIP
│   │   ├── Route table → private subnets → NAT Instance
│   │   ├── Amazon Linux AMI pre-configured available
│   │   ├── NOT HA by default → need ASG Multi-AZ + user data
│   │   ├── Bandwidth depends on EC2 type
│   │   └── SGs
│   │       ├── Inbound → HTTP/HTTPS from private, SSH from home
│   │       └── Outbound → HTTP/HTTPS to internet
│   │
│   ├── NAT GATEWAY
│   │   ├── AWS-managed NAT
│   │   ├── Higher bandwidth + availability
│   │   ├── No admin
│   │   ├── Pay per hour + bandwidth
│   │   ├── Specific AZ, uses EIP
│   │   ├── Not usable from same subnet
│   │   ├── Requires IGW
│   │   ├── 5 Gbps → auto-scale up to 45 Gbps
│   │   ├── No SGs needed
│   │   └── HA → resilient per AZ, create multi-AZ for fault-tolerance
│   │       └── No cross-AZ failover (AZ down doesn't need NAT)
│   │
│   ├── NAT INSTANCE vs GATEWAY
│   │   └── Gateway: managed, higher BW, no admin, better HA
│   │
│   ├── DNS RESOLUTION IN VPC
│   │   ├── enableDnsSupport (DNS Resolution)
│   │   │   ├── Default True
│   │   │   └── True → queries at 169.254.169.253
│   │   ├── enableDnsHostname (DNS Hostname)
│   │   │   ├── Default False (new), True (Default VPC)
│   │   │   └── True → public hostname for public-IP EC2
│   │   └── Both True if using Route 53 private zone
│   │
│   ├── NACL vs SECURITY GROUP
│   │   ├── Incoming Request Flow
│   │   │   ├── NACL Inbound Rules (subnet, stateless)
│   │   │   └── SG Inbound Rules (EC2, stateful)
│   │   │   → Outbound allowed (stateful)
│   │   │   → NACL Outbound Rules (stateless)
│   │   └── Outgoing Request Flow
│   │       ├── SG Outbound Rules
│   │       └── NACL Outbound Rules
│   │       → Inbound allowed (stateful)
│   │       → NACL Inbound Rules (stateless)
│   │
│   ├── NETWORK ACLs
│   │   ├── Firewall for subnets
│   │   ├── Default NACL → allow everything
│   │   ├── 1 NACL per subnet (default for new)
│   │   ├── Rules
│   │   │   ├── Numbered 1-32,766
│   │   │   ├── Lower number = higher precedence
│   │   │   ├── #100 ALLOW beats #200 DENY
│   │   │   ├── Asterisk (*) = deny if no match
│   │   │   └── Increment by 100 (recommended)
│   │   ├── New NACL → deny everything
│   │   └── Great for blocking specific IP at subnet level
│   │
│   ├── NACL vs SG COMPARISON (table)
│   │   ├── SG → Instance level, stateful, allow only
│   │   └── NACL → Subnet level, stateless, allow + deny
│   │
│   ├── EPHEMERAL PORTS
│   │   └── NACL must allow ephemeral port range for responses
│   │
│   ├── VPC PEERING
│   │   ├── Connect 2 VPCs privately via AWS network
│   │   ├── Behave as same network
│   │   ├── Non-overlapping CIDR required
│   │   ├── NOT transitive (establish per pair)
│   │   ├── Cross-account supported
│   │   ├── Update route tables both sides
│   │   ├── Inter-region supported
│   │   └── Can reference SGs of peered VPC (cross-account works)
│   │
│   ├── VPC ENDPOINTS
│   │   ├── Connect to AWS services privately (no public internet)
│   │   ├── Horizontally scale + redundant
│   │   ├── Remove need for IGW/NAT
│   │   ├── Interface Endpoint
│   │   │   ├── Provisions ENI (private IP)
│   │   │   ├── Security group attached
│   │   │   └── Most AWS services
│   │   ├── Gateway Endpoint
│   │   │   ├── Provision target + route table
│   │   │   └── S3 + DynamoDB ONLY
│   │   └── Issues
│   │       ├── Check DNS Resolution
│   │       └── Check Route Tables
│   │
│   ├── FLOW LOGS
│   │   ├── Capture IP traffic info
│   │   ├── Levels
│   │   │   ├── VPC Flow Logs
│   │   │   ├── Subnet Flow Logs
│   │   │   └── ENI Flow Logs
│   │   ├── Monitor + troubleshoot connectivity
│   │   ├── Destinations → S3, CloudWatch Logs
│   │   └── AWS managed interfaces → ELB, RDS, ElastiCache, Redshift, WorkSpaces
│   │
│   ├── FLOW LOG SYNTAX
│   │   ├── version, account-id, interface-id
│   │   ├── srcaddr, dstaddr (problematic IPs)
│   │   ├── srcport, dstport (problematic ports)
│   │   ├── protocol, packets, bytes, start, end
│   │   ├── action → ACCEPT/REJECT (SG/NACL)
│   │   ├── log-status
│   │   └── Query via Athena (S3) or CW Logs Insights
│   │
│   ├── FLOW LOGS TROUBLESHOOT SG vs NACL
│   │   ├── Inbound Request
│   │   │   ├── Inbound REJECT → NACL or SG
│   │   │   └── Inbound ACCEPT, Outbound REJECT → NACL
│   │   └── Outbound Request
│   │       ├── Outbound REJECT → NACL or SG
│   │       └── Outbound ACCEPT, Inbound REJECT → NACL
│   │
│   ├── BASTION HOSTS
│   │   ├── SSH into private instances
│   │   ├── Bastion in public subnet
│   │   ├── Tighten bastion SG
│   │   └── Exam Tip → port 22 from your IP only, not SG of other instances
│   │
│   ├── SITE-TO-SITE VPN
│   │   ├── Virtual Private Gateway (VGW)
│   │   │   ├── VPN concentrator on AWS side
│   │   │   ├── Created + attached to VPC
│   │   │   └── Custom ASN
│   │   └── Customer Gateway (CGW)
│   │       ├── Software/physical device on customer side
│   │       └── IP Address
│   │           ├── Static, internet-routable
│   │           └── Behind NAT-T → public NAT IP
│   │
│   ├── DIRECT CONNECT (DX)
│   │   ├── Dedicated private connection
│   │   ├── Between DC + AWS DX locations
│   │   ├── Requires Virtual Private Gateway
│   │   ├── Public + private access on same conn
│   │   ├── IPv4 + IPv6 supported
│   │   └── Use cases
│   │       ├── GB/s data bandwidth
│   │       ├── Real-time feeds
│   │       ├── Hybrid environments
│   │       └── Consistent network
│   │
│   ├── DX DIAGRAM
│   │   ├── Corporate DC → partner cage → AWS cage → DX endpoint
│   │   ├── VLAN 1 → Public VIF → S3, Glacier
│   │   └── VLAN 2 → Private VIF → VGW → VPC
│   │
│   ├── DX GATEWAY
│   │   ├── One DX → many VPCs in many regions (same account)
│   │   └── Must use DX Gateway
│   │
│   ├── DX CONNECTION TYPES
│   │   ├── Dedicated
│   │   │   ├── 1 Gbps + 10 Gbps
│   │   │   ├── Physical ethernet port, dedicated
│   │   │   └── Via AWS + DX Partners
│   │   └── Hosted
│   │       ├── 50 Mbps - 10 Gbps
│   │       ├── Via DX Partners
│   │       ├── Capacity add/remove on-demand
│   │       └── 1/2/5/10 Gbps at select partners
│   │   └── Lead times often >1 month
│   │
│   ├── DX ENCRYPTION
│   │   ├── Not encrypted, but private
│   │   ├── DX + VPN → IPsec-encrypted
│   │   └── Extra security, more complex
│   │
│   ├── DX RESILIENCY
│   │   ├── High Resiliency → one connection at multiple locations
│   │   └── Maximum Resiliency → separate devices in >1 location
│   │
│   ├── EGRESS ONLY INTERNET GATEWAY
│   │   ├── IPv6 ONLY
│   │   ├── Like NAT (for IPv4)
│   │   ├── IPv6 all public → all reachable
│   │   ├── Gives IPv6 internet access, not reachable from internet
│   │   └── Edit route tables after creation
│   │
│   ├── EXPOSING SERVICES TO OTHER VPC
│   │   ├── Option 1 → make public
│   │   │   ├── Public internet
│   │   │   └── Access management tough
│   │   └── Option 2 → VPC Peering
│   │       ├── Many peering relations
│   │       └── Opens whole network
│   │
│   ├── AWS PRIVATELINK (VPC Endpoint Services)
│   │   ├── Most secure + scalable exposure to 1000s VPCs
│   │   ├── No peering/IGW/NAT/route tables
│   │   ├── Requires NLB (service) + ENI (customer)
│   │   └── Multi-AZ NLB + ENI = fault-tolerant
│   │
│   ├── PRIVATE LINK & ECS
│   │   └── ECS service behind NLB + PrivateLink to ENI
│   │
│   ├── EC2-CLASSIC & CLASSIC LINK (deprecated)
│   │   ├── EC2-Classic → shared network
│   │   ├── VPC → isolated per account
│   │   ├── ClassicLink links EC2-Classic to VPC
│   │   ├── Must associate SG
│   │   ├── Private IPv4 communication
│   │   └── Likely distractor at exam
│   │
│   ├── AWS VPN CLOUDHUB
│   │   ├── Secure multi-site VPN comm
│   │   ├── Low-cost hub-and-spoke
│   │   └── Over public internet
│   │
│   ├── TRANSIT GATEWAY
│   │   ├── Transitive peering, hub-and-spoke (star)
│   │   ├── Regional resource, works cross-region
│   │   ├── Share cross-account via RAM
│   │   ├── Peer across regions
│   │   ├── Route Tables → limit VPC communication
│   │   ├── Works with DX Gateway, VPN
│   │   └── IP Multicast (only AWS service)
│   │
│   ├── TGW: SITE-TO-SITE VPN ECMP
│   │   ├── Equal-cost multi-path routing
│   │   ├── Forward over multiple best paths
│   │   └── Use → multiple S2S VPN to increase bandwidth
│   │
│   ├── TGW THROUGHPUT w/ ECMP
│   │   ├── VPN to VGW → 1x = 1.25 Gbps (2 tunnels)
│   │   ├── VPN to TGW
│   │   │   ├── 1x = 2.5 Gbps (ECMP, 2 tunnels)
│   │   │   ├── 2x = 5.0 Gbps
│   │   │   └── 3x = 7.5 Gbps
│   │
│   ├── TGW: SHARE DX BETWEEN ACCOUNTS
│   │   ├── Use RAM to share TGW
│   │   └── Multiple accounts + Transit VIF + DX Gateway
│   │
│   ├── VPC SECTION SUMMARY (3 slides)
│   │   ├── CIDR → IP range
│   │   ├── VPC → IPv4/IPv6 CIDR list
│   │   ├── Subnets → AZ-tied
│   │   ├── IGW → VPC-level, IPv4/IPv6
│   │   ├── Route Tables → edit for IGW, peering, endpoints
│   │   ├── NAT Instances → old, public subnet, disable source/dest check
│   │   ├── NAT Gateway → managed, IPv4 only
│   │   ├── Private DNS + R53 → enable DNS Resolution + Hostnames
│   │   ├── NACL → Stateless, subnet, ephemeral ports
│   │   ├── SGs → Stateful, instance level
│   │   ├── VPC Peering → non-overlapping CIDR, non-transitive
│   │   ├── VPC Endpoints → private AWS service access
│   │   ├── Flow Logs → VPC/subnet/ENI level, ACCEPT/REJECT
│   │   ├── Bastion Host → public EC2 for SSH
│   │   ├── Site-to-Site VPN → CGW on DC, VGW on VPC, over public
│   │   ├── Direct Connect → VGW + DX Location
│   │   ├── DX Gateway → DX to many VPCs different regions
│   │   ├── IGW Egress → NAT for IPv6
│   │   ├── Private Link / VPC Endpoint Services → connect services privately
│   │   ├── ClassicLink → EC2-Classic to VPC
│   │   ├── VPN CloudHub → hub-and-spoke VPN
│   │   └── Transit Gateway → transitive VPC/VPN/DX peering
│   │
│   ├── NETWORKING COSTS (simplified)
│   │   ├── Free → traffic in
│   │   ├── Same AZ private IP → Free
│   │   ├── Cross-AZ private IP → $0.01/GB
│   │   ├── Cross-region → $0.02/GB
│   │   ├── Public/Elastic IP → $0.02/GB
│   │   ├── Tip → Use private IP instead of public
│   │   └── Tip → Same AZ for max savings
│   │
│   ├── MINIMIZING EGRESS TRAFFIC COST
│   │   ├── Egress → outbound (AWS → outside), expensive
│   │   ├── Ingress → inbound (outside → AWS), typically free
│   │   ├── Keep internet traffic within AWS
│   │   └── DX location co-located with region → lower egress
│   │
│   ├── S3 DATA TRANSFER PRICING (USA)
│   │   ├── S3 ingress → free
│   │   ├── S3 → Internet → $0.09/GB
│   │   ├── Transfer Acceleration → +$0.04-0.08/GB
│   │   ├── S3 → CloudFront → $0.00/GB
│   │   ├── CloudFront → Internet → $0.085/GB (cheaper than S3)
│   │   ├── CloudFront benefits → caching + lower request cost (7x cheaper)
│   │   └── S3 Cross-Region Replication → $0.02/GB
│   │
│   ├── NAT GATEWAY vs GATEWAY VPC ENDPOINT
│   │   ├── NAT Gateway
│   │   │   ├── $0.045/hour
│   │   │   ├── $0.045/GB processed
│   │   │   ├── $0.09/GB cross-region to S3
│   │   │   └── $0.00 same-region to S3
│   │   └── Gateway Endpoint
│   │       ├── No cost to use
│   │       └── $0.01/GB same-region in/out
│   │
│   ├── IPv6 IN VPC
│   │   ├── IPv4 cannot be disabled
│   │   ├── Enable IPv6 (public addresses) = dual-stack
│   │   ├── 2001:0db8:... format
│   │   ├── ~2^128 addresses vs 2^32 IPv4
│   │   └── EC2 gets private IPv4 + public IPv6
│   │
│   └── IPv6 TROUBLESHOOTING
│       ├── IPv4 cannot be disabled
│       ├── Can't launch → not IPv6 issue (space huge)
│       ├── Problem → no IPv4 available in subnet
│       └── Solution → new IPv4 CIDR
│
├── [XXII] DISASTER RECOVERY & MIGRATIONS
│   │
│   ├── DISASTER RECOVERY OVERVIEW
│   │   ├── Negative impact event = disaster
│   │   ├── Prepare + recover
│   │   ├── Types
│   │   │   ├── On-prem → On-prem (traditional, expensive)
│   │   │   ├── On-prem → AWS (hybrid)
│   │   │   └── AWS Region A → AWS Region B
│   │   └── Key terms
│   │       ├── RPO → Recovery Point Objective (data loss)
│   │       └── RTO → Recovery Time Objective (downtime)
│   │
│   ├── DR STRATEGIES (faster RTO →)
│   │   ├── Backup and Restore (highest RPO)
│   │   ├── Pilot Light
│   │   ├── Warm Standby
│   │   └── Hot Site / Multi-Site (lowest RTO)
│   │
│   ├── BACKUP AND RESTORE
│   │   ├── Storage Gateway → S3 lifecycle → Glacier
│   │   ├── Snowball → S3
│   │   ├── Regular EBS snapshots
│   │   ├── Redshift + RDS snapshots
│   │   └── EC2 AMIs
│   │
│   ├── PILOT LIGHT
│   │   ├── Small app version always running
│   │   ├── Critical core ("pilot light")
│   │   ├── Similar to Backup/Restore
│   │   ├── Faster (critical systems up)
│   │   ├── Route 53 + EC2 (not running) + RDS (running)
│   │   └── Data replication on
│   │
│   ├── WARM STANDBY
│   │   ├── Full system at minimum size
│   │   ├── Scale to prod load on disaster
│   │   ├── Route 53 → ELB → EC2 ASG (min) → RDS slave (running)
│   │   └── Failover updates DNS
│   │
│   ├── HOT SITE / MULTI-SITE
│   │   ├── Very low RTO (minutes/seconds)
│   │   ├── Very expensive
│   │   ├── Full prod scale AWS + on-prem
│   │   └── Active-active
│   │
│   ├── ALL AWS MULTI-REGION
│   │   ├── Active-active
│   │   ├── Aurora Global (master + slave)
│   │   ├── ELB + ASG in both regions
│   │   └── Route 53 failover
│   │
│   ├── DR TIPS
│   │   ├── Backup
│   │   │   ├── EBS snapshots + RDS auto backups
│   │   │   ├── S3/IA/Glacier + lifecycle + CRR
│   │   │   └── On-prem → Snowball / Storage Gateway
│   │   ├── HA
│   │   │   ├── Route 53 DNS migration
│   │   │   ├── RDS Multi-AZ, ElastiCache Multi-AZ, EFS, S3
│   │   │   └── S2S VPN as DX recovery
│   │   ├── Replication
│   │   │   ├── RDS Cross-Region + Aurora Global
│   │   │   ├── On-prem → RDS replication
│   │   │   └── Storage Gateway
│   │   ├── Automation
│   │   │   ├── CloudFormation / Beanstalk
│   │   │   ├── CloudWatch recover/reboot EC2
│   │   │   └── Lambda custom automations
│   │   └── Chaos
│   │       └── Netflix "simian-army" random termination
│   │
│   ├── DMS (Database Migration Service)
│   │   ├── Quick + secure DB migrations
│   │   ├── Resilient + self-healing
│   │   ├── Source DB remains available
│   │   ├── Types
│   │   │   ├── Homogeneous (Oracle → Oracle)
│   │   │   └── Heterogeneous (SQL Server → Aurora)
│   │   ├── Continuous Data Replication (CDC)
│   │   └── EC2 instance runs replication tasks
│   │
│   ├── DMS SOURCES & TARGETS
│   │   ├── Sources
│   │   │   ├── On-prem + EC2 DBs (Oracle, SQL Server, MySQL, MariaDB, PG, Mongo, SAP, DB2)
│   │   │   ├── Azure → Azure SQL DB
│   │   │   ├── RDS (all incl. Aurora)
│   │   │   └── S3
│   │   └── Targets
│   │       ├── On-prem + EC2 DBs (Oracle, SQL, MySQL, MariaDB, PG, SAP)
│   │       ├── RDS
│   │       ├── Redshift
│   │       ├── DynamoDB
│   │       ├── S3
│   │       ├── ElasticSearch
│   │       ├── Kinesis Data Streams
│   │       └── DocumentDB
│   │
│   ├── AWS SCT (Schema Conversion Tool)
│   │   ├── Convert DB schema between engines
│   │   ├── OLTP examples (SQL Server/Oracle → MySQL/PG/Aurora)
│   │   ├── OLAP examples (Teradata/Oracle → Redshift)
│   │   ├── Prefer compute-intensive instances
│   │   ├── NOT needed for same engine
│   │   └── On-prem PG → RDS PG = no SCT
│   │
│   ├── DMS CONTINUOUS REPLICATION
│   │   └── Full load + CDC from Oracle → MySQL RDS via replication instance
│   │
│   ├── ON-PREMISE STRATEGY WITH AWS
│   │   ├── Amazon Linux 2 AMI as VM (.iso)
│   │   │   └── VMWare, KVM, VirtualBox, Hyper-V
│   │   ├── VM Import/Export
│   │   │   ├── Migrate apps to EC2
│   │   │   ├── DR repository for VMs
│   │   │   └── Export back EC2 to on-prem
│   │   ├── AWS Application Discovery Service
│   │   │   ├── Info on on-prem servers
│   │   │   ├── Utilization + dependency mapping
│   │   │   └── Track via Migration Hub
│   │   ├── DMS
│   │   │   ├── On-prem → AWS, AWS → AWS, AWS → on-prem
│   │   │   └── Various DB technologies
│   │   └── AWS Server Migration Service (SMS)
│   │       └── Incremental replication of on-prem live servers
│   │
│   ├── AWS DATASYNC
│   │   ├── Move large on-prem → AWS data
│   │   ├── Targets → S3 (any class incl. Glacier), EFS, FSx Windows
│   │   ├── Move via NFS or SMB
│   │   ├── Scheduled hourly/daily/weekly
│   │   ├── DataSync agent to connect
│   │   └── Bandwidth limits
│   │
│   ├── DATASYNC DIAGRAMS
│   │   ├── NFS/SMB to AWS
│   │   │   ├── NFS/SMB Server + DataSync Agent
│   │   │   ├── TLS to DataSync service
│   │   │   └── Targets → S3 Standard/Intelligent/IA/OneZone/Glacier/DeepArchive/EFS/FSx
│   │   └── EFS to EFS
│   │       └── Source region → DataSync service → destination EFS
│   │
│   ├── AWS BACKUP
│   │   ├── Fully managed
│   │   ├── Central backup automation
│   │   ├── No custom scripts
│   │   ├── Supported services
│   │   │   ├── FSx, EFS
│   │   │   ├── DynamoDB
│   │   │   ├── EC2, EBS
│   │   │   ├── RDS (all engines)
│   │   │   ├── Aurora
│   │   │   └── Storage Gateway (Volume Gateway)
│   │   ├── Cross-region backups
│   │   ├── Cross-account backups
│   │   ├── PITR support
│   │   ├── On-demand + scheduled
│   │   ├── Tag-based backup policies
│   │   └── Backup Plans
│   │       ├── Frequency (12h/daily/weekly/monthly/cron)
│   │       ├── Backup window
│   │       ├── Transition to Cold Storage
│   │       └── Retention (Days/Weeks/Months/Years/Always)
│   │
│   └── TRANSFERRING LARGE DATA TO AWS (200 TB, 100 Mbps)
│       ├── Internet/S2S VPN → 185 days
│       ├── DX 1 Gbps → 18.5 days (long setup >1 month)
│       ├── Snowball → 2-3 parallel, 1 week end-to-end
│       │   └── Can combine with DMS
│       └── Ongoing replication → S2S VPN or DX + DMS/DataSync
│
├── [XXIII] EXTRA SOLUTION ARCHITECTURES
│   │
│   ├── LAMBDA, SNS & SQS
│   │   ├── SQS + Lambda → try/retry (poll), DLQ blocking
│   │   ├── SQS FIFO + Lambda → try/retry, DLQ
│   │   └── SNS + Lambda → asynchronous, retries, DLQ with SQS
│   │
│   ├── FAN OUT PATTERN
│   │   ├── Option 1 → SDK PUTs to each SQS (3 puts)
│   │   └── Option 2 → SNS PUT → subscribers (SQS × N)
│   │
│   ├── S3 EVENTS
│   │   ├── ObjectCreated/Removed/Restore/Replication
│   │   ├── Filter by name (*.jpg)
│   │   ├── Use → generate thumbnails
│   │   ├── As many events as needed
│   │   ├── Typically seconds (sometimes minute+)
│   │   ├── Concurrent writes → possibly only 1 notification
│   │   ├── Enable versioning for per-write guarantee
│   │   └── Destinations
│   │       ├── SQS (sync)
│   │       ├── SNS (sync)
│   │       ├── Lambda (async)
│   │       └── → DLQ + SQS + SNS chains possible
│   │
│   ├── CACHING STRATEGIES
│   │   ├── Client side → app logic
│   │   ├── CloudFront → edge
│   │   ├── API Gateway → caching responses
│   │   ├── EC2/Lambda → Redis/Memcached
│   │   ├── Database → DAX (DynamoDB)
│   │   └── S3 → CloudFront
│   │   └── Factors → Caching, TTL, Network, Computation, Cost, Latency
│   │
│   ├── BLOCKING AN IP ADDRESS
│   │   ├── Simple
│   │   │   ├── NACL
│   │   │   ├── VPC SG
│   │   │   └── Optional EC2 firewall software
│   │   ├── With ALB
│   │   │   ├── ALB terminates connection
│   │   │   ├── EC2 sees ALB private IP
│   │   │   └── NACL blocks client
│   │   ├── With NLB
│   │   │   ├── NLB passthrough (no SG)
│   │   │   ├── EC2 sees client IP
│   │   │   └── NACL blocks client
│   │   ├── ALB + WAF
│   │   │   ├── WAF IP filtering
│   │   │   └── NACL + SGs as usual
│   │   └── ALB + CloudFront + WAF
│   │       ├── CloudFront public IPs
│   │       ├── Geo Restriction
│   │       ├── WAF IP filtering
│   │       └── NACL NOT helpful (CloudFront fronting)
│   │
│   ├── HIGH PERFORMANCE COMPUTING (HPC)
│   │   ├── Cloud perfect for HPC
│   │   ├── Quick resource creation
│   │   ├── Speed results by adding resources
│   │   ├── Pay only for used
│   │   └── Use cases
│   │       ├── Genomics
│   │       ├── Computational chemistry
│   │       ├── Financial risk modeling
│   │       ├── Weather prediction
│   │       ├── Machine learning / Deep learning
│   │       └── Autonomous driving
│   │
│   ├── HPC DATA MANAGEMENT & TRANSFER
│   │   ├── Direct Connect → GB/s private
│   │   ├── Snowball / Snowmobile → PB of data
│   │   └── DataSync → large on-prem ↔ S3/EFS/FSx Windows
│   │
│   ├── HPC COMPUTE & NETWORKING
│   │   ├── EC2 Instances
│   │   │   ├── CPU / GPU optimized
│   │   │   ├── Spot + Spot Fleets + ASG
│   │   │   └── Placement Groups Cluster → 10 Gbps, low latency
│   │   ├── Enhanced Networking (SR-IOV)
│   │   │   ├── Higher BW, higher PPS, lower latency
│   │   │   ├── Option 1 → ENA up to 100 Gbps
│   │   │   └── Option 2 → Intel 82599 VF up to 10 Gbps (LEGACY)
│   │   └── Elastic Fabric Adapter (EFA)
│   │       ├── Improved ENA for HPC, Linux only
│   │       ├── Inter-node, tightly coupled workloads
│   │       ├── MPI (Message Passing Interface) standard
│   │       └── Bypasses Linux OS for low-latency transport
│   │
│   ├── HPC STORAGE
│   │   ├── Instance-attached
│   │   │   ├── EBS → up to 256K IOPS (io2 Block Express)
│   │   │   └── Instance Store → millions IOPS, low latency
│   │   └── Network
│   │       ├── S3 → large blob, not filesystem
│   │       ├── EFS → scale IOPS by size or provisioned
│   │       └── FSx Lustre → HPC distributed FS, millions IOPS, S3-backed
│   │
│   ├── HPC AUTOMATION & ORCHESTRATION
│   │   ├── AWS Batch
│   │   │   ├── Multi-node parallel jobs (1 job, multiple EC2)
│   │   │   └── Schedule + launch EC2 accordingly
│   │   └── AWS ParallelCluster
│   │       ├── Open source HPC cluster management
│   │       ├── Text file config
│   │       └── Automate VPC/Subnet/Cluster/Instance creation
│   │
│   ├── HA EC2 INSTANCE (Single)
│   │   ├── CloudWatch Event/Alarm
│   │   ├── Start standby instance
│   │   └── Attach EIP
│   │
│   ├── HA EC2 WITH ASG
│   │   ├── ASG Settings → 1 min, 1 max, 1 desired, ≥2 AZ
│   │   ├── EC2 user data attaches EIP
│   │   ├── EC2 role allows API calls
│   │   └── Tag-based attachment
│   │
│   ├── HA EC2 WITH ASG + EBS
│   │   ├── Terminate lifecycle hook → EBS snapshot + tags
│   │   ├── Launch lifecycle hook → EBS volume from snapshot
│   │   └── Tag-based attachment
│   │
│   └── HA BASTION HOST
│       ├── HA Options
│       │   ├── 2 bastions across 2 AZ
│       │   └── 1 across 2 AZ with ASG 1:1:1
│       ├── Routing
│       │   ├── 1 bastion → EIP + user-data
│       │   └── 2 bastions → NLB (Layer 4) multi-AZ
│       ├── With NLB → bastions in private subnet
│       └── Can't use ALB (Layer 7, HTTP)
│
├── [XXIV] OTHER SERVICES
│   │
│   ├── CONTINUOUS INTEGRATION (CI)
│   │   ├── Push often to repo (GitHub/CodeCommit/Bitbucket)
│   │   ├── Testing/build server (CodeBuild/Jenkins)
│   │   ├── Dev feedback on tests
│   │   └── Benefits → early bugs, faster delivery, happier devs
│   │
│   ├── CONTINUOUS DELIVERY (CD)
│   │   ├── Reliable releases when needed
│   │   ├── Frequent + quick deployments
│   │   ├── From "every 3 months" to "5 per day"
│   │   └── Automated → CodeDeploy, Jenkins CD, Spinnaker
│   │
│   ├── CICD TECH STACK
│   │   ├── Code → CodeCommit or GitHub
│   │   ├── Build → CodeBuild or Jenkins CI
│   │   ├── Deploy → CodeDeploy or Beanstalk
│   │   ├── Provision → Beanstalk or CloudFormation
│   │   └── Orchestrate → CodePipeline
│   │
│   ├── INFRASTRUCTURE AS CODE
│   │   ├── Manual work hard to reproduce
│   │   │   ├── Different region
│   │   │   ├── Different account
│   │   │   └── Post-deletion recreation
│   │   └── IaC → deploy code that creates/updates/deletes infra
│   │
│   ├── CLOUDFORMATION
│   │   ├── Declarative AWS infra outline
│   │   ├── Supports most AWS resources
│   │   └── Example declarations
│   │       ├── Security group
│   │       ├── 2 EC2 using that SG
│   │       ├── 2 EIPs
│   │       ├── S3 bucket
│   │       └── ELB in front
│   │
│   ├── CLOUDFORMATION BENEFITS
│   │   ├── IaC
│   │   │   ├── No manual resources
│   │   │   ├── Code version controlled
│   │   │   ├── Review via code
│   │   │   └── Peer review
│   │   ├── Cost
│   │   │   ├── Tagged per stack
│   │   │   ├── Cost estimation
│   │   │   └── Dev → delete at 5pm, recreate 8am
│   │   └── Productivity
│   │       ├── Destroy/recreate on fly
│   │       ├── Auto-generate diagrams
│   │       ├── Declarative (no ordering)
│   │       ├── Separation of concerns (VPC/Network/App stacks)
│   │       └── Leverage existing templates
│   │
│   ├── CLOUDFORMATION HOW
│   │   ├── Upload templates to S3
│   │   ├── Reference in CF (re-upload to update)
│   │   ├── Stacks ID'd by name
│   │   └── Delete stack → deletes all artifacts
│   │
│   ├── CF DEPLOYMENT
│   │   ├── Manual → Designer + Console inputs
│   │   └── Automated → YAML + CLI
│   │
│   ├── CF BUILDING BLOCKS
│   │   ├── Templates
│   │   │   ├── Resources (MANDATORY)
│   │   │   ├── Parameters (dynamic inputs)
│   │   │   ├── Mappings (static vars)
│   │   │   ├── Outputs (references to created)
│   │   │   ├── Conditionals (creation logic)
│   │   │   └── Metadata
│   │   └── Helpers → References, Functions
│   │
│   ├── CF STACKSETS
│   │   ├── Create/update/delete stacks across multi account+region
│   │   ├── Single operation
│   │   ├── Administrator + Trusted accounts
│   │   └── Update propagates across all instances
│   │
│   ├── STEP FUNCTIONS
│   │   ├── Serverless visual workflow
│   │   ├── JSON state machine
│   │   ├── Features → sequence/parallel/conditions/timeouts/errors
│   │   ├── Integrates → EC2, ECS, on-prem, API Gateway
│   │   ├── Max 1 year execution
│   │   ├── Human approval step possible
│   │   └── Use cases
│   │       ├── Order fulfillment
│   │       ├── Data processing
│   │       ├── Web apps
│   │       └── Any workflow
│   │
│   ├── SWF (Simple Workflow Service)
│   │   ├── Coordinate work amongst apps
│   │   ├── Code runs on EC2 (not serverless)
│   │   ├── 1 year max runtime
│   │   ├── "Activity step" + "decision step"
│   │   ├── Built-in "human intervention"
│   │   ├── Use → order fulfillment
│   │   └── Step Functions for new apps EXCEPT
│   │       ├── External signals needed
│   │       └── Child processes returning values
│   │
│   ├── EMR (Elastic MapReduce)
│   │   ├── Hadoop clusters for big data
│   │   ├── 100s EC2 instances
│   │   ├── Supports → Apache Spark, HBase, Presto, Flink
│   │   ├── Auto provisioning + config
│   │   ├── Auto-scaling + Spot integration
│   │   └── Use → data processing, ML, web indexing, big data
│   │
│   ├── OPSWORKS
│   │   ├── Managed Chef & Puppet
│   │   ├── Server config automation
│   │   ├── Works with EC2 + on-prem VM
│   │   ├── Alternative to SSM
│   │   └── Exam tip → Chef & Puppet → Opsworks
│   │
│   ├── CHEF / PUPPET
│   │   ├── Config as code
│   │   ├── Consistent deployments
│   │   ├── Linux + Windows
│   │   ├── Automate → users, cron, ntp, packages, services
│   │   ├── "Recipes" (Chef) / "Manifests" (Puppet)
│   │   └── Similar to SSM/Beanstalk/CF but cross-cloud OSS
│   │
│   ├── AWS WORKSPACES
│   │   ├── Managed, secure cloud desktop
│   │   ├── Eliminates on-prem VDI
│   │   ├── On-demand, per usage pricing
│   │   ├── Secure, encrypted, isolated
│   │   └── Integrated with MS AD
│   │
│   ├── AWS APPSYNC
│   │   ├── Store/sync data across mobile+web real-time
│   │   ├── Uses GraphQL (Facebook)
│   │   ├── Auto client code generation
│   │   ├── Integrates → DynamoDB / Lambda
│   │   ├── Real-time subscriptions
│   │   ├── Offline data sync (replaces Cognito Sync)
│   │   └── Fine-grained security
│   │
│   └── COST EXPLORER
│       ├── Visualize + understand AWS costs over time
│       ├── Custom reports on cost + usage
│       ├── Granularity → total, monthly, hourly, resource level
│       ├── Optimal Savings Plan suggestions
│       ├── Forecast usage up to 12 months
│       ├── Monthly cost by AWS Service
│       ├── Hourly & Resource Level
│       ├── Savings Plans (alternative to RI)
│       └── Forecast usage charts
│
├── [XXV] WHITE PAPERS & WELL-ARCHITECTED FRAMEWORK
│   │
│   ├── SECTION OVERVIEW
│   │   ├── Well-Architected Framework Whitepaper
│   │   ├── Well-Architected Tool
│   │   ├── AWS Trusted Advisor
│   │   ├── Reference architectures
│   │   └── DR on AWS Whitepaper
│   │
│   ├── WELL-ARCHITECTED GUIDING PRINCIPLES
│   │   ├── Stop guessing capacity needs
│   │   ├── Test at production scale
│   │   ├── Automate architectural experimentation
│   │   ├── Allow evolutionary architectures
│   │   ├── Design for changing requirements
│   │   ├── Drive architectures with data
│   │   └── Improve through game days (flash sale simulation)
│   │
│   ├── 5 PILLARS
│   │   ├── Operational Excellence
│   │   ├── Security
│   │   ├── Reliability
│   │   ├── Performance Efficiency
│   │   └── Cost Optimization
│   │   └── NOT trade-offs → synergy
│   │
│   ├── WELL-ARCHITECTED TOOL
│   │   └── Questions answered at console.aws.amazon.com/wellarchitected
│   │
│   ├── PILLAR 1 — OPERATIONAL EXCELLENCE
│   │   ├── Run + monitor systems for business value
│   │   ├── Principles
│   │   │   ├── Operations as code (IaC)
│   │   │   ├── Annotate documentation (auto per build)
│   │   │   ├── Frequent, small, reversible changes
│   │   │   ├── Refine procedures frequently
│   │   │   ├── Anticipate failure
│   │   │   └── Learn from all failures
│   │   └── Services
│   │       ├── Prepare → CloudFormation, Config
│   │       ├── Operate → CF, Config, CloudTrail, CloudWatch, X-Ray
│   │       └── Evolve → CF, CodeBuild/Commit/Deploy/Pipeline
│   │
│   ├── PILLAR 2 — SECURITY
│   │   ├── Protect info/systems/assets via risk strategies
│   │   ├── Principles
│   │   │   ├── Strong identity foundation (least privilege + IAM)
│   │   │   ├── Traceability (logs + metrics + auto-respond)
│   │   │   ├── Security at all layers (edge/VPC/subnet/LB/instance/OS/app)
│   │   │   ├── Automate best practices
│   │   │   ├── Protect data in transit + at rest (encryption/tokens/AC)
│   │   │   ├── Keep people away from data (reduce direct access)
│   │   │   └── Prepare for events (simulations + auto-response)
│   │   └── Services
│   │       ├── IAM → IAM, STS, MFA, Organizations
│   │       ├── Detective → Config, CloudTrail, CloudWatch
│   │       ├── Infra → CloudFront, VPC, Shield, WAF, Inspector
│   │       ├── Data → KMS, S3, ELB, EBS, RDS
│   │       └── Incident → IAM, CF, CW Events
│   │
│   ├── PILLAR 3 — RELIABILITY
│   │   ├── Recover, acquire resources dynamically, mitigate disruptions
│   │   ├── Principles
│   │   │   ├── Test recovery procedures (automate failure sim)
│   │   │   ├── Auto-recover from failure (anticipate)
│   │   │   ├── Scale horizontally for availability (distribute)
│   │   │   ├── Stop guessing capacity (Auto Scaling)
│   │   │   └── Manage change in automation (infra changes)
│   │   └── Services
│   │       ├── Foundations → Service Quotas, IAM, VPC, Trusted Advisor
│   │       ├── Change Mgmt → Auto Scaling
│   │       └── Failure Mgmt → CW, CloudTrail, Config, Backups, CF, Glacier, S3, R53
│   │
│   ├── PILLAR 4 — PERFORMANCE EFFICIENCY
│   │   ├── Efficient compute usage as demand + tech evolves
│   │   ├── Principles
│   │   │   ├── Democratize advanced tech (services free you up)
│   │   │   ├── Go global in minutes (multi-region deploys)
│   │   │   ├── Serverless architectures (avoid server mgmt)
│   │   │   ├── Experiment more (easy comparative testing)
│   │   │   └── Mechanical sympathy (know AWS services)
│   │   └── Services
│   │       ├── Selection → Auto Scaling, EBS, Lambda, S3, RDS
│   │       ├── Review → CloudFormation
│   │       ├── Monitoring → CloudWatch, Lambda
│   │       └── Tradeoffs → RDS, ElastiCache, Snowball, CloudFront
│   │
│   ├── PILLAR 5 — COST OPTIMIZATION
│   │   ├── Run systems at lowest price point
│   │   ├── Principles
│   │   │   ├── Adopt consumption mode (pay per use)
│   │   │   ├── Measure overall efficiency (CloudWatch)
│   │   │   ├── Stop spending on DC ops
│   │   │   ├── Analyze + attribute expenditure (tagging)
│   │   │   └── Managed + app-level services (lower TCO)
│   │   └── Services
│   │       ├── Expenditure Awareness → Budgets, Cost + Usage Report, Cost Explorer, RI Reporting
│   │       ├── Cost-Effective → Spot, Reserved, Glacier
│   │       ├── Supply/Demand → Auto Scaling, Lambda
│   │       └── Optimize Over Time → Trusted Advisor, Cost Usage Report
│   │
│   ├── TRUSTED ADVISOR
│   │   ├── No install, high-level AWS account assessment
│   │   ├── Analyzes + recommends
│   │   │   ├── Core Checks → all customers
│   │   │   ├── Weekly email notifications
│   │   │   └── Full Trusted Advisor → Business + Enterprise support
│   │   ├── CloudWatch alarms on limits
│   │   └── Programmatic via AWS Support API
│   │
│   ├── TRUSTED ADVISOR CHECKS
│   │   ├── Cost Optimization
│   │   │   ├── Low utilization EC2, idle ELB
│   │   │   ├── Under-utilized EBS
│   │   │   └── RI + Savings Plan optimizations
│   │   ├── Performance
│   │   │   ├── High utilization EC2
│   │   │   ├── CloudFront CDN
│   │   │   ├── EC2 to EBS throughput
│   │   │   └── Alias records
│   │   ├── Security
│   │   │   ├── Root MFA
│   │   │   ├── IAM key rotation, exposed Access Keys
│   │   │   ├── S3 public permissions
│   │   │   └── SGs with unrestricted ports
│   │   ├── Fault Tolerance
│   │   │   ├── EBS snapshot age
│   │   │   ├── AZ balance
│   │   │   ├── ASG Multi-AZ, RDS Multi-AZ
│   │   │   └── ELB config
│   │   └── Service Limits
│   │
│   └── MORE ARCHITECTURE RESOURCES
│       ├── Classic → EC2, ELB, RDS, ElastiCache
│       ├── Serverless → S3, Lambda, DynamoDB, CloudFront, API Gateway
│       ├── aws.amazon.com/architecture/
│       └── aws.amazon.com/solutions/
│
└── [XXVI] EXAM REVIEW & TIPS
    │
    ├── STATE OF LEARNING CHECKPOINT
    │   └── aws.amazon.com/certification/certified-solutions-architect-associate/
    │
    ├── PRACTICE MAKES PERFECT
    │   ├── Recommended → 1+ year hands-on
    │   ├── If new → practice before rushing
    │   └── Overwhelmed? → review course again
    │
    ├── PROCEED BY ELIMINATION
    │   ├── Most questions scenario-based
    │   ├── Rule out clearly wrong answers
    │   ├── For remaining → most sensible
    │   ├── Very few trick questions
    │   ├── Don't over-think
    │   └── Highly complicated = probably wrong
    │
    ├── SKIM AWS WHITEPAPERS
    │   ├── Architecting for Cloud → Best Practices
    │   ├── Well-Architected Framework
    │   └── DR on AWS
    │
    ├── READ EACH SERVICE FAQ
    │   ├── Frequently Asked Questions
    │   ├── Covers many exam questions
    │   └── Confirms understanding
    │
    ├── AWS COMMUNITY
    │   ├── Course Q&A
    │   ├── Forums
    │   ├── Blogs
    │   ├── Local meetups
    │   └── re:Invent YouTube videos
    │
    ├── EXAM LOGISTICS
    │   ├── Register → aws.training
    │   ├── Fee → $150
    │   ├── 2 ID documents required
    │   ├── No notes/pen/speaking
    │   ├── 65 questions in 130 minutes
    │   ├── Optional final review
    │   ├── Pass/fail immediate
    │   ├── Right/wrong answers NOT shown
    │   ├── Score in email a few days later
    │   ├── Pass threshold → 720/1000
    │   └── Retake → 14 days after fail
    │
    └── AFTER THE EXAM
        ├── Leave a review
        ├── Post on LinkedIn
        └── Become a tremendously good AWS Solutions Architect
```
