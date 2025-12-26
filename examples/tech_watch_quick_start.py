"""
Quick Start - Tech Watch Example

Run your first technology monitoring session in minutes!

This example demonstrates how to quickly set up and run
technology watch on current hot topics.

Usage:
    python examples/tech_watch_quick_start.py
"""

import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_council

def main():
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    print("=" * 80)
    print("  TECH WATCH - QUICK START")
    print("=" * 80)
    print()
    print("This example will research 3 current hot topics in technology:")
    print("  1. Kubernetes security best practices")
    print("  2. LLM deployment strategies")
    print("  3. Cloud cost optimization")
    print()
    print("Each topic will be analyzed by 4 FREE AI models:")
    print("  - DeepSeek-Coder (security & code expert)")
    print("  - Llama 3.1 (well-rounded analysis)")
    print("  - Mistral (critical thinking)")
    print("  - Gemini 2.5 (fast synthesis)")
    print()
    print("Cost: $0.00 | Time: ~5-10 minutes")
    print("=" * 80)
    print()
    
    # Topic 1: Kubernetes Security
    print("\n" + "=" * 80)
    print("[1/3] TOPIC: Kubernetes Security Best Practices")
    print("=" * 80)
    print()
    
    council_k8s = create_council([
        "ollama:deepseek-coder:6.7b",
        "ollama:llama3.1:8b",
        "ollama:mistral:7b",
        "gemini"
    ])
    
    result_k8s = council_k8s.debate(
        topic="""
        Kubernetes security best practices in 2025:
        - Latest CVE vulnerabilities and fixes
        - Pod security standards and enforcement
        - Network policies and zero-trust implementation
        - RBAC best practices
        - Image scanning and supply chain security
        - Security tools (Falco, OPA, Kyverno)
        - References to official K8s security documentation
        - Recent security incidents and lessons learned
        """,
        rounds=4,
        save_results=True,
        save_markdown=True
    )
    
    print(f"\n[OK] Topic 1 completed: {result_k8s.total_tokens:,} tokens")
    
    # Topic 2: LLM Deployment
    print("\n" + "=" * 80)
    print("[2/3] TOPIC: LLM Deployment Strategies")
    print("=" * 80)
    print()
    
    council_llm = create_council([
        "ollama:llama3.1:8b",
        "ollama:mistral:7b",
        "gemini"
    ])
    
    result_llm = council_llm.debate(
        topic="""
        LLM deployment strategies comparison in 2025:
        - Cloud providers (AWS Bedrock, Azure OpenAI, GCP Vertex)
        - Self-hosted solutions (vLLM, Text Generation Inference)
        - Local deployment (Ollama, llama.cpp)
        - Quantization techniques (GGUF, GPTQ, AWQ) with benchmarks
        - Cost analysis with real numbers
        - Performance comparison (tokens/second, latency)
        - Use case recommendations
        - References to benchmarks and case studies
        """,
        rounds=3,
        save_results=True,
        save_markdown=True
    )
    
    print(f"\n[OK] Topic 2 completed: {result_llm.total_tokens:,} tokens")
    
    # Topic 3: Cloud Cost Optimization
    print("\n" + "=" * 80)
    print("[3/3] TOPIC: Cloud Cost Optimization")
    print("=" * 80)
    print()
    
    council_cost = create_council([
        "ollama:llama3.1:8b",
        "ollama:mistral:7b",
        "gemini"
    ])
    
    result_cost = council_cost.debate(
        topic="""
        Cloud cost optimization strategies for 2025:
        - FinOps best practices with sources
        - Right-sizing compute resources
        - Spot instances and reserved capacity
        - Kubernetes cost optimization (cluster autoscaling, pod right-sizing)
        - Storage optimization techniques
        - Cost monitoring and alerting tools
        - Multi-cloud cost comparison
        - Real-world cost savings case studies
        - References to FinOps framework and tools
        """,
        rounds=3,
        save_results=True,
        save_markdown=True
    )
    
    print(f"\n[OK] Topic 3 completed: {result_cost.total_tokens:,} tokens")
    
    # Summary
    total_tokens = result_k8s.total_tokens + result_llm.total_tokens + result_cost.total_tokens
    
    print()
    print("=" * 80)
    print("  TECH WATCH SESSION COMPLETE!")
    print("=" * 80)
    print()
    print(f"[OK] Topics Researched: 3")
    print(f"[OK] Total Tokens: {total_tokens:,}")
    print(f"[OK] Total Cost: $0.00 (100% FREE!)")
    print()
    print("Generated Files:")
    print("  - 6 JSON files (raw debate data)")
    print("  - 6 Markdown articles (formatted reports with diagrams)")
    print()
    print("Next Steps:")
    print("  1. Review the generated Markdown articles")
    print("  2. Extract key insights and trends")
    print("  3. Share findings with your team")
    print("  4. Customize topics for your specific needs")
    print()
    print("To customize topics, edit: examples/tech_watch_quick_start.py")
    print("To automate weekly: Run tech_watch_automation.py")
    print()
    print("=" * 80)
    print()
    print("📚 Read TECH_WATCH_GUIDE.md for comprehensive guide!")
    print()

if __name__ == "__main__":
    main()

