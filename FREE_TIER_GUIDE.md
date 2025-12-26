# 🆓 Free Tier Setup Guide - LLM Council

## Run LLM Council with ZERO Cost!

This guide shows you how to use LLM Council completely free using local models and free APIs.

---

## 🎯 Three Free Options

### Option 1: Completely Free Local (Ollama) ⭐ RECOMMENDED
**Cost**: $0 (runs on your hardware)  
**Speed**: Fast (depends on your hardware)  
**Quality**: Good  
**Privacy**: Complete (everything local)

### Option 2: Free Cloud APIs
**Cost**: $0 (free tier limits apply)  
**Speed**: Very fast  
**Quality**: Excellent  
**Privacy**: Standard API terms

### Option 3: Mix Free + Paid (Optimal)
**Cost**: Minimal (only for premium models)  
**Speed**: Fast  
**Quality**: Best  
**Privacy**: Mixed

---

## 🚀 Option 1: Ollama (Completely Free Local)

### Step 1: Install Ollama

Visit: https://ollama.ai/

**Windows/Mac/Linux**: Download and install

### Step 2: Pull Models

```bash
# Essential models (choose 2-3)
ollama pull llama2          # 7B model, good balance
ollama pull mistral         # 7B model, fast
ollama pull codellama       # Great for technical topics

# Optional larger models (if you have >16GB RAM)
ollama pull llama3          # Latest Llama
ollama pull mixtral         # Mixture of experts
```

### Step 3: Install Python Package

```bash
pip install ollama
```

### Step 4: Run Free Local Debate

```bash
# No API keys needed!
python examples/free_local_debate.py

# Or use directly
python main.py "Your topic" --models ollama
```

### Ollama Model Recommendations

| Model | Size | Use Case | RAM Needed |
|-------|------|----------|------------|
| **llama2** | 7B | General purpose | 8GB |
| **mistral** | 7B | Fast inference | 8GB |
| **codellama** | 7B | Technical topics | 8GB |
| **llama3** | 8B | Latest/best | 8GB |
| **mixtral** | 8x7B | High quality | 16GB+ |

---

## 🌐 Option 2: Free Cloud APIs

### Groq (Free, Ultra-Fast)

**Free Tier**: Generous free usage  
**Speed**: 500+ tokens/second (very fast!)  
**Models**: Llama 3, Mixtral, Gemma

#### Setup:

1. Get API key: https://console.groq.com/
2. Add to `.env`:
   ```bash
   GROQ_API_KEY=your_groq_key
   GROQ_MODEL=llama3-70b-8192
   ```
3. Install:
   ```bash
   pip install groq
   ```
4. Use:
   ```bash
   python main.py "Your topic" --models groq
   ```

### Google Gemini (Free Tier)

**Free Tier**: 60 requests/minute  
**Speed**: Fast  
**Models**: Gemini 1.5 Flash (free), Gemini 1.5 Pro

#### Setup:

1. Get API key: https://makersuite.google.com/app/apikey
2. Add to `.env`:
   ```bash
   GOOGLE_API_KEY=your_google_key
   ```
3. Already installed in requirements.txt
4. Use:
   ```bash
   python main.py "Your topic" --models gemini
   ```

### Hugging Face Inference API (Free)

**Free Tier**: Community models free  
**Speed**: Moderate  
**Models**: Thousands of open models

#### Setup:

1. Optional: Get token at https://huggingface.co/settings/tokens
2. Add to `.env` (optional for public models):
   ```bash
   HUGGINGFACE_API_KEY=your_hf_token
   HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2
   ```
3. Install:
   ```bash
   pip install huggingface_hub
   ```
4. Use:
   ```bash
   python main.py "Your topic" --models huggingface
   ```

---

## 🎯 Complete Free Setup Examples

### All Free Cloud (No Local Installation)

```bash
# .env file
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key

# Run debate
python main.py "Your topic" --models groq gemini
```

### All Free Local (No API Keys)

```bash
# Terminal
ollama pull llama2
ollama pull mistral

# Run debate  
python main.py "Your topic" --models ollama
```

### Best Free Combination

```bash
# .env file
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key

# Also have Ollama running locally

# Run debate with all free options
python examples/free_cloud_debate.py
```

---

## 💰 Cost Comparison

| Setup | Cost/1000 Tokens | Cost/Debate (3 rounds, 4 agents) |
|-------|------------------|----------------------------------|
| **Ollama Local** | $0 | $0 |
| **Groq API** | $0 (free tier) | $0 |
| **Gemini Flash** | $0 (free tier) | $0 |
| **HuggingFace** | $0 (public models) | $0 |
| Mix Free | $0 | $0 |
| Claude + GPT-4 | ~$0.04 | ~$2-5 |

---

## 🎓 Recommended Learning Path

### Absolute Beginner (Zero Cost)
```bash
1. Install Ollama
2. ollama pull llama2
3. pip install ollama
4. python examples/free_local_debate.py
```

### Want Speed (Free Cloud)
```bash
1. Get Groq API key (free)
2. Get Google API key (free)
3. pip install groq
4. python examples/free_cloud_debate.py
```

### Best Quality (Small Cost)
```bash
1. Use free models for volume
2. Add Claude for synthesis
3. python examples/hybrid_free_paid.py
```

---

## 📊 Feature Comparison

| Feature | Ollama | Groq | Gemini | HuggingFace |
|---------|--------|------|--------|-------------|
| **Cost** | Free | Free | Free tier | Free |
| **Speed** | Medium | Very Fast | Fast | Medium |
| **Quality** | Good | Excellent | Excellent | Good |
| **Privacy** | 100% Local | Cloud | Cloud | Cloud |
| **Setup** | Easy | Very Easy | Very Easy | Easy |
| **Limits** | Hardware | API limits | 60 req/min | API limits |

---

## 🔧 Troubleshooting

### Ollama Issues

**"Model not found"**
```bash
ollama list              # Check installed models
ollama pull llama2       # Download model
```

**"Connection refused"**
```bash
ollama serve             # Start Ollama server
```

**Slow inference**
- Use smaller models (llama2, mistral)
- Reduce max_tokens in config
- Use fewer rounds

### API Issues

**Groq rate limits**
- Free tier has limits
- Wait a minute and retry
- Use fewer rounds

**Gemini limits**
- 60 requests/minute free
- Use with other models
- Add delays between rounds

---

## 🎯 Quick Start Commands

### Just Try It (Groq + Gemini)
```bash
# Get free API keys, add to .env, then:
python main.py "What is the future of AI?" --models groq gemini --rounds 2
```

### Completely Free Local
```bash
# Install Ollama, download models, then:
python main.py "What is the future of AI?" --models ollama --rounds 2
```

### Best Free Experience
```bash
# Use all free options:
python main.py "Your topic" --models groq gemini ollama
```

---

## 📚 Examples Included

- `examples/free_local_debate.py` - Pure Ollama (local)
- `examples/free_cloud_debate.py` - Groq + Gemini
- `examples/hybrid_free_paid.py` - Mix free + premium

---

## 🆓 Free Model Recommendations

### For Beginners
- **Groq** (llama3-70b) + **Gemini** (1.5-flash)
- Easy setup, fast, high quality
- Get keys in 5 minutes

### For Privacy
- **Ollama** (llama2 + mistral)
- Everything runs locally
- No data sent to cloud

### For Best Results
- **Groq** + **Gemini** + **Ollama**
- Diverse perspectives
- Zero cost, great quality

---

## 💡 Pro Tips

1. **Start with Groq + Gemini** - Easiest free setup
2. **Add Ollama later** - For privacy and offline use
3. **Use 2-3 rounds** - Faster, still good quality
4. **Mix free + paid** - Free for volume, paid for critical decisions
5. **Monitor usage** - Stay within free tier limits

---

## 🎉 You're Ready!

**Completely Free Options:**
- ✅ Ollama (local)
- ✅ Groq (cloud)
- ✅ Gemini (cloud)
- ✅ HuggingFace (cloud)

**Choose your path:**
- Want **privacy**? → Use Ollama
- Want **speed**? → Use Groq
- Want **easy**? → Use Groq + Gemini
- Want **best**? → Mix all free options!

Run your first free debate now:
```bash
python examples/free_cloud_debate.py
```

---

**🏛️ LLM Council - Now Accessible to Everyone! 🆓**

