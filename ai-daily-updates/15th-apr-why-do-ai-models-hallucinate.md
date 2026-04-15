```
WHY DO AI MODELS HALLUCINATE
│
├── What are hallucinations
│   ├── AI makes stuff up
│   ├── Appears very confident
│   ├── Tries to convince you it's right
│   └── Worse than just making a mistake
│
├── How they show up
│   ├── Cite papers that don't exist
│   ├── Make up fake statistics
│   └── Get facts wrong about real people/events
│
├── Example
│   ├── Asked Claude about papers by Jared Kaplan
│   ├── Confidently gave answers
│   └── None of those titles actually exist
│
├── Why it's tricky
│   ├── Hard to anticipate
│   ├── Hard to catch
│   ├── Wrong answer looks like right one
│   └── Becoming more rare so people don't bother checking
│
├── Why it happens
│   ├── AI learns by reading huge amounts of text
│   ├── Gets good at predicting next words
│   │   └── Like phone suggesting next word as you type
│   ├── Obscure topics lack enough information
│   ├── AI tries to be helpful, takes a guess
│   ├── Sometimes that guess is wrong
│   └── Like a friend who read every popular book
│       ├── Takes pride in knowing random facts
│       └── Says something confidently wrong instead of "I don't know"
│
├── What Anthropic does about it
│   ├── Train Claude to be honest
│   ├── Teach Claude to say "I don't know"
│   ├── Honesty = right thing to do + more helpful
│   ├── Test with thousands of tricky questions
│   │   ├── Obscure facts
│   │   ├── Niche topics
│   │   └── Questions where truthful answer is "I don't know"
│   ├── Measure
│   │   ├── How often Claude correctly says unsure
│   │   ├── Does it make up citations or statistics
│   │   └── Hedges appropriately vs false confidence
│   ├── Each new Claude version improves
│   └── Ongoing challenge, not a solved problem
│
├── When hallucinations are most likely
│   ├── Specific facts, statistics, citations
│   ├── Obscure, niche, or very recent topics
│   ├── Real but not widely known people/places
│   └── Exact details like dates, names, numbers
│
└── Tips to reduce hallucinations
    ├── Ask AI to find sources for its claims
    ├── Ask it to check sources actually support what it's saying
    ├── Tell AI upfront "it's okay if you don't know"
    ├── Ask how confident it is
    ├── Start new chat to find errors in previous answer
    ├── Cross reference with trusted sources
    ├── Be skeptical of numbers, dates, citations
    └── Ask follow-up questions if something sounds off
```
