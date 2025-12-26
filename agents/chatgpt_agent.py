"""ChatGPT (OpenAI) agent implementation."""
from typing import Optional, List
from openai import OpenAI
from .base_agent import BaseAgent, AgentResponse
from config import Config


class ChatGPTAgent(BaseAgent):
    """Agent powered by ChatGPT (OpenAI)."""
    
    def __init__(
        self, 
        name: str = "ChatGPT", 
        role: str = "Pragmatic Problem Solver",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using ChatGPT."""
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
            tokens_used = response.usage.total_tokens
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )

