"""Mistral AI agent implementation."""
from typing import Optional, List
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from .base_agent import BaseAgent, AgentResponse
from config import Config


class MistralAgent(BaseAgent):
    """Agent powered by Mistral AI."""
    
    def __init__(
        self, 
        name: str = "Mistral", 
        role: str = "Devil's Advocate",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        self.client = MistralClient(api_key=Config.MISTRAL_API_KEY)
        self.model = Config.MISTRAL_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Mistral."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            
            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(role="user", content=prompt)
            ]
            
            response = self.client.chat(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=Config.MAX_TOKENS
            )
            
            content = response.choices[0].message.content
            tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else None
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "prompt_tokens": response.usage.prompt_tokens if hasattr(response, 'usage') else None,
                    "completion_tokens": response.usage.completion_tokens if hasattr(response, 'usage') else None
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

