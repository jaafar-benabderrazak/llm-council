"""Gemini (Google) agent implementation."""
from typing import Optional, List
import google.generativeai as genai
from .base_agent import BaseAgent, AgentResponse
from config import Config


class GeminiAgent(BaseAgent):
    """Agent powered by Gemini (Google)."""
    
    def __init__(
        self, 
        name: str = "Gemini", 
        role: str = "Research Synthesizer",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(Config.GOOGLE_MODEL)
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Gemini."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            full_prompt = f"{system_prompt}\n\nUser Question: {prompt}"
            
            generation_config = genai.types.GenerationConfig(
                temperature=self.temperature,
                max_output_tokens=Config.MAX_TOKENS
            )
            
            response = self.model.generate_content(
                full_prompt,
                generation_config=generation_config
            )
            
            content = response.text
            
            # Gemini doesn't always provide token counts in the same way
            tokens_used = None
            if hasattr(response, 'usage_metadata'):
                tokens_used = (
                    response.usage_metadata.prompt_token_count + 
                    response.usage_metadata.candidates_token_count
                )
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=Config.GOOGLE_MODEL,
                tokens_used=tokens_used,
                metadata={
                    "safety_ratings": [
                        {
                            "category": rating.category.name,
                            "probability": rating.probability.name
                        }
                        for rating in response.candidates[0].safety_ratings
                    ] if hasattr(response, 'candidates') else None
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=Config.GOOGLE_MODEL,
                metadata={"error": str(e)}
            )

