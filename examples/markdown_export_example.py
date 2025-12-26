"""
Example: Markdown Article Export with Mermaid Diagrams

This example demonstrates how LLM Council automatically generates:
1. Comprehensive Markdown article with proper formatting
2. Mermaid diagrams showing debate flow and statistics
3. Round-by-round analysis
4. Final synthesis with verified sources
5. Beautiful, shareable documentation

The generated Markdown file can be:
- Viewed in GitHub (with rendered Mermaid diagrams)
- Converted to PDF
- Shared as documentation
- Published as blog posts
- Used in academic papers
"""

import sys
import os

# Add parent directory to path to import from main project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_council

def main():
    print("=" * 80)
    print("MARKDOWN ARTICLE EXPORT DEMONSTRATION")
    print("=" * 80)
    print()
    print("This example will generate a comprehensive Markdown article with:")
    print("  ✅ Mermaid diagrams (debate flow, statistics)")
    print("  ✅ Round-by-round analysis")
    print("  ✅ Comprehensive synthesis with sources")
    print("  ✅ Token distribution charts")
    print("  ✅ Beautiful formatting for GitHub/documentation")
    print()
    print("=" * 80)
    print()
    
    # Example 1: Technical Decision with Markdown Export
    topic = """
    Compare serverless computing vs traditional server infrastructure:
    - Cost structure (cite pricing data)
    - Performance characteristics (cite benchmarks)
    - Scalability patterns (reference documentation)
    - Use case recommendations (provide examples)
    
    Include technical specifications and authoritative sources.
    """
    
    print("Running research debate...")
    print(f"Topic: {topic.strip()[:100]}...")
    print()
    
    # Create council with free tier models (or use paid models if available)
    try:
        council = create_council(
            models=["groq", "gemini"]  # Free tier for demonstration
        )
    except:
        # Fallback to any available models
        council = create_council()
    
    # Run debate - automatically saves both JSON and Markdown
    result = council.debate(
        topic=topic,
        rounds=2,  # 2 rounds: analysis + validation
        save_results=True,  # Saves JSON
        save_markdown=True  # Saves Markdown with Mermaid diagrams
    )
    
    print()
    print("=" * 80)
    print("MARKDOWN ARTICLE GENERATED!")
    print("=" * 80)
    print()
    print("Files generated:")
    print(f"  📄 JSON (raw data): debate_*.json")
    print(f"  📝 Markdown (article): article_*.md")
    print()
    print("The Markdown file includes:")
    print("  • Mermaid diagram showing debate flow")
    print("  • Mermaid sequence diagram of agent interactions")
    print("  • Round-by-round agent responses")
    print("  • Comprehensive synthesis article")
    print("  • Mermaid pie chart of token distribution")
    print("  • Statistics table")
    print()
    print("View the article:")
    print("  • Open in any Markdown editor")
    print("  • Push to GitHub (Mermaid renders automatically)")
    print("  • Convert to PDF with pandoc or similar tools")
    print("  • Share as documentation")
    print()
    print("=" * 80)
    
    # Example of accessing the result programmatically
    print()
    print("Quick Stats:")
    print(f"  Total Tokens: {result.total_tokens:,}")
    print(f"  Agents: {', '.join(result.participating_agents)}")
    print(f"  Rounds: {len(result.rounds)}")
    print()
    
    # You can also manually save markdown with custom filename
    print("You can also save with a custom filename:")
    custom_filename = result.save_to_markdown("serverless_vs_traditional")
    print(f"  Custom file saved: {custom_filename}")
    print()
    
    print("=" * 80)
    print("Example complete! Check the generated .md file.")
    print("=" * 80)

if __name__ == "__main__":
    main()

