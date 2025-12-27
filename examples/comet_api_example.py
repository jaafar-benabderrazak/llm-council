"""
Example: Using Comet API

This example demonstrates how to use Comet API in LLM Council.

Setup:
1. API key is already configured in .env
2. Run this example to test the integration

Note: Make sure to verify the correct base_url and model names
for Comet API in agents/comet_agent.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.comet_agent import CometAgent
from agents import GeminiAgent, OllamaAgent
from council import LLMCouncil

def main():
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print("=" * 80)
    print("  COMET API - EXAMPLE")
    print("=" * 80)
    print()
    print("This example uses Comet API alongside free models:")
    print("  1. Comet AI Model")
    print("  2. Ollama (Local)")
    print("  3. Gemini (Google)")
    print()
    print("=" * 80)
    print()
    
    try:
        # Create council with Comet + free models
        agents = [
            CometAgent(
                name="Comet",
                role="Comet AI Analysis"
            ),
            OllamaAgent(
                name="Llama",
                model="llama3.1:8b",
                role="Local Analysis"
            ),
            GeminiAgent(
                name="Gemini",
                role="Fast Cloud Synthesis"
            )
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        topic = """
        Analyze the security implications of microservices architecture:
        
        Provide:
        - Authentication and authorization patterns
        - Service-to-service communication security
        - Common vulnerabilities and mitigations
        - Best practices with sources
        - References to industry standards
        """
        
        print("Starting 3-model analysis...")
        print()
        
        result = council.debate(
            topic=topic,
            rounds=3,
            save_results=True,
            save_markdown=True
        )
        
        print()
        print("=" * 80)
        print("  ANALYSIS COMPLETE!")
        print("=" * 80)
        print()
        print(f"[OK] Models: 3 (Comet + Ollama + Gemini)")
        print(f"[OK] Rounds: 3")
        print(f"[OK] Tokens: {result.total_tokens:,}")
        print()
        print("Files generated:")
        print("  [JSON] debate_*.json")
        print("  [MD] article_*.md")
        print()
        print("=" * 80)
        
    except Exception as e:
        print()
        print("=" * 80)
        print("  ERROR")
        print("=" * 80)
        print()
        print(f"Failed to initialize or run debate: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Verify Comet API key is correct in .env")
        print("  2. Check if base_url in agents/comet_agent.py is correct")
        print("  3. Verify available models with Comet API documentation")
        print("  4. Check API key permissions and rate limits")
        print()
        print("Current configuration:")
        print(f"  - API Key: {os.getenv('COMET_API_KEY', 'Not set')[:20]}...")
        print(f"  - Model: {os.getenv('COMET_MODEL', 'Not set')}")
        print()
        print("=" * 80)
        
        import traceback
        print("\nFull error:")
        traceback.print_exc()

if __name__ == "__main__":
    main()

