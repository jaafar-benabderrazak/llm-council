# Quick Start Guide - LLM Council

## Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up API keys:**
   - Copy `env.example` to `.env`
   - Add your API keys (at least 2 required)

3. **Run your first debate:**
```bash
python main.py "What is the future of artificial intelligence?"
```

## Example Usage

### Interactive Mode
```bash
python main.py
# Enter topic when prompted
```

### Command Line
```bash
# Basic usage
python main.py "Your topic here"

# 5 rounds of debate
python main.py "Your topic" --rounds 5

# Use only Claude and ChatGPT
python main.py "Your topic" --models claude chatgpt

# Quick single-round discussion
python main.py "Your topic" --quick
```

### Python Script
```python
from main import create_council

# Create council
council = create_council()

# Run debate
result = council.debate(
    topic="Should AI be regulated?",
    rounds=3
)

# Get synthesis
print(result.synthesis)
```

## Getting API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/
- **Google**: https://makersuite.google.com/app/apikey
- **Mistral**: https://console.mistral.ai/

## Troubleshooting

**"Need at least 2 models" error:**
- Ensure you have at least 2 valid API keys in your `.env` file

**Import errors:**
- Run: `pip install -r requirements.txt`

**API errors:**
- Check your API keys are valid and have credits
- Verify your `.env` file is in the project root

## Next Steps

- Check out `examples/` directory for more advanced usage
- Read the full `README.md` for detailed documentation
- Customize agent roles in `agents/` directory

