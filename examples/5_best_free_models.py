"""
Example: 5 Best FREE Models Multi-Agent Debate

This example uses 5 completely FREE models for comprehensive research:
1. DeepSeek-Coder (via Ollama) - Code & security expert
2. Llama 3.1 (via Ollama) - Meta's latest model
3. Mistral 7B (via Ollama) - Strong reasoning
4. Phi-3 Mini (via Ollama) - Microsoft's efficient model
5. Gemini Flash (via Google) - Fast, high-quality, free tier

ALL FREE - NO API COSTS!
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import OllamaAgent, GeminiAgent
from council import LLMCouncil

def main():
    print("=" * 80)
    print("5 BEST FREE MODELS - MULTI-AGENT RESEARCH")
    print("=" * 80)
    print()
    print("Using 5 completely FREE models:")
    print("  1. [Tech] DeepSeek-Coder 6.7B (Ollama) - Technical expert")
    print("  2. [Meta] Llama 3.1 8B (Ollama) - Meta's latest")
    print("  3. [Core] Mistral 7B (Ollama) - Strong reasoning")
    print("  4. [MSFT] Phi-3 Mini (Ollama) - Microsoft research")
    print("  5. [Fast] Gemini Flash (Google) - Fast & high quality")
    print()
    print("Cost: $0.00 | Rate Limits: Minimal | Quality: Excellent")
    print("=" * 80)
    print()
    
    # Create 5 free agents
    agents = [
        OllamaAgent(
            name="DeepSeek",
            role="Security & Code Expert",
            model="deepseek-coder:6.7b"
        ),
        OllamaAgent(
            name="Llama",
            role="General Analyst",
            model="llama3.1:8b"
        ),
        OllamaAgent(
            name="Mistral",
            role="Critical Thinker",
            model="mistral:7b"
        ),
        OllamaAgent(
            name="Phi",
            role="Efficient Analyst",
            model="phi3:mini"
        ),
        GeminiAgent(
            name="Gemini",
            role="Fast Research Synthesizer"
        )
    ]
    
    council = LLMCouncil(agents, verbose=True)
    
    topic = """
    How to make A2A (Application-to-Application) protocol secure and reliable?
    
    Provide:
    - Security best practices with sources
    - Authentication mechanisms (OAuth, mTLS, API keys)
    - Common vulnerabilities and mitigations
    - Reliability patterns (retry, circuit breaker, timeout)
    - Monitoring and observability
    - References to OWASP, NIST, RFC standards
    """
    
    print("Running 3-round research debate with 5 FREE models...")
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
    print(f"[OK] Agents: {len(agents)}")
    print(f"[OK] Rounds: 3")
    print(f"[OK] Tokens: {result.total_tokens:,}")
    print(f"[OK] Cost: $0.00 (100% FREE!)")
    print()
    print("Files generated:")
    print("  [DATA] debate_*.json - Raw data")
    print("  [ARTICLE] article_*.md - Comprehensive article with Mermaid diagrams")
    print()
    print("=" * 80)
    print()
    print("[SUCCESS] 5 FREE Models Summary:")
    print("-" * 80)
    print("DeepSeek-Coder : Technical & security analysis")
    print("Llama 3.1      : Latest Meta model, well-rounded")
    print("Mistral 7B     : Strong reasoning and logic")
    print("Phi-3 Mini     : Microsoft's efficient model")
    print("Gemini Flash   : Google's fast, high-quality model")
    print()
    print("ALL models have:")
    print("  [YES] No API costs")
    print("  [YES] No rate limits (Ollama) or generous limits (Gemini)")
    print("  [YES] Good quality")
    print("  [YES] Multiple perspectives")
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()

