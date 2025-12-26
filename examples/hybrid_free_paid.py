"""Example: Mixing free and paid models for optimal cost/quality."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Run a debate mixing free and paid models."""
    
    print("="*70)
    print("HYBRID DEBATE - Mix free and paid models")
    print("="*70)
    print()
    print("This example demonstrates mixing:")
    print("  • Free: Groq (fast) + Local Ollama")
    print("  • Paid: Claude (premium quality)")
    print()
    print("Strategy: Use free models for initial rounds,")
    print("          paid model for synthesis/refinement")
    print()
    
    try:
        from agents import GroqAgent, OllamaAgent, ClaudeAgent
        from council import LLMCouncil
        
        # Mix of free and paid agents
        agents = [
            GroqAgent(
                name="Groq-Fast",
                role="Quick Analysis Specialist"
            ),
            OllamaAgent(
                name="Llama-Local",
                role="Local Reasoning Expert",
                model="llama2"
            ),
            ClaudeAgent(
                name="Claude-Premium",
                role="Critical Synthesis Expert"
            )
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        topic = """
        How should a startup balance technical debt vs feature velocity 
        in their first year?
        """
        
        print(f"Topic: {topic.strip()}")
        print()
        
        result = council.debate(
            topic=topic,
            rounds=3,
            save_results=True
        )
        
        print("\n" + "="*70)
        print("HYBRID DEBATE COMPLETE")
        print(f"Total tokens: {result.total_tokens}")
        print("Strategy: Free models for volume, paid for quality")
        print("="*70)
        
    except Exception as e:
        print(f"Error: {e}")
        print()
        print("This example requires:")
        print("  • Ollama running locally (ollama.ai)")
        print("  • Groq API key (free at console.groq.com)")
        print("  • Claude API key (anthropic.com)")


if __name__ == "__main__":
    main()

