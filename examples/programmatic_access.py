"""Example 4: Programmatic access to debate results."""
import sys
from pathlib import Path
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Access and analyze debate results programmatically."""
    
    council = create_council()
    
    topic = "What are the ethical implications of using AI in hiring decisions?"
    
    # Run debate without verbose output
    council.verbose = False
    result = council.debate(topic=topic, rounds=2, save_results=False)
    
    # Access individual round responses
    print(f"Topic: {topic}\n")
    print(f"Total rounds: {len(result.rounds)}")
    print(f"Total tokens: {result.total_tokens}\n")
    
    # Analyze each round
    for round_num, round_responses in enumerate(result.rounds, 1):
        print(f"\n--- Round {round_num} ---")
        for response in round_responses:
            print(f"\n{response.agent_name}:")
            print(f"  Model: {response.model}")
            print(f"  Tokens: {response.tokens_used}")
            print(f"  Response length: {len(response.content)} characters")
            print(f"  Preview: {response.content[:100]}...")
    
    # Show synthesis
    print("\n\n" + "="*80)
    print("FINAL SYNTHESIS:")
    print("="*80)
    print(result.synthesis)
    
    # Save to custom location
    filename = result.save_to_file("my_debate_results.json")
    print(f"\n\nResults saved to: {filename}")
    
    # Load and verify
    with open(filename, 'r') as f:
        loaded_data = json.load(f)
        print(f"Verified: Loaded {len(loaded_data['rounds'])} rounds from file")


if __name__ == "__main__":
    main()

