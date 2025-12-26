"""
Example: 5 Best FREE Models with Specific Model Selection

This example demonstrates using multiple different Ollama models
in a single debate by specifying each model explicitly.

Models used:
1. ollama:deepseek-coder:6.7b - Code & security expert
2. ollama:llama3.1:8b - Meta's latest model  
3. ollama:mistral:7b - Strong reasoning
4. ollama:phi3:mini - Microsoft's efficient model
5. gemini - Google's fast Gemini Flash

Run with: python examples/5_models_specific.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_council

def main():
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print("=" * 80)
    print("5 SPECIFIC FREE MODELS - MULTI-PERSPECTIVE DEBATE")
    print("=" * 80)
    print()
    print("Using 5 specific models in one debate:")
    print("  1. [DeepSeek] deepseek-coder:6.7b (Ollama) - Code & security")
    print("  2. [Llama3.1] llama3.1:8b (Ollama) - Meta's latest")
    print("  3. [Mistral] mistral:7b (Ollama) - Strong reasoning")
    print("  4. [Phi3] phi3:mini (Ollama) - Microsoft research")
    print("  5. [Gemini] gemini-1.5-flash (Google Cloud) - Fast synthesis")
    print()
    print("Cost: $0.00 | ALL FREE | 5 Different AI Perspectives")
    print("=" * 80)
    print()
    
    # Create council with specific models
    council = create_council([
        "ollama:deepseek-coder:6.7b",
        "ollama:llama3.1:8b",
        "ollama:mistral:7b",
        "ollama:phi3:mini",
        "gemini"
    ])
    
    topic = """
    How to make A2A (Application-to-Application) protocol secure and reliable?
    
    Provide technical details with sources:
    - Authentication mechanisms (OAuth 2.0, mTLS, JWT, API keys)
    - Security best practices (OWASP, NIST guidelines)
    - Common vulnerabilities (injection, MITM, replay attacks)
    - Reliability patterns (circuit breaker, retry with backoff, timeout)
    - Monitoring and observability (metrics, logging, tracing)
    - Standards and RFC references
    """
    
    print("Starting 3-round research debate...")
    print()
    
    result = council.debate(
        topic=topic,
        rounds=3,
        save_results=True,
        save_markdown=True
    )
    
    print()
    print("=" * 80)
    print("DEBATE COMPLETE!")
    print("=" * 80)
    print()
    print(f"[OK] Agents: 5 (DeepSeek-Coder, Llama 3.1, Mistral, Phi-3, Gemini)")
    print(f"[OK] Rounds: 3")
    print(f"[OK] Tokens: {result.total_tokens:,}")
    print(f"[OK] Cost: $0.00 (100% FREE)")
    print()
    print("Files generated:")
    print("  [JSON] debate_*.json - Raw debate data")
    print("  [MD] article_*.md - Formatted article with diagrams")
    print()
    print("=" * 80)
    print()
    print("Model Summary:")
    print("-" * 80)
    print("DeepSeek-Coder 6.7B : Technical security & code analysis")
    print("Llama 3.1 8B        : Meta's latest, general intelligence")
    print("Mistral 7B          : Strong reasoning & critical thinking")
    print("Phi-3 Mini          : Microsoft's efficient model")
    print("Gemini Flash        : Google's fast cloud synthesis")
    print()
    print("Benefits:")
    print("  [YES] 5 diverse AI perspectives")
    print("  [YES] Completely free (no API costs)")
    print("  [YES] No rate limits (4 local + 1 generous cloud)")
    print("  [YES] High quality research output")
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()

