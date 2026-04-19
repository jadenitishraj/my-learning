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
├── [XIV] CONTAINERS (ECS, EKS, Farg
```
