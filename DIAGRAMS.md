# LLM Council - Architecture & Workflow Diagrams

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         LLM COUNCIL                              │
│                    Multi-Agent Framework                         │
└─────────────────────────────────────────────────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
         ┌──────────▼─────────┐  ┌───────▼────────┐
         │   CLI Interface    │  │  Python API    │
         │     (main.py)      │  │   (import)     │
         └──────────┬─────────┘  └───────┬────────┘
                    │                     │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   LLMCouncil        │
                    │   (council.py)      │
                    │                     │
                    │ - Orchestrates      │
                    │ - Manages rounds    │
                    │ - Generates synthesis│
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼────────┐   ┌──▼────────┐  ┌───▼────────┐
     │   BaseAgent     │   │  Config   │  │DebateResult│
     │  (base_agent)   │   │(config.py)│  │ (results)  │
     └────────┬────────┘   └───────────┘  └────────────┘
              │
     ┌────────┴─────────────────────────┐
     │                                  │
┌────▼────────┐  ┌──────────────┐  ┌──▼──────────┐  ┌──────────────┐
│ClaudeAgent  │  │ChatGPTAgent  │  │GeminiAgent  │  │MistralAgent  │
│             │  │              │  │             │  │              │
│Anthropic    │  │OpenAI        │  │Google       │  │Mistral AI    │
│Claude       │  │GPT-4         │  │Gemini       │  │Mistral       │
└─────────────┘  └──────────────┘  └─────────────┘  └──────────────┘
```

## Debate Flow

```
START
  │
  ├─► User provides TOPIC
  │
  ├─► Initialize Council with Agents
  │
  ▼
┌─────────────────────────────────────────────┐
│           ROUND 1 (Initial)                 │
├─────────────────────────────────────────────┤
│                                             │
│  Claude:   "Here's my critical analysis..." │
│     ↓                                       │
│  ChatGPT:  "From a practical view..."      │
│     ↓      (receives Claude's response)    │
│  Gemini:   "Research shows..."             │
│     ↓      (receives Claude + ChatGPT)     │
│  Mistral:  "But consider this..."          │
│            (receives all previous)         │
└─────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────┐
│         ROUND 2 (Refinement)                │
├─────────────────────────────────────────────┤
│                                             │
│  All agents receive:                        │
│  - Original topic                           │
│  - All Round 1 responses                    │
│                                             │
│  Claude:   "I challenge Mistral's point..." │
│  ChatGPT:  "Building on Gemini's idea..."  │
│  Gemini:   "Supporting Claude's analysis..."│
│  Mistral:  "New perspective on..."         │
└─────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────┐
│       ROUND 3+ (Deep Analysis)              │
├─────────────────────────────────────────────┤
│                                             │
│  - Further refinement                       │
│  - Address gaps                             │
│  - Strengthen arguments                     │
│  - Challenge weaknesses                     │
└─────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────┐
│          SYNTHESIS PHASE                    │
├─────────────────────────────────────────────┤
│                                             │
│  Synthesizer (usually Claude):              │
│                                             │
│  ✓ Reviews ALL responses from ALL rounds    │
│  ✓ Identifies agreements                    │
│  ✓ Summarizes disagreements                 │
│  ✓ Highlights strongest arguments           │
│  ✓ Provides balanced conclusion             │
│  ✓ Notes gaps for further research          │
└─────────────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────────────┐
│         FINAL OUTPUT                        │
├─────────────────────────────────────────────┤
│                                             │
│  • Comprehensive synthesis                  │
│  • All round transcripts                    │
│  • Token usage statistics                   │
│  • JSON export                              │
│  • Console display                          │
└─────────────────────────────────────────────┘
  │
  ▼
 END
```

## Agent Interaction Pattern

```
TOPIC: "Should we use microservices?"

┌──────────────────────────────────────────────────────────┐
│                    ROUND 1                               │
└──────────────────────────────────────────────────────────┘

Agent 1 (Claude - Critical Analyst)
├─► Receives: Topic only
└─► Responds: "Let's examine the complexity costs..."

Agent 2 (ChatGPT - Pragmatic)
├─► Receives: Topic + Claude's response
└─► Responds: "From practical experience, consider..."

Agent 3 (Gemini - Researcher)
├─► Receives: Topic + Claude + ChatGPT
└─► Responds: "Research shows that teams under 10..."

Agent 4 (Mistral - Devil's Advocate)
├─► Receives: Topic + All previous (Claude, ChatGPT, Gemini)
└─► Responds: "But wait, what about the monitoring overhead..."

┌──────────────────────────────────────────────────────────┐
│                    ROUND 2                               │
└──────────────────────────────────────────────────────────┘

ALL agents receive:
  - Original topic
  - ALL Round 1 responses

Agent 1 (Claude)
└─► "I agree with Mistral's concern about monitoring..."

Agent 2 (ChatGPT)
└─► "To address Claude's complexity point..."

Agent 3 (Gemini)
└─► "Supporting evidence for ChatGPT's team size argument..."

Agent 4 (Mistral)
└─► "Challenging Gemini's assumption about..."

[Continues for N rounds...]
```

## Data Flow Diagram

```
┌─────────────┐
│ User Input  │
│   "Topic"   │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│   Config.validate() │
│ Check API keys      │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ create_council()    │
│ Initialize agents   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐         ┌──────────────┐
│  council.debate()   │◄────────│ Configuration│
│                     │         │ - rounds     │
│  For each round:    │         │ - temp       │
│  ├─ Build context   │         │ - max_tokens │
│  ├─ Call agents     │         └──────────────┘
│  └─ Collect results │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────────────────┐
│  For each agent:                │
│                                 │
│  1. agent.generate_response()   │
│     ├─ get_system_prompt()      │
│     ├─ format_context()         │
│     └─ API call                 │
│                                 │
│  2. Return AgentResponse        │
│     ├─ content                  │
│     ├─ tokens_used              │
│     └─ metadata                 │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────┐
│ _generate_synthesis()│
│                     │
│ Synthesizer reviews │
│ all responses       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   DebateResult      │
│   ├─ rounds[]       │
│   ├─ synthesis      │
│   ├─ tokens         │
│   └─ timestamp      │
└──────┬──────────────┘
       │
       ├────────────────────┐
       │                    │
       ▼                    ▼
┌─────────────┐    ┌───────────────┐
│ Console     │    │  JSON File    │
│ Display     │    │  Export       │
│ (Rich UI)   │    │  (.json)      │
└─────────────┘    └───────────────┘
```

## Agent Role Distribution

```
        ┌────────────────────────────────────┐
        │         TOPIC / QUESTION           │
        └────────────────┬───────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │      Distributed to Agents      │
        └────────────────┬────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼─────┐    ┌───▼────┐    ┌────▼─────┐    ┌──────────┐
    │  Claude  │    │ChatGPT │    │  Gemini  │    │ Mistral  │
    │          │    │        │    │          │    │          │
    │ Critical │    │Pragmatic│   │ Research │    │ Devil's  │
    │ Analyst  │    │Solver  │    │Synthesizer│   │ Advocate │
    └────┬─────┘    └───┬────┘    └────┬─────┘    └────┬─────┘
         │              │              │              │
         │ Questions    │ Practical    │ Evidence     │ Challenges
         │ assumptions  │ solutions    │ based        │ consensus
         │              │              │              │
         └──────────────┴──────────────┴──────────────┘
                         │
                    ┌────▼─────┐
                    │Synthesis │
                    │  Agent   │
                    └────┬─────┘
                         │
                    ┌────▼──────┐
                    │   BEST    │
                    │ RESPONSE  │
                    └───────────┘
```

## File Dependencies

```
main.py
  ├─► imports council.py
  ├─► imports config.py
  └─► imports agents/
          ├─► __init__.py
          ├─► base_agent.py
          ├─► claude_agent.py
          ├─► chatgpt_agent.py
          ├─► gemini_agent.py
          └─► mistral_agent.py

council.py
  ├─► imports agents.base_agent
  ├─► imports config
  └─► uses rich (display)

config.py
  └─► imports dotenv

Each agent file:
  ├─► imports base_agent
  ├─► imports config
  └─► imports respective SDK
      ├─► anthropic (Claude)
      ├─► openai (ChatGPT)
      ├─► google.generativeai (Gemini)
      └─► mistralai (Mistral)
```

## Context Building

```
ROUND 1: Initial Responses
─────────────────────────────

Agent 1: [Topic] → Response₁
Agent 2: [Topic + Response₁] → Response₂
Agent 3: [Topic + Response₁ + Response₂] → Response₃
Agent 4: [Topic + Response₁ + Response₂ + Response₃] → Response₄

Context grows: Topic → Topic+R₁ → Topic+R₁+R₂ → Topic+R₁+R₂+R₃


ROUND 2: Refinement
─────────────────────────────

All agents receive SAME context:
[Topic + All Round 1 Responses]

Agent 1: [Full Context] → Response₅
Agent 2: [Full Context] → Response₆
Agent 3: [Full Context] → Response₇
Agent 4: [Full Context] → Response₈


SYNTHESIS: Final Analysis
─────────────────────────────

Synthesizer receives:
[Topic + All Responses from All Rounds]

Synthesizer → Comprehensive Analysis
```

## Token Flow

```
┌──────────────────────────────────────────┐
│           Token Usage Tracking           │
└──────────────────────────────────────────┘

User initiates debate
       │
       ▼
┌─────────────────────────────────────────┐
│  Round 1: Agent 1                       │
│  ├─ Prompt tokens: 150                  │
│  ├─ Completion tokens: 300              │
│  └─ Total: 450                          │
├─────────────────────────────────────────┤
│  Round 1: Agent 2                       │
│  ├─ Prompt tokens: 450 (includes R1.A1) │
│  ├─ Completion tokens: 320              │
│  └─ Total: 770                          │
├─────────────────────────────────────────┤
│  ... (continues for all agents/rounds)  │
├─────────────────────────────────────────┤
│  Synthesis                              │
│  ├─ Prompt tokens: 2500 (all context)   │
│  ├─ Completion tokens: 800              │
│  └─ Total: 3300                         │
└─────────────────────────────────────────┘
       │
       ▼
Total tokens tracked in DebateResult
Costs can be calculated per provider
```

## Usage Pattern Examples

```
EXAMPLE 1: Quick Question
═════════════════════════
python main.py "Quick question" --quick
       │
       ├─► 1 round only
       ├─► Faster results
       └─► Lower token usage

EXAMPLE 2: Standard Debate
═══════════════════════════
python main.py "Complex topic" --rounds 3
       │
       ├─► 3 rounds (balanced)
       ├─► Moderate depth
       └─► Reasonable token usage

EXAMPLE 3: Deep Analysis
════════════════════════
python main.py "Critical decision" --rounds 5
       │
       ├─► 5 rounds (thorough)
       ├─► Deep analysis
       └─► Higher token usage

EXAMPLE 4: Specific Models
═══════════════════════════
python main.py "Topic" --models claude chatgpt
       │
       ├─► Only 2 models
       ├─► Faster execution
       └─► Lower costs
```

---

**These diagrams illustrate the multi-agent architecture and workflow of LLM Council.**

For implementation details, see the source code.
For usage instructions, see USAGE_GUIDE.md.

