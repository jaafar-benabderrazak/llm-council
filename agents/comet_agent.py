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
    """
    
    def __init__(
        self, 
        name: str = "Comet",
        role: str = "Comet AI Model Agent",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        if OpenAI is None:
            raise ImportError(
                "OpenAI package required for Comet API. "
                "Install with: pip install openai"
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
        
        # Set model (use default or provided)
        self.model = model or getattr(
            Config, 
            'COMET_MODEL', 
            'gpt-3.5-turbo'  # Default model, adjust as needed
        )
    
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
                    "provider": "comet"
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

