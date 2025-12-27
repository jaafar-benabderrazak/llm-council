"""
Extract Results from Markdown Article

This script extracts only the results, conclusions, and key findings
from an existing full Markdown article, removing the detailed discussions.

Usage:
    python extract_results.py article.md
    python extract_results.py article.md --output results.md
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime
import re

def extract_results_from_markdown(markdown_content):
    """Extract results-focused content from a full article."""
    
    lines = markdown_content.split('\n')
    
    # Extract header information
    header_lines = []
    i = 0
    while i < len(lines) and i < 50:  # Check first 50 lines for header
        line = lines[i].strip()
        if line.startswith('#') and not line.startswith('##'):
            header_lines.append(lines[i])
        elif line.startswith('**') and any(keyword in line for keyword in ['Generated', 'Date', 'Models', 'Agents', 'Tokens', 'Cost']):
            header_lines.append(lines[i])
        elif '---' in line and len(header_lines) > 0:
            header_lines.append(lines[i])
            break
        elif header_lines:
            header_lines.append(lines[i])
        i += 1
    
    # Sections to extract (results-focused)
    sections_to_extract = {
        'EXECUTIVE SUMMARY': [],
        'KEY FINDINGS': [],
        'INTRODUCTION': [],
        'ANALYSIS': [],
        'SOURCE VALIDATION': [],
        'VERIFIED SOURCES': [],
        'REFERENCES': [],
        'CONSENSUS': [],
        'DISAGREEMENTS': [],
        'MISCONCEPTIONS': [],
        'COMMON MISCONCEPTIONS': [],
        'TECHNICAL': [],
        'BEST PRACTICES': [],
        'RECOMMENDATIONS': [],
        'IMPLEMENTATION': [],
        'PRACTICAL': [],
        'LIMITATIONS': [],
        'GAPS': [],
        'FUTURE': [],
        'OUTLOOK': [],
        'CONCLUSION': [],
        'NEXT STEPS': []
    }
    
    # Sections to skip (discussion-focused)
    sections_to_skip = [
        'ROUND', 'DEBATE', 'DISCUSSION', 'AGENT RESPONSES',
        'CONVERSATION', 'DIALOGUE', 'EXCHANGE'
    ]
    
    current_section = None
    current_content = []
    extracted_sections = {}
    
    for line in lines[i:]:
        # Detect section headers (## or ###)
        if line.strip().startswith('##'):
            # Save previous section
            if current_section and current_content:
                # Check if not a skip section
                if not any(skip_word in current_section.upper() for skip_word in sections_to_skip):
                    extracted_sections[current_section] = '\n'.join(current_content)
            
            # Start new section
            current_section = line.strip('#').strip()
            current_content = [line]
        elif current_section:
            current_content.append(line)
    
    # Save last section
    if current_section and current_content:
        if not any(skip_word in current_section.upper() for skip_word in sections_to_skip):
            extracted_sections[current_section] = '\n'.join(current_content)
    
    # Build results article
    results = []
    
    # Add header
    results.extend(header_lines)
    results.append('')
    results.append('---')
    results.append('')
    results.append('## 📊 Document Purpose')
    results.append('')
    results.append('This document presents the **synthesized results and key findings** extracted from')
    results.append('a comprehensive multi-agent AI analysis. The focus is on actionable insights,')
    results.append('verified information, and conclusions rather than the detailed discussion process.')
    results.append('')
    results.append('---')
    results.append('')
    
    # Priority order for sections
    priority_sections = [
        ('EXECUTIVE SUMMARY', '🎯'),
        ('KEY FINDINGS', '🔍'),
        ('INTRODUCTION', '📖'),
        ('ANALYSIS', '📊'),
        ('SOURCE VALIDATION', '✅'),
        ('VERIFIED SOURCES', '📚'),
        ('REFERENCES', '📚'),
        ('CONSENSUS', '🤝'),
        ('DISAGREEMENTS', '⚖️'),
        ('MISCONCEPTIONS', '⚠️'),
        ('COMMON MISCONCEPTIONS', '⚠️'),
        ('TECHNICAL', '🔧'),
        ('BEST PRACTICES', '💡'),
        ('RECOMMENDATIONS', '💡'),
        ('IMPLEMENTATION', '🚀'),
        ('PRACTICAL', '🛠️'),
        ('LIMITATIONS', '⚡'),
        ('GAPS', '⚡'),
        ('FUTURE', '🔮'),
        ('OUTLOOK', '🔮'),
        ('CONCLUSION', '🎓'),
        ('NEXT STEPS', '👉')
    ]
    
    added_sections = set()
    
    for section_keyword, emoji in priority_sections:
        for section_name, content in extracted_sections.items():
            if section_keyword in section_name.upper() and section_name not in added_sections:
                # Add section with emoji
                section_lines = content.split('\n')
                if section_lines and section_lines[0].startswith('##'):
                    # Replace header with emoji version
                    results.append(f"## {emoji} {section_lines[0].strip('#').strip()}")
                    results.extend(section_lines[1:])
                else:
                    results.append(f"## {emoji} {section_name}")
                    results.append('')
                    results.extend(section_lines)
                
                results.append('')
                results.append('---')
                results.append('')
                added_sections.add(section_name)
    
    # Add metadata footer
    results.append('')
    results.append('## 📋 About This Document')
    results.append('')
    results.append('**Generated by**: [LLM Council](https://github.com/jaafar-benabderrazak/llm-council)')
    results.append('**Type**: Results-Only Extract')
    results.append('**Extraction Date**: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    results.append('')
    results.append('**Note**: This document contains only the synthesized results, conclusions, and verified')
    results.append('references. Detailed round-by-round discussions have been excluded for clarity.')
    results.append('')
    results.append('For the complete analysis including all debates and discussions, please refer to the')
    results.append('original full article.')
    results.append('')
    results.append('---')
    results.append('')
    results.append('*This research was conducted using FREE open-source AI models with zero cost.*')
    
    return '\n'.join(results)

def main():
    parser = argparse.ArgumentParser(
        description="Extract results-only content from a full article"
    )
    parser.add_argument(
        'article_file',
        help="Path to full Markdown article"
    )
    parser.add_argument(
        '--output', '-o',
        help="Output Markdown file path (default: results_<original_name>.md)",
        default=None
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    article_path = Path(args.article_file)
    if not article_path.exists():
        print(f"Error: File not found: {args.article_file}")
        
        # Try to find article files
        article_files = list(Path('.').glob('article_*.md'))
        if article_files:
            print("\nAvailable article files:")
            for i, file in enumerate(sorted(article_files, reverse=True)[:5], 1):
                print(f"  {i}. {file.name}")
            print("\nTry: python extract_results.py <filename>")
        return 1
    
    print("=" * 70)
    print("  RESULTS EXTRACTOR")
    print("=" * 70)
    print()
    print(f"Input:  {args.article_file}")
    
    # Read article
    try:
        markdown_content = article_path.read_text(encoding='utf-8')
        
        # Extract results
        results_content = extract_results_from_markdown(markdown_content)
        
        # Determine output filename
        if args.output:
            output_path = Path(args.output)
        else:
            # Generate output filename
            original_name = article_path.stem
            output_path = Path(f"results_{original_name}.md")
        
        # Save results
        output_path.write_text(results_content, encoding='utf-8')
        
        print(f"Output: {output_path}")
        print()
        print("=" * 70)
        print("  RESULTS EXTRACTED!")
        print("=" * 70)
        print()
        print(f"[OK] File: {output_path}")
        print(f"[OK] Original size: {len(markdown_content):,} characters")
        print(f"[OK] Results size: {len(results_content):,} characters")
        print(f"[OK] Reduction: {100 - (len(results_content) * 100 // len(markdown_content))}%")
        print()
        
        # Count sections
        section_count = results_content.count('## ')
        print(f"Sections extracted: {section_count}")
        print()
        print("Content includes:")
        if 'Executive Summary' in results_content:
            print("  [OK] Executive Summary")
        if 'Introduction' in results_content:
            print("  [OK] Introduction")
        if 'Key Findings' in results_content or 'Analysis' in results_content:
            print("  [OK] Key Findings/Analysis")
        if 'Verified Sources' in results_content or 'References' in results_content:
            print("  [OK] Verified Sources")
        if 'Misconceptions' in results_content:
            print("  [OK] Misconceptions Addressed")
        if 'Best Practices' in results_content or 'Recommendations' in results_content:
            print("  [OK] Best Practices/Recommendations")
        if 'Conclusion' in results_content:
            print("  [OK] Conclusion")
        print()
        print("Excluded:")
        print("  [X] Round-by-round discussions")
        print("  [X] Detailed debates")
        print("  [X] Agent responses")
        print()
        print("=" * 70)
        print()
        print(f"[SUCCESS] Results article ready: {output_path}")
        print()
        
    except Exception as e:
        print(f"\n[ERROR] Failed to extract results: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

