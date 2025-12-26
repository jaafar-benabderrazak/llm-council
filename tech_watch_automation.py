"""
Tech Watch Automation - Python Script

This script automates technology monitoring by running scheduled
debates on various technology topics and organizing the results.

Usage:
    python tech_watch_automation.py

Customize:
    - Modify RESEARCH_TOPICS to add your topics
    - Adjust models and rounds per topic
    - Set output directory structure
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import create_council

# ===== Configuration =====

# Output directory structure
OUTPUT_BASE = Path("tech-watch")
CURRENT_MONTH = datetime.now().strftime("%Y-%m")
OUTPUT_DIR = OUTPUT_BASE / CURRENT_MONTH

# Research topics configuration
RESEARCH_TOPICS = [
    {
        "name": "kubernetes-security",
        "question": """
        Latest Kubernetes security features and best practices in 2025:
        - Recent CVEs and security updates
        - Security tools and integrations (Falco, OPA, etc.)
        - mTLS and service mesh security
        - RBAC improvements
        - Pod security standards
        - Supply chain security (SBOM, image scanning)
        - References to official security advisories
        """,
        "models": [
            "ollama:deepseek-coder:6.7b",
            "ollama:llama3.1:8b",
            "ollama:mistral:7b",
            "gemini"
        ],
        "rounds": 4,
        "category": "security"
    },
    {
        "name": "llm-deployment",
        "question": """
        LLM deployment strategies in 2025:
        - Cloud vs local deployment comparison
        - Quantization techniques (GGUF, GPTQ, AWQ)
        - Cost analysis with real numbers
        - Performance benchmarks
        - Inference optimization (vLLM, TGI, llama.cpp)
        - Production case studies
        - Technical references and benchmarks
        """,
        "models": [
            "ollama:llama3.1:8b",
            "ollama:mistral:7b",
            "gemini"
        ],
        "rounds": 4,
        "category": "ai-ml"
    },
    {
        "name": "cloud-native-trends",
        "question": """
        Cloud-native landscape trends Q1 2025:
        - Service mesh evolution (Istio, Linkerd, Cilium)
        - eBPF adoption for networking and observability
        - GitOps maturity (ArgoCD, Flux)
        - Cost optimization patterns
        - Multi-cloud strategies
        - Industry adoption statistics
        - References to CNCF reports
        """,
        "models": [
            "ollama:llama3.1:8b",
            "ollama:mistral:7b",
            "gemini"
        ],
        "rounds": 3,
        "category": "cloud-native"
    },
    {
        "name": "frontend-performance",
        "question": """
        Frontend performance optimization in 2025:
        - React, Vue, Svelte performance comparison
        - Core Web Vitals optimization
        - Bundle size optimization techniques
        - Rendering patterns (SSR, SSG, ISR, Streaming)
        - Performance monitoring tools
        - Real-world case studies
        - Benchmarks and statistics
        """,
        "models": [
            "ollama:llama3.1:8b",
            "ollama:mistral:7b",
            "gemini"
        ],
        "rounds": 3,
        "category": "frontend"
    }
]

# ===== Functions =====

def setup_directories():
    """Create output directory structure."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create category subdirectories
    categories = set(topic["category"] for topic in RESEARCH_TOPICS)
    for category in categories:
        (OUTPUT_DIR / category).mkdir(exist_ok=True)
    
    print(f"[OK] Output directory: {OUTPUT_DIR}")
    print()

def run_research(topic_config):
    """Run research debate for a single topic."""
    print("=" * 70)
    print(f"RESEARCHING: {topic_config['name']}")
    print("=" * 70)
    print()
    
    try:
        # Create council with specified models
        council = create_council(topic_config["models"])
        
        print(f"Models: {', '.join(topic_config['models'])}")
        print(f"Rounds: {topic_config['rounds']}")
        print()
        
        # Run debate
        result = council.debate(
            topic=topic_config["question"].strip(),
            rounds=topic_config["rounds"],
            save_results=True,
            save_markdown=True
        )
        
        print()
        print("[SUCCESS] Research completed!")
        print(f"  - Tokens: {result.total_tokens:,}")
        print(f"  - Cost: $0.00 (FREE!)")
        print()
        
        return {
            "status": "success",
            "topic": topic_config["name"],
            "category": topic_config["category"],
            "tokens": result.total_tokens,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"[ERROR] Research failed: {e}")
        print()
        return {
            "status": "error",
            "topic": topic_config["name"],
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def organize_results():
    """Organize generated files into category folders."""
    print("Organizing results...")
    
    # Get all generated files from current directory
    json_files = list(Path(".").glob("debate_*.json"))
    md_files = list(Path(".").glob("article_*.md"))
    
    moved_count = 0
    
    for file in json_files + md_files:
        # Try to match with a topic category
        for topic in RESEARCH_TOPICS:
            # Move to category folder
            dest = OUTPUT_DIR / topic["category"] / file.name
            file.rename(dest)
            moved_count += 1
            print(f"  Moved: {file.name} -> {topic['category']}/")
            break
    
    print(f"[OK] Moved {moved_count} files")
    print()

def generate_summary(results):
    """Generate summary report."""
    summary_file = OUTPUT_DIR / f"summary_{CURRENT_MONTH}.md"
    
    success_count = sum(1 for r in results if r["status"] == "success")
    error_count = len(results) - success_count
    total_tokens = sum(r.get("tokens", 0) for r in results if r["status"] == "success")
    
    summary_content = f"""# Tech Watch Summary - {CURRENT_MONTH}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Overview

- **Topics Researched**: {len(results)}
- **Successful**: {success_count}
- **Failed**: {error_count}
- **Total Tokens**: {total_tokens:,}
- **Total Cost**: $0.00 (100% FREE)

## Topics

"""
    
    # Group by category
    by_category = {}
    for result in results:
        category = result.get("category", "uncategorized")
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(result)
    
    for category, topics in sorted(by_category.items()):
        summary_content += f"\n### {category.title()}\n\n"
        for topic in topics:
            status_icon = "✅" if topic["status"] == "success" else "❌"
            summary_content += f"- {status_icon} **{topic['topic']}**\n"
            if topic["status"] == "success":
                summary_content += f"  - Tokens: {topic.get('tokens', 0):,}\n"
            else:
                summary_content += f"  - Error: {topic.get('error', 'Unknown')}\n"
    
    summary_content += f"""

## Files Generated

```bash
{OUTPUT_DIR}/
"""
    
    for category in sorted(by_category.keys()):
        summary_content += f"├── {category}/\n"
        category_dir = OUTPUT_DIR / category
        if category_dir.exists():
            files = list(category_dir.glob("*"))
            for i, file in enumerate(sorted(files)):
                prefix = "└──" if i == len(files) - 1 else "├──"
                summary_content += f"│   {prefix} {file.name}\n"
    
    summary_content += f"""```

## Next Steps

1. Review generated articles in `{OUTPUT_DIR}/`
2. Extract key insights and trends
3. Share findings with team
4. Schedule next tech watch cycle

---

**Generated by LLM Council** 🚀
Cost: $0.00 | Models: DeepSeek-Coder, Llama 3.1, Mistral, Gemini
"""
    
    summary_file.write_text(summary_content, encoding="utf-8")
    print(f"[OK] Summary saved to: {summary_file}")
    print()

def main():
    """Main execution function."""
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print()
    print("=" * 70)
    print("  LLM COUNCIL - TECH WATCH AUTOMATION")
    print("=" * 70)
    print()
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Topics: {len(RESEARCH_TOPICS)}")
    print()
    
    # Setup
    setup_directories()
    
    # Run research for each topic
    results = []
    for i, topic in enumerate(RESEARCH_TOPICS, 1):
        print(f"\n[{i}/{len(RESEARCH_TOPICS)}] ", end="")
        result = run_research(topic)
        results.append(result)
        
        # Small delay between topics
        if i < len(RESEARCH_TOPICS):
            import time
            print("Waiting 5 seconds before next topic...\n")
            time.sleep(5)
    
    # Organize results
    organize_results()
    
    # Generate summary
    generate_summary(results)
    
    # Final summary
    success_count = sum(1 for r in results if r["status"] == "success")
    error_count = len(results) - success_count
    
    print("=" * 70)
    print("  TECH WATCH COMPLETE!")
    print("=" * 70)
    print()
    print(f"[OK] Successful: {success_count}")
    print(f"[X] Failed: {error_count}")
    print()
    print(f"Results: {OUTPUT_DIR}")
    print()
    
    # List files
    json_count = len(list(OUTPUT_DIR.rglob("*.json")))
    md_count = len(list(OUTPUT_DIR.rglob("*.md")))
    
    print("Generated files:")
    print(f"  - JSON: {json_count}")
    print(f"  - Markdown: {md_count}")
    print()
    print("=" * 70)
    print()

if __name__ == "__main__":
    main()

