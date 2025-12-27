"""Comet API agent implementation."""
from typing import Optional, List
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class CometAgent(BaseAgent):
    """
    Agent powered by Comet API.
    
    Comet provides access to various AI models through their API.
    Supports category-based model selection for easy aggregation.
    
    Categories:
    - 'advanced': Premium models (gpt-5.2, claude-3-opus, gpt-4-turbo)
    - 'opensource': Open-source models (llama-3.1-70b, mixtral-8x7b)
    - 'free': Economical models (gpt-3.5-turbo, claude-3-haiku)
    - 'fast': Ultra-fast models (gpt-3.5-turbo, claude-3-haiku)
    """
    
    # Model categories for aggregation
    CATEGORIES = {
        'advanced': ['gpt-5.2', 'gpt-4-turbo', 'gpt-4', 'claude-3-opus', 'claude-3-sonnet'],
        'opensource': ['llama-3.1-70b', 'llama-3-70b', 'mixtral-8x7b', 'mistral-large', 'qwen-72b'],
        'free': ['gpt-3.5-turbo', 'claude-3-haiku', 'llama-3-8b'],
        'fast': ['gpt-3.5-turbo', 'claude-3-haiku', 'gemini-pro']
    }
    
    def __init__(
        self, 
        name: str = "Comet",
        role: str = "Comet AI Model Agent",
        temperature: float = 0.7,
        model: str = None,
        category: str = None  # NEW: auto-select from category
    ):
        super().__init__(name, role, temperature)
        if OpenAI is None:
            raise ImportError(
                "OpenAI package required for Comet API. "
                "Install with: pip install openai"
            )
        
        # Auto-select model from category if specified
        if category and not model:
            if category.lower() in self.CATEGORIES:
                model = self.CATEGORIES[category.lower()][0]  # Use first in category
                if name == "Comet":  # Update default name with category
                    self.name = f"Comet-{category.title()}"
            else:
                raise ValueError(
                    f"Unknown category: {category}. "
                    f"Choose from: {', '.join(self.CATEGORIES.keys())}"
                )
        
        # Get API key from config
        api_key = getattr(Config, 'COMET_API_KEY', None)
        if not api_key:
            raise ValueError(
                "COMET_API_KEY not found in environment. "
                "Add your key to .env file"
            )
        
        # Initialize OpenAI-compatible client with Comet base URL
        # Note: Adjust base_url if Comet uses a different endpoint
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.comet.ml/api/v1"  # Adjust if needed
        )
        
        # Set model (use provided, category-selected, or default)
        self.model = model or getattr(
            Config, 
            'COMET_MODEL', 
            'gpt-3.5-turbo'  # Default model
        )
        
        # Store category for metadata
        self.category = category
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Comet API."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=getattr(Config, 'MAX_TOKENS', 2000)
            )
            
            content = response.choices[0].message.content
            tokens_used = response.usage.total_tokens if response.usage else None
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "input_tokens": response.usage.prompt_tokens if response.usage else None,
                    "output_tokens": response.usage.completion_tokens if response.usage else None,
                    "provider": "comet",
                    "category": self.category  # Include category in metadata
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

