"""
Example: Using DeepSeek - Affordable Chinese LLM

DeepSeek is a Chinese LLM provider offering:
- Affordable API pricing (significantly cheaper than OpenAI/Anthropic)
- Good performance for technical tasks
- DeepSeek-Chat: General purpose model
- DeepSeek-Coder: Specialized for coding tasks
- OpenAI-compatible API (easy integration)

Pricing: ~10x cheaper than GPT-4, ~5x cheaper than Claude
API: https://platform.deepseek.com/

This example demonstrates using DeepSeek in LLM Council for cost-effective research.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_council

def main():
    print("=" * 80)
    print("DEEPSEEK EXAMPLE - Affordable AI Research")
    print("=" * 80)
    print()
    print("DeepSeek Benefits:")
    print("  💰 10x cheaper than GPT-4")
    print("  🚀 Good performance for technical tasks")
    print("  🔧 DeepSeek-Coder available for code-specific tasks")
    print("  🌏 Chinese AI provider alternative")
    print()
    print("Get API key: https://platform.deepseek.com/")
    print("=" * 80)
    print()
    
    # Example 1: Technical Analysis with DeepSeek + Groq (both affordable/free)
    topic = """
    Compare React vs Vue.js for a large-scale enterprise application:
    - Performance benchmarks (cite specific tests)
    - Learning curve and developer productivity (cite surveys)
    - Ecosystem and tooling (cite package statistics)
    - Enterprise adoption (cite case studies)
    
    Provide technical specifications and authoritative sources.
    """
    
    print("Running affordable research debate...")
    print("Using: DeepSeek + Groq (cost-effective combination)")
    print()
    
    try:
        # Try DeepSeek + Groq combination (very affordable)
        council = create_council(models=["deepseek", "groq"])
        
        result = council.debate(
            topic=topic,
            rounds=2,
            save_results=True,
            save_markdown=True
        )
        
        print()
        print("=" * 80)
        print("DEBATE COMPLETE!")
        print("=" * 80)
        print()
        print(f"Total Tokens Used: {result.total_tokens:,}")
        print(f"Estimated Cost with DeepSeek: ~${result.total_tokens * 0.00000014:.6f}")
        print(f"(Compare to GPT-4: ~${result.total_tokens * 0.00003:.4f})")
        print()
        print("Cost savings: ~200x cheaper than GPT-4!")
        print()
        print("=" * 80)
        
    except ValueError as e:
        print(f"Error: {e}")
        print()
        print("Setup Instructions:")
        print("1. Get DeepSeek API key: https://platform.deepseek.com/")
        print("2. Get Groq API key: https://console.groq.com/ (free)")
        print("3. Add to .env file:")
        print("   DEEPSEEK_API_KEY=your_key_here")
        print("   GROQ_API_KEY=your_key_here")
        print("4. Run: python examples/deepseek_example.py")
        return
    
    # Example 2: Code Analysis with DeepSeek-Coder
    print()
    print("=" * 80)
    print("TIP: For code-specific tasks, use DeepSeek-Coder model")
    print("=" * 80)
    print()
    print("In your .env file, set:")
    print("  DEEPSEEK_MODEL=deepseek-coder")
    print()
    print("DeepSeek-Coder is optimized for:")
    print("  • Code review and analysis")
    print("  • Algorithm explanations")
    print("  • Debugging assistance")
    print("  • Technical architecture discussions")
    print()
    print("=" * 80)
    
    # Cost comparison
    print()
    print("COST COMPARISON (per 1M tokens):")
    print("-" * 80)
    print("  GPT-4 Turbo:        $10.00 input / $30.00 output")
    print("  Claude 3.5 Sonnet:  $3.00 input  / $15.00 output")
    print("  DeepSeek-Chat:      $0.14 input  / $0.28 output  ← ~70x cheaper!")
    print("  DeepSeek-Coder:     $0.14 input  / $0.28 output")
    print("  Groq (Llama3):      FREE (with rate limits)")
    print("-" * 80)
    print()
    print("For a typical 3-round debate (10K-15K tokens):")
    print("  GPT-4:      ~$0.30-0.45")
    print("  Claude:     ~$0.09-0.15")
    print("  DeepSeek:   ~$0.002-0.004  ← Extremely affordable!")
    print("  Groq:       $0.00 (free)")
    print()
    print("=" * 80)
    print("RECOMMENDATION: Use DeepSeek + Groq for cost-effective research!")
    print("=" * 80)

if __name__ == "__main__":
    main()

