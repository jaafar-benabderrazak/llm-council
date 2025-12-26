"""Example 3: Custom council with specific models."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import ClaudeAgent, ChatGPTAgent
from council import LLMCouncil

def main():
    """Create a custom council with only Claude and ChatGPT."""
    
    # Create custom agents with specific roles
    agents = [
        ClaudeAgent(
            name="Claude - Security Expert",
            role="Cybersecurity and privacy specialist",
            temperature=0.6
        ),
        ChatGPTAgent(
            name="ChatGPT - Business Analyst",
            role="Business strategy and implementation expert",
            temperature=0.7
        )
    ]
    
    # Create council
    council = LLMCouncil(agents, verbose=True)
    
    # Discuss a specific topic
    topic = """
    A startup wants to implement end-to-end encryption for their messaging app.
    What are the key considerations from both security and business perspectives?
    """
    
    result = council.debate(
        topic=topic,
        rounds=2,  # Just 2 rounds for this focused discussion
        save_results=True
    )
    
    print("\nDebate complete!")
    print(f"Synthesis saved with {result.total_tokens} tokens used.")


if __name__ == "__main__":
    main()

