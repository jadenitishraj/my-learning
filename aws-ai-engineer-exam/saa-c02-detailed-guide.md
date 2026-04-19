SAA-C02 EXAM STUDY GUIDE - THE ULTIMATE 2000+ LINE SYNTHESIS
==========================================================

[I] THE AWS GLOBAL INFRASTRUCTURE
|
+-- REGIONS
|   |-- Cluster of Data Centers
|   |-- Most services are region-scoped
|   |-- Choice factors: Compliance, Proximity, Service Availability, Pricing
|   |-- Naming: us-east-1, eu-west-3, ap-southeast-2
|   +-- EXAM TIP: If a question mentions "Data Sovereignty", choose the region in the specific country.
|
+-- AVAILABILITY ZONES (AZ)
|   |-- Discrete data centers with redundant power and networking
|   |-- Connected via low-latency fiber
|   |-- Physically isolated from each other
|   +-- EXAM TIP: "High Availability" always involves spreading resources across MULTIPLE AZs.
|
+-- EDGE LOCATIONS
|   |-- Points of Presence (PoP) for CloudFront (CDN)
|   |-- Route 53 (DNS)
|   +-- EXAM TIP: Use for caching content at the edge to reduce user latency.
|
+-- LOCAL ZONES
|   +-- Extension of regions closer to urban centers for ultra-low latency tasks.
|
+-- WAVELENGTH ZONES
    +-- Compute optimized for 5G mobile networks.

[II] IAM (IDENTITY AND ACCESS MANAGEMENT) - THE SECURITY CORE
|
+-- IAM CORE CONCEPTS
|   |-- GLOBAL SERVICE (No regions)
|   |-- AUTHENTICATION (Who you are) vs AUTHORIZATION (What you can do)
|   +-- LEAST PRIVILEGE: Best practice to grant minimal permissions required.
|
+-- IAM ENTITIES
|   |-- ROOT ACCOUNT: Created on signup. Best practice: Enable MFA, lock away keys.
|   |-- USERS: People or applications. Up to 5000 per account.
|   |-- GROUPS: Collections of users. Permissions applied to groups are inherited by users.
|   |   +-- NOTE: Groups cannot contain other groups.
|   +-- ROLES: Temporary identities for services (EC2, Lambda) or federated users.
|
+-- IAM POLICIES (JSON)
|   |-- STRUCTURE:
|   |   |-- Version: "2012-10-17"
|   |   |-- Statement: List of permissions
|   |   |   |-- Sid: Optional identifier
|   |   |   |-- Effect: Allow or Deny (Explicit Deny always wins)
|   |   |   |-- Action: API operations (e.g., s3:ListBucket)
|   |   |   |-- Resource: ARN (Amazon Resource Name)
|   |   |   +-- Condition: Logic to restrict (e.g., source IP, MFA)
|   |-- MANAGED POLICIES: Reusable (AWS Managed or Customer Managed)
|   |-- INLINE POLICIES: Embedded directly in user/role (harder to manage)
|   +-- PERMISSIONS BOUNDARY: Maximum permissions a principal can have.
|
+-- IAM FEDERATION
|   |-- SAML 2.0: Web-based SSO (Active Directory / Okta)
|   |-- OIDC: Identity providers like Google, FB, Amazon
|   |-- COGNITO USER POOLS: Database of users for apps
|   +-- COGNITO IDENTITY POOLS: Grant temp AWS credentials to app users.
|
+-- IAM BEST PRACTICES
    |-- Use Roles for EC2 instead of Access Keys
    |-- Rotate keys regularly
    |-- Monitor IAM activity with CloudTrail
    +-- Use IAM Access Analyzer to find public sharing.

[III] EC2 (ELASTIC COMPUTE CLOUD) - SCALABLE SERVERS
|
+-- EC2 FUNDAMENTALS
|   |-- IaaS (Infrastructure as a Service)
|   |-- AMI (Amazon Machine Image): OS + Apps + Configuration
|   |-- INSTANCE TYPES: (M) General, (C) Compute, (R) Memory, (I/D/H) Storage, (P/G/F) GPU
|   +-- USER DATA: Scripts that run at first boot (Bootstrapping).
|
+-- PURCHASING OPTIONS
|   |-- ON-DEMAND: No commitment, pay per sec/hr.
|   |-- RESERVED (RI): 1 or 3 yr commitment. Up to 72% discount.
|   |   |-- Standard: Fixed type/region
|   |   +-- Convertible: Can change type/os
|   |-- SAVINGS PLANS: $ per hour commitment. Flexible across regions/services.
|   |-- SPOT INSTANCES: Bid for spare capacity. Up to 90% discount.
|   |   |-- Risk: Can be terminated with 2-min warning.
|   |   +-- Best for: Batch processing, stateless apps, data analysis.
|   +-- DEDICATED HOSTS: Physical servers. Good for strict licensing (BYOL).
|
+-- EC2 STORAGE (EBS & INSTANCE STORE)
|   |-- EBS (ELASTIC BLOCK STORE): Network storage. Survives instance termination.
|   |   |-- gp2/gp3: General purpose SSD
|   |   |-- io1/io2: Provisioned IOPS SSD (High performance)
|   |   |-- st1: Throughput Optimized HDD (Big Data)
|   |   +-- sc1: Cold HDD (Cheapest, archives)
|   |-- EBS SNAPSHOTS: Backups to S3. Incremental.
|   +-- INSTANCE STORE: Local physical storage. Ephemeral (Data lost on STOP/TERMINATE).
|       +-- Use Case: High performance cache, swap files.
|
+-- EFS (ELASTIC FILE SYSTEM)
|   |-- Managed NFS (Network File System)
|   |-- Shared storage for 1000s of Linux instances
|   |-- Multi-AZ availability
|   +-- Costly compared to EBS but highly scalable.
|
+-- EC2 PLACEMENT GROUPS
    |-- CLUSTER: Low latency, 10Gbps+ (Same rack/AZ)
    |-- SPREAD: High availability (Different racks)
    +-- PARTITION: Isolates groups of instances from each other.

[IV] S3 (SIMPLE STORAGE SERVICE) - OBJECT STORAGE
|
+-- S3 FUNDAMENTALS
|   |-- Objects (files) stored in Buckets (folders)
|   |-- Globally unique bucket names
|   |-- Unlimited storage capacity
|   +-- Max object size: 5 TB
|
+-- STORAGE CLASSES
|   |-- STANDARD: 11 9's durability. Default.
|   |-- INTELLIGENT-TIERING: Automatic movement based on access patterns.
|   |-- STANDARD-IA (Infrequent Access): Cheaper, access fee.
|   |-- ONE ZONE-IA: 1 AZ only. 20% cheaper than IA.
|   |-- GLACIER INSTANT RETRIEVAL: Ms access, cheaper store.
|   |-- GLACIER FLEXIBLE: 1 min to hours retrieval.
|   +-- GLACIER DEEP ARCHIVE: Cheapest. 12-48 hr retrieval.
|
+-- S3 SECURITY
|   |-- BUCKET POLICIES: Resource-based access rules.
|   |-- ACLs: Access Control Lists (Legacy).
|   |-- ENCRYPTION:
|   |   |-- SSE-S3: AWS managed keys
|   |   |-- SSE-KMS: AWS KMS for rotation/audit
|   |   +-- SSE-C: Customer provided keys
|   |-- VERSIONING: Protect against accidental deletes/overwrites.
|   +-- MFA DELETE: Requires MFA token to permanently delete objects.
|
+-- S3 PERFORMANCE
    |-- MULTIPART UPLOAD: Required for >5GB objects.
    |-- S3 TRANSFER ACCELERATION: Use Edge Locations for faster uploads.
    +-- S3 SELECT: Run SQL queries on data in S3 without downloading it all.

[V] VPC (VIRTUAL PRIVATE CLOUD) - NETWORKING
|
+-- VPC CORE
|   |-- Private network in AWS
|   |-- Subnets: Segments of the VPC IP range
|   |-- Internet Gateway (IGW): Entry/Exit for the VPC
|   |-- Route Tables: Instructions on where traffic goes
|   +-- NAT GATEWAY: Allows private subnets to reach internet (Outbound only).
|
+-- VPC SECURITY
|   |-- SECURITY GROUPS: STATEFUL. Instance level. Rules only ALLOW.
|   +-- NACL (Network Access Control List): STATELESS. Subnet level. ALLOW and DENY rules.
|
+-- VPC PEERING & CONNECTIVITY
|   |-- VPC PEERING: Private link between two VPCs. (Not transitive)
|   |-- TRANSIT GATEWAY: Regional hub for VPC/VPN connection.
|   |-- VPN: Site-to-Site. Public internet, encrypted.
|   +-- DIRECT CONNECT (DX): Private fiber. Reliable, expensive, consistent.
|
+-- VPC ENDPOINTS
    |-- INTERFACE ENDPOINT: Uses PrivateLink (ENI). Costly.
    +-- GATEWAY ENDPOINT: S3 and DynamoDB only. FREE.

[VI] ROUTE 53 - GLOBAL DNS
|
+-- ROUTING POLICIES
|   |-- SIMPLE: Single IP
|   |-- WEIGHTED: % of traffic (A/B testing)
|   |-- LATENCY: Based on user's proximity
|   |-- FAILOVER: Secondary IP if primary health check fails
|   |-- GEOLOCATION: Based on user's country
|   +-- MULTI-VALUE ANSWER: Up to 8 healthy IPs
|
+-- RECORDS
    |-- A RECORD: URL to IPv4
    |-- AAAA RECORD: URL to IPv6
    |-- CNAME: URL to URL (Cannot be root/apex)
    +-- ALIAS: AWS resource specific (Can be root/apex). FREE.

[VII] ASG & LOAD BALANCING (HA & SCALING)
|
+-- ELB (ELASTIC LOAD BALANCER)
|   |-- ALB (Application): Layer 7 (HTTP/S, gRPC). Path/Host routing.
|   |-- NLB (Network): Layer 4 (TCP/UDP, TLS). Ultra high performance, Static IP.
|   +-- GWLB (Gateway): For security appliances (firewalls).
|
+-- ASG (AUTO SCALING GROUP)
    |-- SCALE IN/OUT based on metrics (CPU, Request count)
    |-- MAINTAIN MIN/MAX/DESIRED count
    +-- TARGET TRACKING: Scale to keep metric at a specific value.

[VIII] RDS & AURORA (RELATIONAL DATABASES)
|
+-- AMAZON RDS
|   |-- Managed SQL: MySQL, Postgres, Oracle, SQL Server, MariaDB
|   |-- MULTI-AZ: HIGH AVAILABILITY (Sync replication, automatic failover)
|   +-- READ REPLICAS: SCALABILITY (Async replication, up to 15 per instance)
|
+-- AMAZON AURORA
    |-- Cloud native SQL. 5x MySQL, 3x Postgres performance.
    |-- Storage auto-scaling.
    |-- Aurora Global Database: Multi-region active-read.
    +-- Aurora Serverless: Instant scaling based on query load.

[IX] DYNAMODB & CACHING
|
+-- DYNAMODB (NoSQL)
|   |-- Key-Value store. Millions of requests/sec.
|   |-- Serverless. No administration.
|   +-- DAX (DynamoDB Accelerator): In-memory cache for DynamoDB (Microsecond latency).
|
+-- ELASTICACHE
    |-- REDIS: Advanced structures, persistence, HA.
    +-- MEMCACHED: Simple key-value cache. Multithreaded.

[X] MESSAGING & SERVERLESS
|
+-- SQS (Simple Queue Service)
|   |-- STANDARD: Unlimited throughput, at-least-once, best effort order.
|   +-- FIFO: Exactly-once, strictly ordered (300 msgs/sec).
|
+-- SNS (Simple Notification Service)
|   +-- Pub/Sub. Fan-out to SQS, Lambda, Email, SMS.
|
+-- KINESIS
|   |-- Real-time analytics and streaming.
|   |-- DATA STREAMS: Shard-based, real-time code processing.
|   +-- FIREHOSE: Near real-time loading to S3/Redshift/Splunk.
|
+-- LAMBDA
    |-- Run code without servers. Pay per request/duration.
    |-- MAX EXECUTION TIME: 15 Minutes.
    +-- Scaling: Up to 1000 concurrent executions per region (default).

[XI] MONITORING & AUDITING
|
+-- CLOUDWATCH: Metrics, Logs, Alarms, Events (Performance).
+-- CLOUDTRAIL: API call history (Security/Audit).
+-- AWS CONFIG: Resource inventory and compliance tracking.
+-- VPC FLOW LOGS: IP traffic monitoring.

[XII] SECURITY SERVICES
|
+-- KMS: Key Management Service (Region level).
+-- SECRETS MANAGER: API keys, DB passwords (includes auto-rotation).
+-- WAF & SHIELD: Web app firewall & DDoS protection.
+-- GUARDDUTY: ML-based threat detection (Logs analysis).
+-- INSPECTOR: Automated vulnerability scanning for EC2/ECR.
+-- MACIE: Finds sensitive data in S3 using ML.

[XIII] DATA ANALYTICS
|
+-- ATHENA: SQL on S3. Serverless.
+-- REDSHIFT: Data warehouse (OLAP). Columnar storage.
+-- GLUE: ETL service + Data Catalog.
+-- EMR: Managed Spark/Hadoop.

[XIV] HYBRID CLOUD & MIGRATION
|
+-- STORAGE GATEWAY:
|   |-- File Gateway (S3)
|   |-- Volume Gateway (Block cache)
|   +-- Tape Gateway (VTL)
+-- SNOW FAMILY: Snowcone (8TB), Snowball Edge (80TB), Snowmobile (100PB).
+-- DMS (Database Migration Service): CDC (Change Data Capture) support.

[XV] THE WELL-ARCHITECTED FRAMEWORK
|
+-- OPERATIONAL EXCELLENCE: Automate, document.
+-- SECURITY: Protect data, layers, zero trust.
+-- RELIABILITY: HA, failover, scaling.
+-- PERFORMANCE: Right sizing, managed services.
+-- COST OPTIMIZATION: Budgets, Spot, S3 lifecycle.

[XVI] DETAILED SERVICE COMMAND CHEAT SHEET
|
|-- IAM COMMANDS
|   |-- `aws iam create-user --user-name Alice`
|   |-- `aws iam list-users`
|   |-- `aws iam attach-user-policy --user-name Alice --policy-arn ...`
|   |-- `aws iam create-group --group-name Developers`
|   |-- `aws iam add-user-to-group --user-name Alice --group-name Developers`
|   |-- `aws iam create-role --role-name EC2Role --assume-role-policy-document ...`
|   |-- `aws iam list-roles`
|   |-- `aws iam get-user-policy --user-name Alice --policy-name ...`
|   |-- `aws iam delete-user --user-name Alice`
|   +-- `aws iam get-account-summary`
|
|-- EC2 COMMANDS
|   |-- `aws ec2 run-instances --image-id ami-012345 --instance-type t2.micro`
|   |-- `aws ec2 describe-instances`
|   |-- `aws ec2 start-instances --instance-ids i-012345`
|   |-- `aws ec2 stop-instances --instance-ids i-012345`
|   |-- `aws ec2 terminate-instances --instance-ids i-012345`
|   |-- `aws ec2 create-volume --size 8 --availability-zone us-east-1a`
|   |-- `aws ec2 attach-volume --volume-id vol-012345 --instance-id i-012345 --device /dev/sdf`
|   |-- `aws ec2 create-snapshot --volume-id vol-012345`
|   |-- `aws ec2 create-security-group --group-name WebSG --description "HTTP access"`
|   |-- `aws ec2 authorize-security-group-ingress --group-id sg-012345 --protocol tcp --port 80 --cidr 0.0.0.0/0`
|   |-- `aws ec2 allocate-address --domain vpc`
|   |-- `aws ec2 associate-address --instance-id i-012345 --allocation-id eipalloc-012345`
|   |-- `aws ec2 create-image --instance-id i-012345 --name "MyAMI"`
|   |-- `aws ec2 describe-images --owners self`
|   |-- `aws ec2 create-vpc --cidr-block 10.0.0.0/16`
|   |-- `aws ec2 create-subnet --vpc-id vpc-012345 --cidr-block 10.0.1.0/24`
|   |-- `aws ec2 create-internet-gateway`
|   |-- `aws ec2 attach-internet-gateway --internet-gateway-id igw-012345 --vpc-id vpc-012345`
|   +-- `aws ec2 describe-vpcs`
|
|-- S3 COMMANDS
|   |-- `aws s3 mb s3://my-special-bucket`
|   |-- `aws s3 ls`
|   |-- `aws s3 cp local-file.txt s3://my-special-bucket/`
|   |-- `aws s3 mv s3://bucket1/file.txt s3://bucket2/`
|   |-- `aws s3 sync ./local-folder s3://my-special-bucket/backup/`
|   |-- `aws s3 rm s3://my-special-bucket/file.txt`
|   |-- `aws s3 presign s3://my-special-bucket/file.txt --expires-in 3600`
|   |-- `aws s3api get-bucket-policy --bucket my-special-bucket`
|   |-- `aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled`
|   +-- `aws s3api list-buckets`
|
|-- RDS COMMANDS
|   |-- `aws rds create-db-instance --db-instance-identifier mydb --engine mysql --db-instance-class db.t2.micro`
|   |-- `aws rds describe-db-instances`
|   |-- `aws rds stop-db-instance --db-instance-identifier mydb`
|   |-- `aws rds start-db-instance --db-instance-identifier mydb`
|   |-- `aws rds create-db-snapshot --db-instance-identifier mydb --db-snapshot-identifier mysnap`
|   |-- `aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot`
|   +-- `aws rds create-db-instance-read-replica --db-instance-identifier my-replica --source-db-instance-identifier mydb`
|
|-- LAMBDA COMMANDS
|   |-- `aws lambda list-functions`
|   |-- `aws lambda invoke --function-name my-func output.json`
|   |-- `aws lambda update-function-code --function-name my-func --zip-file fileb://code.zip`
|   |-- `aws lambda create-function --function-name my-func --runtime python3.8 --role ... --handler index.handler --zip-file ...`
|   +-- `aws lambda list-layers`
|
|-- SQS/SNS COMMANDS
|   |-- `aws sqs create-queue --queue-name MyQueue`
|   |-- `aws sqs send-message --queue-url ... --message-body "Test message"`
|   |-- `aws sqs receive-message --queue-url ...`
|   |-- `aws sns create-topic --name MyTopic`
|   |-- `aws sns subscribe --topic-arn ... --protocol email --notification-endpoint test@example.com`
|   +-- `aws sns publish --topic-arn ... --message "Hello World"`
|
|-- CLOUDWATCH COMMANDS
|   |-- `aws cloudwatch list-metrics`
|   |-- `aws cloudwatch put-metric-alarm --alarm-name "HighCPU" --metric-name CPUUtilization --namespace AWS/EC2 ...`
|   +-- `aws logs describe-log-groups`
|
+-- KMS COMMANDS
    |-- `aws kms create-key --description "My Master Key"`
    |-- `aws kms create-alias --alias-name alias/mykey --target-key-id ...`
    +-- `aws kms list-keys`

[XVII] GLOSSARY OF SAA-C02 TERMS (A-Z)
|
|-- ACL: Access Control List; firewall for subnets (stateless) or S3 (legacy).
|-- ALB: Application Load Balancer; Layer 7, routes by URL path/host.
|-- AMI: Amazon Machine Image; template for EC2 instances.
|-- ARN: Amazon Resource Name; unique naming for every resource.
|-- ASG: Auto Scaling Group; manages EC2 scaling.
|-- ATHENA: SQL service for analyzing S3 data.
|-- AURORA: Cloud-native database, 5x speed of MySQL.
|-- AZ: Availability Zone; one or more isolated data centers.
|-- BASTION HOST: EC2 in public subnet for entry into private subnet via SSH.
|-- BEANSTALK: PaaS for deploying web apps easily.
|-- CIDR: Classless Inter-Domain Routing; IP range method.
|-- CLOUDFORMATION: Infrastructure as Code (JSON/YAML).
|-- CLOUDFRONT: Content Delivery Network (CDN) with edge locations.
|-- CLOUDTRAIL: Logs of every API call made in an account.
|-- CLOUDWATCH: Metrics and alarms service.
|-- COGNITO: User identity and app authentication service.
|-- CONFIG: Records configuration history and compliance.
|-- DIRECT CONNECT: Dedicated network connection to AWS.
|-- DMS: Database Migration Service.
|-- DYNAMODB: Scalable NoSQL database.
|-- EBS: Elastic Block Store; persistent disk for EC2.
|-- EFS: Elastic File System; shared Linux storage.
|-- EIP: Elastic IP Address; static public IPv4.
|-- ELB: Elastic Load Balancer; parent service for ALB/NLB/GWLB.
|-- EMR: Elastic MapReduce; Big Data Spark/Hadoop processing.
|-- FARGATE: Serverless container engine.
|-- FSX: High-performance file systems (Lustre / Windows).
|-- GLACIER: Low-cost archival storage in S3.
|-- GLOBAL ACCELERATOR: Network acceleration using static Anycast IPs.
|-- GUARDDUTY: ML threat detection service.
|-- IAM: Identity and Access Management.
|-- IGW: Internet Gateway; the door to the public internet for VPC.
|-- INSPECTOR: EC2 vulnerability scanning.
|-- KINESIS: Streaming data service (Firehose/Streams/Analytics).
|-- KMS: Key Management Service for encryption.
|-- LAMBDA: Serverless functions.
|-- MACIE: PII data discovery in S3.
|-- NACL: Network Access Control List; stateless subnet firewall.
|-- NAT GATEWAY: Managed service for outbound private traffic.
|-- NLB: Network Load Balancer; Layer 4, ultra-fast, handles billions of req.
|-- ORGANIZATIONS: Manage multiple AWS accounts.
|-- PRIVATE LINK: Access services over AWS backbone without IGW.
|-- RAM: Resource Access Manager; share resources across accounts.
|-- RDS: Relational Database Service (Managed SQL).
|-- REDSHIFT: OLAP data warehouse.
|-- ROUTE 53: Scalable DNS service.
|-- S3: Simple Storage Service (Object store).
|-- SAM: Serverless Application Model; extension of CloudFormation.
|-- SCP: Service Control Policy; max permissions for AWS accounts.
|-- SECRETS MANAGER: RDS and API keys rotation/storage.
|-- SHIELD: DDoS protection.
|-- SNS: Simple Notification Service (Push).
|-- SQS: Simple Queue Service (Pull/Buffer).
|-- SSM: Systems Manager; instance patching and remote config.
|-- STEP FUNCTIONS: Orchestrate serverless workflows.
|-- STORAGE GATEWAY: Hybrid storage link.
|-- STS: Security Token Service (Temporary credentials).
|-- TRANSIT GATEWAY: Hub-and-spoke networking.
|-- TRUSTED ADVISOR: Optimization suggestions (Cost, Security).
|-- VPC: Virtual Private Cloud.
|-- VPG: Virtual Private Gateway; connection point for VPN.
|-- WAF: Web Application Firewall (L7 protection).
+-- X-RAY: Analysis and debugging for distributed apps.

[XVIII] ARCHITECTURAL SCENARIOS & SOLUTIONS
|
|-- SCENARIO: Millions of requests, ultra-low latency mobile app.
|   +-- SOLUTION: Route 53 -> CloudFront -> NLB -> API Gateway -> Lambda -> DynamoDB (w/ DAX).
|
|-- SCENARIO: Migrate legacy app with high-performance shared drive.
|   +-- SOLUTION: EC2 instances + FSx for Windows/Lustre + DMS for database.
|
|-- SCENARIO: Cost-effective image processing.
|   +-- SOLUTION: S3 Upload Trigger -> Lambda -> S3 Thumbnail Bucket. Use Spot instances for heavy batch work.
|
|-- SCENARIO: Compliance requiring no data deletion for 7 years.
|   +-- SOLUTION: S3 Versioning + S3 Object Lock (Compliance Mode).
|
|-- SCENARIO: Multi-region failover with zero downtime.
|   +-- SOLUTION: Route 53 Health Checks + Aurora Global Database + Cross-region S3 replication.
|
|-- SCENARIO: Audit unauthorized Amazon S3 bucket public access.
|   +-- SOLUTION: AWS Config Rules (Managed) + IAM Access Analyzer.
|
|-- SCENARIO: Encrypt existing unencrypted EBS volumes.
|   +-- SOLUTION: Create Snapshot -> Copy Snapshot with Encryption checked -> Create Volume from Encrypted Snapshot.
|
|-- SCENARIO: Block specific IPs attacking web application.
|   +-- SOLUTION: Use NACL Deny rules (Subnet level) or WAF (L7 Application level).
|
|-- SCENARIO: Isolate dev/test/prod environments with central billing.
|   +-- SOLUTION: AWS Organizations + Separate Accounts + Consolidated Billing.
|
+-- SCENARIO: High-performance computing cluster.
    +-- SOLUTION: Compute Optimized EC2 (C family) + EFA (Elastic Fabric Adapter) + Cluster Placement Group.

[XIX] FINAL EXAM STRATEGY - THE ARCHITECT'S MINDSET
|
|-- KEYWORD ASSOCIATION:
|   |-- "Shared storage for Linux" -> EFS
|   |-- "Shared storage for Windows" -> FSx for Windows
|   |-- "Managed MySQL/Oracle" -> RDS
|   |-- "Cloud Native DB, 5x speed" -> Aurora
|   |-- "Unstructured data, massive scale" -> S3
|   |-- "Streaming data" -> Kinesis
|   |-- "Long-term archival" -> Glacier
|   |-- "Decouple / Buffer" -> SQS
|   |-- "Audit API Calls" -> CloudTrail
|   |-- "Global static IP, network speed" -> Global Accelerator
|   |-- "Content Delivery, Edge" -> CloudFront
|   |-- "Analyze S3 with SQL" -> Athena
|   |-- "OLAP / Data Warehouse" -> Redshift
|   |-- "ETL / Data Catalog" -> Glue
|   |-- "Hybrid Database Migration" -> DMS
|   |-- "Hardware-based encryption" -> CloudHSM
|   |-- "Discover PII in S3" -> Macie
|   +-- "Block SQL Injection" -> WAF
|
|-- COST STRATEGY:
|   |-- Choose Spot for stateless/batch.
|   |-- Use S3 Lifecycle rules for aging data.
|   |-- Pick Right Sized instances (don't over-provision).
|   |-- Use Trusted Advisor to find idle resources.
|   +-- Choose Aurora Serverless for unpredictable workloads.
|
|-- SECURITY STRATEGY:
|   |-- Always use IAM Roles for EC2.
|   |-- Implement MFA everywhere.
|   |-- Force HTTPS using SSL/TLS (ACM).
|   |-- Use Secrets Manager for rotation.
|   +-- Lock Root account key and delete access keys.
|
+-- PERFORMANCE STRATEGY:
    |-- Use CloudFront for global users.
    |-- Choose NLB for TCP/Low latency.
    |-- Use Multi-AZ for Availability, Read Replicas for Scaling.
    |-- Partition S3 data for faster Athena queries.
    +-- Use DynamoDB DAX for microsecond response times.

[XX] CONCLUSION - YOU ARE READY!
|
|-- You have mastered the core services: IAM, EC2, S3, VPC, RDS, SQS, SNS.
|-- You understand the Well-Architected Framework.
|-- You know when to use which service based on the scenario.
|-- You have a massive CLI cheat sheet for reference.
|-- You have a full glossary of SAA-C02 terms.
|
+-- GOOD LUCK ON YOUR AWS CERTIFIED SOLUTIONS ARCHITECT ASSOCIATE EXAM!
    +-- Remember: Think like an architect! High Availability, Security, Cost, and Performance.
|
[XXI] THE ULTIMATE MASTER CLI "COMMANDER" LIST (DEEP DIVE)
|
|-- ADVANCED IAM CLI COMMANDS
|   |-- `aws iam get-credential-report`
|   |-- `aws iam generate-credential-report`
|   |-- `aws iam list-access-keys --user-name Admin`
|   |-- `aws iam update-access-key --access-key-id AKIA123 --status Inactive`
|   |-- `aws iam delete-access-key --access-key-id AKIA123 --user-name Admin`
|   |-- `aws iam list-mfa-devices --user-name Admin`
|   |-- `aws iam enable-mfa-device --user-name Admin --serial-number arn:aws:iam::123:mfa/Admin --authentication-code-1 123456 --authentication-code-2 654321`
|   |-- `aws iam deactivate-mfa-device --user-name Admin --serial-number arn:aws:iam::123:mfa/Admin`
|   |-- `aws iam list-virtual-mfa-devices`
|   |-- `aws iam create-virtual-mfa-device --virtual-mfa-device-name AdminMFA`
|   |-- `aws iam delete-virtual-mfa-device --serial-number arn:aws:iam::123:mfa/Admin`
|   |-- `aws iam resync-mfa-device --user-name Admin --serial-number arn:aws:iam::123:mfa/Admin --authentication-code-1 123456 --authentication-code-2 654321`
|   |-- `aws iam update-user --user-name OldName --new-user-name NewName`
|   |-- `aws iam create-login-profile --user-name Bob --password MyComplexPassword!123 --password-reset-required`
|   |-- `aws iam update-login-profile --user-name Bob --password NewPassword!456`
|   |-- `aws iam delete-login-profile --user-name Bob`
|   |-- `aws iam change-password --old-password OldPass --new-password NewPass`
|   |-- `aws iam get-account-password-policy`
|   |-- `aws iam update-account-password-policy --minimum-password-length 12 --require-symbols --require-numbers`
|   |-- `aws iam delete-account-password-policy`
|   |-- `aws iam create-policy --policy-name S3ReadOnly --policy-document file://s3-policy.json`
|   |-- `aws iam delete-policy --policy-arn arn:aws:iam::123:policy/S3ReadOnly`
|   |-- `aws iam list-policies --scope Local`
|   |-- `aws iam list-policy-versions --policy-arn arn:aws:iam::123:policy/S3ReadOnly`
|   |-- `aws iam create-policy-version --policy-arn arn:aws:iam::123:policy/S3ReadOnly --policy-document file://new-policy.json --set-as-default`
|   |-- `aws iam delete-policy-version --policy-arn arn:aws:iam::123:policy/S3ReadOnly --version-id v2`
|   |-- `aws iam set-default-policy-version --policy-arn arn:aws:iam::123:policy/S3ReadOnly --version-id v3`
|   |-- `aws iam list-entities-for-policy --policy-arn arn:aws:iam::123:policy/S3ReadOnly`
|   |-- `aws iam list-attached-user-policies --user-name Bob`
|   |-- `aws iam attach-user-policy --user-name Bob --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`
|   |-- `aws iam detach-user-policy --user-name Bob --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`
|   |-- `aws iam list-user-policies --user-name Bob`
|   |-- `aws iam put-user-policy --user-name Bob --policy-name InlineBucketAccess --policy-document file://inline.json`
|   |-- `aws iam get-user-policy --user-name Bob --policy-name InlineBucketAccess`
|   |-- `aws iam delete-user-policy --user-name Bob --policy-name InlineBucketAccess`
|   |-- `aws iam create-group --group-name Admins`
|   |-- `aws iam delete-group --group-name Admins`
|   |-- `aws iam list-groups`
|   |-- `aws iam get-group --group-name Admins`
|   |-- `aws iam update-group --group-name OldGroup --new-group-name NewGroup`
|   |-- `aws iam add-user-to-group --user-name Bob --group-name Admins`
|   |-- `aws iam remove-user-from-group --user-name Bob --group-name Admins`
|   |-- `aws iam list-groups-for-user --user-name Bob`
|   |-- `aws iam list-attached-group-policies --group-name Admins`
|   |-- `aws iam attach-group-policy --group-name Admins --policy-arn arn:aws:iam::aws:policy/AdministratorAccess`
|   |-- `aws iam detach-group-policy --group-name Admins --policy-arn arn:aws:iam::aws:policy/AdministratorAccess`
|   |-- `aws iam list-group-policies --group-name Admins`
|   |-- `aws iam put-group-policy --group-name Admins --policy-name GroupPolicy --policy-document file://policy.json`
|   |-- `aws iam get-group-policy --group-name Admins --policy-name GroupPolicy`
|   |-- `aws iam delete-group-policy --group-name Admins --policy-name GroupPolicy`
|   |-- `aws iam create-role --role-name LambdaExecutionRole --assume-role-policy-document file://trust-policy.json`
|   |-- `aws iam delete-role --role-name LambdaExecutionRole`
|   |-- `aws iam list-roles`
|   |-- `aws iam get-role --role-name LambdaExecutionRole`
|   |-- `aws iam update-role --role-name LambdaExecutionRole --description "New Description"`
|   |-- `aws iam update-assume-role-policy --role-name LambdaExecutionRole --policy-document file://new-trust.json`
|   |-- `aws iam list-attached-role-policies --role-name LambdaExecutionRole`
|   |-- `aws iam attach-role-policy --role-name LambdaExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole`
|   |-- `aws iam detach-role-policy --role-name LambdaExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole`
|   |-- `aws iam list-role-policies --role-name LambdaExecutionRole`
|   |-- `aws iam put-role-policy --role-name LambdaExecutionRole --policy-name InlineRolePolicy --policy-document file://inline.json`
|   |-- `aws iam get-role-policy --role-name LambdaExecutionRole --policy-name InlineRolePolicy`
|   |-- `aws iam delete-role-policy --role-name LambdaExecutionRole --policy-name InlineRolePolicy`
|   |-- `aws iam create-instance-profile --instance-profile-name WebServerProfile`
|   |-- `aws iam delete-instance-profile --instance-profile-name WebServerProfile`
|   |-- `aws iam list-instance-profiles`
|   |-- `aws iam get-instance-profile --instance-profile-name WebServerProfile`
|   |-- `aws iam add-role-to-instance-profile --instance-profile-name WebServerProfile --role-name WebRole`
|   |-- `aws iam remove-role-from-instance-profile --instance-profile-name WebServerProfile --role-name WebRole`
|   |-- `aws iam list-saml-providers`
|   |-- `aws iam create-saml-provider --saml-metadata-document file://saml.xml --name MyOkta`
|   |-- `aws iam get-saml-provider --saml-provider-arn arn:aws:iam::123:saml-provider/MyOkta`
|   |-- `aws iam update-saml-provider --saml-metadata-document file://new-saml.xml --saml-provider-arn arn:aws:iam::123:saml-provider/MyOkta`
|   +-- `aws iam delete-saml-provider --saml-provider-arn arn:aws:iam::123:saml-provider/MyOkta`
|
|-- ADVANCED EC2 CLI COMMANDS
|   |-- `aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro"`
|   |-- `aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,Status:State.Name}"`
|   |-- `aws ec2 run-instances --image-id ami-12345 --count 5 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-123 --subnet-id subnet-123`
|   |-- `aws ec2 terminate-instances --instance-ids i-123 i-456 i-789`
|   |-- `aws ec2 stop-instances --instance-ids i-123`
|   |-- `aws ec2 start-instances --instance-ids i-123`
|   |-- `aws ec2 reboot-instances --instance-ids i-123`
|   |-- `aws ec2 monitor-instances --instance-ids i-123`
|   |-- `aws ec2 unmonitor-instances --instance-ids i-123`
|   |-- `aws ec2 modify-instance-attribute --instance-id i-123 --instance-type t3.small`
|   |-- `aws ec2 modify-instance-attribute --instance-id i-123 --no-disable-api-termination`
|   |-- `aws ec2 describe-instance-status --instance-ids i-123`
|   |-- `aws ec2 get-console-output --instance-id i-123`
|   |-- `aws ec2 get-password-data --instance-id i-123 --priv-launch-key my-key.pem`
|   |-- `aws ec2 create-key-pair --key-name NewKey --query 'KeyMaterial' --output text > NewKey.pem`
|   |-- `aws ec2 delete-key-pair --key-name NewKey`
|   |-- `aws ec2 describe-key-pairs`
|   |-- `aws ec2 create-security-group --group-name MySG --description "My description" --vpc-id vpc-123`
|   |-- `aws ec2 delete-security-group --group-id sg-123`
|   |-- `aws ec2 describe-security-groups --group-ids sg-123`
|   |-- `aws ec2 authorize-security-group-ingress --group-id sg-123 --protocol tcp --port 22 --cidr 203.0.113.0/24`
|   |-- `aws ec2 authorize-security-group-egress --group-id sg-123 --protocol tcp --port 80 --cidr 0.0.0.0/0`
|   |-- `aws ec2 revoke-security-group-ingress --group-id sg-123 --protocol tcp --port 22 --cidr 203.0.113.0/24`
|   |-- `aws ec2 create-volume --size 100 --availability-zone us-east-1a --volume-type gp3`
|   |-- `aws ec2 delete-volume --volume-id vol-123`
|   |-- `aws ec2 attach-volume --volume-id vol-123 --instance-id i-123 --device /dev/sdf`
|   |-- `aws ec2 detach-volume --volume-id vol-123`
|   |-- `aws ec2 modify-volume --volume-id vol-123 --size 200 --volume-type io1 --iops 10000`
|   |-- `aws ec2 create-snapshot --volume-id vol-123 --description "My backup"`
|   |-- `aws ec2 delete-snapshot --snapshot-id snap-123`
|   |-- `aws ec2 copy-snapshot --source-region us-east-1 --source-snapshot-id snap-123 --description "Copy for DR"`
|   |-- `aws ec2 create-image --instance-id i-123 --name "Legacy-App-Backup"`
|   |-- `aws ec2 deregister-image --image-id ami-123`
|   |-- `aws ec2 allocate-address --domain vpc`
|   |-- `aws ec2 associate-address --instance-id i-123 --allocation-id eipalloc-123`
|   |-- `aws ec2 disassociate-address --public-ip 203.0.113.1`
|   |-- `aws ec2 release-address --allocation-id eipalloc-123`
|   |-- `aws ec2 modify-vpc-attribute --vpc-id vpc-123 --enable-dns-hostnames '{"Value":true}'`
|   |-- `aws ec2 create-vpc --cidr-block 172.16.0.0/16`
|   |-- `aws ec2 delete-vpc --vpc-id vpc-123`
|   |-- `aws ec2 create-subnet --vpc-id vpc-123 --cidr-block 172.16.1.0/24 --availability-zone us-east-1a`
|   |-- `aws ec2 delete-subnet --subnet-id subnet-123`
|   |-- `aws ec2 modify-subnet-attribute --subnet-id subnet-123 --map-public-ip-on-launch`
|   |-- `aws ec2 create-internet-gateway`
|   |-- `aws ec2 attach-internet-gateway --internet-gateway-id igw-123 --vpc-id vpc-123`
|   |-- `aws ec2 detach-internet-gateway --internet-gateway-id igw-123 --vpc-id vpc-123`
|   |-- `aws ec2 create-route-table --vpc-id vpc-123`
|   |-- `aws ec2 delete-route-table --route-table-id rtb-123`
|   |-- `aws ec2 create-route --route-table-id rtb-123 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-123`
|   |-- `aws ec2 associate-route-table --route-table-id rtb-123 --subnet-id subnet-123`
|   |-- `aws ec2 create-nat-gateway --subnet-id subnet-public --allocation-id eipalloc-123`
|   |-- `aws ec2 delete-nat-gateway --nat-gateway-id nat-123`
|   |-- `aws ec2 create-vpc-peering-connection --vpc-id vpc-source --peer-vpc-id vpc-dest`
|   |-- `aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id pcx-123`
|   |-- `aws ec2 create-vpc-endpoint --vpc-id vpc-123 --service-name com.amazonaws.us-east-1.s3 --route-table-ids rtb-123`
|   |-- `aws ec2 create-flow-logs --resource-ids vpc-123 --resource-type VPC --traffic-type ALL --log-group-name MyFlowLogs`
|   +-- `aws ec2 describe-vpcs --filters "Name=is-default,Values=true"`
|
|-- ADVANCED S3 CLI COMMANDS
|   |-- `aws s3 mb s3://my-huge-bucket --region us-east-1`
|   |-- `aws s3 rb s3://my-huge-bucket --force`
|   |-- `aws s3 ls s3://my-huge-bucket --recursive --summarize`
|   |-- `aws s3 cp my-large-file.zip s3://my-huge-bucket/archives/ --storage-class GLACIER`
|   |-- `aws s3 mv s3://my-huge-bucket/logs/2020/ s3://my-huge-bucket/archives/2020/ --recursive`
|   |-- `aws s3 sync ./dist/ s3://my-static-site/ --delete`
|   |-- `aws s3 presign s3://my-huge-bucket/private.pdf --expires-in 600`
|   |-- `aws s3api list-buckets --query "Buckets[].Name"`
|   |-- `aws s3api head-object --bucket my-huge-bucket --key image.png`
|   |-- `aws s3api get-bucket-location --bucket my-huge-bucket`
|   |-- `aws s3api put-bucket-policy --bucket my-huge-bucket --policy file://policy.json`
|   |-- `aws s3api get-bucket-policy --bucket my-huge-bucket`
|   |-- `aws s3api delete-bucket-policy --bucket my-huge-bucket`
|   |-- `aws s3api put-bucket-versioning --bucket my-huge-bucket --versioning-configuration Status=Enabled`
|   |-- `aws s3api get-bucket-versioning --bucket my-huge-bucket`
|   |-- `aws s3api list-object-versions --bucket my-huge-bucket`
|   |-- `aws s3api put-bucket-lifecycle-configuration --bucket my-huge-bucket --lifecycle-configuration file://lifecycle.json`
|   |-- `aws s3api get-bucket-lifecycle-configuration --bucket my-huge-bucket`
|   |-- `aws s3api put-bucket-replication --bucket source-bucket --replication-configuration file://replication.json`
|   |-- `aws s3api get-bucket-replication --bucket source-bucket`
|   |-- `aws s3api put-bucket-encryption --bucket my-huge-bucket --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'`
|   |-- `aws s3api get-bucket-encryption --bucket my-huge-bucket`
|   |-- `aws s3api put-bucket-notification-configuration --bucket my-huge-bucket --notification-configuration file://notify.json`
|   |-- `aws s3api list-multipart-uploads --bucket my-huge-bucket`
|   |-- `aws s3api abort-multipart-upload --bucket my-huge-bucket --key large.file --upload-id 123`
|   +-- `aws s3api select-object-content --bucket my-huge-bucket --key data.csv --expression "SELECT * FROM s3object s WHERE s.age > 30" --expression-type 'SQL' --input-serialization '{"CSV": {}}' --output-serialization '{"JSON": {}}' result.json`
|
|-- ADVANCED RDS CLI COMMANDS
|   |-- `aws rds describe-db-instances --query "DBInstances[*].{ID:DBInstanceIdentifier,Engine:Engine,Status:DBInstanceStatus}"`
|   |-- `aws rds create-db-instance --db-instance-identifier prod-db --db-instance-class db.m5.large --engine postgres --allocated-storage 100 --vpc-security-group-ids sg-123 --db-subnet-group-name my-subnets --multi-az`
|   |-- `aws rds modify-db-instance --db-instance-identifier prod-db --allocated-storage 200 --apply-immediately`
|   |-- `aws rds stop-db-instance --db-instance-identifier dev-db`
|   |-- `aws rds start-db-instance --db-instance-identifier dev-db`
|   |-- `aws rds reboot-db-instance --db-instance-identifier prod-db`
|   |-- `aws rds delete-db-instance --db-instance-identifier test-db --skip-final-snapshot`
|   |-- `aws rds create-db-snapshot --db-instance-identifier prod-db --db-snapshot-identifier prod-backup-today`
|   |-- `aws rds copy-db-snapshot --source-db-snapshot-identifier arn:aws:rds:us-east-1:123:snapshot:snap1 --target-db-snapshot-identifier snap1-copy`
|   |-- `aws rds restore-db-instance-from-db-snapshot --db-instance-identifier new-prod-db --db-snapshot-identifier prod-backup-today`
|   |-- `aws rds create-db-instance-read-replica --db-instance-identifier prod-db-replica-1 --source-db-instance-identifier prod-db`
|   |-- `aws rds promote-read-replica --db-instance-identifier prod-db-replica-1`
|   |-- `aws rds describe-db-log-files --db-instance-identifier prod-db`
|   |-- `aws rds download-db-log-file-portion --db-instance-identifier prod-db --log-file-name error/postgresql.log.2020-01-01 > local.log`
|   |-- `aws rds modify-db-parameter-group --db-parameter-group-name my-pg --parameters "ParameterName=max_connections,ParameterValue=1000,ApplyMethod=immediate"`
|   +-- `aws rds describe-events --source-identifier prod-db --source-type db-instance --duration 1440`
|
|-- ADVANCED LAMBDA CLI COMMANDS
|   |-- `aws lambda list-functions --max-items 10`
|   |-- `aws lambda get-function --function-name MyProcessor`
|   |-- `aws lambda create-function --function-name ImageResizer --runtime python3.8 --role arn:aws:iam::123:role/LambdaRole --handler lambda_function.handler --zip-file fileb://function.zip`
|   |-- `aws lambda update-function-code --function-name ImageResizer --zip-file fileb://new-code.zip`
|   |-- `aws lambda update-function-configuration --function-name ImageResizer --timeout 60 --memory-size 512`
|   |-- `aws lambda invoke --function-name ImageResizer --payload '{"key": "value"}' output.json`
|   |-- `aws lambda delete-function --function-name ImageResizer`
|   |-- `aws lambda add-permission --function-name ImageResizer --statement-id s3-trigger --action lambda:InvokeFunction --principal s3.amazonaws.com --source-arn arn:aws:s3:::my-bucket`
|   |-- `aws lambda remove-permission --function-name ImageResizer --statement-id s3-trigger`
|   |-- `aws lambda create-alias --function-name ImageResizer --name PROD --function-version 1`
|   |-- `aws lambda update-alias --function-name ImageResizer --name PROD --function-version 2`
|   |-- `aws lambda publish-version --function-name ImageResizer`
|   |-- `aws lambda list-versions-by-function --function-name ImageResizer`
|   |-- `aws lambda create-event-source-mapping --function-name MySQSProcessor --event-source-arn arn:aws:sqs:us-east-1:123:MyQueue --batch-size 10`
|   |-- `aws lambda list-layers`
|   |-- `aws lambda publish-layer-version --layer-name MyPythonLib --description "Shared utils" --content fileb://layer.zip --compatible-runtimes python3.7 python3.8`
|   +-- `aws lambda get-layer-version --layer-name MyPythonLib --version-number 1`
|
|-- ADVANCED CLOUDWATCH CLI COMMANDS
|   |-- `aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name CPUUtilization`
|   |-- `aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --dimensions Name=InstanceId,Value=i-123 --start-time 2020-01-01T00:00:00Z --end-time 2020-01-01T23:59:59Z --period 3600 --statistics Average`
|   |-- `aws cloudwatch put-metric-data --namespace AppMetrics --metric-data file://metric.json`
|   |-- `aws cloudwatch put-metric-alarm --alarm-name HighTraffic --metric-name RequestCount --namespace AWS/ApplicationELB --statistic Sum --period 60 --threshold 1000 --comparison-operator GreaterThanThreshold --alarm-actions arn:aws:sns:us-east-1:123:Alerts`
|   |-- `aws cloudwatch describe-alarms`
|   |-- `aws cloudwatch set-alarm-state --alarm-name HighTraffic --state-value ALARM --state-reason "Testing"`
|   |-- `aws logs describe-log-groups --log-group-name-prefix /aws/lambda/`
|   |-- `aws logs create-log-group --log-group-name /my/app/logs`
|   |-- `aws logs put-retention-policy --log-group-name /my/app/logs --retention-in-days 30`
|   |-- `aws logs create-log-stream --log-group-name /my/app/logs --log-stream-name instance-1`
|   |-- `aws logs get-log-events --log-group-name /my/app/logs --log-stream-name instance-1`
|   +-- `aws logs filter-log-events --log-group-name /my/app/logs --filter-pattern "ERROR"`
|
|-- ADVANCED CLOUDFORMATION CLI COMMANDS
|   |-- `aws cloudformation list-stacks`
|   |-- `aws cloudformation create-stack --stack-name VPCStack --template-body file://vpc.yaml --parameters ParameterKey=Cidr,ParameterValue=10.0.0.0/16`
|   |-- `aws cloudformation update-stack --stack-name VPCStack --template-body file://vpc-v2.yaml`
|   |-- `aws cloudformation delete-stack --stack-name VPCStack`
|   |-- `aws cloudformation describe-stacks --stack-name VPCStack`
|   |-- `aws cloudformation describe-stack-resources --stack-name VPCStack`
|   |-- `aws cloudformation get-template --stack-name VPCStack`
|   |-- `aws cloudformation validate-template --template-body file://infra.yaml`
|   |-- `aws cloudformation detect-stack-drift --stack-name VPCStack`
|   |-- `aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id 123`
|   |-- `aws cloudformation list-exports`
|   +-- `aws cloudformation create-stack-set --stack-set-name GlobalInfra --template-body file://global.yaml`
|
|-- ADVANCED DYNAMODB CLI COMMANDS
|   |-- `aws dynamodb list-tables`
|   |-- `aws dynamodb describe-table --table-name Users`
|   |-- `aws dynamodb put-item --table-name Users --item '{"UserID": {"S": "123"}, "Name": {"S": "Alice"}}'`
|   |-- `aws dynamodb get-item --table-name Users --key '{"UserID": {"S": "123"}}'`
|   |-- `aws dynamodb update-item --table-name Users --key '{"UserID": {"S": "123"}}' --update-expression "SET Age = :a" --expression-attribute-values '{":a": {"N": "25"}}'`
|   |-- `aws dynamodb delete-item --table-name Users --key '{"UserID": {"S": "123"}}'`
|   |-- `aws dynamodb query --table-name Orders --key-condition-expression "CustomerID = :c" --expression-attribute-values '{":c": {"S": "ALICE123"}}'`
|   |-- `aws dynamodb scan --table-name Users --filter-expression "Age > :a" --expression-attribute-values '{":a": {"N": "20"}}'`
|   |-- `aws dynamodb create-table --table-name Products --attribute-definitions AttributeName=ID,AttributeType=S --key-schema AttributeName=ID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5`
|   |-- `aws dynamodb update-table --table-name Products --billing-mode PAY_PER_REQUEST`
|   +-- `aws dynamodb delete-table --table-name Products`
|
+-- ADVANCED COGNITO CLI COMMANDS
    |-- `aws cognito-idp list-user-pools --max-results 10`
    |-- `aws cognito-idp describe-user-pool --user-pool-id us-east-1_abc123`
    |-- `aws cognito-idp list-users --user-pool-id us-east-1_abc123`
    |-- `aws cognito-idp admin-create-user --user-pool-id us-east-1_abc123 --username bob@example.com`
    |-- `aws cognito-idp admin-delete-user --user-pool-id us-east-1_abc123 --username bob@example.com`
    |-- `aws cognito-idp create-user-pool-client --user-pool-id us-east-1_abc123 --client-name MyAppClient`
    |-- `aws cognito-identity list-identity-pools --max-results 10`
    +-- `aws cognito-identity get-id --identity-pool-id us-east-1:123-456`

[XXII] AWS SERVICE LIMITS & QUOTAS (DETAILED)
|
|-- VPC LIMITS
|   |-- VPCs per region: 5 (Soft limit, can be increased)
|   |-- Subnets per VPC: 200
|   |-- Route tables per VPC: 200
|   |-- Routes per route table: 50
|   |-- Internet Gateways per region: 5
|   |-- Elastic IPs per region: 5
|   |-- Security Groups per VPC: 2500
|   |-- Rules per Security Group: 60
|   |-- Inbound/Outbound rules per NACL: 20
|   |-- VPC Peering connections per VPC: 50
|   +-- NAT Gateways per AZ: 5
|
|-- EC2 LIMITS
|   |-- Running On-Demand instances: Based on vCPU quota (default 32-128)
|   |-- Placement Groups per account: 100
|   |-- Running Spot instances: Based on vCPU quota
|   |-- Standard Reserved Instances: 20 per region
|   |-- Key pairs per region: 5000
|   |-- Security Groups per Network Interface: 5
|   +-- EBS Volumes per account: 5000
|
|-- S3 LIMITS
|   |-- Buckets per account: 100 (Increaseable to 1000)
|   |-- Objects per bucket: Unlimited
|   |-- Max object size: 5 TB
|   |-- Max part size (Multipart): 5 GB
|   +-- Max parts per object: 10,000
|
|-- IAM LIMITS
|   |-- Users per account: 5,000
|   |-- Groups per account: 500
|   |-- Roles per account: 1,000
|   |-- Policies per account: 1,500
|   |-- Managed policies per user: 10
|   |-- Managed policies per group: 10
|   |-- Managed policies per role: 10
|   |-- API keys (Access Keys) per user: 2
|   |-- Groups a user can belong to: 10
|   +-- MFA devices per user: 8 (standard virtual)
|
|-- LAMBDA LIMITS
|   |-- Concurrent executions: 1,000 per region
|   |-- Memory allocation: 128 MB to 10 GB
|   |-- Timeout: 1 to 900 seconds (15 mins)
|   |-- Temp disk space (/tmp): 512 MB to 10 GB
|   |-- Deployment package size (zipped): 50 MB
|   |-- Deployment package size (unzipped): 250 MB
|   |-- Layer size: 250 MB
|   |-- Env variables size: 4 KB
|   +-- Request payload (sync): 6 MB
|
|-- DYNAMODB LIMITS
|   |-- Tables per region: 256
|   |-- Item size: 400 KB
|   |-- Partition key length: 2048 bytes
|   |-- Sort key length: 1024 bytes
|   |-- LSIs per table: 5
|   |-- GSIs per table: 20
|   +-- Max throughput: No hard limit; soft limit at 40k RCU/WCU
|
+-- RDS LIMITS
    |-- DB instances per account: 40
    |-- Read replicas per master: 15 (Aurora) / 5 (Standard RDS)
    |-- Max storage per instance: 64 TB (Standard) / 128 TB (Aurora)
    |-- Allocated storage minimum: 20 GB
    +-- Snapshots per account: 100

[XXIII] AWS WELL-ARCHITECTED LENSES (INDUSTRY SPECIFIC)
|
|-- FINANCIAL SERVICES LENS
|   |-- Higher focus on Security and Governance
|   |-- Immutability of logs (WORM storage)
|   |-- Multi-region Active-Active architecture for critical systems
|   |-- Data encryption at rest and in transit (KMS + TLS 1.2+)
|   +-- Hardware HSM for key storage (CloudHSM)
|
|-- RETAIL & E-COMMERCE LENS
|   |-- Focus on Performance Efficiency and Cost Optimization
|   |-- Leverage CDNs (CloudFront) for product catalog
|   |-- Use Serverless (Lambda) for checkout processing
|   |-- Implement caching (ElastiCache/DAX) for peak traffic (Black Friday)
|   +-- Use Spot instances for non-critical background jobs (order processing retries)
|
|-- HEALTHCARE LENS
|   |-- Focus on Compliance (HIPAA/GDPR)
|   |-- Encryption is mandatory
|   |-- Audit logs and history (CloudTrail + CloudWatch Logs)
|   |-- Disaster recovery is critical (RTO/RPO approach)
|   +-- Use Direct Connect for stable data transfer from research labs
|
+-- MANUFACTURING & IoT LENS
    |-- Focus on Reliability and IoT Core integrations
    |-- Use IoT Greengrass for edge processing
    |-- Kinesis Firehose for telemetry storage in S3
    +-- Amazon Timestream for sequence data analysis (Sensor data)

[XXIV] AWS WHITE PAPERS CORE SUMMARIES (FOR SAA-C02)
|
|-- "DISASTER RECOVERY OF ON-PREMISES APPLICATIONS TO AWS"
|   |-- Objective: Ensure business continuity during on-prem failure.
|   |-- Strategy 1: Backup & Restore (Hours/Days) - Cheap S3 storage.
|   |-- Strategy 2: Pilot Light (10-15 mins) - Database replicates, servers are AMIs.
|   |-- Strategy 3: Warm Standby (Minutes) - Scaled down version running.
|   +-- Strategy 4: Multi-Site Active-Active (Real-time) - Full capacity on AWS.
|
|-- "SECURITY AT THE EDGE"
|   |-- Goal: Protect against DDoS and L7 attacks before they reach the VPC.
|   |-- Tools: CloudFront, WAF, Shield Advanced, Route 53.
|   +-- Key pattern: OAC (Origin Access Control) to prevent direct S3 access.
|
|-- "AWS WELL-ARCHITECTED FRAMEWORK - THE 5 PILLARS"
|   |-- RELIABILITY: Stop guessing capacity, use horizontal scaling.
|   |-- PERFORMANCE: Use right instance types (Right Sizing).
|   |-- SECURITY: IAM, Data protection, incident response.
|   |-- COST: Savings Plans, Spot, Tagging.
|   +-- OPS EXCELLENCE: Operations as code (Clouformation/Terraform).
|
|-- "MIGRATING TO CLOUD-NATIVE DATABASES"
|   |-- Strategy: Rehost (RDS), Replatform (Aurora), Refactor (DynamoDB).
|   +-- Tools: SCT (Schema Conversion Tool) and DMS (Database Migration Service).
|
+-- "BUILDING MICROSERVICES ON AWS"
    |-- Pattern: API Gateway -> Lambda -> DynamoDB.
    |-- Pattern: ECS/EKS for containerized workloads.
    +-- Pattern: EventBridge/SQS for async communication.

[XXV] 100 ADDITIONAL ARCHITECTURAL SCENARIOS (QUICK RECALL)
|
|-- 21. Scenario: Real-time sensor data analysis with <1s latency.
|   +-- Solution: Kinesis Data Streams -> Lambda -> DynamoDB.
|-- 22. Scenario: Share data between thousands of EC2s globally.
|   +-- Solution: EFS with Cross-Region replication or S3 with Multi-Region access.
|-- 23. Scenario: Securely call 3rd party API from Lambda in VPC.
|   +-- Solution: Lambda -> Private Subnet -> NAT Gateway -> IGW -> API.
|-- 24. Scenario: Detect SSH login attempts in real-time.
|   +-- Solution: CloudWatch Logs Filter -> SNS Alert.
|-- 25. Scenario: Store user profile images in a cost-effective way.
|   +-- Solution: S3 Standard for 30 days -> S3 Standard-IA after 30 days -> Glacier after 90 days.
|-- 26. Scenario: High-speed upload of 100TB data from office.
|   +-- Solution: AWS Direct Connect or Snowball Edge (multiple devices).
|-- 27. Scenario: Zero-downtime Blue/Green update for monolithic app.
|   +-- Solution: Route 53 Weighted routing or ALB Target Group swap.
|-- 28. Scenario: Monitor EC2 memory usage.
|   +-- Solution: CloudWatch Agent (Custom Metric) - Standard EC2 metrics don't include RAM.
|-- 29. Scenario: Block countries from accessing video content.
|   +-- Solution: CloudFront Geo-Restriction (Geoblocking).
|-- 30. Scenario: Shared storage for Windows cluster (AD integrated).
|   +-- Solution: Amazon FSx for Windows File Server.
|[...SCENARIOS 31-100 CONTINUED IN DEEP DETAIL...]
|-- 31. Scenario: Process 1 million S3 objects using parallel Lambda.
|   +-- Solution: S3 Event Notification -> SQS -> Lambda (Batch).
|-- 32. Scenario: Encrypt data in S3 with keys you manage physically.
|   +-- SOLUTION: CloudHSM or SSE-C.
|-- 33. Scenario: Connect remote office to 50 VPCs in different regions.
|   +-- SOLUTION: Transit Gateway with VPN/DX attachments.
|-- 34. Scenario: Automatically delete objects older than 365 days.
|   +-- SOLUTION: S3 Lifecycle Expire rule.
|-- 35. Scenario: Route users to closest server based on network speed.
|   +-- SOLUTION: Route 53 Latency Routing Policy.
|-- 36. Scenario: High-availability DB for mobile app with global users.
|   +-- SOLUTION: DynamoDB Global Tables (Active-Active).
|-- 37. Scenario: Host a React website with HTTPS and custom domain.
|   +-- SOLUTION: S3 (Static Website) -> CloudFront (SSL/TLS) -> Route 53 (DNS).
|-- 38. Scenario: Backup EC2 EBS volumes once a week.
|   +-- SOLUTION: Amazon Data Lifecycle Manager (DLM) or AWS Backup.
|-- 39. Scenario: Scale EC2 based on SQS queue depth.
|   +-- SOLUTION: CloudWatch SQS QueueLength Metric -> ASG Step Scaling.
|-- 40. Scenario: Securely access Amazon S3 from private EC2 (No Internet).
|   +-- SOLUTION: VPC Gateway Endpoint for S3.
|-- 41. Scenario: Managed service for Hadoop big data processing.
|   +-- SOLUTION: Amazon EMR.
|-- 42. Scenario: Discover PII (Credit Cards) in a specific S3 bucket.
|   +-- SOLUTION: Amazon Macie.
|-- 43. Scenario: ML-based monitoring of all AWS account activity.
|   +-- SOLUTION: Amazon GuardDuty.
|-- 44. Scenario: Distributed tracing for serverless microservices.
|   +-- SOLUTION: AWS X-Ray.
|-- 45. Scenario: Synchronize data between S3 and EFS.
|   +-- SOLUTION: AWS DataSync.
|-- 46. Scenario: Managed VPN service with fine-grained access.
|   +-- SOLUTION: Client VPN.
|-- 47. Scenario: Orchestrate multiple Lambda functions in order.
|   +-- SOLUTION: AWS Step Functions.
|-- 48. Scenario: Auto-rotation of database passwords.
|   +-- SOLUTION: AWS Secrets Manager.
|-- 49. Scenario: Fast response to SQL queries on files in S3.
|   +-- SOLUTION: Amazon Athena.
|-- 50. Scenario: Static IP for a load balancer.
|   +-- SOLUTION: Network Load Balancer (NLB) or Global Accelerator.
|-- 51. Scenario: Block SQL injection on a legacy app server.
|   +-- SOLUTION: AWS WAF (Layer 7).
|-- 52. Scenario: Multi-region active-read for a Postgres database.
|   +-- SOLUTION: Amazon Aurora Global Database.
|-- 53. Scenario: Managed Kafka service.
|   +-- SOLUTION: Amazon MSK.
|-- 54. Scenario: Connect on-prem network to AWS via dedicated fiber.
|   +-- SOLUTION: AWS Direct Connect.
|-- 55. Scenario: High-volume message broadcasting (Pub/Sub).
|   +-- SOLUTION: Amazon SNS.
|-- 56. Scenario: Exactly-once delivery of messages.
|   +-- SOLUTION: SQS FIFO Queue.
|-- 57. Scenario: Re-use common Python libraries across 10 Lambdas.
|   +-- SOLUTION: Lambda Layers.
|-- 58. Scenario: Visualize S3 data with a business dashboard.
|   +-- SOLUTION: Amazon QuickSight.
|-- 59. Scenario: High-performance compute with sub-millisecond inter-node latency.
|   +-- SOLUTION: Cluster Placement Group + EFA.
|-- 60. Scenario: Host containers without managing EC2 instances.
|   +-- SOLUTION: AWS Fargate.
|-- 61. Scenario: Deploy code from Git automatically to EC2.
|   +-- SOLUTION: AWS CodePipeline + CodeBuild + CodeDeploy.
|-- 62. Scenario: Private connection to a SaaS provider on AWS.
|   +-- SOLUTION: AWS PrivateLink.
|-- 63. Scenario: Search for logs with millisecond latency.
|   +-- SOLUTION: Amazon OpenSearch (Elasticsearch).
|-- 64. Scenario: Audit resource configuration changes over time.
|   +-- SOLUTION: AWS Config.
|-- 65. Scenario: Dedicated hardware for SSL termination.
|   +-- SOLUTION: CloudHSM.
|-- 66. Scenario: Block users from specific countries.
|   +-- SOLUTION: CloudFront Geo-Restriction.
|-- 67. Scenario: Managed MongoDB service.
|   +-- SOLUTION: Amazon DocumentDB.
|-- 68. Scenario: Managed Cassandra service.
|   +-- SOLUTION: Amazon Keyspaces.
|-- 69. Scenario: Managed Graph database.
|   +-- SOLUTION: Amazon Neptune.
|-- 70. Scenario: Continuous compliance for AWS accounts.
|   +-- SOLUTION: AWS Config Rules.
|-- 71. Scenario: Automate the setup of a landing zone with multiple accounts.
|   +-- SOLUTION: AWS Control Tower.
|-- 72. Scenario: Centralized billing for 50 child accounts.
|   +-- SOLUTION: AWS Organizations.
|-- 73. Scenario: Share a subnet between two different AWS accounts.
|   +-- SOLUTION: AWS Resource Access Manager (RAM).
|-- 74. Scenario: Detect if an EC2 instance is publicly accessible.
|   +-- SOLUTION: IAM Access Analyzer for Network Reachability.
|-- 75. Scenario: Move 1 petabyte of data in 1 month without fiber.
|   +-- SOLUTION: Snowball Edge (multiple).
|-- 76. Scenario: Automated patching of 1000 EC2 instances.
|   +-- SOLUTION: Systems Manager (SSM) Patch Manager.
|-- 77. Scenario: Store application config parameters securely.
|   +-- SOLUTION: SSM Parameter Store.
|-- 78. Scenario: Trigger a script on EC2 on a schedule.
|   +-- SOLUTION: EventBridge (CloudWatch Events) -> SSM Run Command.
|-- 79. Scenario: Low-latency access to shared files for a gaming server.
|   +-- SOLUTION: FSx for Lustre.
|-- 80. Scenario: Backup on-prem tapes to the cloud.
|   +-- SOLUTION: AWS Storage Gateway (Tape Gateway).
|-- 81. Scenario: Host a virtual desktop for remote workers.
|   +-- SOLUTION: Amazon WorkSpaces.
|-- 82. Scenario: Stream specific apps to users via a web browser.
|   +-- SOLUTION: Amazon AppStream 2.0.
|-- 83. Scenario: Real-time fraud detection on streaming transactions.
|   +-- SOLUTION: Kinesis Data Analytics.
|-- 84. Scenario: Connect IoT devices with a secure message broker.
|   +-- SOLUTION: AWS IoT Core.
|-- 85. Scenario: Managed Docker registry.
|   +-- SOLUTION: Amazon ECR (Elastic Container Registry).
|-- 86. Scenario: Managed Kubernetes service.
|   +-- SOLUTION: Amazon EKS (Elastic Kubernetes Service).
|-- 87. Scenario: Managed Docker Swarm/Orchestration.
|   +-- SOLUTION: Amazon ECS (Elastic Container Service).
|-- 88. Scenario: Automated data lifecycle management for S3.
|   +-- SOLUTION: S3 Lifecycle Policies.
|-- 89. Scenario: Cross-region disaster recovery for RDS.
|   +-- SOLUTION: RDS Snapshot Copy to Region or Cross-Region Read Replica.
|-- 90. Scenario: Redirect traffic to a secondary region if primary is down.
|   +-- SOLUTION: Route 53 Failover Routing.
|-- 91. Scenario: Distribute traffic based on user's physical location.
|   +-- SOLUTION: Route 53 Geoproximity Routing.
|-- 92. Scenario: Test a new version of the site with 10% of users.
|   +-- SOLUTION: Route 53 Weighted Routing.
|-- 93. Scenario: High-speed DNS resolution for on-prem networks.
|   +-- SOLUTION: Route 53 Resolver (Inbound/Outbound Endpoints).
|-- 94. Scenario: Shield your web servers from massive DDoS attack.
|   +-- SOLUTION: Shield Advanced.
|-- 95. Scenario: Secure the communication between microservices within a VPC.
|   +-- SOLUTION: Security Groups referencing each other.
|-- 96. Scenario: Scale vertically (Instance Type) based on performance.
|   +-- SOLUTION: Impossible with ASG (it only scales horizontally). Manual stop/modify/start is needed.
|-- 97. Scenario: Cache results of complex SQL queries.
|   +-- SOLUTION: ElastiCache.
|-- 98. Scenario: Managed service for transactional emails.
|   +-- SOLUTION: Amazon SES (Simple Email Service).
|-- 99. Scenario: Manage SSL/TLS certificates centrally.
|   +-- SOLUTION: AWS Certificate Manager (ACM).
+-- 100. Scenario: Monitor the costs of each project using tags.
    +-- SOLUTION: AWS Cost Explorer + Active Cost Allocation Tags.

[XXVI] FINAL CHECKLIST & RECALL (THE GOLDEN RULES)
|
|-- 1. If it's MANAGED SQL -> RDS.
|-- 2. If it's MANAGED NoSQL -> DynamoDB.
|-- 3. If it's BIG DATA / SPARK -> EMR.
|-- 4. If it's MILLISECOND SEARCH -> OpenSearch.
|-- 5. If it's GLOBAL CDN -> CloudFront.
|-- 6. If it's DNS -> Route 53.
|-- 7. If it's HYBRID STORAGE -> Storage Gateway.
|-- 8. If it's PHYSICAL DATA MOVE -> Snow Family.
|-- 9. If it's SERVERLESS COMPUTE -> Lambda.
|-- 10. If it's INFRA AS CODE -> CloudFormation.
|-- 11. If it's COMPLIANCE AUDIT -> CloudTrail.
|-- 12. If it's PERFORMANCE MONITOR -> CloudWatch.
|-- 13. If it's DECOUPLING -> SQS.
|-- 14. If it's PUSH NOTIFICATION -> SNS.
|-- 15. If it's SECURITY GROUPS -> Stateful.
|-- 16. If it's NACLS -> Stateless.
|-- 17. If it's PRIVATE IP OVER INTERNET -> VPN.
|-- 18. If it's PRIVATE LINE NO INTERNET -> Direct Connect (DX).
|-- 19. If it's SCALE HORIZONTALLY -> ASG.
|-- 20. If it's SCALE VERTICALLY -> Increase Instance Size (Manual).
|-- 21. If it's DATABASE FAILOVER -> Multi-AZ.
|-- 22. If it's DATABASE READ SCALING -> Read Replica.
|-- 23. If it's S3 CHEAPEST ARCHIVE -> Glacier Deep Archive.
|-- 24. If it's S3 QUICK ACCESS ARCHIVE -> Glacier Instant Retrieval.
+-- 25. If it's KMS -> Single region encryption.

[XXVII] PARTING WORDS
|
|-- Architecture is about TRADE-OFFS.
|-- Cost vs Performance.
|-- Availability vs Complexity.
|-- Managed vs Self-Managed.
|-- Always read the question for "Least Cost" or "Highest Reliability".
|
+-- GO CONQUER THE SAA-C02 EXAM!
|
[XXVIII] THE ARCHITECT'S SERVICE COMPARISON TABLES (ASCII)
|
|-- STORAGE COMPARISON
|   +-------------------+------------+-----------+------------+------------------+
|   | Feature           | S3         | EBS       | EFS        | Instance Store   |
|   +-------------------+------------+-----------+------------+------------------+
|   | Type              | Object     | Block     | File (NFS) | Block (Local)    |
|   | Durability        | 99.99...%  | 99.999%   | 99.99...%  | Low (Ephemeral)  |
|   | Availability      | 99.99%     | 99.999%   | 99.99%     | High (per inst)  |
|   | Multi-Instance    | Yes (Global)| No (1 AZ) | Yes (100s) | No              |
|   | Usage             | Static Web | DB Disk   | Shared Web | Cache / Temp     |
|   | Cost              | Lowest     | Medium    | High       | Free (with inst) |
|   +-------------------+------------+-----------+------------+------------------+
|
|-- DATABASE COMPARISON
|   +-------------------+------------+------------+------------+------------------+
|   | Feature           | RDS        | Aurora     | DynamoDB   | Redshift         |
|   +-------------------+------------+------------+------------+------------------+
|   | Type              | SQL        | SQL        | NoSQL      | SQL (OLAP)       |
|   | Scalability       | Vertical   | Auto       | Auto       | Horizontal       |
|   | High Availability | Multi-AZ   | Native     | Native     | Multi-Node       |
|   | Response Time     | ms         | ms         | <10ms      | seconds/mins     |
|   | Use Case          | Standard DB| High Perf  | Web Scaling| Big Data BI      |
|   +-------------------+------------+------------+------------+------------------+
|
|-- NETWORKING COMPARISON
|   +-------------------+------------+--------------------+------------------+
|   | Feature           | VPN        | Direct Connect (DX)| Transit Gateway  |
|   +-------------------+------------+--------------------+------------------+
|   | Setup Time        | Minutes    | Weeks/Months       | Minutes          |
|   | Cost              | Low        | High               | Medium           |
|   | Reliability       | Standard   | Highest            | Highest          |
|   | Speed             | <1.25 Gbps | 1-100 Gbps         | 50 Gbps per VPC  |
|   | Encryption        | IPsec VPN  | No (use public VIP)| AWS Backbone     |
|   +-------------------+------------+--------------------+------------------+
|
|-- MESSAGING COMPARISON
|   +-------------------+------------+------------+------------+
|   | Feature           | SQS        | SNS        | Kinesis    |
|   +-------------------+------------+------------+------------+
|   | Model             | Pull (Poll)| Push       | Pull       |
|   | Pattern           | Queue      | Pub/Sub    | Streaming  |
|   | Ordering          | FIFO (Opt) | No         | Shard-based|
|   | Consumers         | 1 per msg  | Many       | 1 per shard|
|   | Size              | 256 KB     | 256 KB     | 1 MB       |
|   +-------------------+------------+------------+------------+
|
[XXIX] ADVANCED MANAGEMENT & ANALYTICS CLI (PART 3)
|
|-- CLOUDFRONT CLI
|   |-- `aws cloudfront list-distributions`
|   |-- `aws cloudfront get-distribution --id <dist-id>`
|   |-- `aws cloudfront create-invalidation --distribution-id <id> --paths "/*"`
|   |-- `aws cloudfront create-origin-access-control --origin-access-control-config file://oac.json`
|   +-- `aws cloudfront update-distribution --id <id> --if-match <etag> --distribution-config file://config.json`
|
|-- ROUTE 53 CLI
|   |-- `aws route53 list-hosted-zones`
|   |-- `aws route53 get-hosted-zone --id <id>`
|   |-- `aws route53 change-resource-record-sets --hosted-zone-id <id> --change-batch file://records.json`
|   |-- `aws route53 list-resource-record-sets --hosted-zone-id <id>`
|   |-- `aws route53 create-health-check --caller-reference <ref> --health-check-config ...`
|   +-- `aws route53 list-health-checks`
|
|-- ATHENA & GLUE CLI
|   |-- `aws athena start-query-execution --query-string "SELECT * FROM my_table" --result-configuration OutputLocation=s3://buckets/results/`
|   |-- `aws athena get-query-execution --query-execution-id <id>`
|   |-- `aws athena list-work-groups`
|   |-- `aws glue list-crawlers`
|   |-- `aws glue start-crawler --name MyS3Crawler`
|   |-- `aws glue get-table --database-name my_db --name my_table`
|   +-- `aws glue create-job --name MyETLJob --role ... --command ...`
|
|-- REDSHIFT CLI
|   |-- `aws redshift describe-clusters`
|   |-- `aws redshift create-cluster --cluster-identifier my-cluster --node-type ds2.xlarge --master-username admin --master-user-password Password123 --number-of-nodes 2`
|   |-- `aws redshift stop-cluster --cluster-identifier my-cluster`
|   |-- `aws redshift start-cluster --cluster-identifier my-cluster`
|   |-- `aws redshift reboot-cluster --cluster-identifier my-cluster`
|   |-- `aws redshift delete-cluster --cluster-identifier my-cluster --skip-final-cluster-snapshot`
|   |-- `aws redshift modify-cluster --cluster-identifier my-cluster --node-type ra3.4xlarge --number-of-nodes 4`
|   +-- `aws redshift describe-cluster-snapshots`
|
|-- SYSTEMS MANAGER (SSM) CLI
|   |-- `aws ssm describe-instance-information`
|   |-- `aws ssm list-commands --instance-id i-123`
|   |-- `aws ssm send-command --instance-ids i-123 --document-name AWS-RunShellScript --parameters commands="ls -al"`
|   |-- `aws ssm get-parameter --name /my-app/db-url`
|   |-- `aws ssm put-parameter --name /my-app/api-key --value 12345 --type SecureString`
|   |-- `aws ssm start-session --target i-123`
|   |-- `aws ssm list-associations --instance-id i-123`
|   +-- `aws ssm describe-patch-groups`
|
|-- CLOUDHSM & WAF CLI
|   |-- `aws cloudhsmv2 describe-clusters`
|   |-- `aws cloudhsmv2 create-cluster --subnet-ids subnet-123 --hsm-type hsm1.medium`
|   |-- `aws wafv2 list-web-acls --scope REGIONAL`
|   |-- `aws wafv2 create-web-acl --name BlockIPs --scope REGIONAL --default-action Allow={} --rules ...`
|   +-- `aws wafv2 get-web-acl --name BlockIPs --scope REGIONAL --id <id>`
|
[XXX] SAA-C02 PRACTICE QUIZ BANK (100 QUESTIONS)
|
|-- Q1: An application requires shared storage that can be mounted by multiple EC2 instances simultaneously and scales automatically. Which service should you use?
|   +-- A1: Amazon EFS.
|
|-- Q2: You need to migrate an on-premises Oracle database to AWS Aurora with minimal downtime. Which combination of services should you use?
|   +-- A2: AWS SCT (Schema Conversion Tool) and AWS DMS (Database Migration Service) with CDC (Change Data Capture).
|
|-- Q3: Your application uses a large number of short-lived compute tasks. Which purchasing option is most cost-effective?
|   +-- A3: Amazon EC2 Spot Instances.
|
|-- Q4: A user reports that they cannot access your web server. You suspect the Network ACL is blocking the traffic. How do you verify this?
|   +-- A4: Check VPC Flow Logs.
|
|-- Q5: Which service provides a dashboard of your AWS service health?
|   +-- A5: AWS Personal Health Dashboard.
|
|-- Q6: You want to host a static website with the lowest possible latency for global users. Which combination should you use?
|   +-- A6: Amazon S3 and Amazon CloudFront.
|
|-- Q7: An application requires block storage that survives instance termination and can be attached to one instance at a time. Which service should you use?
|   +-- A7: Amazon EBS.
|
|-- Q8: How can you protect against accidental deletion of objects in an S3 bucket?
|   +-- A8: Enable S3 Versioning and MFA Delete.
|
|-- Q9: You need to store vast amounts of data for 10 years for compliance reasons. The data is rarely accessed, but when it is, a 12-hour retrieval time is acceptable. Which S3 storage class is best?
|   +-- A9: S3 Glacier Deep Archive.
|
|-- Q10: Which Route 53 routing policy should be used to route traffic to the resource with the lowest network latency?
|   +-- A10: Latency Routing Policy.
|
|-- Q11: Which service helps you model and provision AWS infrastructure using JSON or YAML?
|   +-- A11: AWS CloudFormation.
|
|-- Q12: You need a managed NoSQL database that provides single-digit millisecond latency at any scale. Which service do you choose?
|   +-- A12: Amazon DynamoDB.
|
|-- Q13: An application needs to process real-time streaming data and store it in an S3 bucket within minutes. Which service should you use?
|   +-- A13: Amazon Kinesis Data Firehose.
|
|-- Q14: Which service allows you to run code without provisioning or managing servers?
|   +-- A14: AWS Lambda.
|
|-- Q15: You want to distribute incoming application traffic across multiple EC2 instances in multiple Availability Zones. Which service should you use?
|   +-- A15: Elastic Load Balancing (ELB).
|
|-- Q16: Which AWS service can be used to track who made a specific API call to terminate an EC2 instance?
|   +-- A16: AWS CloudTrail.
|
|-- Q17: You need to establish a dedicated, private connection from your data center to AWS. Which service should you use?
|   +-- A17: AWS Direct Connect.
|
|-- Q18: What is the most cost-effective way to handle unpredictable, bursty traffic for a SQL database?
|   +-- A18: Amazon Aurora Serverless.
|
|-- Q19: Which service provides ML-based threat detection by analyzing VPC Flow Logs and CloudTrail logs?
|   +-- A19: Amazon GuardDuty.
|
|-- Q20: A company wants to share a VPC subnet with another AWS account in the same organization. Which service should they use?
|   +-- A20: AWS Resource Access Manager (RAM).
|
|-- Q21: Which service allows you to create and manage encryption keys?
|   +-- A21: AWS KMS.
|
|-- Q22: You need to store sensitive information like database passwords and rotate them automatically. Which service should you use?
|   +-- A22: AWS Secrets Manager.
|
|-- Q23: An application requires high-performance shared storage for a Windows-based application cluster. Which service do you choose?
|   +-- A23: Amazon FSx for Windows File Server.
|
|-- Q24: Which Route 53 record type maps a domain name to another domain name and cannot be used for the zone apex?
|   +-- A24: CNAME.
|
|-- Q25: How can you improve the performance of read-heavy workloads on an Amazon RDS database?
|   +-- A25: Create RDS Read Replicas.
|
|-- Q26: Which service provides automated patching and remote management of EC2 instances?
|   +-- A26: AWS Systems Manager (SSM).
|
|-- Q27: A company needs to move 50TB of data to AWS but has limited internet bandwidth. Which service should they use?
|   +-- A27: AWS Snowball Edge.
|
|-- Q28: Which service can be used for automated vulnerability scanning of EC2 instances?
|   +-- A28: Amazon Inspector.
|
|-- Q29: What is the primary difference between a Security Group and a Network ACL?
|   +-- A29: Security Groups are stateful (inbound allowed = outbound allowed), while Network ACLs are stateless (must explicitly allow return traffic).
|
|-- Q30: Which service is used to decouple application components by buffering messages?
|   +-- A30: Amazon SQS.
|
|-- Q31: Which service should be used to broadcast messages to multiple subscribers simultaneously?
|   +-- A31: Amazon SNS.
|
|-- Q32: A development team wants to deploy their application using a managed 플랫폼 that handles capacity provisioning and health monitoring. Which service should they use?
|   +-- A32: AWS Elastic Beanstalk.
|
|-- Q33: Which service allows you to run SQL queries directly on data stored in an S3 bucket?
|   +-- A33: Amazon Athena.
|
|-- Q34: What is the maximum visibility timeout for an SQS message?
|   +-- A34: 12 hours.
|
|-- Q35: Which S3 encryption method requires AWS to manage the keys and handle the encryption/decryption process?
|   +-- A35: SSE-S3.
|
|-- Q36: You need to connect multiple VPCs and on-premises networks in a hub-and-spoke configuration. Which service should you use?
|   +-- A36: AWS Transit Gateway.
|
|-- Q37: Which service provides a visual overview of how your application's components are interacting and identifies performance bottlenecks?
|   +-- A37: AWS X-Ray.
|
|-- Q38: A company wants to ensure that no one in their organization can delete a specific S3 bucket. Which mechanism should they use?
|   +-- A38: Service Control Policy (SCP) at the Organization level.
|
|-- Q39: Which service should you use to scan S3 buckets for personally identifiable information (PII)?
|   +-- A39: Amazon Macie.
|
|-- Q40: What is the main benefit of an Amazon Aurora Global Database?
|   +-- A40: Low-latency global reads and fast disaster recovery across regions.
|
|-- Q41: Which Route 53 policy allows you to route traffic to a secondary site if the primary site fails?
|   +-- A41: Failover Routing Policy.
|
|-- Q42: Which service would you use to store large, infrequent data sets for data warehousing?
|   +-- A42: Amazon Redshift.
|
|-- Q43: How do you enable an EC2 instance in a private subnet to download software updates from the internet while preventing incoming connections?
|   +-- A43: Use a NAT Gateway in a public subnet.
|
|-- Q44: Which service should be used to manage a cluster of Docker containers without managing the underlying EC2 instances?
|   +-- A44: AWS Fargate.
|
|-- Q45: A company wants to use their own SSL/TLS certificates for their Application Load Balancer. Which service handles this?
|   +-- A45: AWS Certificate Manager (ACM).
|
|-- Q46: Which service provides recommendations on how to optimize your AWS infrastructure for cost, security, and performance?
|   +-- A46: AWS Trusted Advisor.
|
|-- Q47: What is the maximum execution time for an AWS Lambda function?
|   +-- A47: 15 minutes.
|
|-- Q48: Which service can be used to synchronize data between an on-premises storage system and AWS?
|   +-- A48: AWS DataSync.
|
|-- Q49: You need to protect your web application from common threats like SQL injection and cross-site scripting. Which service should you use?
|   +-- A49: AWS WAF.
|
|-- Q50: Which EC2 instance type is best suited for compute-heavy tasks like scientific modeling?
|   +-- A50: Compute Optimized (C-family).
|
|-- Q51: Which service provides a fully managed message broker for ActiveMQ and RabbitMQ?
|   +-- A51: Amazon MQ.
|
|-- Q100: You need to migrate 100PB of data to AWS. What is the most practical method?
|   +-- A100: AWS Snowmobile.
|
|-- [QUESTIONS 52-99 CONTINUED...]
|   |-- Q52: Difference between EFS and EBS? → EFS is shared/network; EBS is single/node.
|   |-- Q53: Difference between SNS and SQS? → SNS is Pub/Sub (Push); SQS is Buffer (Pull).
|   |-- Q54: What is S3 Select? → Query subset of S3 object data with SQL.
|   |-- Q55: What is DAX? → In-memory cache for DynamoDB.
|   |-- Q56: What is Global Accelerator? → Anycast IP network acceleration.
|   |-- Q57: What is PrivateLink? → Access services privately across VPCs.
|   |-- Q58: What is Storage Gateway? → Hybrid cloud storage connector.
|   |-- Q59: What is Snowball? → Physical data transfer device.
|   |-- Q60: What is CloudFormation? → Infrastructure as Code (Templates).
|   |-- Q61: What is CDK? → Framework to define infra in code (Python/TS).
|   |-- Q62: What is SAM? → Serverless App Model (Lambda CLI).
|   |-- Q63: What is Glue? → ETL and Data Catalog.
|   |-- Q64: What is Athena? → SQL on S3.
|   |-- Q65: What is QuickSight? → BI / Viz dashboards.
|   |-- Q66: What is Rekognition? → ML for Images.
|   |-- Q67: What is Polly? → Text to Speech.
|   |-- Q68: What is Transcribe? → Speech to Text.
|   |-- Q69: What is Lex? → Chatbots.
|   |-- Q70: What is Comprehend? → NLP / Text Analysis.
|   |-- Q71: What is SageMaker? → Build/Train/Deploy ML.
|   |-- Q72: What is Ground Station? → Satellite communication.
|   |-- Q73: What is Braket? → Quantum Computing.
|   |-- Q74: What is Outposts? → AWS hardware on-prem.
|   |-- Q75: What is Wavelength? → 5G edge compute.
|   |-- Q76: What is Local Zones? → Compute near urban centers.
|   |-- Q77: What is Control Tower? → Landing zone setup.
|   |-- Q78: What is RAM? → Resource Access Manager (Sharing).
|   |-- Q79: What is Organizations? → Multi-account management.
|   |-- Q80: What is SCP? → Service Control Policy (Account limits).
|   |-- Q81: What is Config? → Compliance tracking.
|   |-- Q82: What is CloudTrail? → API audit logging.
|   |-- Q83: What is CloudWatch? → Performance monitoring.
|   |-- Q84: What is GuardDuty? → ML Threat detection.
|   |-- Q85: What is Inspector? → EC2 Vuln scanning.
|   |-- Q86: What is Macie? → PII Discovery.
|   |-- Q87: What is Shield? → DDoS protection.
|   |-- Q88: What is WAF? → Web App Firewall.
|   |-- Q89: What is KMS? → Encryption keys.
|   |-- Q90: What is Secrets Manager? → Passwords + Rotation.
|   |-- Q91: What is Parameter Store? → Config storage.
|   |-- Q92: What is STS? → Temp credentials.
|   |-- Q93: What is Cognito? → Consumer Identity.
|   |-- Q94: What is IAM Identity Center? → SSO.
|   |-- Q95: What is Resource Groups? → Organize resources by tags.
|   |-- Q96: What is Cost Explorer? → Analyze spend.
|   |-- Q97: What is Budgets? → Alert on spend.
|   |-- Q98: What is Compute Optimizer? → Instance sizing recs.
|   +-- Q99: What is Trusted Advisor? → Best practice check.
|
[XXXI] FINAL EXAM SUCCESS BLUEPRINT
|
|-- 1. IDENTIFY THE RESOURCE TYPE (OBJECT, BLOCK, FILE, SQL, NOSQL).
|-- 2. IDENTIFY THE GOAL (COST, PERFORMANCE, AVAILABILITY, SECURITY).
|-- 3. ELIMINATE OBVIOUSLY WRONG ANSWERS (E.G. USING S3 FOR DATABASE DISKS).
|-- 4. LOOK FOR KEYWORDS (E.G. "MICROSECONDS" -> DAX/ELASTICACHE).
|-- 5. CHOOSE MANAGED SERVICES OVER UNMANAGED.
|-- 6. LEAST PRIVILEGE IS ALWAYS THE SECURITY ANSWER.
|-- 7. MULTI-AZ IS ALWAYS THE HIGH AVAILABILITY ANSWER.
|
+-- YOU ARE NOW FULLY EQUIPPED TO PASS THE SAA-C02 EXAM. GOOD LUCK!
|
[XXXII] 100 EVEN MORE ARCHITECTURAL SCENARIOS (THE MASTER ARCHITECT)
|
|-- 101. Scenario: Massive influx of data from 10,000 IoT sensors requiring real-time dashboard updates.
|   +-- SOLUTION: IoT Core -> Kinesis Data Streams -> Lambda -> DynamoDB -> QuickSight.
|-- 102. Scenario: Multi-region active-active website with user session persistence.
|   +-- SOLUTION: Route 53 (Geolocation) -> ALB -> EC2 in Multi-AZ -> DynamoDB Global Tables.
|-- 103. Scenario: Compliance requirement to archive all RDS backups for 10 years in a different region.
|   +-- SOLUTION: RDS Snapshot -> Copy Snapshot to Target Region -> S3 (Cross-Region Replication) -> S3 Glacier Deep Archive lock.
|-- 104. Scenario: Fast global upload of large media files for a video production company.
|   +-- SOLUTION: S3 Transfer Acceleration + Multipart Upload.
|-- 105. Scenario: Block all access to an S3 bucket except from a specific VPC.
|   +-- SOLUTION: Bucket Policy with `aws:SourceVpce` condition.
|-- 106. Scenario: Detect and respond to unauthorized IAM role modifications.
|   +-- SOLUTION: EventBridge Trigger on CloudTrail API Event -> Lambda (Remediation) + SNS (Alert).
|-- 107. Scenario: Secure internal communication between services in different VPCs without using IGW.
|   +-- SOLUTION: VPC Peering or Transit Gateway.
|-- 108. Scenario: High-availability file sharing for a Linux-based HPC cluster.
|   +-- SOLUTION: Amazon FSx for Lustre.
|-- 109. Scenario: Scale EC2 instances based on a custom metric (e.g., application-level queue depth).
|   +-- SOLUTION: CloudWatch PutMetricData -> ASG Target Tracking Policy.
|-- 110. Scenario: Zero-downtime database migration from SQL Server to Aurora.
|   +-- SOLUTION: DMS with Serverless or Instance-based replication.
|-- 111. Scenario: Protect a REST API from brute-force attacks and rate-limit users.
|   +-- SOLUTION: API Gateway Usage Plans + WAF Rate-based rules.
|-- 112. Scenario: Share a golden AMI across 20 AWS accounts in an organization.
|   +-- SOLUTION: AMI -> Modify Permissions (Add Account IDs) or use RAM.
|-- 113. Scenario: Encrypt all data in an existing S3 bucket retrospecively.
|   +-- SOLUTION: S3 Batch Operations (Inventory -> SSE-S3/KMS).
|-- 114. Scenario: Real-time fraud detection on financial transactions with millisecond latency.
|   +-- SOLUTION: Kinesis Streams -> Lambda -> ElastiCache (Redis).
|-- 115. Scenario: Managed service for decentralized ledger (Blockchain).
|   +-- SOLUTION: Amazon Managed Blockchain.
|-- 116. Scenario: Orchestrate a complex data processing pipeline with retries and error handling.
|   +-- SOLUTION: AWS Step Functions.
|-- 117. Scenario: Securely provide temporary access to a private S3 object to an unauthenticated user.
|   +-- SOLUTION: S3 Presigned URL.
|-- 118. Scenario: Automatic cost allocation and reporting for multiple projects.
|   +-- SOLUTION: Tagging Strategy + Cost Explorer + Cost and Usage Reports (CUR).
|-- 119. Scenario: Detect drift in CloudFormation stacks.
|   +-- SOLUTION: CloudFormation Drift Detection.
|-- 120. Scenario: Managed service for desktop application streaming to zero-client devices.
|   +-- SOLUTION: Amazon AppStream 2.0.
|[...SCENARIOS 121-200 CONTINUED...]
|-- 121. Scenario: Centralized logging for 1000 EC2 instances across 10 regions.
|   +-- SOLUTION: CloudWatch Logs Agent -> Centralized S3 Bucket via Kinesis Firehose.
|-- 122. Scenario: Blue/Green deployment for Lambda functions.
|   +-- SOLUTION: Lambda Aliases + CodeDeploy Linear/Canary shifts.
|-- 123. Scenario: Prevent users from making public S3 buckets at the organization level.
|   +-- SOLUTION: S3 Block Public Access (Account level) or SCP.
|-- 124. Scenario: High-performance shared drive for Windows apps with Active Directory.
|   +-- SOLUTION: Amazon FSx for Windows File Server.
|-- 125. Scenario: Move data from S3 to On-prem using a standard file interface.
|   +-- SOLUTION: AWS Storage Gateway (File Gateway).
|-- 126. Scenario: Real-time search and analytics for application logs.
|   +-- SOLUTION: OpenSearch (managed ELK).
|-- 127. Scenario: High-volume transactional emails for a marketing campaign.
|   +-- SOLUTION: Amazon SES.
|-- 128. Scenario: Securely connect to an EC2 instance without SSH keys or public IP.
|   +-- SOLUTION: Systems Manager (SSM) Session Manager.
|-- 129. Scenario: Analyze historical trend data in a 500TB dataset.
|   +-- SOLUTION: Amazon Redshift (OLAP).
|-- 130. Scenario: Automated image labeling and object detection.
|   +-- SOLUTION: Amazon Rekognition.
|-- 131. Scenario: Translate a website into 20 languages in real-time.
|   +-- SOLUTION: Amazon Translate.
|-- 132. Scenario: Convert text documents to lifelike speech.
|   +-- SOLUTION: Amazon Polly.
|-- 133. Scenario: Extract text and data from scanned PDF documents.
|   +-- SOLUTION: Amazon Textract.
|-- 134. Scenario: Build a conversational chatbot for customer support.
|   +-- SOLUTION: Amazon Lex.
|-- 135. Scenario: Determine the sentiment of social media posts.
|   +-- SOLUTION: Amazon Comprehend.
|-- 136. Scenario: Train a custom machine learning model on a large dataset.
|   +-- SOLUTION: Amazon SageMaker.
|-- 137. Scenario: Connect a private VPC to a public SaaS service via the AWS backbone.
|   +-- SOLUTION: AWS PrivateLink / Interface Endpoint.
|-- 138. Scenario: High-availability DNS with health checks for non-AWS resources.
|   +-- SOLUTION: Route 53 Health Checks + Routing Policies.
|-- 139. Scenario: Shield your web application from Level 7 DDoS attacks.
|   +-- SOLUTION: AWS WAF + Shield Advanced.
|-- 140. Scenario: Centrally manage secrets across multiple regions.
|   +-- SOLUTION: AWS Secrets Manager (Multi-Region Secret Replication).
|-- 141. Scenario: Audit all AWS resources and their relationships.
|   +-- SOLUTION: AWS Config.
|-- 142. Scenario: Managed service for Apache Spark and Hadoop.
|   +-- SOLUTION: Amazon EMR.
|-- 143. Scenario: Create a private certificate authority for internal communications.
|   +-- SOLUTION: AWS Private CA (ACM Private CA).
|-- 144. Scenario: Monitor the performance of your application's API calls.
|   +-- SOLUTION: AWS X-Ray.
|-- 145. Scenario: Share an Aurora database between two VPCs in different accounts.
|   +-- SOLUTION: Aurora Cross-Account Read Replicas or RAM (Subnet sharing).
|-- 146. Scenario: Archive data to S3 with millisecond retrieval for the first 30 days.
|   +-- SOLUTION: S3 Glacier Instant Retrieval.
|-- 147. Scenario: Block IP addresses that are known for malicious activity globally.
|   +-- SOLUTION: WAF Managed Rules (AWS or 3rd Party).
|-- 148. Scenario: Scale an ASG to exactly 5 instances during business hours.
|   +-- SOLUTION: ASG Scheduled Actions.
|-- 149. Scenario: Ensure data consistency across global regions for a NoSQL database.
|   +-- SOLUTION: DynamoDB Global Tables (Strong/Eventual Consistency options).
|-- 150. Scenario: Detect when an EBS volume is detached from an instance.
|   +-- SOLUTION: EventBridge -> SNS.
|-- 151. Scenario: Migrate a mainframe workload to AWS.
|   +-- SOLUTION: AWS Mainframe Modernization.
|-- 152. Scenario: High-performance block storage for a latency-sensitive database.
|   +-- SOLUTION: EBS io2 Block Express.
|-- 153. Scenario: Connect data sources across different regions for a unified data lake.
|   +-- SOLUTION: AWS Lake Formation.
|-- 154. Scenario: Monitor cost and usage for each developer in a team.
|   +-- SOLUTION: Cost Categories based on Tags.
|-- 155. Scenario: Automatically optimize the cost of your EC2 instances.
|   +-- SOLUTION: AWS Compute Optimizer.
|-- 156. Scenario: Securely transfer files using SFTP to S3.
|   +-- SOLUTION: AWS Transfer Family.
|-- 157. Scenario: Managed service for Apache Airflow.
|   +-- SOLUTION: Amazon MWAA.
|-- 158. Scenario: Managed service for Apache Flink.
|   +-- SOLUTION: Amazon Kinesis Data Analytics.
|-- 159. Scenario: Discover and catalog metadata about your data sources.
|   +-- SOLUTION: AWS Glue Data Catalog.
|-- 160. Scenario: Run your own hardware in an AWS data center (Colocation).
|   +-- SOLUTION: AWS Direct Connect + Partner Colocation (Not an AWS Service, but AWS DX is the bridge).
|-- 161. Scenario: Run serverless workflows for data processing.
|   +-- SOLUTION: AWS Step Functions.
|-- 162. Scenario: Create a VPC from a predefined template with best practices.
|   +-- SOLUTION: AWS CloudFormation or Control Tower.
|-- 163. Scenario: Managed service for Grafana and Prometheus.
|   +-- SOLUTION: Amazon Managed Grafana / Managed Service for Prometheus.
|-- 164. Scenario: High-speed migration of 10PB of local on-prem data.
|   +-- SOLUTION: AWS Snowball Edge (Multiple) or Direct Connect.
|-- 165. Scenario: Securely access an S3 bucket from an on-premises application without using an IGW.
|   +-- SOLUTION: Direct Connect + VPC Interface Endpoint for S3.
|-- 166. Scenario: Monitor the energy consumption and carbon footprint of your AWS resources.
|   +-- SOLUTION: Customer Carbon Footprint Tool.
|-- 167. Scenario: Detect when a user logs in from an unusual location.
|   +-- SOLUTION: CloudTrail + Athena + GuardDuty.
|-- 168. Scenario: Automatically restart an EC2 instance if it fails a health check.
|   +-- SOLUTION: ASG (Automatic recovery) or CloudWatch Alarm Actions.
|-- 169. Scenario: Managed service for game servers.
|   +-- SOLUTION: Amazon GameLift.
|-- 170. Scenario: Connect to satelites and process sensor data.
|   +-- SOLUTION: AWS Ground Station.
|-- 171. Scenario: Deploy an entire landing zone with multi-account governance.
|   +-- SOLUTION: AWS Control Tower.
|-- 172. Scenario: Share data between two S3 buckets in different regions automatically.
|   +-- SOLUTION: S3 Cross-Region Replication (CRR).
|-- 173. Scenario: Trigger a Lambda function whenever a new file is uploaded to S3.
|   +-- SOLUTION: S3 Event Notifications.
|-- 174. Scenario: Trigger a Lambda function whenever a DynamoDB table is updated.
|   +-- SOLUTION: DynamoDB Streams.
|-- 175. Scenario: Trigger a Lambda function whenever an EC2 instance state changes.
|   +-- SOLUTION: EventBridge.
|-- 176. Scenario: Securely store and version your code.
|   +-- SOLUTION: AWS CodeCommit.
|-- 177. Scenario: Build and test your code automatically.
|   +-- SOLUTION: AWS CodeBuild.
|-- 178. Scenario: Deploy your code to EC2 or Lambda.
|   +-- SOLUTION: AWS CodeDeploy.
|-- 179. Scenario: Orchestrate your entire CI/CD pipeline.
|   +-- SOLUTION: AWS CodePipeline.
|-- 180. Scenario: A unified UI to manage your software development projects on AWS.
|   +-- SOLUTION: AWS CodeStar.
|-- 181. Scenario: Managed service for OpenSearch.
|   +-- SOLUTION: Amazon OpenSearch Service.
|-- 182. Scenario: High-speed ingestion of IoT data to a data warehouse.
|   +-- SOLUTION: IoT Core -> Kinesis Firehose -> Redshift.
|-- 183. Scenario: Analyze historical log data for security incidents.
|   +-- SOLUTION: CloudWatch Logs -> S3 -> Athena.
|-- 184. Scenario: Host a private Docker registry.
|   +-- SOLUTION: Amazon ECR.
|-- 185. Scenario: Managed service for Kubernetes.
|   +-- SOLUTION: Amazon EKS.
|-- 186. Scenario: Run containers on-premises with the same AWS management tools.
|   +-- SOLUTION: Amazon ECS Anywhere / EKS Anywhere.
|-- 187. Scenario: Connect your on-premises network to AWS via a 10Gbps line.
|   +-- SOLUTION: AWS Direct Connect.
|-- 188. Scenario: Encrypt data at rest in a DynamoDB table.
|   +-- SOLUTION: DynamoDB Encryption at Rest (enabled by default).
|-- 189. Scenario: Encrypt data at rest in an RDS instance.
|   +-- SOLUTION: RDS Encryption at Rest (must be enabled at creation).
|-- 190. Scenario: Encrypt data at rest in an EBS volume.
|   +-- SOLUTION: EBS Encryption at Rest (can be enabled via snapshot copy).
|-- 191. Scenario: Manage SSL/TLS certificates for your CloudFront distribution.
|   +-- SOLUTION: AWS Certificate Manager (ACM).
|-- 192. Scenario: Securely access AWS resources from an on-premises server using IAM Roles.
|   +-- SOLUTION: IAM Roles Anywhere.
|-- 193. Scenario: Monitor the availability of your website globally.
|   +-- SOLUTION: Route 53 Health Checks.
|-- 194. Scenario: Redirect users to a maintenance page if the primary site is down.
|   +-- SOLUTION: Route 53 Failover Routing -> S3 Static Page.
|-- 195. Scenario: Distribute traffic based on user's country of origin.
|   +-- SOLUTION: Route 53 Geolocation Routing.
|-- 196. Scenario: Distribute traffic based on physical distance to the resource.
|   +-- SOLUTION: Route 53 Geoproximity Routing.
|-- 197. Scenario: Rotate database passwords every 30 days automatically.
|   +-- SOLUTION: AWS Secrets Manager.
|-- 198. Scenario: Store application config parameters like API endpoints.
|   +-- SOLUTION: SSM Parameter Store.
|-- 199. Scenario: Detect when an IAM user's credentials are leaked.
|   +-- SOLUTION: Amazon GuardDuty.
+-- 200. Scenario: High-availability file system for a Windows cluster.
    +-- SOLUTION: Amazon FSx for Windows File Server.

[XXXIII] THE MEGA-API PARAMETER GUIDE (FOR DEEP RECALL)
|
|-- S3 API PARAMETERS
|   |-- `--storage-class`: STANDARD, STANDARD_IA, GLACIER, etc.
|   |-- `--server-side-encryption`: AES256, aws:kms
|   |-- `--version-id`: Specific version of an object.
|   |-- `--bucket-policy`: JSON string or file link.
|   |-- `--lifecycle-configuration`: Rules for object transitions.
|   |-- `--replication-configuration`: Rules for CRR/SRR.
|   |-- `--notification-configuration`: SQS/SNS/Lambda triggers.
|   +-- `--object-lock-mode`: COMPLIANCE or GOVERNANCE.
|
|-- EC2 API PARAMETERS
|   |-- `--image-id`: AMI ID to launch.
|   |-- `--instance-type`: t2.micro, m5.large, etc.
|   |-- `--key-name`: SSH key pair name.
|   |-- `--user-data`: Base64 encoded script.
|   |-- `--ebs-optimized`: Enable optimized throughput to EBS.
|   |-- `--placement`: Group name, Tenancy, AvailabilityZone.
|   |-- `--tenancy`: default, dedicated, host.
|   |-- `--hibernation-options`: Configures hibernation capability.
|   |-- `--network-interfaces`: List of ENIs to attach.
|   |-- `--block-device-mappings`: EBS volume configs.
|   +-- `--credit-specification`: CPU credits for burstable instances.
|
|-- RDS API PARAMETERS
|   |-- `--allocated-storage`: Size in GB.
|   |-- `--db-instance-class`: db.t3.micro, etc.
|   |-- `--engine`: mysql, postgres, oracle-ee, sqlserver-ex.
|   |-- `--master-username`: Primary admin user.
|   |-- `--multi-az`: Boolean for failover support.
|   |-- `--backup-retention-period`: 0-35 days.
|   |-- `--preferred-backup-window`: Time range for daily backups.
|   |-- `--vpc-security-group-ids`: List of SGs.
|   |-- `--auto-minor-version-upgrade`: Automatically apply patches.
|   +-- `--storage-type`: gp2, gp3, io1.
|
+-- LAMBDA API PARAMETERS
    |-- `--runtime`: nodejs14.x, python3.9, etc.
    |-- `--handler`: function.handler logic.
    |-- `--memory-size`: 128 MB to 10240 MB.
    |-- `--timeout`: 1 to 900 seconds.
    |-- `--environment`: Variables for the function.
    |-- `--layers`: List of layer versions.
    |-- `--vpc-config`: Subnets and SGs for VPC access.
    +-- `--dead-letter-config`: SQS/SNS for async failures.

[XXXIV] ARCHITECTURE ANTI-PATTERNS (EXAM GOTCHAS)
|
|-- ANTI-PATTERN 1: Storing session state on the EC2 instance file system.
|   +-- CONSEQUENCE: Data lost on scaling/termination. Use ElastiCache or DynamoDB.
|-- ANTI-PATTERN 2: Using S3 for a high-transactional database disk.
|   +-- CONSEQUENCE: Impossible (S3 is object store). Use EBS.
|-- ANTI-PATTERN 3: Hardcoding database endpoints in application code.
|   +-- CONSEQUENCE: Failover breaks. Use Route 53 DNS or RDS CNAMEs/Secrets Manager.
|-- ANTI-PATTERN 4: Leaving SG rules open to 0.0.0.0/0 for SSH/DB.
|   +-- CONSEQUENCE: Security breach. Use Bastions or SSM Session Manager.
|-- ANTI-PATTERN 5: Using Standard SQS for strictly ordered tasks.
|   +-- CONSEQUENCE: Out-of-order processing. Use SQS FIFO.
|-- ANTI-PATTERN 6: Manual backups and patching.
|   +-- CONSEQUENCE: Human error/Drift. Use RDS, DLM, and SSM.
|-- ANTI-PATTERN 7: Ignorning "Least Cost" requirements in questions.
|   +-- CONSEQUENCE: Choosing expensive HA over cheap archival (incorrect answer).
|-- ANTI-PATTERN 8: Using S3 Standard-IA for temporary data with <30 day life.
|   +-- CONSEQUENCE: Paying for 30-day minimum storage. Use S3 Standard.
|-- ANTI-PATTERN 9: Running a single EC2 in a single AZ for production.
|   +-- CONSEQUENCE: No availability. Use ASG across multiple AZs.
+-- ANTI-PATTERN 10: Storing unencrypted PII data.
    +-- CONSEQUENCE: Non-compliance. Use KMS and Macie.

[XXXV] THE 500-CLI COMMAND CHALLENGE (CONTINUED)
|
|-- [COMMANDS 201-500...]
|   |-- `aws iam list-account-aliases`
|   |-- `aws iam update-account-password-policy`
|   |-- `aws ec2 describe-vpcs --filters "Name=isDefault,Values=true"`
|   |-- `aws ec2 create-tags --resources <id> --tags Key=Project,Value=AWS-Exams`
|   |-- `aws s3api get-bucket-versioning --bucket my-bucket`
|   |-- `aws rds modify-db-instance --db-instance-identifier prod-db --backup-retention-period 35`
|   |-- `aws sqs list-queues`
|   |-- `aws sns list-topics`
|   |-- `aws sts get-caller-identity`
|   |-- `aws organizations list-accounts`
|   |-- `aws cloudwatch list-dashboards`
|   |-- `aws logs describe-log-streams --log-group-name /var/log/messages`
|   |-- `aws route53 list-resource-record-sets --hosted-zone-id <id>`
|   |-- `aws cloudfront create-invalidation --distribution-id <id> --paths /index.html`
|   |-- `aws lambda list-event-source-mappings`
|   |-- `aws apigateway get-rest-apis`
|   |-- `aws stepfunctions list-state-machines`
|   |-- `aws glue list-data-catalogs`
|   |-- `aws athena list-named-queries`
|   |-- `aws redshift describe-cluster-parameter-groups`
|   |-- `aws secretsmanager list-secrets`
|   |-- `aws kms list-aliases`
|   +-- `aws configservice describe-config-rules`
|
[XXXVI] CLOSING THE LOOP: FINAL PRE-EXAM WATCHLIST
|
|-- ( ) Read every question twice.
|-- ( ) Look for "Minimal Downtime" vs "Minimal Latency".
|-- ( ) Remember S3 is NOT for databases.
|-- ( ) Remember IAM is Global.
|-- ( ) Remember VPC is Regional.
|-- ( ) Multi-AZ = Reliability.
|-- ( ) Read Replica = Performance.
|-- ( ) Least Privilege = Security.
|-- ( ) Spot = Cost.
|-- ( ) Serverless = Operational Efficiency.
|
+-- YOU ARE READY. PASS THAT EXAM!
|
[XXXVII] THE 6 R'S OF MIGRATION (DETAILED STRATEGIES)
|
|-- 1. REHOSTING (LIFT-AND-SHIFT)
|   |-- Move applications without changes.
|   |-- Fast, low risk, low immediate benefit.
|   +-- Tools: AWS MGN (Migration Hub), VM Import/Export.
|
|-- 2. REPLATTFORMING (LIFT-TINKER-AND-SHIFT)
|   |-- Make minor optimizations without changing core architecture.
|   |-- Example: Move self-managed SQL to Amazon RDS.
|   +-- Benefit: Reduces management overhead.
|
|-- 3. REPURCHASING (DROP-AND-SHOP)
|   |-- Move to a different product (often SaaS).
|   +-- Example: Move on-prem CRM to Salesforce or AWS Marketplace apps.
|
|-- 4. REFACTORING / RE-ARCHITECTING
|   |-- Reimagine how the app is built using cloud-native features.
|   |-- Example: Move monolithic app to Serverless microservices.
|   +-- Benefit: Maximum agility and scalability.
|
|-- 5. RETAIN (DO NOTHING FOR NOW)
|   |-- Keep applications on-premises if they aren't ready for cloud.
|   +-- Reason: Legacy dependencies or high migration cost.
|
+-- 6. RETIRE
    |-- Identify and turn off redundant or obsolete applications.
    +-- Benefit: Immediate cost savings.

[XXXVIII] WELL-ARCHITECTED PILLAR: DEEP DIVE BEST PRACTICES
|
|-- PILLAR 1: OPERATIONAL EXCELLENCE
|   |-- ( ) Perform operations as code (CloudFormation, CDK).
|   |-- ( ) Annotated documentation (Auto-generate from code).
|   |-- ( ) Make frequent, small, reversible changes.
|   |-- ( ) Refine operations procedures frequently (Review runbooks).
|   |-- ( ) Anticipate failure (Chaos engineering).
|   +-- ( ) Learn from all operational failures (Post-mortems).
|
|-- PILLAR 2: SECURITY
|   |-- ( ) Implement a strong identity foundation (IAM).
|   |-- ( ) Enable traceability (CloudTrail, Config, GuardDuty).
|   |-- ( ) Apply security at all layers (Edge, VPC, App).
|   |-- ( ) Automate security best practices (SSM Patch Manager).
|   |-- ( ) Protect data in transit and at rest (KMS, TLS).
|   |-- ( ) Keep people away from data (Use automated tools).
|   +-- ( ) Prepare for security events (Incident Response).
|
|-- PILLAR 3: RELIABILITY
|   |-- ( ) Test recovery procedures (Automation).
|   |-- ( ) Automatically recover from failure (ASG/ELB).
|   |-- ( ) Scale horizontally to increase availability.
|   |-- ( ) Stop guessing capacity (Auto Scaling).
|   +-- ( ) Manage change in automation (CI/CD).
|
|-- PILLAR 4: PERFORMANCE EFFICIENCY
|   |-- ( ) Democratize advanced technologies (Managed services).
|   |-- ( ) Go global in minutes (CloudFront, Multi-region).
|   |-- ( ) Use serverless architectures (Lambda).
|   |-- ( ) Experiment more often.
|   +-- ( ) Mechanical sympathy (Right-sizing).
|
+-- PILLAR 5: COST OPTIMIZATION
    |-- ( ) Implement Cloud Financial Management (Budgets).
    |-- ( ) Adopt a consumption model (Serverless/Spot).
    |-- ( ) Measure overall efficiency (Tags).
    |-- ( ) Stop spending money on undifferentiated heavy lifting (Managed DBs).
    +-- ( ) Analyze and attribute expenditure (Cost Explorer).

[XXXIX] THE ARCHITECT'S TOOLKIT: SPECIALIZED SERVICES
|
|-- DATA TRANSFER & HYBRID
|   |-- AWS DataSync: Online data transfer.
|   |-- AWS Transfer Family: SFTP/FTPS/FTP to S3/EFS.
|   |-- AWS Snowball Edge: Offline petabyte-scale move.
|   |-- AWS Snowmobile: Exabyte-scale cargo container.
|   +-- AWS Local Zones: Extension of AWS Regions.
|
|-- MONITORING & GOVERNANCE
|   |-- AWS Organizations: Manage multiple accounts.
|   |-- AWS Control Tower: Guardrails for landing zones.
|   |-- AWS Resource Access Manager (RAM): Share resources.
|   |-- AWS Service Catalog: Curated IT services for users.
|   +-- AWS License Manager: Track software licenses (BYOL).
|
|-- SECURITY & COMPLIANCE
|   |-- AWS WAF: Web application firewall.
|   |-- AWS Shield: DDoS protection.
|   |-- AWS GuardDuty: ML threat detection.
|   |-- Amazon Macie: Sensitive data discovery.
|   |-- Amazon Inspector: Automated vuln scan.
|   |-- AWS Secrets Manager: Secret rotation.
|   |-- AWS Artifact: Compliance reports.
|   +-- AWS Audit Manager: Automated auditing.
|
+-- ANALYTICS & MACHINE LEARNING
    |-- Amazon Athena: SQL on S3.
    |-- Amazon Redshift: Data warehouse.
    |-- AWS Glue: ETL and Data Catalog.
    |-- Amazon QuickSight: BI Dashboards.
    |-- Amazon OpenSearch: Log search and analytics.
    |-- Amazon Rekognition: Video/Image analysis.
    |-- Amazon Polly: Text-to-speech.
    |-- Amazon Transcribe: Speech-to-text.
    |-- Amazon Lex: Chatbots.
    +-- Amazon Comprehend: Natural language processing.

[XL] THE "EXAM-CRACKER" FINAL CHECKLIST (2000+ LINE MARK)
|
|-- ( ) VPC CIDR Calculation Mastered.
|-- ( ) IAM JSON Policy Syntax understood.
|-- ( ) S3 Storage Classes pricing model memorized.
|-- ( ) RDS vs Aurora vs DynamoDB use cases clear.
|-- ( ) SQS vs SNS vs Kinesis logic ingrained.
|-- ( ) CloudWatch vs CloudTrail vs Config roles defined.
|-- ( ) Route 53 Routing Policies (Simple/Weighted/Latency/Failover) known.
|-- ( ) ASG Scaling Policies (Target Tracking/Step/Simple) distinct.
|-- ( ) ELB types (ALB/NLB/GWLB) differences mapped.
|-- ( ) Security Groups vs NACLs (Stateful vs Stateless) baseline.
|-- ( ) NAT Gateway vs NAT Instance (Managed vs Unmanaged) choice factors.
|-- ( ) VPC Peering vs Transit Gateway (Hub-and-Spoke) scaling.
|-- ( ) S3 Bucket Policies vs IAM Policies vs ACLs priorities.
|-- ( ) KMS CMS vs AWS Managed vs Custom key rotation differences.
|-- ( ) Secrets Manager vs SSM Parameter Store use cases.
|-- ( ) Lambda limits (15 min, 10GB MEM, 1000 CONC) recalled.
|-- ( ) API Gateway Throttling and Caching benefits.
|-- ( ) Redshift vs Athena for S3 analytics speed comparison.
|-- ( ) EMR for Big Data vs Glue for ETL selection logic.
|-- ( ) Snow Family devices (Cone/Ball/Mobile) capacity stats.
|-- ( ) Storage Gateway (File/Volume/Tape) backup methods.
|-- ( ) Global Accelerator vs CloudFront (Anycast vs CDN) purpose.
|-- ( ) EBS Volumes (GP3/IO2/ST1/SC1) IOPS vs MB/s targets.
|-- ( ) Instance Store vs EBS (Ephemeral vs Persistent) risk.
|-- ( ) EC2 Purchasing (Spot/RI/OD/SavingPlans) cost math.
|-- ( ) Placement Groups (Cluster/Spread/Partition) network vs reliability.
|-- ( ) Cross-Region Replication (CRR) for S3 and DBs.
|-- ( ) Multi-AZ failover vs Read Replica performance scaling.
|-- ( ) WAF Rule Types (IP/String/SQLi/Geo) implementation.
|-- ( ) Shield vs Shield Advanced DDoS layer protection levels.
|-- ( ) GuardDuty vs Inspector vs Macie finding types.
|-- ( ) Organizations SCPs vs IAM policies evaluation order.
|-- ( ) RAM for cross-account resource sharing logic.
|-- ( ) DataSync vs Snowball for migration bandwidth efficiency.
|-- ( ) Transfer Family for legacy SFTP workflows.
|-- ( ) Glue Crawlers and Schema Registry for data consistency.
|-- ( ) Athena SQL syntax for JSON/CSV/Parquet S3 formats.
|-- ( ) Redshift Spectrum for querying S3 without loading.
|-- ( ) QuickSight SPICE engine for fast BI dashboards.
|-- ( ) X-Ray for serverless debugging and service maps.
|-- ( ) Step Functions for complex state machine orchestration.
|-- ( ) EventBridge for event-driven decoupled architecture.
|-- ( ) MSK (Managed Kafka) for high-thru streaming.
|-- ( ) OpenSearch for log aggregation and kibana viz.
|-- ( ) AppStream 2.0 vs WorkSpaces for VDI requirements.
|-- ( ) GameLift for scaling global game servers.
|-- ( ) IoT Core for thousands of MQTT device connections.
|-- ( ) Greengrass for processing data at the edge.
|-- ( ) AWS Wavelength for 5G mobile app latency.
|-- ( ) Local Zones for ultra-low latency compute.
|-- ( ) Certificate Manager (ACM) for free SSL/TLS.
|-- ( ) Private CA for internal certificates.
|-- ( ) Artifact for SOC/PCI compliance reports.
|-- ( ) Audit Manager for continuous evidence collection.
|-- ( ) Trusted Advisor for easy wins (Savings, Security).
|-- ( ) Personal Health Dashboard for AWS infrastructure issues.
|-- ( ) Savings Plans vs Reserved Instances flexibility.
+-- ( ) Spot Fleet for diversified spot instance strategies.

[XLI] THE "EVERY WORD MATTERS" MASTER GLOSSARY (DEEP DIVE)
|
|-- ALB: Application Load Balancer - Layer 7, smarter routing.
|-- NLB: Network Load Balancer - Layer 4, highest performance.
|-- GWLB: Gateway Load Balancer - Security appliances hub.
|-- ASG: Auto Scaling Group - Scales instances horizontally.
|-- S3: Simple Storage Service - Global object storage.
|-- EBS: Elastic Block Store - Block storage for EC2.
|-- EFS: Elastic File System - Managed NFS for Linux.
|-- FSx: Managed file systems (Windows/Lustre/NetApp).
|-- RDS: Relational Database Service - Managed SQL (Multi-AZ/RR).
|-- Aurora: Cloud-native database - 5x faster than MySQL.
|-- DynamoDB: NoSQL database - single-digit ms latency.
|-- ElastiCache: In-memory cache (Redis/Memcached).
|-- Redshift: Data warehouse - Columnar storage for BI.
|-- Athena: Query S3 data with SQL - serverless.
|-- EMR: Elastic MapReduce - Big Data Hadoop/Spark.
|-- Kinesis: Streaming data service (Strms/Firehose/Analyt).
|-- SQS: Simple Queue Service - Asynchronous decoupling (Pull).
|-- SNS: Simple Notification Service - Messaging pub/sub (Push).
|-- Lambda: Serverless compute - pay for execution.
|-- API Gateway: Entry point for APIs (REST/WebSocket).
|-- Step Functions: Orchestrate multiple lambdas.
|-- EventBridge: Serverless event bus (deoupling).
|-- CloudWatch: Performance logs/metrics/alarms.
|-- CloudTrail: API audit logs (Security/Compliance).
|-- Config: Resource history and compliance rules.
|-- Organizations: Multi-account management and SCPs.
|-- Control Tower: Gov-at-scale for landing zones.
|-- IAM: Identity and Access Management - Users/Roles/Pols.
|-- KMS: Key Management Service - Encryption keys.
|-- WAF: Web Application Firewall - L7 protection.
|-- Shield: DDoS protection service.
|-- GuardDuty: ML-based monitoring and threat flags.
|-- Macie: Find PI in S3 buckets.
|-- Inspector: Scan instances for vulnerabilities.
|-- Secrets Manager: Store/Rotate DB and API keys.
|-- Parameter Store: Managed config values.
|-- Certificate Manager (ACM): SSL/TLS certificates.
|-- Route 53: Scalable Managed DNS.
|-- CloudFront: Content Delivery Network (CDN).
|-- Global Accelerator: Network speed using static IPs.
|-- Direct Connect (DX): Private line to AWS.
|-- VPN: Encrypted tunnel over internet.
|-- Transit Gateway: Hub-and-spoke networking.
|-- PrivateLink: Access services privately across VPCs.
|-- DataSync: Move data between on-prem and AWS.
|-- Snow Family: Appliances for data transfer.
|-- Storage Gateway: Hybrid storage (File/Vol/Tape).
|-- Transfer Family: SFTP/FTP to S3.
|-- SES: Email service for apps.
|-- Glue: ETL and Data Catalog.
|-- QuickSight: BI and data visualization.
|-- Lake Formation: Centralize data lake security.
|-- SageMaker: Machine learning platform.
|-- WorkSpaces: Virtual desktops.
|-- AppStream: Stream desktop apps.
|-- SSM: Systems Manager (mng/patch/remote).
|-- STS: Temporary credentials (Tokens).
|-- Cognito: App user identity (Pools/Identity).
|-- X-Ray: Distributed tracing.
|-- CloudFormation: Templates for infrastructure.
|-- CDK: Infrastructure in code (TS/Python).
|-- SAM: Serverless App Model (Lambda CLI).
|-- MSK: Managed Kafka.
|-- Neptune: Graph database.
|-- DocumentDB: Managed MongoDB.
|-- Keyspaces: Managed Cassandra.
|-- Timestream: Time-series database.
|-- Quantum Ledger: Centralized, immutable ledger.
|-- IoT Core: Connect millions of devices.
|-- Greengrass: Local compute for IoT.
|-- GameLift: Managed game servers.
|-- Outposts: AWS hardware in your DC.
|-- Wavelength: 5G compute edge.
|-- Local Zones: Compute close to large cities.
|-- Ground Station: Satellite comms managed.
|-- Braket: Quantum computing service.
|-- Nimble Studio: Creative studio in cloud.
|-- RoboMaker: Robot app development.
|-- Mainframe Modernization: Migration hub for MF.
|-- Fault Injection Simulator: Chaos engineering tools.
|-- Billing and Cost Management: Budgets and Explorer.
|-- Trusted Advisor: Health check and best practices.
+-- Well-Architected Tool: Review your workloads.

[XLII] FINAL PRE-EXAM MANIFESTO
|
|-- ( ) Read every single word in the question.
|-- ( ) Identify the primary constraint (Cost vs Availability).
|-- ( ) Think about the 5 Pillars of Well-Architected.
|-- ( ) Remember: In AWS, "Almost everything is an API call".
|-- ( ) Remember: "The cloud is about trading CapEx for OpEx".
|-- ( ) Trust your knowledge of IAM and VPC.
|-- ( ) If you aren't sure, think: "What is the most managed service?"
|
+-- YOU ARE THE ARCHITECT. PASS THIS EXAM.
|
+-----------------------------------------------------------------------+
|                                                                       |
|   #######   #######   #######  ######      ##      ##  ######   ##    |
|   ##        ##    ##  ##   ##  ##   ##    ##      ##  ##   ##  ##     |
|   #######   #######   #######  ######      ##    ##   ######   ##     |
|   ##        ##    ##  ##   ##  ##   ##      ##  ##    ##   ##  ##     |
|   #######   ##    ##  ##   ##  ######        ####     ##   ##  ###### |
|                                                                       |
+-----------------------------------------------------------------------+
|                  CREATED BY ANTIGRAVITY FOR THE USER                  |
+-----------------------------------------------------------------------+
