# 🚀 Quick Reference - Specific Model Selection

## ✅ What's New

You can now specify **exact Ollama models** in the `--models` argument!

## 📝 Syntax

```bash
python main.py "topic" --models provider:model-name
```

## 🎯 Examples

### 2 Models (Fast)
```bash
$env:PYTHONIOENCODING="utf-8"
python main.py "topic" --models ollama:llama3.1:8b gemini --rounds 2
```

### 3 Models (Balanced)
```bash
python main.py "topic" \
  --models \
    ollama:deepseek-coder:6.7b \
    ollama:llama3.1:8b \
    gemini \
  --rounds 3
```

### 5 Models (Maximum Quality) ⭐
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

## 🎨 Your A2A Security Question

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

## 📊 Available Models

```bash
ollama list
```

You have:
- `deepseek-coder:6.7b` - Code & security expert
- `llama3.1:8b` - Meta's latest
- `mistral:7b` - Strong reasoning
- `phi3:mini` - Microsoft efficient model

## 💡 Pro Tips

1. **Always set encoding on Windows**:
   ```bash
   $env:PYTHONIOENCODING="utf-8"
   ```

2. **Best combination for security topics**:
   ```bash
   ollama:deepseek-coder:6.7b ollama:llama3.1:8b gemini
   ```

3. **Pull models before use**:
   ```bash
   ollama pull model-name
   ```

4. **Check generated files**:
   - `debate_*.json` - Raw data
   - `article_*.md` - Beautiful article with Mermaid diagrams

## 🔗 Full Documentation

- **Complete Guide**: [SPECIFIC_MODELS_GUIDE.md](SPECIFIC_MODELS_GUIDE.md)
- **Research Mode**: [RESEARCH_MODE.md](RESEARCH_MODE.md)
- **Free Models**: [DEEPSEEK_FREE_GUIDE.md](DEEPSEEK_FREE_GUIDE.md)
- **Rate Limits**: [RATE_LIMIT_GUIDE.md](RATE_LIMIT_GUIDE.md)

## 🎉 Benefits

✅ **5 different AI perspectives** in one debate  
✅ **100% free** (no API costs)  
✅ **No rate limits** (Ollama unlimited)  
✅ **High quality** output with diverse viewpoints  
✅ **Comprehensive articles** with sources & diagrams  

---

**Repository**: https://github.com/jaafar-benabderrazak/llm-council

Enjoy your multi-model AI research! 🚀

