"""Example 2: Quick discussion mode."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Run a quick single-round discussion."""
    
    # Create council
    council = create_council()
    
    # Quick discussion (single round, faster)
    topic = "What are the top 3 emerging technologies that will transform healthcare in the next 5 years?"
    
    print(f"Topic: {topic}\n")
    print("Running quick discussion...\n")
    
    synthesis = council.quick_discuss(topic)
    
    print("\n" + "="*80)
    print("RESULT:")
    print("="*80)
    print(synthesis)


if __name__ == "__main__":
    main()

