"""Example: Using FREE cloud APIs (Groq + Google Gemini)."""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import create_council

def main():
    """Run a debate using only free cloud APIs."""
    
    print("="*70)
    print("FREE CLOUD DEBATE - Using free tier APIs!")
    print("="*70)
    print()
    print("This example uses:")
    print("  • Groq (free API - ultra fast inference)")
    print("  • Google Gemini (free tier available)")
    print()
    print("Setup required:")
    print("  1. Get free Groq API key: https://console.groq.com/")
    print("  2. Get free Google API key: https://makersuite.google.com/")
    print("  3. Add to .env file:")
    print("     GROQ_API_KEY=your_key")
    print("     GOOGLE_API_KEY=your_key")
    print()
    
    try:
        # Use only free models
        council = create_council(models=["groq", "gemini"])
        
        topic = """
        What are the top 3 emerging AI technologies that will 
        transform software development in the next 2 years?
        """
        
        print(f"Topic: {topic.strip()}")
        print()
        print("Starting debate with free APIs...")
        print()
        
        result = council.debate(
            topic=topic,
            rounds=3,
            save_results=True
        )
        
        print("\n" + "="*70)
        print("DEBATE COMPLETE - Using only free tier APIs!")
        print(f"Total tokens: {result.total_tokens}")
        print("Cost: $0.00 (free tier)")
        print("="*70)
        
    except ValueError as e:
        print(f"\nSetup Error: {e}")
        print()
        print("To use this example:")
        print("1. Get free API keys:")
        print("   - Groq: https://console.groq.com/")
        print("   - Google: https://makersuite.google.com/")
        print("2. Add to your .env file:")
        print("   GROQ_API_KEY=your_groq_key")
        print("   GOOGLE_API_KEY=your_google_key")
        print("3. Install packages:")
        print("   pip install groq google-generativeai")
        print()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

