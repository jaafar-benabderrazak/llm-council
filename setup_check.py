#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup script to verify LLM Council installation and configuration."""

import sys
import os
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')


def check_python_version():
    """Check Python version."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check if required packages are installed."""
    print("\nChecking dependencies...")
    required_packages = [
        "anthropic",
        "openai",
        "google.generativeai",
        "mistralai",
        "dotenv",
        "rich",
        "colorama"
    ]
    
    missing = []
    for package in required_packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            elif package == "google.generativeai":
                __import__("google", fromlist=["generativeai"])
            else:
                __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing.append(package)
    
    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True


def check_env_file():
    """Check if .env file exists and has keys."""
    print("\nChecking environment configuration...")
    
    if not Path(".env").exists():
        print("❌ .env file not found")
        print("   Copy env.example to .env and add your API keys")
        return False
    
    print("✓ .env file exists")
    
    # Try to load and check keys
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        keys = {
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
            "MISTRAL_API_KEY": os.getenv("MISTRAL_API_KEY")
        }
        
        configured = [k for k, v in keys.items() if v and v != f"your_{k.lower()}_here"]
        
        print(f"\nConfigured API keys: {len(configured)}/4")
        for key, value in keys.items():
            if value and value != f"your_{key.lower()}_here":
                print(f"✓ {key}")
            else:
                print(f"⚠ {key} (not configured)")
        
        if len(configured) < 2:
            print("\n⚠ Warning: At least 2 API keys required for LLM Council")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking .env: {e}")
        return False


def check_project_structure():
    """Check if all required files exist."""
    print("\nChecking project structure...")
    
    required_files = [
        "main.py",
        "council.py",
        "config.py",
        "requirements.txt",
        "agents/__init__.py",
        "agents/base_agent.py",
        "agents/claude_agent.py",
        "agents/chatgpt_agent.py",
        "agents/gemini_agent.py",
        "agents/mistral_agent.py"
    ]
    
    missing = []
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file}")
        else:
            print(f"❌ {file}")
            missing.append(file)
    
    if missing:
        print(f"\nMissing files: {', '.join(missing)}")
        return False
    
    return True


def main():
    """Run all checks."""
    print("="*60)
    print("LLM Council - Setup Verification")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Project Structure", check_project_structure),
        ("Environment Config", check_env_file)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Error during {name} check: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    
    all_passed = all(result for _, result in results)
    
    for name, result in results:
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 All checks passed! LLM Council is ready to use.")
        print("\nQuick start:")
        print("  python main.py")
        print("\nOr run an example:")
        print("  python examples/basic_debate.py")
        return 0
    else:
        print("\n⚠ Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

