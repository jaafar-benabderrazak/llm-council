"""
Example: Research-Style Debate with Source Validation and Comprehensive Article

This example demonstrates the enhanced LLM Council features:
1. Agents provide sources and citations in Round 1
2. Agents validate and cross-check sources in subsequent rounds
3. Technical depth with specifications and data
4. Final output is a comprehensive academic-style article
5. Addresses common misconceptions
6. Includes verified references

Perfect for:
- Research projects
- Technical decision-making
- Academic literature reviews
- Comprehensive analysis with citations
"""

import sys
import os

# Add parent directory to path to import from main project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_council

def main():
    # Example 1: Technical Architecture Decision
    print("=" * 80)
    print("RESEARCH ARTICLE DEBATE - Technical Architecture Decision")
    print("=" * 80)
    
    topic = """
    Should a fast-growing startup with 100K users choose PostgreSQL or MongoDB 
    for their primary database? Consider:
    - Performance characteristics
    - Scalability patterns
    - Operational complexity
    - Cost implications
    - Team expertise requirements
    
    Provide technical specifications, benchmarks, and cite authoritative sources.
    """
    
    # Use 3 agents with 3 rounds for thorough analysis
    council = create_council(
        topic=topic,
        agents=["groq", "gemini"],  # Using free tier for demonstration
        rounds=3
    )
    
    result = council.debate(
        topic=topic,
        rounds=3,
        save_results=True
    )
    
    print("\n" + "=" * 80)
    print("Article saved to JSON file for further use!")
    print("=" * 80)
    
    # Example 2: Research Topic Analysis
    print("\n\n" + "=" * 80)
    print("RESEARCH ARTICLE DEBATE - AI/ML Topic")
    print("=" * 80)
    
    topic2 = """
    Analyze the current state of large language model reasoning capabilities:
    - Chain-of-Thought vs Tree-of-Thought approaches
    - Benchmarks and performance comparisons
    - Practical applications and limitations
    - Common misconceptions about LLM reasoning
    
    Cite research papers, technical documentation, and benchmark results.
    """
    
    council2 = create_council(
        topic=topic2,
        agents=["groq", "gemini"],
        rounds=2
    )
    
    result2 = council2.debate(
        topic=topic2,
        rounds=2,
        save_results=True
    )
    
    print("\n" + "=" * 80)
    print("COMPREHENSIVE ARTICLES GENERATED!")
    print("Check the JSON files for the complete analysis with sources.")
    print("=" * 80)

if __name__ == "__main__":
    main()

