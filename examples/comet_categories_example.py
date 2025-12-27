"""
Example: Comet API with Model Categories

This example demonstrates using Comet API models organized by categories:
- Advanced: Premium quality (gpt-5.2, claude-3-opus, gpt-4-turbo)
- Open-Source: Balance quality/cost (llama-3.1-70b, mixtral-8x7b)
- Free: Economical (gpt-3.5-turbo, claude-3-haiku)
- Fast: Ultra-fast (gpt-3.5-turbo, claude-3-haiku)

Usage:
    python examples/comet_categories_example.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.comet_agent import CometAgent
from agents import GeminiAgent, OllamaAgent
from council import LLMCouncil

def example_advanced_category():
    """Example: Using advanced category models."""
    print("=" * 80)
    print("  COMET API - ADVANCED CATEGORY")
    print("=" * 80)
    print()
    print("Using premium models for maximum quality")
    print()
    
    try:
        agents = [
            CometAgent(name="GPT-5", model="gpt-5.2", role="Advanced Analysis"),
            CometAgent(name="Claude-Opus", model="claude-3-opus", role="Deep Reasoning"),
            CometAgent(name="GPT-4", model="gpt-4-turbo", role="Expert Analysis"),
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        result = council.debate(
            "Advanced cryptography patterns for zero-trust architectures",
            rounds=3
        )
        
        print(f"\n[OK] Advanced analysis complete: {result.total_tokens:,} tokens")
        print("[COST] Premium models ($$$$)")
        
    except Exception as e:
        print(f"[ERROR] {e}")

def example_mixed_categories():
    """Example: Mix categories for balanced approach."""
    print("\n" + "=" * 80)
    print("  COMET API - MIXED CATEGORIES")
    print("=" * 80)
    print()
    print("Mixing advanced, open-source, and free models")
    print()
    
    try:
        agents = [
            # Advanced for quality
            CometAgent(name="GPT-4", model="gpt-4-turbo", role="Premium Analysis"),
            
            # Open-source for balance
            CometAgent(name="Llama-70B", model="llama-3.1-70b", role="Open Analysis"),
            
            # Free for cost control
            CometAgent(name="GPT-3.5", model="gpt-3.5-turbo", role="Quick Validation"),
            
            # Local free model
            OllamaAgent(name="Local", model="llama3.1:8b", role="Local Analysis"),
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        result = council.debate(
            "Design patterns for microservices with verified sources",
            rounds=3
        )
        
        print(f"\n[OK] Mixed analysis complete: {result.total_tokens:,} tokens")
        print("[COST] Balanced ($$)")
        
    except Exception as e:
        print(f"[ERROR] {e}")

def example_category_auto_select():
    """Example: Auto-select models from category."""
    print("\n" + "=" * 80)
    print("  COMET API - AUTO-SELECT FROM CATEGORY")
    print("=" * 80)
    print()
    print("Using category parameter for automatic model selection")
    print()
    
    try:
        agents = [
            # Auto-select from categories
            CometAgent(category="advanced"),      # Will use gpt-5.2
            CometAgent(category="opensource"),    # Will use llama-3.1-70b
            CometAgent(category="free"),          # Will use gpt-3.5-turbo
            GeminiAgent(),                        # Free cloud model
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        result = council.debate(
            "Cloud-native architecture patterns with best practices",
            rounds=2
        )
        
        print(f"\n[OK] Auto-select complete: {result.total_tokens:,} tokens")
        print("[MODELS] Auto-selected from each category")
        
    except Exception as e:
        print(f"[ERROR] {e}")

def example_cost_effective():
    """Example: Cost-effective setup with free/open-source."""
    print("\n" + "=" * 80)
    print("  COMET API - COST-EFFECTIVE")
    print("=" * 80)
    print()
    print("Using only free and open-source models")
    print()
    
    try:
        agents = [
            # Free Comet models
            CometAgent(name="GPT-3.5", model="gpt-3.5-turbo", role="Quick Analysis"),
            CometAgent(name="Haiku", model="claude-3-haiku", role="Fast Response"),
            
            # Open-source Comet
            CometAgent(name="Llama-70B", model="llama-3.1-70b", role="Open Analysis"),
            
            # Free local
            OllamaAgent(name="Local", model="llama3.1:8b"),
            
            # Free cloud
            GeminiAgent(),
        ]
        
        council = LLMCouncil(agents, verbose=True)
        
        result = council.debate(
            "Database design patterns for high-availability systems",
            rounds=3
        )
        
        print(f"\n[OK] Cost-effective analysis: {result.total_tokens:,} tokens")
        print("[COST] Minimal ($)")
        
    except Exception as e:
        print(f"[ERROR] {e}")

def main():
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print("\n" + "=" * 80)
    print("  COMET API - MODEL CATEGORIES EXAMPLES")
    print("=" * 80)
    print()
    print("This example demonstrates 4 different category-based setups:")
    print("  1. Advanced: Premium models only")
    print("  2. Mixed: Balance quality and cost")
    print("  3. Auto-select: Automatic category selection")
    print("  4. Cost-effective: Free and open-source only")
    print()
    print("=" * 80)
    print()
    
    # Run examples
    examples = [
        ("Advanced Category", example_advanced_category),
        ("Mixed Categories", example_mixed_categories),
        ("Auto-Select", example_category_auto_select),
        ("Cost-Effective", example_cost_effective),
    ]
    
    for name, func in examples:
        try:
            func()
        except Exception as e:
            print(f"\n[SKIP] {name}: {e}")
        
        input("\nPress Enter to continue to next example...")
    
    print("\n" + "=" * 80)
    print("  ALL EXAMPLES COMPLETE!")
    print("=" * 80)
    print()
    print("Category Summary:")
    print("-" * 80)
    print("Advanced   : Maximum quality, highest cost ($$$$)")
    print("Mixed      : Balanced quality/cost ($$)")
    print("Open-Source: Good quality, moderate cost ($)")
    print("Free       : Economical, good for quick tasks ($)")
    print()
    print("Recommendations:")
    print("- Critical research: Use 'advanced' category")
    print("- Production decisions: Use 'mixed' categories")
    print("- General analysis: Use 'opensource' category")
    print("- Quick tasks: Use 'free' or 'fast' category")
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()

