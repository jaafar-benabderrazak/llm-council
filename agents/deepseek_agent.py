"""DeepSeek agent implementation."""
from typing import Optional, List
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class DeepSeekAgent(BaseAgent):
    """Agent powered by DeepSeek (Chinese LLM provider with OpenAI-compatible API)."""
    
    def __init__(
        self, 
        name: str = "DeepSeek", 
        role: str = "Technical Innovator",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        
        if OpenAI is None:
            raise ImportError(
                "OpenAI package not installed. Install with: pip install openai"
            )
        
        if not Config.DEEPSEEK_API_KEY:
            raise ValueError(
                "DEEPSEEK_API_KEY not found in environment. "
                "Get an API key from https://platform.deepseek.com/"
            )
        
        # DeepSeek uses OpenAI-compatible API
        self.client = OpenAI(
            api_key=Config.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"
        )
        self.model = Config.DEEPSEEK_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using DeepSeek."""
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
                max_tokens=Config.MAX_TOKENS
            )
            
            content = response.choices[0].message.content
            
            # DeepSeek provides usage information
            tokens_used = None
            if response.usage:
                tokens_used = response.usage.total_tokens
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "provider": "deepseek",
                    "finish_reason": response.choices[0].finish_reason
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e), "provider": "deepseek"}
            )

