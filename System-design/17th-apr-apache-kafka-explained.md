```
APACHE KAFKA EXPLAINED
│
├── The Problem (Without Kafka)
│   ├── Microservices call each other directly
│   ├── Tight coupling between services
│   ├── Synchronous communication
│   │   └── One slow service backs up everything
│   ├── Single points of failure
│   │   └── 10min outage → 2hr order backlog
│   └── Data loss when services go down
│       └── e.g., analytics service down → lost sales data
│
├── What is Kafka
│   ├── Message broker sitting in the middle
│   ├── Like a post office for microservices
│   ├── Decouples services (no direct calls)
│   ├── Services hand off events & continue working
│   └── Not a database replacement
│
├── Core Concepts
│   ├── Events
│   │   ├── Simple key-value pair + metadata
│   │   └── e.g., "order placed for customer X"
│   │
│   ├── Producers
│   │   ├── Services that create & send events
│   │   ├── Use Kafka Producer API
│   │   └── e.g., Order service produces order events
│   │
│   ├── Consumers
│   │   ├── Services subscribed to topics
│   │   ├── Get notified when new events arrive
│   │   └── e.g., Notification, Inventory, Payment services
│   │
│   ├── Topics
│   │   ├── Group same type of events
│   │   ├── Like sections in a post office
│   │   ├── You define them (schema design)
│   │   └── Examples
│   │       ├── Orders topic
│   │       ├── Payments topic
│   │       └── Inventory topic
│   │
│   ├── Partitions
│   │   ├── Split topics for scalability
│   │   ├── Like adding more workers per section
│   │   ├── Multiple producers write in parallel
│   │   ├── You decide partitioning strategy
│   │   └── e.g., EU orders, US orders, Asia orders
│   │
│   ├── Consumer Groups
│   │   ├── Multiple instances of same service
│   │   ├── Grouped by group ID
│   │   ├── Process events in parallel
│   │   ├── Kafka auto-distributes partitions
│   │   └── If one stops, Kafka reassigns its work
│   │
│   └── Brokers
│       ├── Kafka servers that store data on disk
│       ├── Handle producer/consumer requests
│       └── Replicate data for fault tolerance
│
├── Event Chain Reactions
│   ├── One event triggers multiple actions
│   ├── Example: Order Placed
│   │   ├── → Notification service sends email
│   │   ├── → Inventory service updates stock
│   │   ├── → Payment service generates invoice
│   │   └── → Sales dashboard updates
│   └── Chain continues
│       ├── Inventory update → low stock check
│       └── Low stock → auto restock trigger
│
├── Streams API (Real-Time Analytics)
│   ├── Regular consumers process one event at a time
│   ├── Streams process continuous data flow
│   ├── Aggregations, joins, calculations
│   └── Use Cases
│       ├── Low inventory threshold alerts
│       ├── Real-time sales dashboards
│       └── Uber driver location updates
│
├── Kafka vs Traditional Message Brokers
│   ├── Traditional (like TV)
│   │   ├── Messages deleted after consumption
│   │   ├── Everyone reads at same pace
│   │   └── Miss it = lose it
│   └── Kafka (like Netflix)
│       ├── Persists events (configurable retention)
│       ├── Consumers read anytime, any pace
│       ├── Can replay events
│       └── Enables real-time + historical analytics
│
└── Coordination
    ├── Needs to track brokers, elect leaders
    ├── Previously: ZooKeeper (external)
    └── Now: KRaft (Kafka 3.0+)
        └── Built-in, no external dependency
```
