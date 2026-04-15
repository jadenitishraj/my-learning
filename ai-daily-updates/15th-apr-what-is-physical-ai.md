```
WHAT IS PHYSICAL AI — HOW ROBOTS LEARN & ADAPT IN REAL LIFE
│
├── Digital AI vs Physical AI
│   ├── Digital AI
│   │   ├── Chatbots
│   │   ├── Image generation
│   │   └── Code assistants
│   │       └── Lives in bits and bytes
│   └── Physical AI
│       ├── Crosses into world of atoms
│       ├── Perceive environment
│       ├── Reason about it
│       └── Take action
│
├── Before physical AI
│   ├── Robots used rule-based/scripted instructions
│   ├── Example: robotic arm on production line
│   │   ├── Welds same seam, same spot, 1000 times/day
│   │   ├── Super precise, super repeatable
│   │   └── Super limited
│   └── Only does what explicitly programmed
│
├── Robotic AI agents
│   ├── Equipped with language models
│   ├── General understanding of world
│   ├── Paired with reinforcement learning
│   │   └── Trial and error in simulated environments
│   └── Broad understanding + specialized skills
│
├── Physical AI is more than robotic arms
│   ├── Smart factories
│   │   └── Machines coordinate autonomously
│   ├── Energy grids
│   │   └── Optimize themselves
│   ├── Fleet of autonomous cars
│   └── Any physical system augmented with AI
│
├── Why now — bottlenecks broken
│   ├── 1. VLAs (Vision Language Action models)
│   │   ├── Vision = perceive world
│   │   ├── Language = reason about it
│   │   ├── Action = do something
│   │   ├── Before: robots could see and act, not reason
│   │   └── Open robotics foundation models
│   │       ├── Trained on massive datasets
│   │       ├── Tens of millions of hours of driving/robotics data
│   │       ├── Capture general knowledge of real-world physics
│   │       └── Openly available on Hugging Face
│   ├── 2. Sim-to-real gap closing
│   │   ├── Robots trained in simulation often fail in real world
│   │   ├── Real world is messier than simulation
│   │   └── World foundation models generate physics-aware synthetic data
│   │       └── Actually transfers to messy reality
│   └── 3. Compute efficiency
│       ├── Processing 20M hours of video
│       │   ├── Previously: ~3 years on CPUs
│       │   └── Now: weeks on current GPUs
│       └── Models can process much more data
│
├── How to train physical AI
│   ├── Step 1 — Simulated environment
│   │   ├── Virtual world for training at scale
│   │   ├── Example: robot assembling factory parts
│   │   ├── Simulation contains
│   │   │   ├── The robot itself
│   │   │   ├── Parts to work with
│   │   │   ├── Workbench
│   │   │   └── Varying lighting conditions
│   │   └── Domain randomization
│   │       ├── Varying part orientations
│   │       └── Different friction/humidity
│   ├── Step 2 — Reinforcement learning
│   │   ├── Trial and error
│   │   ├── Succeeds = reward
│   │   ├── Fails = no reward
│   │   └── Thousands/millions of interactions
│   ├── Step 3 — Deploy to real world
│   │   ├── Hits success threshold in simulation
│   │   └── Encounters stuff not in simulation
│   │       ├── Parts slightly different
│   │       └── Surfaces behave unexpectedly
│   └── Step 4 — Feedback loop
│       ├── Capture real-world data
│       ├── Feed back into simulation
│       ├── Train again, deploy again
│       └── Closes sim-to-real gap
│
└── Where we are now
    ├── Models are good enough
    ├── Compute is cheap enough
    ├── Simulation is realistic enough
    ├── Moving from research labs into real places
    │   ├── Factories
    │   ├── Warehouses
    │   └── Roads
    └── AI crossing from bits into atoms
```
