# 🚀 LLM Council - Complete Usage Guide

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Command Line Usage](#command-line-usage)
4. [Python API](#python-api)
5. [Configuration](#configuration)
6. [Advanced Usage](#advanced-usage)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)

---

## Installation

### Step 1: Clone and Navigate

```bash
cd "LLM Council"
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys

Copy the example environment file:
```bash
cp env.example .env
```

Edit `.env` and add your API keys:
```bash
# Get API keys from:
# OpenAI: https://platform.openai.com/api-keys
# Anthropic: https://console.anthropic.com/
# Google: https://makersuite.google.com/app/apikey
# Mistral: https://console.mistral.ai/

OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
MISTRAL_API_KEY=...
```

### Step 4: Verify Setup

```bash
python setup_check.py
```

---

## Quick Start

### Interactive Mode

```bash
python main.py
```

You'll be prompted to enter a topic:
```
🏛️  Welcome to LLM Council

Available models: claude, chatgpt, gemini, mistral

Enter a topic for discussion: What is the future of AI in education?
```

### Direct Command

```bash
python main.py "Should we colonize Mars?"
```

---

## Command Line Usage

### Basic Syntax

```bash
python main.py [TOPIC] [OPTIONS]
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--rounds N` | Number of debate rounds | 3 |
| `--models M1 M2 ...` | Specific models to use | All available |
| `--quick` | Single round discussion | False |
| `--no-save` | Don't save results to JSON | False |

### Examples

**Standard debate with 5 rounds:**
```bash
python main.py "Climate change solutions" --rounds 5
```

**Use only Claude and ChatGPT:**
```bash
python main.py "Best programming language" --models claude chatgpt
```

**Quick single-round discussion:**
```bash
python main.py "Top 3 tech trends" --quick
```

**Don't save results:**
```bash
python main.py "Quick question" --no-save
```

---

## Python API

### Basic Usage

```python
from main import create_council

# Create council with all available models
council = create_council()

# Run debate
result = council.debate(
    topic="Your topic here",
    rounds=3,
    save_results=True
)

# Access results
print(result.synthesis)
print(f"Tokens used: {result.total_tokens}")
```

### Custom Agent Configuration

```python
from agents import ClaudeAgent, ChatGPTAgent, GeminiAgent
from council import LLMCouncil

# Create custom agents
agents = [
    ClaudeAgent(
        name="Claude - Legal Expert",
        role="Legal analysis and compliance specialist",
        temperature=0.6
    ),
    ChatGPTAgent(
        name="ChatGPT - Tech Lead",
        role="Technical architecture and implementation",
        temperature=0.7
    ),
    GeminiAgent(
        name="Gemini - Researcher",
        role="Academic research and citation",
        temperature=0.5
    )
]

# Create council
council = LLMCouncil(agents, verbose=True)

# Run debate
result = council.debate("Your specific topic", rounds=2)
```

### Specific Models Only

```python
from main import create_council

# Use only specified models
council = create_council(models=["claude", "gemini"])

result = council.debate("Compare FP vs OOP")
```

### Quick Discussion (Single Round)

```python
council = create_council()

# Fast single-round discussion
synthesis = council.quick_discuss("Quick question here")
print(synthesis)
```

### Programmatic Access to Results

```python
result = council.debate("Topic", rounds=3)

# Access individual rounds
for round_num, round_responses in enumerate(result.rounds, 1):
    print(f"\n=== Round {round_num} ===")
    for response in round_responses:
        print(f"{response.agent_name}: {len(response.content)} chars")
        print(f"  Tokens: {response.tokens_used}")
        print(f"  Model: {response.model}")

# Access synthesis
print("\nFinal Synthesis:")
print(result.synthesis)

# Save to custom location
result.save_to_file("custom_name.json")
```

### Silent Mode (No Console Output)

```python
council = create_council()
council.verbose = False

result = council.debate("Topic", rounds=2)
# No terminal output, just results
```

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Required: API Keys (at least 2)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
MISTRAL_API_KEY=your_key_here

# Optional: Model Selection
OPENAI_MODEL=gpt-4-turbo-preview
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
GOOGLE_MODEL=gemini-1.5-pro
MISTRAL_MODEL=mistral-large-latest

# Optional: Council Settings
MAX_ROUNDS=3
TEMPERATURE=0.7
MAX_TOKENS=2000
```

### Model Options

**OpenAI Models:**
- `gpt-4-turbo-preview` (Recommended)
- `gpt-4`
- `gpt-3.5-turbo`

**Anthropic Models:**
- `claude-3-5-sonnet-20241022` (Recommended)
- `claude-3-opus-20240229`
- `claude-3-sonnet-20240229`
- `claude-3-haiku-20240307`

**Google Models:**
- `gemini-1.5-pro` (Recommended)
- `gemini-1.5-flash`
- `gemini-pro`

**Mistral Models:**
- `mistral-large-latest` (Recommended)
- `mistral-medium-latest`
- `mistral-small-latest`

---

## Advanced Usage

### Custom System Prompts

```python
from agents.claude_agent import ClaudeAgent

class CustomClaudeAgent(ClaudeAgent):
    def get_system_prompt(self, context=None):
        custom_prompt = """You are a specialized expert in [YOUR DOMAIN].
        
        Your role: [SPECIFIC ROLE]
        
        Guidelines:
        1. Focus on [ASPECT 1]
        2. Consider [ASPECT 2]
        3. Prioritize [ASPECT 3]
        """
        
        if context:
            custom_prompt += "\n\n" + self.format_context(context)
        
        return custom_prompt

# Use custom agent
agent = CustomClaudeAgent(name="Domain Expert")
```

### Temperature Tuning

```python
# More creative/diverse (0.8-1.0)
agent = ClaudeAgent(temperature=0.9)

# Balanced (0.6-0.7)
agent = ClaudeAgent(temperature=0.7)

# More focused/deterministic (0.3-0.5)
agent = ClaudeAgent(temperature=0.4)
```

### Error Handling

```python
from config import Config

try:
    # Validate configuration
    Config.validate()
    
    # Create council
    council = create_council()
    
    # Run debate
    result = council.debate("Topic")
    
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Error during debate: {e}")
```

### Loading Previous Debates

```python
import json

# Load saved debate
with open("debate_20241226_120000.json", 'r') as f:
    debate_data = json.load(f)

# Access data
print(f"Topic: {debate_data['topic']}")
print(f"Timestamp: {debate_data['timestamp']}")
print(f"Synthesis: {debate_data['synthesis']}")

# Analyze rounds
for round_num, round_data in enumerate(debate_data['rounds'], 1):
    print(f"\nRound {round_num}:")
    for response in round_data:
        print(f"  {response['agent_name']}: {response['tokens_used']} tokens")
```

---

## Examples

### 1. Research Analysis

```python
council = create_council()

topic = """
Analyze the impact of quantum computing on cryptography.
Consider: current encryption methods, timeline for quantum 
threat, and potential post-quantum solutions.
"""

result = council.debate(topic, rounds=4)
```

### 2. Product Decision

```python
council = create_council(models=["claude", "chatgpt"])

topic = """
Should our mobile app prioritize:
A) Native development (Swift/Kotlin)
B) Cross-platform (React Native/Flutter)
C) Progressive Web App

Consider: team expertise, timeline, budget, user experience
"""

result = council.debate(topic, rounds=3)
```

### 3. Ethical Dilemma

```python
council = create_council()

topic = """
Autonomous vehicles face a split-second decision:
- Swerve and possibly harm passengers
- Continue and possibly harm pedestrians

How should AI make this decision? Consider utilitarian 
vs deontological ethics, legal liability, and societal impact.
"""

result = council.debate(topic, rounds=5)
```

### 4. Technical Architecture

```python
from agents import ClaudeAgent, ChatGPTAgent
from council import LLMCouncil

agents = [
    ClaudeAgent(name="Security", role="Security expert"),
    ChatGPTAgent(name="Scalability", role="Performance expert")
]

council = LLMCouncil(agents)

topic = "Microservices vs Monolith for a social media platform"
result = council.debate(topic, rounds=3)
```

### 5. Quick Brainstorming

```python
council = create_council()

topics = [
    "5 innovative uses for AR in retail",
    "Marketing campaign ideas for Gen Z",
    "Features for our MVP"
]

for topic in topics:
    print(f"\n{'='*60}")
    print(f"Topic: {topic}")
    print('='*60)
    synthesis = council.quick_discuss(topic)
    print(synthesis)
```

---

## Troubleshooting

### Common Issues

**1. "Need at least 2 API keys" Error**

Solution: Add at least 2 valid API keys to your `.env` file

```bash
# Check which keys are configured
python setup_check.py
```

**2. Import Errors**

Solution: Install all dependencies

```bash
pip install -r requirements.txt
```

**3. API Rate Limits**

Solution: Reduce request frequency or upgrade API plan

```python
# Reduce rounds
result = council.debate(topic, rounds=2)

# Or use fewer models
council = create_council(models=["claude"])
```

**4. Token Limit Exceeded**

Solution: Reduce MAX_TOKENS in `.env`

```bash
MAX_TOKENS=1500
```

**5. Slow Response Times**

Solutions:
- Use `--quick` mode for faster results
- Reduce number of rounds
- Use smaller models (e.g., `gpt-3.5-turbo`)
- Disable verbose output

```python
council.verbose = False
```

### Debug Mode

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Your code here
```

---

## Best Practices

### 1. Topic Formulation

**Good Topics:**
- Specific and well-defined
- Include context and constraints
- Ask for specific perspectives
- Provide evaluation criteria

```python
# Good
topic = """
Should our startup use serverless architecture?
Context: 10K users, budget $5K/month, team of 3 developers.
Consider: costs, scalability, vendor lock-in, learning curve.
"""

# Less effective
topic = "What about serverless?"
```

### 2. Round Selection

- **1 round**: Quick questions, brainstorming
- **2-3 rounds**: Standard debates, balanced discussions
- **4-5 rounds**: Complex topics, thorough analysis
- **5+ rounds**: Research, comprehensive evaluation

### 3. Model Selection

**All 4 Models:**
- Maximum perspective diversity
- Complex, multifaceted topics
- When you need comprehensive coverage

**2-3 Models:**
- Balanced performance and cost
- Standard use cases
- Faster results

**Specific Combinations:**
- Claude + ChatGPT: Technical discussions
- Claude + Gemini: Research and analysis
- All 4: Critical decisions

### 4. Cost Optimization

```python
# Monitor token usage
result = council.debate(topic, rounds=3)
print(f"Total tokens: {result.total_tokens}")

# Estimate costs (approximate)
# GPT-4: $0.03/1K input, $0.06/1K output
# Claude: $0.003/1K input, $0.015/1K output
# Gemini: $0.0005/1K (Pro)
# Mistral: $0.002/1K input, $0.006/1K output
```

### 5. Result Analysis

```python
result = council.debate(topic)

# Save for review
filename = result.save_to_file()

# Share with team
# Email, Slack, documentation, etc.

# Track over time
# Compare different approaches to same problem
```

### 6. Security

- ✅ Use environment variables for API keys
- ✅ Add `.env` to `.gitignore`
- ✅ Rotate keys regularly
- ✅ Monitor API usage
- ❌ Never commit API keys to version control
- ❌ Never share `.env` files

---

## Performance Tips

1. **Use Quick Mode** for rapid iteration
2. **Cache results** for repeated queries
3. **Adjust temperature** based on use case
4. **Monitor token usage** to control costs
5. **Start with 2 models** then expand
6. **Use specific models** for domain expertise

---

## Next Steps

1. ✅ Run `python setup_check.py`
2. ✅ Try `python main.py` interactively
3. ✅ Experiment with examples in `examples/`
4. ✅ Customize agents for your domain
5. ✅ Integrate into your workflow
6. ✅ Share feedback and contribute!

---

## Getting Help

- 📖 Read the [README](README.md)
- 🚀 Check [QUICKSTART](QUICKSTART.md)
- 📚 Browse [RESOURCES](RESOURCES.md)
- 🤝 See [CONTRIBUTING](CONTRIBUTING.md)
- 🐛 Open a GitHub Issue
- 💬 Join community discussions

---

**Happy Debating! 🏛️**

For the best results, experiment with different combinations of models,
rounds, and temperature settings to find what works for your use case.

