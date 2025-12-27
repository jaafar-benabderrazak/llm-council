"""
Results-Only Article Generator

This script generates a clean, results-focused Markdown article
from a debate JSON file, excluding the detailed round-by-round discussions.

Focus: Synthesis, conclusions, recommendations, and verified sources only.

Usage:
    python generate_results_article.py debate_file.json
    python generate_results_article.py debate_file.json --output results.md
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

def load_debate(json_file):
    """Load debate data from JSON file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_key_points(synthesis):
    """Extract key points from synthesis text."""
    # Simple extraction based on common patterns
    lines = synthesis.split('\n')
    key_points = []
    
    in_section = False
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Detect section headers
        if any(keyword in line.upper() for keyword in [
            'EXECUTIVE SUMMARY', 'KEY FINDINGS', 'CONCLUSIONS',
            'RECOMMENDATIONS', 'MAIN POINTS'
        ]):
            in_section = True
            current_section = line
        elif line.startswith('#'):
            in_section = False
        elif in_section and line and not line.startswith('-'):
            key_points.append(line)
    
    return key_points

def generate_results_article(debate_data, output_file=None):
    """Generate a results-focused article from debate data."""
    
    topic = debate_data.get('topic', 'Unknown Topic')
    timestamp = debate_data.get('timestamp', datetime.now().isoformat())
    
    # Handle synthesis - can be string or dict
    synthesis_data = debate_data.get('synthesis', '')
    if isinstance(synthesis_data, dict):
        synthesis = synthesis_data.get('content', '')
    else:
        synthesis = synthesis_data
    
    total_tokens = debate_data.get('total_tokens', 0)
    
    # Extract metadata
    agents = []
    for round_data in debate_data.get('rounds', []):
        for response in round_data:
            agent_name = response.get('agent_name')
            if agent_name and agent_name not in agents:
                agents.append(agent_name)
    
    # Parse synthesis into sections
    synthesis_lines = synthesis.split('\n')
    sections = {}
    current_section = None
    current_content = []
    
    for line in synthesis_lines:
        # Detect main section headers (## or **SECTION**)
        if line.startswith('##') or (line.startswith('**') and line.endswith('**')):
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = line.strip('#').strip('*').strip()
            current_content = []
        else:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content)
    
    # Generate article
    article = f"""# Research Results: {topic}

**Generated**: {datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')}  
**Analysis by**: {', '.join(agents)}  
**Total Analysis Tokens**: {total_tokens:,}  
**Cost**: $0.00 (100% FREE)

---

## 📊 Document Purpose

This document presents the **synthesized results and conclusions** from a multi-agent AI analysis.
The focus is on actionable insights, verified information, and key findings rather than the 
detailed discussion process.

---

"""

    # Add Executive Summary
    if 'EXECUTIVE SUMMARY' in sections:
        article += f"""## 🎯 Executive Summary

{sections['EXECUTIVE SUMMARY'].strip()}

---

"""

    # Add Introduction
    if 'INTRODUCTION' in sections:
        article += f"""## 📖 Introduction

{sections['INTRODUCTION'].strip()}

---

"""

    # Add Main Analysis/Findings
    analysis_keywords = ['DETAILED ANALYSIS', 'ANALYSIS', 'FINDINGS', 'RESULTS']
    for keyword in analysis_keywords:
        if keyword in sections:
            article += f"""## 🔍 Key Findings & Analysis

{sections[keyword].strip()}

---

"""
            break

    # Add Source Validation
    if 'SOURCE VALIDATION' in sections or 'CROSS-CHECKING' in sections:
        source_section = sections.get('SOURCE VALIDATION', sections.get('CROSS-CHECKING', ''))
        article += f"""## ✅ Verified Sources & References

{source_section.strip()}

---

"""

    # Add Consensus & Disagreements
    if 'CONSENSUS' in sections or 'DISAGREEMENTS' in sections:
        consensus = sections.get('CONSENSUS', sections.get('DISAGREEMENTS', ''))
        article += f"""## 🤝 Expert Consensus & Debates

{consensus.strip()}

---

"""

    # Add Misconceptions
    if 'MISCONCEPTIONS' in sections or 'COMMON MISCONCEPTIONS' in sections:
        misconceptions = sections.get('MISCONCEPTIONS', sections.get('COMMON MISCONCEPTIONS', ''))
        article += f"""## ⚠️ Common Misconceptions Addressed

{misconceptions.strip()}

---

"""

    # Add Technical Details
    if 'TECHNICAL' in sections or 'DEEP DIVE' in sections:
        technical = sections.get('TECHNICAL', sections.get('DEEP DIVE', ''))
        article += f"""## 🔧 Technical Details

{technical.strip()}

---

"""

    # Add Best Practices
    if 'BEST PRACTICES' in sections or 'RECOMMENDATIONS' in sections:
        practices = sections.get('BEST PRACTICES', sections.get('RECOMMENDATIONS', ''))
        article += f"""## 💡 Best Practices & Recommendations

{practices.strip()}

---

"""

    # Add Implementation Guide
    if 'IMPLEMENTATION' in sections or 'PRACTICAL GUIDE' in sections:
        implementation = sections.get('IMPLEMENTATION', sections.get('PRACTICAL GUIDE', ''))
        article += f"""## 🚀 Implementation Guide

{implementation.strip()}

---

"""

    # Add Gaps & Limitations
    if 'GAPS' in sections or 'LIMITATIONS' in sections:
        gaps = sections.get('GAPS', sections.get('LIMITATIONS', ''))
        article += f"""## ⚡ Limitations & Areas for Further Research

{gaps.strip()}

---

"""

    # Add Future Outlook
    if 'FUTURE' in sections or 'OUTLOOK' in sections:
        future = sections.get('FUTURE', sections.get('OUTLOOK', ''))
        article += f"""## 🔮 Future Outlook

{future.strip()}

---

"""

    # Add Conclusion
    if 'CONCLUSION' in sections:
        article += f"""## 🎓 Conclusion

{sections['CONCLUSION'].strip()}

---

"""

    # Add References section
    if 'REFERENCES' in sections or 'SOURCES' in sections:
        references = sections.get('REFERENCES', sections.get('SOURCES', ''))
        article += f"""## 📚 Complete References

{references.strip()}

---

"""

    # Add Metadata Footer
    article += f"""

## 📋 Analysis Metadata

### Research Team
- **AI Agents**: {', '.join(agents)}
- **Total Perspectives**: {len(agents)}

### Research Scope
- **Topic**: {topic}
- **Date**: {datetime.fromisoformat(timestamp).strftime('%Y-%m-%d')}
- **Rounds of Analysis**: {len(debate_data.get('rounds', []))}
- **Total Tokens**: {total_tokens:,}

### Methodology
This analysis was conducted using a multi-agent AI debate system where {len(agents)} different 
AI models analyzed the topic from diverse perspectives, cross-validated sources, and synthesized 
their findings into this comprehensive report.

**Cost**: $0.00 (100% FREE using open-source models)

---

## 🔗 About This Document

**Generated by**: [LLM Council](https://github.com/jaafar-benabderrazak/llm-council)  
**Framework**: Multi-Agent AI Research System  
**Models Used**: {', '.join(agents)}  
**Quality Assurance**: Cross-validated by {len(agents)} independent AI agents  

**Note**: This document focuses on synthesized results and conclusions. For detailed round-by-round 
discussions and the complete debate transcript, please refer to the full debate JSON file.

---

*This research was conducted entirely using FREE and open-source AI models with zero cost.*
"""

    # Save to file
    if output_file:
        output_path = Path(output_file)
    else:
        # Generate output filename
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path(f"results_article_{timestamp_str}.md")
    
    output_path.write_text(article, encoding='utf-8')
    
    return article, str(output_path)

def main():
    parser = argparse.ArgumentParser(
        description="Generate results-focused article from debate JSON"
    )
    parser.add_argument(
        'json_file',
        help="Path to debate JSON file"
    )
    parser.add_argument(
        '--output', '-o',
        help="Output Markdown file path (default: auto-generated)",
        default=None
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.json_file).exists():
        print(f"Error: File not found: {args.json_file}")
        
        # Try to find debate files
        debate_files = list(Path('.').glob('debate_*.json'))
        if debate_files:
            print("\nAvailable debate files:")
            for i, file in enumerate(sorted(debate_files, reverse=True)[:5], 1):
                print(f"  {i}. {file.name}")
            print("\nTry: python generate_results_article.py <filename>")
        return 1
    
    print("=" * 70)
    print("  RESULTS-ONLY ARTICLE GENERATOR")
    print("=" * 70)
    print()
    print(f"Input:  {args.json_file}")
    
    # Load and process
    try:
        debate_data = load_debate(args.json_file)
        article, output_file = generate_results_article(debate_data, args.output)
        
        print(f"Output: {output_file}")
        print()
        print("=" * 70)
        print("  ARTICLE GENERATED!")
        print("=" * 70)
        print()
        print(f"[OK] File: {output_file}")
        print(f"[OK] Size: {len(article):,} characters")
        print(f"[OK] Topic: {debate_data.get('topic', 'N/A')[:60]}...")
        print()
        
        # Count sections
        section_count = article.count('## ')
        print(f"Sections: {section_count}")
        print()
        print("Content includes:")
        if 'Executive Summary' in article:
            print("  ✅ Executive Summary")
        if 'Key Findings' in article:
            print("  ✅ Key Findings")
        if 'Verified Sources' in article:
            print("  ✅ Verified Sources")
        if 'Misconceptions' in article:
            print("  ✅ Misconceptions Addressed")
        if 'Best Practices' in article:
            print("  ✅ Best Practices")
        if 'Conclusion' in article:
            print("  ✅ Conclusion")
        print()
        print("=" * 70)
        print()
        print(f"[SUCCESS] Results article ready: {output_file}")
        print()
        
    except Exception as e:
        print(f"\n[ERROR] Failed to generate article: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

