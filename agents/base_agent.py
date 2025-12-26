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
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
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
    
    def get_system_prompt(self, context: Optional[List[AgentResponse]] = None, round_num: int = 1) -> str:
        """Get the system prompt for this agent."""
        if round_num == 1:
            base_prompt = f"""You are {self.name}, an expert AI participating in a council discussion.

Your role: {self.role}

Instructions for Round {round_num} (Initial Analysis):
1. Provide a thorough, well-researched analysis with technical depth
2. **CITE SOURCES**: Include specific references, research papers, documentation links, or authoritative sources
3. Use proper citations (e.g., "According to [Source], ..." or "Research shows [Reference] that...")
4. Provide concrete examples, data points, and technical specifications where applicable
5. Structure your response with clear sections (Analysis, Evidence, Technical Details, References)
6. Be precise with terminology and explain technical concepts
7. Include relevant URLs, paper titles (with authors/year), or documentation references

FORMAT YOUR RESPONSE AS:
## Analysis
[Your main analysis]

## Technical Evidence
[Specific technical details, data, specifications]

## References & Sources
- [Source 1]: [URL or citation]
- [Source 2]: [URL or citation]
[Add more as needed]"""
        else:
            base_prompt = f"""You are {self.name}, an expert AI participating in a council discussion.

Your role: {self.role}

Instructions for Round {round_num} (Critical Review & Cross-Checking):
1. **VALIDATE SOURCES**: Review and verify references provided by other council members
2. **CROSS-CHECK FACTS**: Identify any factual errors, outdated information, or broken logic
3. **CHALLENGE ASSUMPTIONS**: Question weak arguments with counter-evidence and alternative sources
4. **BUILD ON STRONG POINTS**: Support solid arguments with additional references and evidence
5. **PROVIDE NEW INSIGHTS**: Add perspectives not yet covered, with proper citations
6. **FLAG MISCONCEPTIONS**: Address common misunderstandings related to the topic
7. **TECHNICAL DEPTH**: Dive deeper into technical specifications, benchmarks, or data

CRITICAL REVIEW CHECKLIST:
- Are the cited sources authoritative and current?
- Are there contradicting sources or alternative viewpoints?
- Are technical claims verifiable?
- What evidence is missing?
- What are common misconceptions about this topic?

FORMAT YOUR RESPONSE AS:
## Source Validation
[Review of others' sources - which are valid, which need verification]

## Counter-Analysis / Challenges
[Your challenges to weak points, with supporting evidence]

## Additional Evidence
[New sources and technical details you're contributing]

## Common Misconceptions Addressed
[What people often get wrong about this topic]

## References & Sources
- [Source 1]: [URL or citation] - [Why this source is credible]
- [Source 2]: [URL or citation] - [Why this source is credible]
[Add more as needed]"""

        if context:
            base_prompt += "\n\n" + self.format_context(context)
        
        return base_prompt

