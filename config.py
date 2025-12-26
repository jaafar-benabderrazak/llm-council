"""Configuration module for LLM Council."""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for API keys and model settings."""
    
    # Paid API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    MISTRAL_API_KEY: Optional[str] = os.getenv("MISTRAL_API_KEY")
    
    # Free/Open Source API Keys (optional)
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    HUGGINGFACE_API_KEY: Optional[str] = os.getenv("HUGGINGFACE_API_KEY")  # Optional for public models
    DEEPSEEK_API_KEY: Optional[str] = os.getenv("DEEPSEEK_API_KEY")  # DeepSeek (Chinese provider, affordable)
    
    # Paid Model Names
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
    ANTHROPIC_MODEL: str = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
    GOOGLE_MODEL: str = os.getenv("GOOGLE_MODEL", "gemini-1.5-pro")
    MISTRAL_MODEL: str = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
    
    # Free/Open Source Model Names
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama2")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    HUGGINGFACE_MODEL: str = os.getenv("HUGGINGFACE_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
    DEEPSEEK_MODEL: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")  # deepseek-chat or deepseek-coder
    
    # Council Settings
    MAX_ROUNDS: int = int(os.getenv("MAX_ROUNDS", "3"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "2000"))
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that at least some models are available (API keys OR installed packages)."""
        # Check paid API keys
        keys = [
            cls.OPENAI_API_KEY,
            cls.ANTHROPIC_API_KEY,
            cls.GOOGLE_API_KEY,
            cls.MISTRAL_API_KEY,
            cls.GROQ_API_KEY,
            cls.DEEPSEEK_API_KEY
        ]
        available_keys = [k for k in keys if k]
        
        # Check for installed free packages
        free_packages = []
        try:
            import ollama
            free_packages.append("ollama")
        except ImportError:
            pass
        
        try:
            import groq
            if cls.GROQ_API_KEY:  # Groq needs an API key
                free_packages.append("groq")
        except ImportError:
            pass
        
        try:
            import huggingface_hub
            free_packages.append("huggingface")
        except ImportError:
            pass
        
        total_available = len(available_keys) + len(free_packages)
        
        if total_available < 2:
            raise ValueError(
                f"At least 2 models must be available for LLM Council to work.\n"
                f"Found: {len(available_keys)} API key(s) and {len(free_packages)} free package(s).\n\n"
                f"Options:\n"
                f"1. Add API keys to your .env file (OpenAI, Anthropic, Google, Mistral, Groq, or DeepSeek)\n"
                f"2. Install free packages: pip install ollama groq huggingface-hub\n"
                f"3. For Ollama: Download from https://ollama.ai/ and run 'ollama pull llama2'\n"
                f"4. For Groq: Get free API key from https://console.groq.com/\n"
                f"5. For DeepSeek: Get affordable API key from https://platform.deepseek.com/\n\n"
                f"See FREE_TIER_GUIDE.md for complete setup instructions."
            )
        return True
    
    @classmethod
    def get_available_models(cls) -> list[str]:
        """Return list of available models based on API keys and installed packages."""
        models = []
        
        # Paid models
        if cls.OPENAI_API_KEY:
            models.append("chatgpt")
        if cls.ANTHROPIC_API_KEY:
            models.append("claude")
        if cls.GOOGLE_API_KEY:
            models.append("gemini")
        if cls.MISTRAL_API_KEY:
            models.append("mistral")
        
        # Affordable/Free models
        if cls.DEEPSEEK_API_KEY:
            models.append("deepseek")
        
        # Free/Open source models
        try:
            import ollama
            models.append("ollama")
        except ImportError:
            pass
        
        if cls.GROQ_API_KEY:
            try:
                import groq
                models.append("groq")
            except ImportError:
                pass
        
        try:
            import huggingface_hub
            models.append("huggingface")
        except ImportError:
            pass
        
        return models

