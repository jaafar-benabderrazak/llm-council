"""
Example: 100% FREE DeepSeek Research via Ollama

This example demonstrates using DeepSeek's open-source models
completely FREE through Ollama - no API key required!

Models available:
- deepseek-coder:6.7b (Code-focused, 3.8GB)
- deepseek-llm:7b (General purpose, 4.1GB)
- deepseek-r1:7b (Reasoning, 4.7GB)
- deepseek-coder:33b (Advanced, 19GB)

Benefits:
- 💰 100% FREE - No API costs
- 🔒 Complete privacy - Runs locally
- ⚡ No rate limits - Use as much as you want
- 📡 Works offline (after download)
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import OllamaAgent, GroqAgent
from council import LLMCouncil

def check_ollama_setup():
    """Check if Ollama and DeepSeek models are available."""
    try:
        import ollama
        client = ollama.Client()
        
        # Get available models
        models = client.list()
        model_names = [m['name'] for m in models['models']]
        
        # Check for DeepSeek models
        deepseek_models = [m for m in model_names if 'deepseek' in m.lower()]
        
        if deepseek_models:
            print("✅ DeepSeek models found:")
            for model in deepseek_models:
                print(f"   - {model}")
            return True, deepseek_models[0]
        else:
            print("❌ No DeepSeek models found")
            print()
            print("Install DeepSeek with:")
            print("  ollama pull deepseek-coder:6.7b   # For code (recommended)")
            print("  ollama pull deepseek-llm:7b       # For general tasks")
            print("  ollama pull deepseek-r1:7b        # For reasoning")
            print()
            return False, None
            
    except ImportError:
        print("❌ Ollama not installed")
        print()
        print("Install Ollama:")
        print("  1. Download from: https://ollama.ai/")
        print("  2. Install ollama Python package: pip install ollama")
        print("  3. Pull DeepSeek model: ollama pull deepseek-coder:6.7b")
        print()
        return False, None
    except Exception as e:
        print(f"❌ Error checking Ollama: {e}")
        print()
        print("Make sure Ollama is running!")
        return False, None

def main():
    print("=" * 80)
    print("100% FREE DEEPSEEK RESEARCH via Ollama")
    print("=" * 80)
    print()
    
    # Check setup
    has_deepseek, model_name = check_ollama_setup()
    
    if not has_deepseek:
        return
    
    print()
    print("=" * 80)
    print()
    
    # Example 1: Free Local DeepSeek Only
    print("EXAMPLE 1: Pure Local Research (100% Free)")
    print("-" * 80)
    
    topic1 = """
    Compare Python async/await vs threading:
    - Performance characteristics (cite benchmarks)
    - Use case recommendations (cite documentation)
    - Best practices (cite authoritative sources)
    """
    
    print(f"Topic: {topic1.strip()[:60]}...")
    print(f"Using: {model_name} (local, free)")
    print()
    
    try:
        deepseek = OllamaAgent(
            name="DeepSeek-Local",
            role="Code Analysis Expert - Free Local AI",
            model=model_name
        )
        
        council = LLMCouncil([deepseek])
        
        print("Running debate...")
        result = council.debate(
            topic=topic1,
            rounds=1,
            save_markdown=True
        )
        
        print()
        print("✅ Debate Complete!")
        print(f"   Tokens: {result.total_tokens:,}")
        print(f"   Cost: $0.00 (FREE!)")
        print()
        
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Example 2: DeepSeek + Groq (Both Free)
    print()
    print("=" * 80)
    print()
    print("EXAMPLE 2: Multi-Agent Free Research")
    print("-" * 80)
    
    topic2 = """
    Analyze microservices vs monolithic architecture for startups:
    - Scalability patterns (cite case studies)
    - Operational complexity (cite documentation)
    - Cost implications (cite data)
    - When to choose each approach
    """
    
    print(f"Topic: {topic2.strip()[:60]}...")
    print(f"Using: {model_name} (local, free) + Groq (cloud, free)")
    print()
    
    try:
        deepseek = OllamaAgent(
            name="DeepSeek",
            role="Technical Analysis Expert",
            model=model_name
        )
        
        # Try adding Groq if available
        try:
            groq = GroqAgent(
                name="Groq",
                role="Fast Inference Specialist"
            )
            agents = [deepseek, groq]
            print("✅ Groq added (free cloud API)")
        except:
            agents = [deepseek]
            print("ℹ️  Groq not configured (optional)")
            print("   Get free key: https://console.groq.com/")
        
        print()
        
        council = LLMCouncil(agents)
        
        print("Running 2-round research debate...")
        result = council.debate(
            topic=topic2,
            rounds=2,
            save_markdown=True
        )
        
        print()
        print("✅ Multi-Agent Debate Complete!")
        print(f"   Agents: {len(agents)}")
        print(f"   Rounds: 2")
        print(f"   Tokens: {result.total_tokens:,}")
        print(f"   Cost: $0.00 (100% FREE!)")
        print()
        print(f"   Files generated:")
        print(f"   - JSON: debate_*.json")
        print(f"   - Markdown: article_*.md (with Mermaid diagrams)")
        print()
        
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Summary
    print()
    print("=" * 80)
    print("SUMMARY: DeepSeek Free Open-Source Benefits")
    print("=" * 80)
    print()
    print("✅ Benefits:")
    print("   • 100% FREE - No API costs, ever")
    print("   • Complete privacy - Runs on your machine")
    print("   • No rate limits - Use unlimited")
    print("   • Works offline - After model download")
    print("   • Good quality - Competitive with GPT-3.5 for code")
    print()
    print("📊 Available Models:")
    print("   • deepseek-coder:6.7b (3.8GB) - Code analysis, debugging")
    print("   • deepseek-llm:7b (4.1GB) - General purpose")
    print("   • deepseek-r1:7b (4.7GB) - Reasoning tasks")
    print("   • deepseek-coder:33b (19GB) - Advanced (needs 32GB RAM)")
    print()
    print("🚀 Quick Start:")
    print("   1. Install: https://ollama.ai/")
    print("   2. Pull model: ollama pull deepseek-coder:6.7b")
    print("   3. Run: python examples/free_deepseek_debate.py")
    print()
    print("💡 Best Combination (All Free):")
    print("   DeepSeek (local) + Groq (cloud) + Gemini (free tier)")
    print("   = Multi-perspective research for $0.00")
    print()
    print("=" * 80)
    print("See DEEPSEEK_FREE_GUIDE.md for complete documentation")
    print("=" * 80)

if __name__ == "__main__":
    main()

