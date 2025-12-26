"""Quick test script for free options - No paid API keys needed!"""
# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Add parent directory to path and change to project directory
project_dir = Path(__file__).parent
os.chdir(project_dir)
sys.path.insert(0, str(project_dir))

# Now import from the local config
import config
Config = config.Config

def main():
    """Check what free options are available."""
    
    print("="*70)
    print("FREE LLM COUNCIL - FREE OPTIONS CHECK")
    print("="*70)
    print()
    
    available = Config.get_available_models()
    
    print(f"Available models: {', '.join(available) if available else 'None'}")
    print()
    
    print("📋 Setup Status:")
    print()
    
    # Check each free option
    free_options = []
    
    # Ollama (local)
    try:
        import ollama
        print("✅ Ollama: Installed")
        print("   To use: 1) Download from https://ollama.ai/")
        print("          2) Run: ollama pull llama2")
        print("          3) Use: python main.py --models ollama")
        free_options.append("ollama")
    except ImportError:
        print("❌ Ollama: Not installed (pip install ollama)")
    print()
    
    # Groq (cloud)
    if Config.GROQ_API_KEY:
        print("✅ Groq: API key configured")
        print("   Ready to use: python main.py --models groq")
        free_options.append("groq")
    else:
        print("⚠️  Groq: No API key")
        print("   Get free key: https://console.groq.com/")
        print("   Add to .env: GROQ_API_KEY=your_key")
    print()
    
    # Gemini (free tier)
    if Config.GOOGLE_API_KEY:
        print("✅ Google Gemini: API key configured")
        print("   Ready to use: python main.py --models gemini")
        free_options.append("gemini")
    else:
        print("⚠️  Google Gemini: No API key")
        print("   Get free key: https://makersuite.google.com/")
        print("   Add to .env: GOOGLE_API_KEY=your_key")
    print()
    
    # HuggingFace
    try:
        import huggingface_hub
        print("✅ HuggingFace: Installed")
        print("   Optional token from: https://huggingface.co/settings/tokens")
        print("   Use: python main.py --models huggingface")
        free_options.append("huggingface")
    except ImportError:
        print("❌ HuggingFace: Not installed")
    print()
    
    print("="*70)
    print("SUMMARY")
    print("="*70)
    print()
    
    if len(free_options) >= 2:
        print(f"✅ You can run LLM Council with {len(free_options)} free options!")
        print()
        print("Quick start:")
        print(f"  python main.py \"Your topic\" --models {' '.join(free_options[:2])}")
        print()
    elif len(free_options) == 1:
        print(f"⚠️  Only 1 free option available: {free_options[0]}")
        print("   LLM Council needs at least 2 models for a debate.")
        print()
        print("Recommended: Add Groq (fastest setup)")
        print("1. Get free API key: https://console.groq.com/")
        print("2. Add to .env: GROQ_API_KEY=your_key")
        print()
    else:
        print("❌ No free options configured yet!")
        print()
        print("🚀 EASIEST SETUP (5 minutes):")
        print("1. Get Groq API key: https://console.groq.com/")
        print("2. Get Google API key: https://makersuite.google.com/")
        print("3. Create .env file:")
        print("   echo GROQ_API_KEY=your_groq_key >> .env")
        print("   echo GOOGLE_API_KEY=your_google_key >> .env")
        print("4. Run: python main.py \"Your topic\" --models groq gemini")
        print()
    
    print("="*70)
    print()
    print("See FREE_TIER_GUIDE.md for complete setup instructions")
    print()


if __name__ == "__main__":
    main()

