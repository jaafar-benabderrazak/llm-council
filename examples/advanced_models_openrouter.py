"""
Example: Using Advanced Models via OpenRouter

OpenRouter provides access to 100+ advanced models including:
- GPT-4, GPT-4 Turbo, GPT-4o
- Claude 3 Opus, Sonnet, Haiku
- Llama 3.1 70B, 405B
- Mixtral 8x22B
- And many more...

Setup:
1. Get API key: https://openrouter.ai/keys
2. Add to .env: OPENROUTER_API_KEY=your-key
3. Run this example

Cost: Varies by model (typically $0.01-0.10 per debate)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.openrouter_agent import OpenRouterAgent
from agents import GeminiAgent, OllamaAgent
from council import LLMCouncil

def main():
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print("=" * 80)
    print("  ADVANCED MODELS - OPENROUTER EXAMPLE")
    print("=" * 80)
    print()
    print("This example uses premium models via OpenRouter:")
    print("  1. Claude 3.5 Sonnet (Anthropic) - Top quality")
    print("  2. GPT-4 Turbo (OpenAI) - Excellent reasoning")
    print("  3. Llama 3.1 70B (Meta) - Powerful open-source")
    print("  4. Gemini Flash (Google) - Fast & free")
    print()
    print("Cost: ~$0.05-0.15 per debate (premium models)")
    print("=" * 80)
    print()
    
    # Create council with mix of premium and free models
    agents = [
        # Premium models via OpenRouter
        OpenRouterAgent(
            name="Claude-3.5",
            model="anthropic/claude-3.5-sonnet",
            role="Premium Analysis - Top Quality"
        ),
        OpenRouterAgent(
            name="GPT-4",
            model="openai/gpt-4-turbo",
            role="Premium Analysis - Excellent Reasoning"
        ),
        OpenRouterAgent(
            name="Llama-70B",
            model="meta-llama/llama-3.1-70b-instruct",
            role="Powerful Open-Source via Cloud"
        ),
        
        # Free model for comparison
        GeminiAgent(
            name="Gemini",
            role="Fast Free Synthesis"
        )
    ]
    
    council = LLMCouncil(agents, verbose=True)
    
    topic = """
    Advanced cybersecurity architecture for zero-trust microservices:
    
    Analyze and provide:
    - Zero-trust implementation patterns with sources
    - Service mesh security (Istio, Linkerd, Cilium) comparison
    - mTLS best practices and pitfalls
    - Policy enforcement (OPA, Kyverno, Gatekeeper)
    - Identity and access management (SPIFFE/SPIRE)
    - Network segmentation strategies
    - Monitoring and observability
    - Recent CVEs and security advisories
    - References to NIST, OWASP, CNCF guidelines
    """
    
    print("Starting premium 4-model analysis...")
    print()
    
    result = council.debate(
        topic=topic,
        rounds=3,
        save_results=True,
        save_markdown=True
    )
    
    print()
    print("=" * 80)
    print("  PREMIUM ANALYSIS COMPLETE!")
    print("=" * 80)
    print()
    print(f"[OK] Models: 4 (3 Premium + 1 Free)")
    print(f"[OK] Rounds: 3")
    print(f"[OK] Tokens: {result.total_tokens:,}")
    print(f"[OK] Estimated cost: ~$0.05-0.15 (premium models)")
    print()
    print("Quality comparison:")
    print("  Premium models: Claude 3.5, GPT-4, Llama 70B")
    print("  Free model: Gemini Flash")
    print()
    print("Files generated:")
    print("  [JSON] debate_*.json")
    print("  [MD] article_*.md - Premium quality analysis")
    print()
    print("=" * 80)
    print()
    print("Model Summary:")
    print("-" * 80)
    print("Claude 3.5 Sonnet : Anthropic's latest, top quality analysis")
    print("GPT-4 Turbo      : OpenAI's advanced model, excellent reasoning")
    print("Llama 3.1 70B    : Meta's powerful open-source")
    print("Gemini Flash     : Google's fast free model for comparison")
    print()
    print("Benefits of premium models:")
    print("  [YES] Higher quality analysis")
    print("  [YES] Better reasoning and logic")
    print("  [YES] More accurate source validation")
    print("  [YES] Deeper technical insights")
    print()
    print("Cost breakdown (estimated):")
    print("  - Claude 3.5: ~$0.02-0.05")
    print("  - GPT-4: ~$0.02-0.05")
    print("  - Llama 70B: ~$0.005-0.01")
    print("  - Gemini: $0.00 (free)")
    print("  - Total: ~$0.045-0.11 per debate")
    print()
    print("=" * 80)
    print()
    print("Available OpenRouter models:")
    print("-" * 80)
    print("Anthropic:")
    print("  - anthropic/claude-3-opus (best quality, $$$)")
    print("  - anthropic/claude-3.5-sonnet (excellent, $$)")
    print("  - anthropic/claude-3-haiku (fast, $)")
    print()
    print("OpenAI:")
    print("  - openai/gpt-4o (latest, $$)")
    print("  - openai/gpt-4-turbo (excellent, $$)")
    print("  - openai/gpt-3.5-turbo (good, $)")
    print()
    print("Open-Source (via OpenRouter):")
    print("  - meta-llama/llama-3.1-405b-instruct (huge, $$)")
    print("  - meta-llama/llama-3.1-70b-instruct (powerful, $)")
    print("  - mistralai/mixtral-8x22b-instruct (excellent, $)")
    print("  - qwen/qwen-2.5-72b-instruct (strong, $)")
    print()
    print("See ADVANCED_MODELS_GUIDE.md for complete list!")
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()

