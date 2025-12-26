"""Ollama agent implementation for free local LLM inference."""
from typing import Optional, List
try:
    import ollama
except ImportError:
    ollama = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class OllamaAgent(BaseAgent):
    """Agent powered by Ollama (free local LLMs)."""
    
    def __init__(
        self, 
        name: str = "Llama", 
        role: str = "Local Reasoning Expert",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        
        if ollama is None:
            raise ImportError(
                "Ollama package not installed. Install with: pip install ollama"
            )
        
        self.model = model or Config.OLLAMA_MODEL
        self.client = ollama.Client()
        
        # Verify model is available
        try:
            available_models = [m['name'] for m in self.client.list()['models']]
            if self.model not in available_models:
                print(f"Warning: Model '{self.model}' not found locally.")
                print(f"Available models: {', '.join(available_models)}")
                print(f"Pull it with: ollama pull {self.model}")
        except Exception as e:
            print(f"Warning: Could not verify Ollama models: {e}")
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Ollama."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            
            response = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                options={
                    "temperature": self.temperature,
                    "num_predict": Config.MAX_TOKENS
                }
            )
            
            content = response['message']['content']
            
            # Ollama provides some token info
            tokens_used = None
            if 'eval_count' in response:
                tokens_used = response.get('prompt_eval_count', 0) + response.get('eval_count', 0)
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "total_duration": response.get('total_duration'),
                    "load_duration": response.get('load_duration'),
                    "eval_count": response.get('eval_count'),
                    "local": True
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e), "local": True}
            )

