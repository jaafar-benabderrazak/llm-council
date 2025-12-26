# Contributing to LLM Council

Thank you for your interest in contributing to LLM Council! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Relevant error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:
- Clear description of the enhancement
- Use case and benefits
- Any implementation ideas

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/yourusername/llm-council.git
cd llm-council
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment:
```bash
cp env.example .env
# Add your API keys
```

4. Verify setup:
```bash
python setup_check.py
```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and concise
- Comment complex logic

## Adding New LLM Providers

To add a new LLM provider:

1. Create new agent file: `agents/your_llm_agent.py`
2. Extend `BaseAgent` class
3. Implement `generate_response()` method
4. Add to `agents/__init__.py`
5. Update `config.py` with API key handling
6. Update `main.py` `create_council()` function
7. Add example usage
8. Update documentation

Example template:

```python
from .base_agent import BaseAgent, AgentResponse
from config import Config

class YourLLMAgent(BaseAgent):
    def __init__(self, name="YourLLM", role="Specialist", temperature=0.7):
        super().__init__(name, role, temperature)
        # Initialize your client
        
    def generate_response(self, prompt, context=None):
        # Implement response generation
        pass
```

## Testing

Before submitting a PR:

1. Test with different model combinations
2. Verify error handling
3. Check token counting
4. Test CLI commands
5. Validate JSON output format

## Documentation

Update relevant documentation:
- README.md for major features
- Docstrings for code changes
- Examples for new functionality
- QUICKSTART.md if setup changes

## Areas for Contribution

Current priorities:

### High Priority
- [ ] Add more LLM providers (Llama, Cohere, etc.)
- [ ] Implement streaming responses
- [ ] Add unit tests
- [ ] Improve error handling

### Medium Priority
- [ ] Web interface (Gradio/Streamlit)
- [ ] Voting mechanisms for best responses
- [ ] Custom synthesis strategies
- [ ] Performance optimizations
- [ ] Caching layer

### Nice to Have
- [ ] Export to different formats (Markdown, PDF)
- [ ] Debate visualizations
- [ ] Conversation history management
- [ ] Agent personality customization
- [ ] Multi-language support

## Community

- Be respectful and constructive
- Help others in issues and discussions
- Share your use cases and experiences
- Suggest improvements

## Questions?

Feel free to open an issue for:
- Questions about the codebase
- Implementation discussions
- Feature proposals
- General feedback

---

Thank you for contributing to LLM Council! 🏛️

