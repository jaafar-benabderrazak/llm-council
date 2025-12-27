# 🎯 Comet API - Model Categories & Aggregation

## Available Comet Models

Based on your Comet API access, here are the available models organized by category:

### 🌟 Advanced/Premium Models
```python
COMET_ADVANCED_MODELS = [
    "gpt-5.2",           # Latest GPT-5 (if available)
    "gpt-4-turbo",       # GPT-4 Turbo
    "gpt-4",             # GPT-4
    "claude-3-opus",     # Claude 3 Opus
    "claude-3-sonnet",   # Claude 3 Sonnet
]
```

### 🚀 Open-Source Models
```python
COMET_OPENSOURCE_MODELS = [
    "llama-3.1-70b",     # Meta Llama 3.1 70B
    "llama-3-70b",       # Meta Llama 3 70B
    "mixtral-8x7b",      # Mistral Mixtral
    "mistral-large",     # Mistral Large
    "qwen-72b",          # Alibaba Qwen
]
```

### 💰 Free/Economic Models
```python
COMET_FREE_MODELS = [
    "gpt-3.5-turbo",     # GPT-3.5 Turbo (economical)
    "claude-3-haiku",    # Claude 3 Haiku (fast & cheap)
    "llama-3-8b",        # Llama 3 8B (free tier)
]
```

### ⚡ Fast Models
```python
COMET_FAST_MODELS = [
    "gpt-3.5-turbo",     # Very fast
    "claude-3-haiku",    # Ultra fast
    "gemini-pro",        # Fast cloud
]
```

---

## 🔧 Configuration in .env

Add to your `.env` file:

```bash
# Comet API
COMET_API_KEY=sk-qVmPMt1sEw1R77GOWiMpqj18FcrytykDXDu1RBEHFIwTsvYN

# Available Models (lines 20-24 in your .env)
# Advanced
COMET_MODEL_ADVANCED=gpt-5.2
# or: gpt-4-turbo, claude-3-opus

# Open-Source
COMET_MODEL_OPENSOURCE=llama-3.1-70b
# or: mixtral-8x7b, mistral-large

# Free/Economic
COMET_MODEL_FREE=gpt-3.5-turbo
# or: claude-3-haiku, llama-3-8b

# Fast
COMET_MODEL_FAST=gpt-3.5-turbo
# or: claude-3-haiku

# Default (current)
COMET_MODEL=gpt-3.5-turbo
```

---

## 🚀 Usage with Categories

### Using Model Categories in Code

```python
from agents.comet_agent import CometAgent
from council import LLMCouncil

# Advanced models for premium quality
advanced_agents = [
    CometAgent(name="GPT-5", model="gpt-5.2", role="Advanced Analysis"),
    CometAgent(name="Claude-Opus", model="claude-3-opus", role="Deep Thinking"),
]

# Open-source models for balance
opensource_agents = [
    CometAgent(name="Llama-70B", model="llama-3.1-70b", role="Open Analysis"),
    CometAgent(name="Mixtral", model="mixtral-8x7b", role="Expert Reasoning"),
]

# Free models for cost efficiency
free_agents = [
    CometAgent(name="GPT-3.5", model="gpt-3.5-turbo", role="Quick Analysis"),
    CometAgent(name="Claude-Haiku", model="claude-3-haiku", role="Fast Response"),
]

# Mix by category
council = LLMCouncil(advanced_agents + opensource_agents)
```

### Command Line with Specific Models

```bash
# Using advanced model
python examples/comet_api_example.py --comet-model gpt-5.2

# Using open-source model
python examples/comet_api_example.py --comet-model llama-3.1-70b

# Using free model
python examples/comet_api_example.py --comet-model gpt-3.5-turbo
```

---

## 📊 Model Comparison

| Model | Category | Speed | Cost | Quality | Use Case |
|-------|----------|-------|------|---------|----------|
| **gpt-5.2** | Advanced | ⭐⭐⭐ | $$$$ | ⭐⭐⭐⭐⭐ | Critical research |
| **gpt-4-turbo** | Advanced | ⭐⭐⭐⭐ | $$$ | ⭐⭐⭐⭐⭐ | Premium analysis |
| **claude-3-opus** | Advanced | ⭐⭐⭐ | $$$$ | ⭐⭐⭐⭐⭐ | Deep reasoning |
| **claude-3-sonnet** | Advanced | ⭐⭐⭐⭐ | $$$ | ⭐⭐⭐⭐ | Balanced premium |
| **llama-3.1-70b** | Open-Source | ⭐⭐⭐ | $$ | ⭐⭐⭐⭐ | General purpose |
| **mixtral-8x7b** | Open-Source | ⭐⭐⭐⭐ | $$ | ⭐⭐⭐⭐ | Expert analysis |
| **gpt-3.5-turbo** | Free | ⭐⭐⭐⭐⭐ | $ | ⭐⭐⭐ | Quick tasks |
| **claude-3-haiku** | Free | ⭐⭐⭐⭐⭐ | $ | ⭐⭐⭐ | Fast response |

---

## 🎯 Recommended Combinations

### Maximum Quality (Advanced)
```python
council = LLMCouncil([
    CometAgent(name="GPT-5", model="gpt-5.2"),
    CometAgent(name="Claude-Opus", model="claude-3-opus"),
    CometAgent(name="GPT-4", model="gpt-4-turbo"),
])
# Cost: $$$$ | Quality: ⭐⭐⭐⭐⭐
```

### Balanced (Mixed)
```python
council = LLMCouncil([
    CometAgent(name="GPT-4", model="gpt-4-turbo"),          # Advanced
    CometAgent(name="Llama-70B", model="llama-3.1-70b"),    # Open-source
    CometAgent(name="GPT-3.5", model="gpt-3.5-turbo"),      # Free
])
# Cost: $$ | Quality: ⭐⭐⭐⭐
```

### Cost-Effective (Free/Open)
```python
council = LLMCouncil([
    CometAgent(name="Llama-70B", model="llama-3.1-70b"),
    CometAgent(name="Mixtral", model="mixtral-8x7b"),
    CometAgent(name="GPT-3.5", model="gpt-3.5-turbo"),
])
# Cost: $ | Quality: ⭐⭐⭐⭐
```

### Ultra-Fast (Speed Priority)
```python
council = LLMCouncil([
    CometAgent(name="GPT-3.5", model="gpt-3.5-turbo"),
    CometAgent(name="Haiku", model="claude-3-haiku"),
])
# Cost: $ | Speed: ⭐⭐⭐⭐⭐
```

---

## 💡 Usage Examples

### Example 1: Premium Research
```bash
python main.py "Advanced cryptography research" \
  --models \
    comet:gpt-5.2 \
    comet:claude-3-opus \
    comet:gpt-4-turbo \
  --rounds 5
# Uses top 3 advanced models
```

### Example 2: Open-Source Analysis
```bash
python main.py "System design patterns" \
  --models \
    comet:llama-3.1-70b \
    comet:mixtral-8x7b \
    ollama:mistral:7b \
  --rounds 4
# Mix Comet open-source + local Ollama
```

### Example 3: Cost-Effective
```bash
python main.py "Quick technology overview" \
  --models \
    comet:gpt-3.5-turbo \
    comet:claude-3-haiku \
    gemini \
  --rounds 3
# All economical models
```

---

## 🔄 Automatic Category Selection

### Update `agents/comet_agent.py`

Add category support:

```python
class CometAgent(BaseAgent):
    """Agent with category-based model selection."""
    
    # Model categories
    CATEGORIES = {
        'advanced': ['gpt-5.2', 'gpt-4-turbo', 'gpt-4', 'claude-3-opus', 'claude-3-sonnet'],
        'opensource': ['llama-3.1-70b', 'llama-3-70b', 'mixtral-8x7b', 'mistral-large'],
        'free': ['gpt-3.5-turbo', 'claude-3-haiku', 'llama-3-8b'],
        'fast': ['gpt-3.5-turbo', 'claude-3-haiku', 'gemini-pro']
    }
    
    def __init__(
        self, 
        name: str = "Comet",
        role: str = "Comet AI Model Agent",
        temperature: float = 0.7,
        model: str = None,
        category: str = None  # NEW: auto-select from category
    ):
        super().__init__(name, role, temperature)
        
        # Auto-select model from category
        if category and not model:
            if category in self.CATEGORIES:
                model = self.CATEGORIES[category][0]  # Use first in category
            else:
                raise ValueError(f"Unknown category: {category}. Choose from: {list(self.CATEGORIES.keys())}")
        
        # ... rest of init
```

### Usage with Categories

```python
# Auto-select from category
agent_advanced = CometAgent(name="Advanced", category="advanced")  # Uses gpt-5.2
agent_opensource = CometAgent(name="OpenSource", category="opensource")  # Uses llama-3.1-70b
agent_free = CometAgent(name="Free", category="free")  # Uses gpt-3.5-turbo
```

---

## 🎨 Complete Example with Categories

```python
from agents.comet_agent import CometAgent
from council import LLMCouncil

# Create agents by category
agents = [
    # Advanced
    CometAgent(name="GPT-5", model="gpt-5.2", role="Premium Analysis"),
    CometAgent(name="Claude-Opus", model="claude-3-opus", role="Deep Reasoning"),
    
    # Open-Source
    CometAgent(name="Llama-70B", model="llama-3.1-70b", role="Open Analysis"),
    CometAgent(name="Mixtral", model="mixtral-8x7b", role="Expert System"),
    
    # Free (for cost control)
    CometAgent(name="GPT-3.5", model="gpt-3.5-turbo", role="Quick Validation"),
]

council = LLMCouncil(agents, verbose=True)

result = council.debate(
    "Design patterns for distributed systems with verified sources",
    rounds=4
)

print(f"Cost estimate: Premium models used: 3")
print(f"Quality: Maximum (5 perspectives)")
```

---

## 📋 Quick Reference

### By Use Case

| Use Case | Recommended Category | Models |
|----------|---------------------|---------|
| **Critical Research** | Advanced | gpt-5.2, claude-3-opus |
| **Production Decisions** | Advanced + Open | gpt-4-turbo, llama-3.1-70b |
| **General Analysis** | Open-Source | llama-3.1-70b, mixtral-8x7b |
| **Quick Tasks** | Free/Fast | gpt-3.5-turbo, claude-3-haiku |
| **Cost-Sensitive** | Free + Open | gpt-3.5-turbo, llama-3-70b |

### By Budget

| Budget | Setup |
|--------|-------|
| **High ($$$)** | All Advanced models |
| **Medium ($$)** | Mix Advanced + Open-Source |
| **Low ($)** | Open-Source + Free |
| **Minimal** | Free only |

---

## ✅ Action Items

1. **Update `.env` with your models** (lines 20-24)
   ```bash
   COMET_MODEL_ADVANCED=gpt-5.2
   COMET_MODEL_OPENSOURCE=llama-3.1-70b
   COMET_MODEL_FREE=gpt-3.5-turbo
   COMET_MODEL_FAST=gpt-3.5-turbo
   ```

2. **Test each category**
   ```bash
   # Test advanced
   python -c "from agents.comet_agent import CometAgent; agent = CometAgent(model='gpt-5.2'); print('OK')"
   
   # Test opensource
   python -c "from agents.comet_agent import CometAgent; agent = CometAgent(model='llama-3.1-70b'); print('OK')"
   ```

3. **Use in your debates**
   ```bash
   python main.py "Your topic" \
     --models comet:gpt-5.2 comet:llama-3.1-70b ollama gemini \
     --rounds 4
   ```

---

**Repository**: https://github.com/jaafar-benabderrazak/llm-council

**Comet models organized by category!** 🎯✨

