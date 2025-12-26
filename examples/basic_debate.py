"""Example 1: Basic usage of LLM Council."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Run a simple debate on AI ethics."""
    
    # Create council with all available models
    council = create_council()
    
    # Define the topic
    topic = """
    Should AI companies be required to make their training data publicly available?
    Consider: transparency, privacy, competition, and innovation.
    """
    
    # Run the debate (3 rounds by default)
    result = council.debate(
        topic=topic,
        rounds=3,
        save_results=True
    )
    
    print("\n" + "="*80)
    print("SYNTHESIS:")
    print("="*80)
    print(result.synthesis)
    print("\n" + "="*80)
    print(f"Total tokens used: {result.total_tokens}")
    print(f"Participating agents: {', '.join(result.participating_agents)}")


if __name__ == "__main__":
    main()

