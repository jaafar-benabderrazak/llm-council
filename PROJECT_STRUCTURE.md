# LLM Council Project Structure

```
LLM Council/
│
├── 📄 main.py                      # Main entry point & CLI
├── 📄 council.py                   # Core debate orchestrator
├── 📄 config.py                    # Configuration management
│
├── 📁 agents/                      # Agent implementations
│   ├── __init__.py
│   ├── base_agent.py              # Abstract base class
│   ├── claude_agent.py            # Anthropic Claude
│   ├── chatgpt_agent.py           # OpenAI GPT
│   ├── gemini_agent.py            # Google Gemini
│   └── mistral_agent.py           # Mistral AI
│
├── 📁 examples/                    # Usage examples
│   ├── basic_debate.py
│   ├── quick_discussion.py
│   ├── custom_council.py
│   ├── programmatic_access.py
│   └── specific_models.py
│
├── 📄 requirements.txt             # Python dependencies
├── 📄 .gitignore                   # Git ignore rules
├── 📄 env.example                  # Environment template
├── 📄 README.md                    # Full documentation
├── 📄 QUICKSTART.md                # Quick start guide
├── 📄 LICENSE                      # MIT License
└── 📄 PROJECT_STRUCTURE.md         # This file
```

## Key Components

### Core Files

- **main.py**: CLI interface and council factory
- **council.py**: Orchestrates multi-round debates and synthesis
- **config.py**: Manages API keys and configuration

### Agents Module

Each agent implements the `BaseAgent` interface:
- `generate_response()`: Main response generation
- `format_context()`: Context management from previous responses
- `get_system_prompt()`: Role-specific prompting

### Examples

Comprehensive examples demonstrating:
- Basic multi-round debates
- Quick single-round discussions
- Custom agent configurations
- Programmatic result access
- Model-specific councils

## Data Flow

```
User Topic
    ↓
LLMCouncil.debate()
    ↓
Multi-Round Process:
    ↓
Round 1: Each agent responds to topic
    ↓
Round 2+: Each agent responds with context from previous responses
    ↓
    ... (repeat for N rounds)
    ↓
Synthesis: First agent generates comprehensive conclusion
    ↓
DebateResult (JSON exportable)
```

## Adding New Agents

1. Create new file in `agents/` (e.g., `new_agent.py`)
2. Extend `BaseAgent` class
3. Implement `generate_response()` method
4. Add to `agents/__init__.py`
5. Update `main.py` `create_council()` function
6. Add API key to `config.py`

## Configuration

Environment variables in `.env`:
- API keys for each provider
- Model selection
- Temperature, max tokens, rounds

## Output

Debates saved as JSON with:
- Full conversation history
- Token usage per agent
- Metadata and timestamps
- Final synthesis

