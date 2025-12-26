# Specific Model Selection Guide

## 🎯 Overview

LLM Council now supports **specific model selection** using the syntax `provider:model-name`. This allows you to:

- Use **multiple different Ollama models** in a single debate
- Specify **exact models** for each provider
- Create **diverse AI councils** with different perspectives

---

## 📝 Syntax

### Basic Syntax
```bash
python main.py "topic" --models provider:model-name
```

### Examples

#### **Single Model**
```bash
# Use default Ollama model
python main.py "topic" --models ollama gemini

# Use specific Ollama model
python main.py "topic" --models ollama:llama3.1:8b gemini
```

#### **Multiple Different Ollama Models**
```bash
# Use 3 different Ollama models + Gemini
python main.py "topic" --models \
  ollama:deepseek-coder:6.7b \
  ollama:llama3.1:8b \
  ollama:mistral:7b \
  gemini
```

#### **5 Best FREE Models** ⭐
```bash
# Ultimate free research setup
python main.py "topic" --models \
  ollama:deepseek-coder:6.7b \
  ollama:llama3.1:8b \
  ollama:mistral:7b \
  ollama:phi3:mini \
  gemini \
  --rounds 3
```

---

## 🚀 Complete Examples

### Example 1: Security Research (Recommended)
```bash
$env:PYTHONIOENCODING="utf-8"

python main.py "How to make A2A protocol secure and reliable? Provide resources." \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:llama3.1:8b \
    gemini \
  --rounds 5
```

**Why this combination?**
- `deepseek-coder:6.7b` - Security & code expert
- `llama3.1:8b` - General intelligence & reasoning
- `gemini` - Fast cloud synthesis & cross-checking

---

### Example 2: Code Review
```bash
python main.py "Best practices for REST API design" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:mistral:7b \
  --rounds 3
```

**Why this combination?**
- `deepseek-coder:6.7b` - Code-specific expertise
- `mistral:7b` - Critical analysis & reasoning

---

### Example 3: General Research (5 Models)
```bash
python main.py "Impact of AI on software development" \
  --models \
    ollama:llama3.1:8b \
    ollama:mistral:7b \
    ollama:phi3:mini \
    ollama:qwen:7b \
    gemini \
  --rounds 4
```

**Maximum diversity** - 5 different AI perspectives!

---

## 📊 Available Ollama Models

### Currently Downloaded
Run `ollama list` to see your models:

```bash
ollama list
```

Output:
```
NAME                     SIZE
deepseek-coder:6.7b     3.8 GB
llama3.1:8b             4.6 GB
mistral:7b              4.1 GB
phi3:mini               2.3 GB
```

### Popular Models to Try

| Model | Size | Best For | Command |
|-------|------|----------|---------|
| **deepseek-coder:6.7b** | 3.8GB | Code, security | `ollama pull deepseek-coder:6.7b` |
| **llama3.1:8b** | 4.6GB | General, reasoning | `ollama pull llama3.1:8b` |
| **mistral:7b** | 4.1GB | Critical thinking | `ollama pull mistral:7b` |
| **phi3:mini** | 2.3GB | Fast, efficient | `ollama pull phi3:mini` |
| **qwen:7b** | 4.4GB | Chinese + English | `ollama pull qwen:7b` |
| **codellama:7b** | 3.8GB | Code generation | `ollama pull codellama:7b` |
| **llama3.1:70b** | 40GB | Highest quality | `ollama pull llama3.1:70b` |

---

## 🎨 Model Combinations

### Best Combinations by Use Case

#### **Security & DevOps**
```bash
--models \
  ollama:deepseek-coder:6.7b \
  ollama:mistral:7b \
  gemini
```

#### **Academic Research**
```bash
--models \
  ollama:llama3.1:8b \
  ollama:mistral:7b \
  ollama:phi3:mini \
  gemini
```

#### **Code Review & Architecture**
```bash
--models \
  ollama:deepseek-coder:6.7b \
  ollama:codellama:7b \
  ollama:llama3.1:8b
```

#### **Maximum Free Quality** ⭐
```bash
--models \
  ollama:llama3.1:70b \
  gemini \
  --rounds 2
```
*Note: 70B model is slow but highest quality*

#### **Fast & Balanced**
```bash
--models \
  ollama:phi3:mini \
  ollama:mistral:7b \
  gemini \
  --rounds 3
```

---

## 💡 Pro Tips

### 1. **Model Variety = Better Output**
Using different models gives you diverse perspectives:
- **DeepSeek** - Technical & code-focused
- **Llama** - Balanced & well-rounded
- **Mistral** - Critical thinking
- **Phi-3** - Efficient & concise
- **Gemini** - Fast synthesis

### 2. **Local + Cloud = Best Balance**
```bash
# 3-4 local Ollama models + 1 cloud (Gemini)
# = No rate limits + diverse perspectives
```

### 3. **Model Size Trade-offs**

| Size | Speed | Quality | Use When |
|------|-------|---------|----------|
| Mini (2-3GB) | ⚡ Fast | ✓ Good | Quick tasks, many models |
| 7-8B (4-5GB) | ⚡ Medium | ✓✓ Great | Balanced use |
| 70B (40GB) | 🐌 Slow | ✓✓✓ Best | Important research |

### 4. **Windows Users**
Always set encoding first:
```bash
$env:PYTHONIOENCODING="utf-8"
```

### 5. **Check Model Availability**
Before running, verify models are pulled:
```bash
ollama list
```

If missing:
```bash
ollama pull model-name
```

---

## 🔧 Common Patterns

### Pattern 1: Quick 2-Model Debate
```bash
python main.py "topic" \
  --models ollama:llama3.1:8b gemini \
  --rounds 2
```

### Pattern 2: Deep 5-Model Research
```bash
python main.py "topic" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:llama3.1:8b \
    ollama:mistral:7b \
    ollama:phi3:mini \
    gemini \
  --rounds 5
```

### Pattern 3: Code-Focused Analysis
```bash
python main.py "code topic" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:codellama:7b \
  --rounds 3
```

### Pattern 4: Python API (Programmatic)
```python
from main import create_council

# Specify exact models
council = create_council([
    "ollama:deepseek-coder:6.7b",
    "ollama:llama3.1:8b",
    "ollama:mistral:7b",
    "gemini"
])

result = council.debate("Your topic", rounds=3)
```

---

## ❌ Common Mistakes

### ❌ Wrong: Missing colon
```bash
--models ollama llama3.1:8b  # Wrong!
```

### ✅ Correct: Use full syntax
```bash
--models ollama:llama3.1:8b  # Correct!
```

---

### ❌ Wrong: Model not pulled
```bash
--models ollama:nonexistent:model
# Error: model not found
```

### ✅ Correct: Pull first
```bash
ollama pull llama3.1:8b
python main.py "topic" --models ollama:llama3.1:8b
```

---

### ❌ Wrong: Single model
```bash
--models ollama:llama3.1:8b
# Error: Need at least 2 models
```

### ✅ Correct: Use 2+ models
```bash
--models ollama:llama3.1:8b gemini
```

---

## 📖 Full Command Reference

### Minimal Command
```bash
python main.py "topic"
# Uses all available models (default)
```

### Specify 2 Models
```bash
python main.py "topic" --models model1 model2
```

### Specify Exact Ollama Models
```bash
python main.py "topic" --models ollama:llama3.1:8b ollama:mistral:7b
```

### With Rounds
```bash
python main.py "topic" --models model1 model2 --rounds 5
```

### No File Output
```bash
python main.py "topic" --models model1 model2 --no-save
```

### No Markdown (JSON only)
```bash
python main.py "topic" --models model1 model2 --no-markdown
```

### Complete Example
```bash
$env:PYTHONIOENCODING="utf-8"

python main.py "How to secure microservices?" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:llama3.1:8b \
    ollama:mistral:7b \
    gemini \
  --rounds 4
```

---

## 🎯 Recommended Setup

### For Your A2A Security Question
```bash
$env:PYTHONIOENCODING="utf-8"

python main.py "how to make a2a protocol secure and reliable? give resources" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:llama3.1:8b \
    ollama:mistral:7b \
    gemini \
  --rounds 5
```

**Why?**
- ✅ 4 AI perspectives (3 local + 1 cloud)
- ✅ Security expert (DeepSeek-Coder)
- ✅ General reasoning (Llama 3.1)
- ✅ Critical analysis (Mistral)
- ✅ Fast synthesis (Gemini)
- ✅ 100% free, no rate limits
- ✅ 5 rounds for thorough research

---

## 🚀 Next Steps

1. **Check your Ollama models**:
   ```bash
   ollama list
   ```

2. **Pull any missing models**:
   ```bash
   ollama pull deepseek-coder:6.7b
   ollama pull llama3.1:8b
   ollama pull mistral:7b
   ollama pull phi3:mini
   ```

3. **Try the recommended command**:
   ```bash
   $env:PYTHONIOENCODING="utf-8"
   
   python main.py "your topic" \
     --models \
       ollama:deepseek-coder:6.7b \
       ollama:llama3.1:8b \
       ollama:mistral:7b \
       gemini \
     --rounds 3
   ```

4. **Check the generated files**:
   - `debate_*.json` - Raw data
   - `article_*.md` - Beautiful article with diagrams

---

## 💬 Support

If you encounter issues:

1. **Model not found**:
   ```bash
   ollama list  # Check available models
   ollama pull model-name  # Download missing model
   ```

2. **Encoding errors** (Windows):
   ```bash
   $env:PYTHONIOENCODING="utf-8"
   ```

3. **Need at least 2 models**:
   - Add more models to `--models` argument
   - Or remove `--models` to use all available

4. **Rate limits**:
   - Use Ollama models (unlimited)
   - Add Gemini (generous free tier: 60 req/min)

---

**Enjoy your 5-model AI research council!** 🎉

