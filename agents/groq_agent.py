"""Groq agent implementation for fast, free cloud inference."""
from typing import Optional, List
try:
    from groq import Groq
except ImportError:
    Groq = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class GroqAgent(BaseAgent):
    """Agent powered by Groq (free, ultra-fast inference)."""
    
    def __init__(
        self, 
        name: str = "Groq", 
        role: str = "Fast Inference Specialist",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        
        if Groq is None:
            raise ImportError(
                "Groq package not installed. Install with: pip install groq"
            )
        
        if not Config.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found in environment. "
                "Get a free API key from https://console.groq.com/"
            )
        
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None
    ) -> AgentResponse:
        """Generate response using Groq."""
        try:
            system_prompt = self.get_system_prompt(context)
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=Config.MAX_TOKENS
            )
            
            content = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "free_tier": True
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

