"""OpenRouter agent implementation - Access to 100+ advanced models."""
from typing import Optional, List
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class OpenRouterAgent(BaseAgent):
    """
    Agent powered by OpenRouter - Access to 100+ models.
    
    Supported models:
    - anthropic/claude-3.5-sonnet
    - anthropic/claude-3-opus
    - openai/gpt-4-turbo
    - openai/gpt-4o
    - meta-llama/llama-3.1-70b-instruct
    - meta-llama/llama-3.1-405b-instruct
    - mistralai/mixtral-8x22b-instruct
    - qwen/qwen-2.5-72b-instruct
    - And 90+ more...
    
    Get API key: https://openrouter.ai/keys
    """
    
    def __init__(
        self, 
        name: str = "OpenRouter",
        role: str = "Advanced Multi-Model Agent",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        if OpenAI is None:
            raise ImportError(
                "OpenAI package required for OpenRouter. "
                "Install with: pip install openai"
            )
        
        # Get API key from config
        api_key = getattr(Config, 'OPENROUTER_API_KEY', None)
        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY not found in environment. "
                "Get a key from https://openrouter.ai/keys "
                "and add to your .env file"
            )
        
        # Initialize OpenAI client with OpenRouter base URL
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        
        # Set model (default to Claude 3.5 Sonnet)
        self.model = model or getattr(
            Config, 
            'OPENROUTER_MODEL', 
            'anthropic/claude-3.5-sonnet'
        )
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using OpenRouter."""
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
                max_tokens=getattr(Config, 'MAX_TOKENS', 2000),
                extra_headers={
                    "HTTP-Referer": "https://github.com/jaafar-benabderrazak/llm-council",
                    "X-Title": "LLM Council"
                }
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
                    "provider": "openrouter"
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

