# 🆓 DeepSeek Free Open-Source Guide

## Overview

DeepSeek offers **completely free open-source models** that you can run locally or use through free APIs:

1. **Via Ollama** (Local, 100% Free, No API Key)
2. **Via HuggingFace** (Free API, No Credit Card)

No API key required! No cost! Complete privacy!

---

## Option 1: DeepSeek via Ollama (Recommended - Completely Free)

### What You Get
- ✅ **100% Free** - No API key, no costs
- ✅ **Complete Privacy** - Runs on your machine
- ✅ **No Rate Limits** - Use as much as you want
- ✅ **Offline Capable** - Works without internet (after download)
- ✅ **Multiple Models** - deepseek-coder, deepseek-llm, deepseek-r1

### Available DeepSeek Models on Ollama

| Model | Size | Use Case | Command |
|-------|------|----------|---------|
| **deepseek-coder:6.7b** | 3.8GB | Code, technical tasks | `ollama pull deepseek-coder:6.7b` |
| **deepseek-coder:33b** | 19GB | Advanced coding | `ollama pull deepseek-coder:33b` |
| **deepseek-llm:7b** | 4.1GB | General chat | `ollama pull deepseek-llm:7b` |
| **deepseek-r1:7b** | 4.7GB | Reasoning tasks | `ollama pull deepseek-r1:7b` |
| **deepseek-r1:14b** | 9.0GB | Advanced reasoning | `ollama pull deepseek-r1:14b` |

### Setup Instructions

#### Step 1: Install Ollama
```bash
# Download from https://ollama.ai/

# Or via command line:
# Windows: Download installer from website
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh
```

#### Step 2: Pull DeepSeek Model
```bash
# For code-focused tasks (recommended):
ollama pull deepseek-coder:6.7b

# For general tasks:
ollama pull deepseek-llm:7b

# For reasoning tasks (newer model):
ollama pull deepseek-r1:7b

# For best quality (requires more RAM):
ollama pull deepseek-coder:33b
```

#### Step 3: Configure LLM Council
Add to your `.env` file:
```bash
OLLAMA_MODEL=deepseek-coder:6.7b
# or
OLLAMA_MODEL=deepseek-llm:7b
# or
OLLAMA_MODEL=deepseek-r1:7b
```

#### Step 4: Run Debates
```bash
# Use free local DeepSeek
python main.py "Your topic" --models ollama

# Combine with Groq (also free)
python main.py "Your topic" --models ollama groq

# Python API
python examples/free_deepseek_debate.py
```

---

## Option 2: DeepSeek via HuggingFace (Free API)

### Available Models
- `deepseek-ai/deepseek-coder-6.7b-instruct`
- `deepseek-ai/deepseek-llm-7b-chat`
- `deepseek-ai/deepseek-math-7b-instruct`

### Setup Instructions

#### Step 1: Get Free HuggingFace Token
1. Go to https://huggingface.co/settings/tokens
2. Create a new token (free, no credit card)
3. Copy the token

#### Step 2: Configure
Add to `.env`:
```bash
HUGGINGFACE_API_KEY=your_token_here
HUGGINGFACE_MODEL=deepseek-ai/deepseek-coder-6.7b-instruct
```

#### Step 3: Run
```bash
python main.py "Your topic" --models huggingface
```

---

## Comparison: Ollama vs HuggingFace

| Feature | Ollama | HuggingFace |
|---------|--------|-------------|
| **Cost** | 100% Free | Free (rate limited) |
| **Privacy** | Complete (local) | Data sent to HF |
| **Speed** | Fast (local GPU) | Variable (cloud) |
| **Rate Limits** | None | Yes (limited) |
| **Setup** | Download models | Just API token |
| **Offline** | Yes (after download) | No (requires internet) |
| **RAM Required** | 8-32GB | None (cloud) |

**Recommendation**: Use **Ollama** for privacy and unlimited usage!

---

## Complete Example: Free DeepSeek Research

### Example 1: Code Analysis with DeepSeek-Coder (Local)

```python
from agents import OllamaAgent
from council import LLMCouncil

# Use local DeepSeek-Coder
deepseek = OllamaAgent(
    name="DeepSeek-Coder",
    role="Code Analysis Expert",
    model="deepseek-coder:6.7b"
)

# Combine with Groq (also free)
from agents import GroqAgent
groq = GroqAgent()

council = LLMCouncil([deepseek, groq])

result = council.debate(
    topic="Analyze the pros and cons of microservices architecture",
    rounds=2
)

print(result.synthesis)
```

### Example 2: Technical Research (100% Free)

```bash
# Pull models first
ollama pull deepseek-coder:6.7b

# Set in .env
OLLAMA_MODEL=deepseek-coder:6.7b
GROQ_API_KEY=your_free_groq_key

# Run debate
python main.py "Compare PostgreSQL vs MongoDB" --models ollama groq --rounds 3
```

---

## DeepSeek Models - Detailed Info

### DeepSeek-Coder (Best for Code)
- **Strengths**: Code generation, debugging, technical analysis
- **Languages**: Python, JavaScript, Java, C++, Go, Rust, etc.
- **Context**: 16K tokens
- **Performance**: Competitive with GPT-3.5 on code tasks

**Use Cases**:
- Code review
- Algorithm explanations
- Architecture decisions
- Debugging assistance

### DeepSeek-LLM (General Purpose)
- **Strengths**: General conversations, reasoning, analysis
- **Context**: 4K tokens
- **Performance**: Good for general tasks

**Use Cases**:
- Research analysis
- Decision making
- Content creation
- General discussions

### DeepSeek-R1 (Reasoning)
- **Strengths**: Complex reasoning, math, logic
- **Context**: 8K tokens
- **Performance**: Strong reasoning capabilities

**Use Cases**:
- Mathematical problems
- Logical reasoning
- Complex analysis
- Step-by-step breakdowns

---

## Performance Tips

### For Best Performance

1. **RAM Requirements**:
   - 6.7B models: 8GB RAM minimum
   - 7B models: 8GB RAM minimum
   - 14B models: 16GB RAM minimum
   - 33B models: 32GB RAM minimum

2. **GPU Acceleration** (Optional but faster):
   - Ollama automatically uses GPU if available
   - NVIDIA GPU: Ensure CUDA is installed
   - Apple Silicon: Works out of the box
   - CPU only: Still works, just slower

3. **Model Selection**:
   - Start with **deepseek-coder:6.7b** (good balance)
   - Use **deepseek-r1:7b** for reasoning tasks
   - Upgrade to 33B if you have RAM

4. **Speed Optimization**:
   ```bash
   # Keep model loaded in memory
   ollama run deepseek-coder:6.7b
   # Leave running in background
   ```

---

## Cost Comparison

### Your Options (Ordered by Cost)

| Option | Cost | Quality | Use Case |
|--------|------|---------|----------|
| **DeepSeek (Ollama)** | **$0.00** | Good | Code, technical tasks |
| **Groq (Free API)** | **$0.00** | Good | Fast inference |
| **HuggingFace (Free)** | **$0.00** | Variable | Open-source models |
| **Gemini (Free tier)** | **$0.00** | Excellent | 60 req/min limit |
| **DeepSeek (API)** | **$0.14/1M** | Good | When local won't work |
| **GPT-4** | $10/1M | Excellent | Premium quality |

**For 100% Free Research**: Ollama (DeepSeek) + Groq + Gemini!

---

## Troubleshooting

### "Model not found" Error
```bash
# List available models
ollama list

# Pull the model
ollama pull deepseek-coder:6.7b

# Verify it's there
ollama list
```

### "Out of Memory" Error
```bash
# Use smaller model
ollama pull deepseek-coder:6.7b  # Instead of 33b

# Or close other applications
# Ollama needs ~8GB RAM minimum
```

### Slow Performance
```bash
# Check if model is loaded
ollama ps

# Pre-load model for faster responses
ollama run deepseek-coder:6.7b
# Leave this running, open new terminal for LLM Council
```

### GPU Not Being Used
```bash
# Check GPU availability
nvidia-smi  # For NVIDIA

# Ollama should auto-detect GPU
# If not, reinstall Ollama with GPU support
```

---

## Recommended Setups

### Budget: $0 (Completely Free)

**Option A: All Local**
```bash
# Install Ollama
ollama pull deepseek-coder:6.7b
ollama pull llama2

# In .env: (no API keys needed!)
OLLAMA_MODEL=deepseek-coder:6.7b

# Run
python main.py "Your topic" --models ollama
```

**Option B: Local + Free Cloud** (Best Quality)
```bash
# Local
ollama pull deepseek-coder:6.7b

# Get free API keys
# Groq: https://console.groq.com/
# Gemini: https://makersuite.google.com/

# In .env:
OLLAMA_MODEL=deepseek-coder:6.7b
GROQ_API_KEY=your_free_key
GOOGLE_API_KEY=your_free_key

# Run
python main.py "Your topic" --models ollama groq gemini --rounds 3
```

### Budget: Small (< $0.01 per debate)

```bash
# Local DeepSeek + Affordable cloud
ollama pull deepseek-coder:6.7b

# In .env:
OLLAMA_MODEL=deepseek-coder:6.7b
DEEPSEEK_API_KEY=your_api_key  # For cloud DeepSeek when needed
GROQ_API_KEY=your_free_key

# Run
python main.py "Your topic" --models ollama deepseek groq
```

---

## Example Scripts

### Script 1: Free Code Analysis
```python
# examples/free_deepseek_code_analysis.py
from agents import OllamaAgent, GroqAgent
from council import LLMCouncil

# Local DeepSeek-Coder
deepseek = OllamaAgent(
    name="DeepSeek",
    role="Code Expert",
    model="deepseek-coder:6.7b"
)

# Free Groq
groq = GroqAgent()

council = LLMCouncil([deepseek, groq])

result = council.debate(
    topic="""
    Analyze REST vs GraphQL APIs:
    - Performance characteristics
    - Development complexity
    - Use case recommendations
    Cite technical documentation.
    """,
    rounds=2
)

print(result.synthesis)
```

### Script 2: Multi-Model Free Research
```python
# examples/free_multi_model_research.py
from agents import OllamaAgent, GroqAgent, GeminiAgent
from council import LLMCouncil

# All free models!
agents = [
    OllamaAgent(model="deepseek-coder:6.7b"),
    GroqAgent(),
    GeminiAgent()  # Free tier
]

council = LLMCouncil(agents)

result = council.debate(
    topic="Best database for a startup: PostgreSQL, MongoDB, or both?",
    rounds=3,
    save_markdown=True
)

print(f"Cost: $0.00")
print(f"Tokens: {result.total_tokens:,}")
```

---

## FAQ

**Q: Which DeepSeek model should I use?**
A: For code tasks: `deepseek-coder:6.7b`. For general: `deepseek-r1:7b`. For best quality: `deepseek-coder:33b` (if you have 32GB RAM).

**Q: Is Ollama really free?**
A: Yes! 100% free, open-source, no hidden costs, no API keys needed.

**Q: Can I use DeepSeek offline?**
A: Yes! With Ollama, models run locally. After downloading, no internet needed.

**Q: How does quality compare to ChatGPT?**
A: DeepSeek-Coder is competitive with GPT-3.5 for code. For general tasks, GPT-4 is better but DeepSeek is free!

**Q: Can I combine free and paid models?**
A: Yes! Use free models (Ollama, Groq) for most of the work, add one premium model (Claude) for final synthesis.

---

## Next Steps

1. **Install Ollama**: https://ollama.ai/
2. **Pull DeepSeek**: `ollama pull deepseek-coder:6.7b`
3. **Get Free Groq Key**: https://console.groq.com/
4. **Run Example**: `python examples/free_deepseek_debate.py`

---

## Resources

- **Ollama**: https://ollama.ai/
- **DeepSeek Models**: https://ollama.com/library/deepseek-coder
- **DeepSeek GitHub**: https://github.com/deepseek-ai
- **HuggingFace**: https://huggingface.co/deepseek-ai
- **Groq (Free)**: https://console.groq.com/

---

**LLM Council** - Now with 100% free DeepSeek support via Ollama! 🚀

*No API keys. No costs. Just AI.*

