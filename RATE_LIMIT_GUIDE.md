# 🚦 Rate Limit Management Guide

## Understanding Rate Limits

Different LLM providers have different rate limits. Here's how to manage them effectively in LLM Council.

---

## Provider Rate Limits

### Free Providers

| Provider | Daily Limit | Per Minute | Notes |
|----------|-------------|------------|-------|
| **Groq** | 100K tokens/day | 30 req/min | Per model limits |
| **Gemini Free** | Unlimited | 60 req/min | Very generous |
| **Ollama** | ∞ Unlimited | ∞ Unlimited | Local, no limits! |
| **HuggingFace** | Variable | Variable | Depends on model |

### Paid Providers

| Provider | Tier | Limits |
|----------|------|--------|
| **OpenAI** | Pay-as-go | Based on tier |
| **Claude** | Pay-as-go | Based on tier |
| **Mistral** | Pay-as-go | Based on tier |
| **DeepSeek API** | Pay-as-go | Very high limits |

---

## Common Error: Groq Rate Limit

### Error Message
```
Error code: 429 - Rate limit reached for model llama-3.3-70b-versatile
Limit 100000, Used 99885, Requested 2149
Please try again in 29m17.376s
```

### Why This Happens
- Groq's free tier has **100K tokens/day** limit per model
- Different models have separate counters
- Resets every 24 hours
- You've used ~99,885 tokens (that's a lot of research!)

---

## Quick Fixes

### Fix 1: Switch to Local Ollama (BEST)

**No rate limits, completely free:**

```bash
# Install Ollama from https://ollama.ai/

# Pull a model
ollama pull deepseek-coder:6.7b
# or
ollama pull llama2

# Update .env
OLLAMA_MODEL=deepseek-coder:6.7b

# Use it
python main.py "Your topic" --models ollama
```

**Benefits**:
- ✅ Unlimited usage
- ✅ No wait time
- ✅ Complete privacy
- ✅ Works offline

---

### Fix 2: Switch Groq Models

Different Groq models have **separate rate limit counters**:

**Update your `.env` file:**
```bash
# Option 1: Use smaller, faster model
GROQ_MODEL=llama3-8b-8192

# Option 2: Use Mixtral
GROQ_MODEL=mixtral-8x7b-32768

# Option 3: Use Gemma
GROQ_MODEL=gemma-7b-it
```

**Available Groq Models:**
- `llama3-8b-8192` - Fast, efficient (RECOMMENDED)
- `llama3-70b-8192` - Larger, better quality
- `llama-3.3-70b-versatile` - Latest (may hit limits faster)
- `mixtral-8x7b-32768` - Good quality, 32K context
- `gemma-7b-it` - Google's model

---

### Fix 3: Use Gemini Free Tier

**Very generous limits (60 req/min):**

```bash
# Get free key: https://makersuite.google.com/
# Add to .env:
GOOGLE_API_KEY=your_key_here

# Use Gemini
python main.py "Your topic" --models gemini

# Or combine with Ollama
python main.py "Your topic" --models ollama gemini
```

---

### Fix 4: Mix Free Providers

**Combine multiple free providers to avoid limits:**

```bash
# Best free combination:
python main.py "Your topic" --models ollama gemini

# If you have Groq tokens left:
python main.py "Your topic" --models ollama groq gemini --rounds 2

# All local (no limits):
python main.py "Your topic" --models ollama
```

---

## Rate Limit Best Practices

### 1. **Use Ollama as Primary** (No Limits)

```python
# Always include Ollama when possible
models=["ollama", "groq", "gemini"]

# If Groq hits limit, still have Ollama + Gemini
```

### 2. **Reduce Rounds When Testing**

```bash
# Testing: Use 1-2 rounds
python main.py "Test topic" --rounds 1

# Production: Use 3+ rounds
python main.py "Important topic" --rounds 3
```

### 3. **Use Smaller Models for Groq**

```bash
# In .env - use 8B model instead of 70B
GROQ_MODEL=llama3-8b-8192  # Uses 8x less tokens per response
```

### 4. **Monitor Token Usage**

```python
result = council.debate(topic, rounds=2)
print(f"Tokens used: {result.total_tokens:,}")

# If approaching 100K, switch to Ollama
```

### 5. **Rotate Models**

```python
# Morning: Use Groq
models=["groq", "gemini"]

# Evening (if Groq limited): Use Ollama
models=["ollama", "gemini"]
```

---

## Emergency Fallbacks

### If ALL Free APIs Are Limited

**Option 1: Pure Local (Always Works)**
```bash
ollama pull deepseek-coder:6.7b
python main.py "Your topic" --models ollama
```

**Option 2: Wait for Reset**
```bash
# Groq resets every 24 hours
# Check your usage: https://console.groq.com/
```

**Option 3: Use Paid Tier**
```bash
# DeepSeek API (~70x cheaper than GPT-4)
DEEPSEEK_API_KEY=your_key
python main.py "Your topic" --models deepseek
```

---

## Checking Your Groq Usage

### Via Groq Console
1. Go to https://console.groq.com/
2. Check "Usage" or "Settings"
3. See tokens used and when reset occurs

### Via Error Message
The error tells you:
- Limit: 100,000 tokens
- Used: 99,885 tokens  
- Requested: 2,149 tokens
- Reset in: 29m17s

---

## Optimal Free Configurations

### Configuration 1: Maximum Reliability
```bash
# Ollama (unlimited) + Gemini (generous)
models=["ollama", "gemini"]

# Cost: $0
# Rate Limits: Minimal
# Quality: Good
```

### Configuration 2: Best Quality Free
```bash
# Ollama + Gemini + Groq (when available)
models=["ollama", "gemini", "groq"]

# Cost: $0
# Rate Limits: Moderate (Groq may limit)
# Quality: Excellent
```

### Configuration 3: Pure Local (No Limits Ever)
```bash
# Just Ollama with multiple models
OLLAMA_MODEL=deepseek-coder:6.7b

models=["ollama"]

# Cost: $0
# Rate Limits: None
# Quality: Good
# Privacy: Maximum
```

---

## Token-Saving Strategies

### 1. **Be Specific in Prompts**

**Bad** (uses more tokens):
```
"Tell me everything about databases"
```

**Good** (focused, fewer tokens):
```
"Compare PostgreSQL vs MongoDB for startups:
- Performance (cite benchmarks)
- Scalability (cite docs)
- Cost (cite data)"
```

### 2. **Use Fewer Rounds for Simple Topics**

```bash
# Simple question: 1 round
python main.py "What is REST API?" --rounds 1

# Complex research: 3 rounds
python main.py "Microservices vs monolith" --rounds 3
```

### 3. **Limit Agents for Testing**

```bash
# Testing: 2 agents
python main.py "Test" --models ollama gemini

# Production: 3+ agents
python main.py "Important" --models ollama gemini groq
```

---

## Troubleshooting

### "Rate limit reached" - Groq

**Solution**: Switch to Ollama or Gemini
```bash
python main.py "Your topic" --models ollama gemini
```

### "Rate limit reached" - Gemini

**Solution**: Use Ollama (unlimited)
```bash
python main.py "Your topic" --models ollama
```

### "All APIs rate limited"

**Solution**: Use pure local
```bash
ollama pull deepseek-coder:6.7b
python main.py "Your topic" --models ollama
```

### "No models available"

**Solution**: Install Ollama
```bash
# Install from https://ollama.ai/
ollama pull llama2
python main.py "Your topic" --models ollama
```

---

## Summary

**Best Strategy for Avoiding Rate Limits:**

1. **Primary**: Use Ollama (unlimited, local)
2. **Secondary**: Add Gemini (generous limits)
3. **Optional**: Add Groq (when tokens available)
4. **Fallback**: Use paid DeepSeek API (very cheap)

**Recommended `.env` Configuration:**
```bash
# Free, unlimited
OLLAMA_MODEL=deepseek-coder:6.7b

# Free, generous (60 req/min)
GOOGLE_API_KEY=your_key

# Free, limited (100K tokens/day)
GROQ_API_KEY=your_key
GROQ_MODEL=llama3-8b-8192  # Use 8B, not 70B

# Affordable fallback (~$0.002 per debate)
DEEPSEEK_API_KEY=your_key
```

**Usage Pattern:**
```bash
# Default: All free options
python main.py "Your topic" --models ollama gemini groq

# If Groq limited: Still works!
python main.py "Your topic" --models ollama gemini

# Emergency: Pure local
python main.py "Your topic" --models ollama
```

---

**Key Takeaway**: With Ollama + Gemini, you have **effectively unlimited free usage** with excellent quality!

🚀 **Never get rate limited again!**

