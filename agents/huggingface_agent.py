"""Hugging Face agent implementation for free inference API."""
from typing import Optional, List
try:
    from huggingface_hub import InferenceClient
except ImportError:
    InferenceClient = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class HuggingFaceAgent(BaseAgent):
    """Agent powered by Hugging Face Inference API (free tier available)."""
    
    def __init__(
        self, 
        name: str = "HuggingFace", 
        role: str = "Open Source Specialist",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        
        if InferenceClient is None:
            raise ImportError(
                "Hugging Face Hub not installed. Install with: pip install huggingface_hub"
            )
        
        self.model = Config.HUGGINGFACE_MODEL
        self.client = InferenceClient(
            model=self.model,
            token=Config.HUGGINGFACE_API_KEY  # Optional for public models
        )
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None
    ) -> AgentResponse:
        """Generate response using Hugging Face."""
        try:
            system_prompt = self.get_system_prompt(context)
            full_prompt = f"{system_prompt}\n\nUser: {prompt}\n\nAssistant:"
            
            # Use text generation
            response = self.client.text_generation(
                full_prompt,
                max_new_tokens=Config.MAX_TOKENS,
                temperature=self.temperature,
                return_full_text=False
            )
            
            content = response.strip()
            
            # HF doesn't always provide token counts
            tokens_used = None
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "inference_api": "huggingface",
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

