# 🏛️ LLM Council

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                         🏛️  LLM COUNCIL  🏛️                              ║
║                                                                          ║
║        Multi-Agent AI Discussion Framework for Best Responses           ║
║                                                                          ║
║   Claude 🤝 ChatGPT 🤝 Gemini 🤝 Mistral → Collaborative Intelligence   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Where diverse AI perspectives converge to produce the best responses.**

LLM Council is a powerful framework that orchestrates discussions between multiple Large Language Models (Claude Sonnet, ChatGPT, Gemini, and Mistral) to generate well-rounded, critically analyzed responses through collaborative debate.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Multi-Agent](https://img.shields.io/badge/Multi--Agent-Framework-green.svg)]()

## 🌟 Features

### Core Capabilities
- **Multi-Agent Debates**: Multiple AI models discuss, challenge, and build upon each other's perspectives
- **🔬 Research Mode**: Academic-style debates with source citations, validation, and comprehensive articles
- **Flexible Configuration**: Use any combination of 7 LLM providers (Claude, ChatGPT, Gemini, Mistral, Ollama, Groq, HuggingFace)
- **Multi-Round Discussions**: Conduct iterative debates with context-aware responses
- **Intelligent Synthesis**: Automatically generate comprehensive conclusions from all perspectives
- **Rich CLI Interface**: Beautiful terminal output with progress indicators and formatted results
- **Programmatic API**: Full Python API for custom integrations
- **Result Persistence**: Save debate transcripts and analysis as JSON
- **Token Tracking**: Monitor API usage across all models

### 🆕 Research Mode Features (NEW!)
- **📚 Source Citations**: Agents provide and validate references, research papers, and documentation
- **✅ Cross-Checking**: Agents verify each other's sources and identify errors
- **🎓 Academic Articles**: Generate 1000+ word comprehensive articles with verified sources
- **⚠️ Misconception Detection**: Automatically identifies and corrects common misunderstandings
- **📊 Technical Depth**: Detailed specifications, benchmarks, and data-driven analysis
- **🔍 Source Credibility**: Agents rate source reliability (High/Medium/Low)
- **💡 Structured Output**: Executive summary, analysis, references, conclusion in academic format

**Perfect for**: Research projects, technical decisions, literature reviews, comprehensive analysis

👉 **[See Research Mode Documentation](RESEARCH_MODE.md)** for detailed guide

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd llm-council
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API Keys**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

Required API keys (at least 2):
- `OPENAI_API_KEY` - For ChatGPT
- `ANTHROPIC_API_KEY` - For Claude
- `GOOGLE_API_KEY` - For Gemini
- `MISTRAL_API_KEY` - For Mistral AI

### Basic Usage

**Command Line:**
```bash
# Interactive mode
python main.py

# Direct topic
python main.py "What are the ethical implications of AGI?"

# Specify number of rounds
python main.py "Best practices for microservices architecture" --rounds 5

# Use specific models only
python main.py "Future of quantum computing" --models claude chatgpt

# Quick mode (single round)
python main.py "Top 3 programming languages for AI" --quick
```

**Python API:**
```python
from main import create_council

# Create council with all available models
council = create_council()

# Run a debate
result = council.debate(
    topic="Should AI development be regulated?",
    rounds=3,
    save_results=True
)

# Access results
print(result.synthesis)
print(f"Total tokens: {result.total_tokens}")
```

## 📖 How It Works

### The Council Process

1. **Initialization**: Configure agents with distinct roles
   - Claude: Critical Analyst
   - ChatGPT: Pragmatic Problem Solver
   - Gemini: Research Synthesizer
   - Mistral: Devil's Advocate

2. **Multi-Round Debate**:
   - **Round 1**: Each agent provides initial perspective
   - **Round 2+**: Agents review previous responses, challenge weak points, and add insights
   - Each response includes context from previous agents

3. **Synthesis**: Generate comprehensive conclusion that:
   - Identifies key agreements and disagreements
   - Highlights strongest arguments
   - Provides balanced, actionable insights
   - Notes gaps requiring further investigation

### Architecture

```
LLM Council
├── agents/
│   ├── base_agent.py      # Abstract base class
│   ├── claude_agent.py    # Anthropic Claude
│   ├── chatgpt_agent.py   # OpenAI GPT
│   ├── gemini_agent.py    # Google Gemini
│   └── mistral_agent.py   # Mistral AI
├── council.py             # Main orchestrator
├── config.py              # Configuration management
├── main.py                # CLI entry point
└── examples/              # Usage examples
```

## 💡 Examples

### Example 1: Research Mode Debate with Citations
```python
from main import create_council

topic = """
Compare PostgreSQL vs MongoDB for a social media application:
- Performance benchmarks (cite specific tests)
- Scalability patterns (reference documentation)
- Operational complexity (cite sources)
- Real-world case studies

Provide technical specifications and authoritative sources.
"""

council = create_council(
    topic=topic,
    agents=["claude", "chatgpt", "groq"],
    rounds=3  # Multiple rounds for source validation
)

result = council.debate(topic=topic, rounds=3)
# Generates comprehensive article with verified sources
print(result.synthesis)
```

### Example 2: Basic Debate
```python
from main import create_council

council = create_council()

topic = """
Should AI companies be required to make their 
training data publicly available?
"""

result = council.debate(topic=topic, rounds=3)
print(result.synthesis)
```

### Example 3: Custom Council
```python
from agents import ClaudeAgent, ChatGPTAgent
from council import LLMCouncil

agents = [
    ClaudeAgent(name="Security Expert", role="Cybersecurity specialist"),
    ChatGPTAgent(name="Business Analyst", role="Strategy expert")
]

council = LLMCouncil(agents, verbose=True)
result = council.debate("How to secure a cloud infrastructure?")
```

### Example 4: Free Tier Research
```python
# Use only free models for comprehensive research
council = create_council(
    topic="Analyze transformer architectures: BERT vs GPT",
    agents=["groq", "gemini", "ollama"],
    rounds=2
)

result = council.debate(topic="...", rounds=2)
# Still generates citation-backed article - completely free!
```

More examples in the `examples/` directory!

## 🎯 Use Cases

### Standard Mode
- **Quick Analysis**: Get multi-perspective insights on any topic
- **Decision Making**: Evaluate pros/cons from different angles
- **Problem Solving**: Generate comprehensive solutions through collaborative thinking
- **Content Creation**: Develop well-rounded content incorporating diverse viewpoints
- **Education**: Explore topics through structured debate and discussion

### 🔬 Research Mode
- **Academic Research**: Generate literature reviews with verified citations
- **Technical Decisions**: Architecture decisions with benchmarks and sources
- **Comprehensive Reports**: In-depth analysis with cross-checked facts
- **Documentation**: Feature comparisons with authoritative references
- **Learning Resources**: Educational content with credible sources
- **Fact-Checking**: Multi-agent validation of claims and sources
- **Code Review**: Get multiple perspectives on architectural decisions

## ⚙️ Configuration

### Environment Variables

```bash
# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
MISTRAL_API_KEY=...

# Model Selection (optional)
OPENAI_MODEL=gpt-4-turbo-preview
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
GOOGLE_MODEL=gemini-1.5-pro
MISTRAL_MODEL=mistral-large-latest

# Council Settings (optional)
MAX_ROUNDS=3
TEMPERATURE=0.7
MAX_TOKENS=2000
```

### CLI Arguments

```bash
python main.py [topic] [options]

Options:
  --rounds N          Number of debate rounds (default: 3)
  --models M1 M2      Specific models to use (claude, chatgpt, gemini, mistral)
  --quick             Single round discussion
  --no-save           Don't save results to file
```

## 📊 Output Format

Debates are saved as JSON with the following structure:

```json
{
  "topic": "Discussion topic",
  "timestamp": "2024-12-26T...",
  "total_tokens": 15234,
  "participating_agents": ["Claude", "ChatGPT", "Gemini", "Mistral"],
  "rounds": [
    [
      {
        "agent_name": "Claude",
        "model": "claude-3-5-sonnet-20241022",
        "content": "...",
        "tokens_used": 1234
      }
    ]
  ],
  "synthesis": "Final synthesized response..."
}
```

## 🔧 Advanced Usage

### Custom Agent Roles

```python
from agents import ClaudeAgent

agent = ClaudeAgent(
    name="Custom Claude",
    role="Domain-specific expert in blockchain technology",
    temperature=0.8
)
```

### Programmatic Result Analysis

```python
result = council.debate(topic, rounds=3)

# Access individual rounds
for round_num, responses in enumerate(result.rounds):
    for response in responses:
        print(f"{response.agent_name}: {response.tokens_used} tokens")

# Save to custom location
result.save_to_file("my_debate.json")
```

### Disable Verbose Output

```python
council = create_council()
council.verbose = False
result = council.debate(topic)
```

## 🧪 Testing

Run the example scripts:

```bash
# Basic debate
python examples/basic_debate.py

# Quick discussion
python examples/quick_discussion.py

# Custom council
python examples/custom_council.py

# Programmatic access
python examples/programmatic_access.py

# Specific models
python examples/specific_models.py
```

## 📋 Requirements

- Python 3.8+
- At least 2 LLM API keys (OpenAI, Anthropic, Google, or Mistral)
- See `requirements.txt` for full dependency list

## 🤝 Contributing

Contributions welcome! Areas for enhancement:

- Additional LLM providers (Llama, Cohere, etc.)
- Voting mechanisms for best arguments
- Debate moderation strategies
- Custom synthesis algorithms
- Web interface
- Streaming responses

## 📚 Resources

### LLM Provider Documentation
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Mistral AI API](https://docs.mistral.ai/)

### Multi-Agent Frameworks
- [LangChain](https://python.langchain.com/)
- [CrewAI](https://docs.crewai.com/)
- [AutoGen](https://microsoft.github.io/autogen/)

### Research Papers
- "Multi-Agent Systems and Large Language Models" - Survey of collaborative AI
- "Debate Dynamics in AI Systems" - Analysis of multi-model discussions
- "Constitutional AI" - Anthropic's approach to AI alignment through debate

### Related Projects
- [ChatGPT Ensemble](https://github.com/example/ensemble) - Similar multi-model approach
- [LangGraph](https://github.com/langchain-ai/langgraph) - Graph-based multi-agent workflows
- [Agent Protocol](https://agentprotocol.ai/) - Standard for AI agent communication

### Books & Articles
- "Life 3.0" by Max Tegmark - Future of AI and collective intelligence
- "The Alignment Problem" by Brian Christian - AI safety through diverse perspectives
- "Superforecasting" by Philip Tetlock - Group wisdom and prediction

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built with:
- [OpenAI GPT](https://openai.com/)
- [Anthropic Claude](https://anthropic.com/)
- [Google Gemini](https://deepmind.google/technologies/gemini/)
- [Mistral AI](https://mistral.ai/)
- [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting
- [LangChain](https://langchain.com/) - LLM framework

---

**LLM Council** - Where diverse AI perspectives converge to produce the best responses.

Made with ❤️ for the AI community

