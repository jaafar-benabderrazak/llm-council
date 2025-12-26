"""Main LLM Council orchestrator."""
import sys
import os
from typing import List, Optional, Dict
from dataclasses import dataclass, asdict
import json
from datetime import datetime

# Fix Windows console encoding issues with Rich
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

from agents import BaseAgent, AgentResponse
from config import Config


@dataclass
class DebateResult:
    """Results from a council debate."""
    topic: str
    rounds: List[List[AgentResponse]]
    synthesis: str
    timestamp: str
    total_tokens: int
    participating_agents: List[str]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "topic": self.topic,
            "timestamp": self.timestamp,
            "total_tokens": self.total_tokens,
            "participating_agents": self.participating_agents,
            "rounds": [
                [
                    {
                        "agent_name": resp.agent_name,
                        "model": resp.model,
                        "content": resp.content,
                        "tokens_used": resp.tokens_used,
                        "metadata": resp.metadata
                    }
                    for resp in round_responses
                ]
                for round_responses in self.rounds
            ],
            "synthesis": self.synthesis
        }
    
    def save_to_file(self, filename: Optional[str] = None):
        """Save debate results to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"debate_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
        
        return filename


class LLMCouncil:
    """Orchestrates multi-agent debates between different LLMs."""
    
    def __init__(self, agents: List[BaseAgent], verbose: bool = True):
        """
        Initialize the LLM Council.
        
        Args:
            agents: List of agents to participate in debates
            verbose: Whether to print progress information
        """
        self.agents = agents
        self.verbose = verbose
        if verbose:
            # Use legacy_windows=False to avoid encoding issues on Windows
            self.console = Console(legacy_windows=False) if sys.platform == "win32" else Console()
        else:
            self.console = None
    
    def debate(
        self, 
        topic: str, 
        rounds: int = 3,
        save_results: bool = True
    ) -> DebateResult:
        """
        Conduct a multi-round debate on a topic.
        
        Args:
            topic: The topic to debate
            rounds: Number of debate rounds
            save_results: Whether to save results to file
            
        Returns:
            DebateResult containing all responses and synthesis
        """
        if self.verbose:
            self.console.print(Panel.fit(
                f"[bold cyan]LLM Council Debate[/bold cyan]\n\n"
                f"[yellow]Topic:[/yellow] {topic}\n"
                f"[yellow]Rounds:[/yellow] {rounds}\n"
                f"[yellow]Participants:[/yellow] {', '.join([a.name for a in self.agents])}",
                border_style="cyan"
            ))
        
        all_rounds = []
        context = None
        total_tokens = 0
        
        # Conduct debate rounds
        for round_num in range(rounds):
            if self.verbose:
                self.console.print(f"\n[bold green]=== Round {round_num + 1}/{rounds} ===[/bold green]\n")
            
            round_responses = self._conduct_round(topic, context, round_num + 1)
            all_rounds.append(round_responses)
            context = round_responses
            
            # Calculate tokens
            for response in round_responses:
                if response.tokens_used:
                    total_tokens += response.tokens_used
        
        # Generate synthesis
        if self.verbose:
            self.console.print("\n[bold magenta]=== Generating Synthesis ===[/bold magenta]\n")
        
        synthesis = self._generate_synthesis(topic, all_rounds)
        
        # Create result
        result = DebateResult(
            topic=topic,
            rounds=all_rounds,
            synthesis=synthesis,
            timestamp=datetime.now().isoformat(),
            total_tokens=total_tokens,
            participating_agents=[agent.name for agent in self.agents]
        )
        
        # Save if requested
        if save_results:
            filename = result.save_to_file()
            if self.verbose:
                self.console.print(f"\n[dim]Results saved to: {filename}[/dim]")
        
        if self.verbose:
            self.console.print("\n[bold green]Debate Complete![/bold green]")
            self._display_synthesis(synthesis)
        
        return result
    
    def _conduct_round(
        self, 
        topic: str, 
        context: Optional[List[AgentResponse]], 
        round_num: int
    ) -> List[AgentResponse]:
        """Conduct a single debate round with all agents."""
        responses = []
        
        # Build the prompt based on round number
        if round_num == 1:
            prompt = f"""Discuss the following topic and provide your initial perspective with proper citations and sources:

TOPIC: {topic}

Remember to:
- Provide technical depth and specific examples
- Cite authoritative sources (research papers, documentation, official resources)
- Include URLs or proper citations
- Be precise with technical specifications"""
        else:
            prompt = f"""Review the previous responses and provide your critical analysis:

TOPIC: {topic}

Your tasks for Round {round_num}:
- VALIDATE sources provided by other council members
- CROSS-CHECK facts and identify any errors
- CHALLENGE weak arguments with counter-evidence
- BUILD ON strong points with additional sources
- ADDRESS common misconceptions
- PROVIDE new insights with proper citations"""
        
        for agent in self.agents:
            if self.verbose:
                self.console.print(f"[cyan]{agent.name} thinking...[/cyan]")
                response = agent.generate_response(prompt, context, round_num)
                self._display_response(response)
            else:
                response = agent.generate_response(prompt, context, round_num)
            
            responses.append(response)
            
            # Update context for next agent in this round
            if context is None:
                context = [response]
            else:
                context = context + [response]
        
        return responses
    
    def _generate_synthesis(
        self, 
        topic: str, 
        all_rounds: List[List[AgentResponse]]
    ) -> str:
        """Generate a comprehensive academic-style article from all debate rounds."""
        # Use the first agent to synthesize
        synthesizer = self.agents[0]
        
        # Build comprehensive context
        all_responses = []
        for round_num, round_responses in enumerate(all_rounds, 1):
            for response in round_responses:
                all_responses.append(response)
        
        synthesis_prompt = f"""Based on the council's multi-round discussion on: "{topic}"

You must now write a COMPREHENSIVE ACADEMIC-STYLE ARTICLE that:

1. **EXECUTIVE SUMMARY**
   - Brief overview of the topic and key findings
   - Main conclusions (2-3 sentences)

2. **INTRODUCTION**
   - Context and importance of the topic
   - Key questions addressed
   - Scope of the analysis

3. **DETAILED ANALYSIS**
   - Synthesize all perspectives presented
   - Include technical details, specifications, and data points
   - Organize by themes or sub-topics
   - Use headings and subheadings

4. **SOURCE VALIDATION & CROSS-CHECKING**
   - Evaluate the quality and reliability of sources cited
   - List VERIFIED sources (URLs, papers, documentation)
   - Note any conflicting sources or disputed claims
   - Rate source credibility (High/Medium/Low with justification)

5. **CONSENSUS & DISAGREEMENTS**
   - Points of strong agreement across council members
   - Areas of disagreement with competing evidence
   - Nuanced perspectives that warrant consideration

6. **COMMON MISCONCEPTIONS ADDRESSED**
   - Identify and correct common misunderstandings about this topic
   - Explain why these misconceptions are wrong
   - Provide correct information with sources

7. **TECHNICAL DEEP DIVE**
   - Detailed technical specifications, benchmarks, or data
   - Implementation considerations
   - Performance characteristics (if applicable)
   - Trade-offs and limitations

8. **GAPS & LIMITATIONS**
   - What the council couldn't fully address
   - Areas requiring further research
   - Acknowledged uncertainties

9. **ACTIONABLE RECOMMENDATIONS**
   - Concrete, specific recommendations
   - Prioritized by importance and feasibility
   - Context-dependent guidance (when to do X vs Y)

10. **VERIFIED REFERENCES & RESOURCES**
    - Complete list of all cited sources
    - Format: [Title/Description] - [URL or Citation] - [Credibility Rating]
    - Organize by category (Research Papers, Documentation, Tools, etc.)

11. **CONCLUSION**
    - Summary of findings
    - Final verdict or recommendations
    - Future outlook

**FORMAT REQUIREMENTS:**
- Use Markdown formatting with proper headers (##, ###)
- Include bullet points and numbered lists where appropriate
- Make it readable, comprehensive, and academically rigorous
- Minimum 1000 words for complex topics
- Every major claim should reference a source from the debate
- Be thorough, objective, and balanced

Generate the complete article now:"""

        if self.verbose:
            self.console.print("[magenta]Generating comprehensive article with verified sources...[/magenta]")
            synthesis_response = synthesizer.generate_response(
                synthesis_prompt, 
                all_responses,
                round_num=999  # Special round number for synthesis
            )
        else:
            synthesis_response = synthesizer.generate_response(
                synthesis_prompt, 
                all_responses,
                round_num=999
            )
        
        return synthesis_response.content
    
    def _display_response(self, response: AgentResponse):
        """Display an agent response in the console."""
        if not self.verbose:
            return
        
        title = f"[bold]{response.agent_name}[/bold] ({response.model})"
        if response.tokens_used:
            title += f" - {response.tokens_used} tokens"
        
        self.console.print(Panel(
            Markdown(response.content),
            title=title,
            border_style="blue",
            padding=(1, 2)
        ))
    
    def _display_synthesis(self, synthesis: str):
        """Display the final comprehensive article."""
        if not self.verbose:
            return
        
        self.console.print("\n")
        self.console.print(Panel(
            Markdown(synthesis),
            title="[bold magenta]COMPREHENSIVE ARTICLE - Council Synthesis with Verified Sources[/bold magenta]",
            border_style="magenta",
            padding=(1, 2)
        ))
    
    def quick_discuss(self, topic: str) -> str:
        """Quick single-round discussion (no multi-round debate)."""
        responses = self._conduct_round(topic, None, 1)
        synthesis = self._generate_synthesis(topic, [responses])
        return synthesis

