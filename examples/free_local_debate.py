"""Example: Using completely FREE local models with Ollama."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

def main():
    """Run a debate using only free local Ollama models."""
    
    print("="*70)
    print("FREE LOCAL DEBATE - No API keys needed!")
    print("="*70)
    print()
    print("This example uses Ollama for completely free local inference.")
    print("Models run on your own hardware - no API costs!")
    print()
    
    try:
        from agents import OllamaAgent
        from council import LLMCouncil
        
        # Create multiple Ollama agents with different models
        agents = [
            OllamaAgent(
                name="Llama2",
                role="Critical Analyst",
                model="llama2"
            ),
            OllamaAgent(
                name="Mistral", 
                role="Pragmatic Problem Solver",
                model="mistral"
            ),
            OllamaAgent(
                name="CodeLlama",
                role="Technical Expert",
                model="codellama"
            )
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        topic = """
        What are the key considerations when choosing between 
        microservices and monolithic architecture for a new project?
        """
        
        print(f"Topic: {topic.strip()}")
        print()
        print("Starting local debate...")
        print()
        
        result = council.debate(
            topic=topic,
            rounds=2,  # Use fewer rounds for faster local inference
            save_results=True
        )
        
        print("\n" + "="*70)
        print("DEBATE COMPLETE - All processing done locally!")
        print(f"Total tokens: {result.total_tokens}")
        print("="*70)
        
    except ImportError:
        print("ERROR: Ollama not installed!")
        print()
        print("To use this example:")
        print("1. Install Ollama: https://ollama.ai/")
        print("2. Pull models:")
        print("   ollama pull llama2")
        print("   ollama pull mistral")
        print("   ollama pull codellama")
        print("3. Install Python package:")
        print("   pip install ollama")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()
        print("Make sure Ollama is running and models are downloaded:")
        print("  ollama list")


if __name__ == "__main__":
    main()

