"""Example 5: Using specific models only."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Run a debate with only Claude and Gemini."""
    
    # Create council with specific models
    council = create_council(models=["claude", "gemini"])
    
    topic = """
    Compare and contrast functional programming and object-oriented programming.
    Which paradigm is better suited for building large-scale distributed systems?
    """
    
    result = council.debate(
        topic=topic,
        rounds=3,
        save_results=True
    )
    
    print(f"\n\nParticipants: {', '.join(result.participating_agents)}")


if __name__ == "__main__":
    main()

