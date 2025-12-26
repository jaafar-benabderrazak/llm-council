"""Claude (Anthropic) agent implementation."""
from typing import Optional, List
from anthropic import Anthropic
from .base_agent import BaseAgent, AgentResponse
from config import Config


class ClaudeAgent(BaseAgent):
    """Agent powered by Claude (Anthropic)."""
    
    def __init__(
        self, 
        name: str = "Claude", 
        role: str = "Critical Analyst",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = Config.ANTHROPIC_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None
    ) -> AgentResponse:
        """Generate response using Claude."""
        try:
            system_prompt = self.get_system_prompt(context)
            
            messages = [
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=Config.MAX_TOKENS,
                temperature=self.temperature,
                system=system_prompt,
                messages=messages
            )
            
            content = response.content[0].text
            tokens_used = response.usage.input_tokens + response.usage.output_tokens
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

