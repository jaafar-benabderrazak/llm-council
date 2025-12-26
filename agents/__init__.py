"""Agent implementations for different LLM providers."""
from .base_agent import BaseAgent, AgentResponse

# Paid APIs (optional - only import if packages are installed)
try:
    from .claude_agent import ClaudeAgent
except ImportError:
    ClaudeAgent = None

try:
    from .chatgpt_agent import ChatGPTAgent
except ImportError:
    ChatGPTAgent = None

try:
    from .gemini_agent import GeminiAgent
except ImportError:
    GeminiAgent = None

try:
    from .mistral_agent import MistralAgent
except ImportError:
    MistralAgent = None

# Free/Open Source Options
try:
    from .ollama_agent import OllamaAgent
except ImportError:
    OllamaAgent = None

try:
    from .groq_agent import GroqAgent
except ImportError:
    GroqAgent = None

try:
    from .huggingface_agent import HuggingFaceAgent
except ImportError:
    HuggingFaceAgent = None

__all__ = [
    "BaseAgent",
    "AgentResponse",
    "ClaudeAgent",
    "ChatGPTAgent",
    "GeminiAgent",
    "MistralAgent",
    "OllamaAgent",
    "GroqAgent",
    "HuggingFaceAgent",
]

