"""Base agent class for LLM Council."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class AgentResponse:
    """Response from an agent."""
    agent_name: str
    content: str
    model: str
    tokens_used: Optional[int] = None
    metadata: Optional[Dict] = None


class BaseAgent(ABC):
    """Abstract base class for all LLM agents."""
    
    def __init__(self, name: str, role: str, temperature: float = 0.7):
        """
        Initialize the agent.
        
        Args:
            name: Agent name/identifier
            role: Agent's role in the discussion
            temperature: Sampling temperature for responses
        """
        self.name = name
        self.role = role
        self.temperature = temperature
        self.conversation_history: List[Dict[str, str]] = []
    
    @abstractmethod
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None
    ) -> AgentResponse:
        """
        Generate a response to the given prompt.
        
        Args:
            prompt: The prompt/question to respond to
            context: Previous responses from other agents
            
        Returns:
            AgentResponse containing the agent's response
        """
        pass
    
    def format_context(self, context: Optional[List[AgentResponse]]) -> str:
        """Format previous responses as context."""
        if not context:
            return ""
        
        formatted = "\n\n--- Previous Responses ---\n"
        for response in context:
            formatted += f"\n{response.agent_name} ({response.model}):\n{response.content}\n"
        formatted += "\n--- End of Previous Responses ---\n"
        return formatted
    
    def add_to_history(self, role: str, content: str):
        """Add a message to conversation history."""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_system_prompt(self, context: Optional[List[AgentResponse]] = None) -> str:
        """Get the system prompt for this agent."""
        base_prompt = f"""You are {self.name}, an expert AI participating in a council discussion.

Your role: {self.role}

Instructions:
1. Provide thoughtful, well-reasoned responses
2. Challenge weak arguments and support strong ones
3. Consider different perspectives
4. Build upon or respectfully critique other council members' points
5. Be specific and provide examples when possible
6. Stay focused on the topic at hand"""

        if context:
            base_prompt += "\n\n" + self.format_context(context)
        
        return base_prompt

