# 🎯 LLM Council - Getting Started in 3 Minutes

## What You'll Build

A multi-agent AI system where **Claude**, **ChatGPT**, **Gemini**, and **Mistral** debate topics and produce synthesized, well-analyzed responses.

---

## ⚡ 3-Minute Quick Start

### Step 1: Install (30 seconds)

```bash
pip install -r requirements.txt
```

This installs:
- `anthropic` (Claude)
- `openai` (ChatGPT)
- `google-generativeai` (Gemini)
- `mistralai` (Mistral)
- Plus utilities (rich, colorama, etc.)

### Step 2: Configure (1 minute)

Create `.env` file:

```bash
# Copy template
cp env.example .env
```

Edit `.env` and add **at least 2 API keys**:

```bash
OPENAI_API_KEY=sk-...           # From platform.openai.com
ANTHROPIC_API_KEY=sk-ant-...    # From console.anthropic.com
GOOGLE_API_KEY=AI...            # From makersuite.google.com
MISTRAL_API_KEY=...             # From console.mistral.ai
```

### Step 3: Run! (30 seconds)

```bash
python main.py
```

Enter a topic when prompted:
```
Enter a topic for discussion: Should we colonize Mars?
```

Watch the magic happen! ✨

---

## 🎨 What Happens Next?

```
🏛️  LLM Council Debate

Topic: Should we colonize Mars?
Rounds: 3
Participants: Claude, ChatGPT, Gemini, Mistral

═══ Round 1/3 ═══

Claude thinking...
✓ Claude (claude-3-5-sonnet-20241022) - 456 tokens
[Response about Mars colonization risks and challenges...]

ChatGPT thinking...
✓ ChatGPT (gpt-4-turbo-preview) - 423 tokens
[Response about practical solutions and technology...]

Gemini thinking...
✓ Gemini (gemini-1.5-pro) - 389 tokens
[Response with research and evidence...]

Mistral thinking...
✓ Mistral (mistral-large-latest) - 412 tokens
[Response challenging assumptions...]

═══ Round 2/3 ═══
[Agents review and respond to each other...]

═══ Round 3/3 ═══
[Further refinement and debate...]

═══ Generating Synthesis ═══

📊 Final Synthesis - Best Response
[Comprehensive conclusion incorporating all perspectives...]

✓ Debate Complete!
Results saved to: debate_20241226_120000.json
```

---

## 🎯 Your First Commands

### Interactive Mode (Recommended for First Time)
```bash
python main.py
```

### Direct Topic
```bash
python main.py "What is the future of AI?"
```

### With Options
```bash
# 5 rounds for deeper analysis
python main.py "Complex topic" --rounds 5

# Use only 2 models
python main.py "Topic" --models claude chatgpt

# Quick single round
python main.py "Quick question" --quick
```

### Verify Setup
```bash
python setup_check.py
```

### Run Examples
```bash
python examples/basic_debate.py
python examples/quick_discussion.py
```

---

## 🔍 Understanding the Output

### Console Output

```
═══ Round 1/3 ═══
```
Shows current progress

```
Claude (claude-3-5-sonnet-20241022) - 456 tokens
```
Agent name, model used, tokens consumed

```
[Panel with formatted response]
```
Each agent's response in a beautiful panel

```
📊 Final Synthesis - Best Response
```
The comprehensive conclusion

### JSON File Output

Saved automatically as `debate_YYYYMMDD_HHMMSS.json`:

```json
{
  "topic": "Your topic",
  "timestamp": "2024-12-26T12:00:00",
  "total_tokens": 5234,
  "participating_agents": ["Claude", "ChatGPT", "Gemini", "Mistral"],
  "rounds": [...],
  "synthesis": "Final comprehensive response..."
}
```

---

## 🎓 Learning Path

### ✅ Just Completed
- [x] Installation
- [x] Basic setup
- [x] First debate

### 📖 Next Steps

**Read these in order:**

1. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** (5 min)
   - Understand what you just built
   - Learn the core concepts

2. **[USAGE_GUIDE.md](USAGE_GUIDE.md)** (20 min)
   - All command-line options
   - Python API usage
   - Configuration details

3. **Try Examples** (15 min)
   ```bash
   python examples/basic_debate.py
   python examples/quick_discussion.py
   python examples/custom_council.py
   python examples/programmatic_access.py
   python examples/specific_models.py
   ```

4. **[README.md](README.md)** (15 min)
   - Complete documentation
   - All features explained

5. **[DIAGRAMS.md](DIAGRAMS.md)** (10 min)
   - Visual understanding of workflow
   - Architecture diagrams

---

## 💡 Try These Topics

### Technology
```bash
python main.py "Compare microservices vs monolithic architecture"
python main.py "Future of quantum computing"
python main.py "Best programming language for AI development"
```

### Ethics & Society
```bash
python main.py "Should AI development be regulated?"
python main.py "Ethical implications of autonomous vehicles"
python main.py "Impact of social media on democracy"
```

### Business & Strategy
```bash
python main.py "Remote work vs office work effectiveness"
python main.py "Sustainable business practices vs profitability"
python main.py "Startup MVP features prioritization"
```

### Science & Research
```bash
python main.py "Approaches to climate change mitigation"
python main.py "Gene editing ethics - CRISPR applications"
python main.py "Space exploration priorities"
```

---

## 🐛 Troubleshooting

### "Need at least 2 API keys"
- Edit `.env` file
- Add at least 2 valid API keys
- Run `python setup_check.py` to verify

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "API Error" or "Rate Limit"
- Verify API keys are correct
- Check you have API credits
- Try with fewer models: `--models claude`

### Slow responses
- Use `--quick` for faster results
- Reduce rounds: `--rounds 2`
- Try smaller models (edit .env)

---

## 🎨 Customization Quick Tips

### Use Specific Models Only

```bash
# Just Claude and ChatGPT
python main.py "Topic" --models claude chatgpt
```

### Adjust Round Count

```bash
# Quick: 1 round
python main.py "Topic" --quick

# Balanced: 2-3 rounds (default: 3)
python main.py "Topic" --rounds 3

# Deep: 5+ rounds
python main.py "Topic" --rounds 5
```

### Python API

```python
from main import create_council

# Create council
council = create_council()

# Run debate
result = council.debate(
    topic="Your question here",
    rounds=3
)

# Get results
print(result.synthesis)
print(f"Used {result.total_tokens} tokens")
```

---

## 📚 Documentation Quick Links

| Document | What's Inside | Read When |
|----------|--------------|-----------|
| **[INDEX.md](INDEX.md)** | Navigation hub | Finding specific info |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Overview | Understanding the project |
| **[QUICKSTART.md](QUICKSTART.md)** | Fast setup | Getting started quickly |
| **[USAGE_GUIDE.md](USAGE_GUIDE.md)** | Complete usage | Learning all features |
| **[README.md](README.md)** | Full docs | Comprehensive understanding |
| **[RESOURCES.md](RESOURCES.md)** | External links | Deep learning |

---

## ✨ What Makes LLM Council Special?

### Traditional Approach
```
You → Single AI Model → Response
```
Limited to one perspective, potential blind spots

### LLM Council Approach
```
You → Multiple AI Models Debating → Synthesized Best Response
```
Multiple perspectives, critical analysis, comprehensive synthesis

### Benefits

✅ **Diverse Perspectives** - 4 different AI models  
✅ **Critical Analysis** - Agents challenge each other  
✅ **Iterative Refinement** - Multi-round discussions  
✅ **Comprehensive Synthesis** - Best of all perspectives  
✅ **Transparent Process** - See all arguments  
✅ **Flexible** - Use 2-4 models, 1-5+ rounds  

---

## 🎯 Success Checklist

After this guide, you should have:

- ✅ Installed all dependencies
- ✅ Configured at least 2 API keys
- ✅ Run `python main.py` successfully
- ✅ Seen multiple AI models debate
- ✅ Received a synthesized response
- ✅ Found the saved JSON file
- ✅ Know where to find more help

---

## 🚀 You're Ready!

You now have a powerful multi-agent AI system at your fingertips!

### What to Do Next?

1. **Experiment** with different topics
2. **Try different** model combinations
3. **Adjust** the number of rounds
4. **Read** the documentation
5. **Build** your own integrations
6. **Share** your results!

---

## 📞 Need Help?

- **Setup issues?** → Run `python setup_check.py`
- **Usage questions?** → Read [USAGE_GUIDE.md](USAGE_GUIDE.md)
- **Want examples?** → Check `examples/` directory
- **Need navigation?** → See [INDEX.md](INDEX.md)
- **Want to learn more?** → Read [RESOURCES.md](RESOURCES.md)

---

**Congratulations! You've successfully set up LLM Council! 🎉**

*Now go debate something interesting!* 🏛️

---

**Pro Tip**: Start with simple topics to understand the flow, then move to complex debates with 5+ rounds for deep analysis.

