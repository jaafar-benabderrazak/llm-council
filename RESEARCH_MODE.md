# 🔬 Research Mode - Academic-Style Debates with Source Validation

LLM Council now features an enhanced **Research Mode** that transforms multi-agent debates into comprehensive, citation-backed academic articles.

## 🎯 What's Different in Research Mode

### Standard Mode vs Research Mode

| Feature | Standard Mode | Research Mode |
|---------|--------------|---------------|
| Citations | Optional | **Required in every response** |
| Source Validation | No | **Yes - agents cross-check sources** |
| Technical Depth | General | **Deep technical specifications** |
| Misconceptions | Not addressed | **Explicitly addressed** |
| Final Output | Brief synthesis | **Comprehensive article (1000+ words)** |
| References | Informal | **Verified and categorized** |

## 📋 How It Works

### Round 1: Initial Analysis with Citations

Each agent provides:
- ✅ Thorough analysis of the topic
- ✅ **Specific sources** (URLs, papers, documentation)
- ✅ Technical details and specifications
- ✅ Proper citations for all claims
- ✅ Structured response with sections

**Example Agent Response Structure:**
```markdown
## Analysis
[Main analysis with citations]

## Technical Evidence
[Specifications, benchmarks, data points]

## References & Sources
- PostgreSQL Documentation: https://postgresql.org/docs - [Why credible]
- Benchmark Paper: "Comparing SQL vs NoSQL" (Smith et al., 2023) - [Why relevant]
```

### Round 2+: Critical Review & Cross-Checking

Each agent:
- ✅ **Validates sources** provided by other agents
- ✅ **Cross-checks facts** for accuracy
- ✅ **Challenges weak arguments** with counter-evidence
- ✅ **Builds on strong points** with additional references
- ✅ **Addresses misconceptions** explicitly
- ✅ **Provides new perspectives** not yet covered

**Example Critical Review Structure:**
```markdown
## Source Validation
- Agent X's PostgreSQL benchmark claim: ✓ Verified via official docs
- Agent Y's scalability claim: ⚠️ Outdated (2019) - newer data available

## Counter-Analysis
[Challenges with supporting evidence]

## Additional Evidence
[New sources and technical details]

## Common Misconceptions Addressed
[What people get wrong + corrections]

## References & Sources
[New sources with credibility ratings]
```

### Final Synthesis: Comprehensive Article

The system generates a **complete academic-style article** including:

1. **Executive Summary** - Key findings at a glance
2. **Introduction** - Context and scope
3. **Detailed Analysis** - Organized by themes with citations
4. **Source Validation** - Which sources are credible and why
5. **Consensus & Disagreements** - What agents agree/disagree on
6. **Common Misconceptions** - Corrections with evidence
7. **Technical Deep Dive** - Specifications, benchmarks, trade-offs
8. **Gaps & Limitations** - What's uncertain or needs more research
9. **Actionable Recommendations** - Concrete, prioritized advice
10. **Verified References** - Complete, categorized bibliography
11. **Conclusion** - Summary and final verdict

## 🚀 Usage Examples

### Basic Research Debate

```python
from main import create_council

topic = """
Analyze the trade-offs between microservices and monolithic architectures:
- Performance implications
- Operational complexity
- Scalability patterns
- Cost considerations

Cite authoritative sources, benchmarks, and technical documentation.
"""

council = create_council(
    topic=topic,
    agents=["claude", "chatgpt", "groq"],
    rounds=3  # More rounds = more thorough analysis
)

result = council.debate(
    topic=topic,
    rounds=3,
    save_results=True  # Saves comprehensive article to JSON
)

# Access the comprehensive article
print(result.synthesis)  # Full article with citations
```

### Free Tier Research

```python
# Use only free models for research
council = create_council(
    topic="Compare transformer architectures: BERT vs GPT vs T5",
    agents=["groq", "gemini", "ollama"],  # All free!
    rounds=2
)

result = council.debate(
    topic="...",
    rounds=2,
    save_results=True
)
```

### CLI Usage

```bash
# Standard research debate
python main.py "Your research topic here" --models groq gemini --rounds 3

# Comprehensive analysis
python main.py "AI safety: alignment approaches" --models claude chatgpt groq --rounds 4
```

## 📊 Example Output Structure

The generated article follows this structure:

```markdown
# [Your Topic]

## Executive Summary
Brief 2-3 sentence overview of findings...

## Introduction
Context about why this topic matters...
Key questions this analysis addresses...

## Detailed Analysis

### Sub-Topic 1: Performance
According to [Source 1](URL), PostgreSQL achieves X throughput...
However, [Source 2](URL) shows MongoDB excels when...

### Sub-Topic 2: Scalability
Research by Smith et al. (2023) demonstrates...

## Source Validation & Cross-Checking

| Source | Agent | Credibility | Status | Notes |
|--------|-------|-------------|--------|-------|
| PostgreSQL Docs | Claude | High | ✓ Verified | Official documentation |
| MongoDB Blog Post | ChatGPT | Medium | ⚠️ Marketing | Cross-reference with benchmarks |
| VLDB Paper 2023 | Groq | High | ✓ Verified | Peer-reviewed research |

## Consensus & Disagreements

**Strong Agreement:**
- All agents agree that [specific point] based on [evidence]

**Divergent Views:**
- Claude argues X (citing [Source A])
- ChatGPT argues Y (citing [Source B])
- Analysis: Both valid depending on [context]

## Common Misconceptions Addressed

### Misconception 1: "MongoDB is always faster than SQL databases"
**Reality:** According to [benchmark source], MongoDB excels at X but PostgreSQL outperforms for Y...
**Why this misconception exists:** Early marketing focused on...

## Technical Deep Dive

### Performance Benchmarks
- PostgreSQL: 150K reads/sec (source: [URL])
- MongoDB: 200K writes/sec (source: [URL])
- Test conditions: [specifications]

### Scalability Patterns
Horizontal scaling approaches differ...

## Gaps & Limitations

This analysis could not fully address:
- Long-term operational costs (data unavailable)
- Performance with specific workload X (needs benchmarking)

## Actionable Recommendations

**For startups < 100K users:**
1. Start with PostgreSQL if [conditions]
2. Consider MongoDB if [conditions]

**For enterprises:**
1. [Specific recommendation with rationale]

## Verified References & Resources

### Research Papers
- [Title] - Author et al., Year - [URL] - Credibility: High
  - Relevance: Provides benchmark data for...

### Official Documentation
- [PostgreSQL Docs] - [URL] - Credibility: High
  - Why credible: Maintained by core team

### Benchmarks & Tools
- [Benchmark suite] - [URL] - Credibility: Medium
  - Note: Independent but not peer-reviewed

## Conclusion
Final synthesis of findings...
Recommended approach: [specific advice]
Future outlook: [what's changing]
```

## 🎯 Best Practices for Research Mode

### 1. **Choose the Right Topic**
Good topics for Research Mode:
- ✅ Technical comparisons (PostgreSQL vs MongoDB)
- ✅ Architecture decisions (Microservices vs Monolith)
- ✅ Research literature reviews (LLM reasoning approaches)
- ✅ Best practices analysis (Security, performance, etc.)

Not ideal:
- ❌ Simple factual questions (use 1 round instead)
- ❌ Opinion-based topics without objective sources
- ❌ Rapidly changing current events (sources go stale quickly)

### 2. **Use Enough Rounds**
- **1 round**: Quick analysis with citations
- **2 rounds**: Basic cross-checking (recommended minimum)
- **3 rounds**: Thorough validation and deep-dive
- **4+ rounds**: Exhaustive research with multiple perspectives

### 3. **Select Appropriate Agents**
**For High-Quality Research:**
- Claude: Excellent at critical analysis and source evaluation
- ChatGPT: Strong at technical details and practical examples
- Gemini: Great at research synthesis and finding connections

**For Free Tier Research:**
- Groq: Fast, good quality, excellent for initial rounds
- Gemini: Free tier + research strengths
- Ollama: Local, private, good for specific domains

**Recommended Combinations:**
- **Maximum Quality**: Claude + ChatGPT + Gemini (3-4 rounds)
- **Free High-Quality**: Groq + Gemini + Ollama (2-3 rounds)
- **Balanced**: Claude + Groq + Gemini (2-3 rounds)

### 4. **Frame Topics for Citation**
❌ **Bad**: "What's the best database?"

✅ **Good**: 
```
Compare PostgreSQL and MongoDB for a social media application:
- Performance benchmarks (cite specific tests)
- Scalability patterns (reference documentation)
- Real-world case studies (cite companies)
- Operational complexity (reference authoritative sources)
```

### 5. **Iterate on Complex Topics**
For deep research:
1. Run initial 2-round debate
2. Review the article
3. Identify gaps or areas needing more depth
4. Run focused follow-up debate on specific sub-topics
5. Combine insights

## 📈 Quality Indicators

A high-quality research article will have:

- ✅ **10+ unique sources** cited and verified
- ✅ **Specific technical data** (numbers, benchmarks, specs)
- ✅ **Credibility ratings** for major sources
- ✅ **Common misconceptions** explicitly addressed
- ✅ **Both consensus and disagreement** documented
- ✅ **Actionable recommendations** with context
- ✅ **Acknowledged gaps** showing intellectual honesty
- ✅ **Organized structure** with clear sections
- ✅ **1000+ words** for complex topics
- ✅ **Balanced perspective** considering trade-offs

## 🔍 Source Validation Features

### What Gets Validated

Agents automatically check:
1. **Authority**: Is the source from an official/authoritative origin?
2. **Currency**: Is the information up-to-date?
3. **Accuracy**: Can claims be verified across multiple sources?
4. **Relevance**: Does it directly address the question?
5. **Bias**: Is there marketing spin or conflicts of interest?

### Credibility Ratings

- **High**: Official docs, peer-reviewed papers, verified benchmarks
- **Medium**: Blog posts from experts, company case studies, established tools
- **Low**: Marketing material, unverified claims, outdated sources

### Cross-Checking Process

1. Agent A cites Source X
2. Agent B validates: checks if source exists, is authoritative, is current
3. Agent B may provide counter-sources if Source X is disputed
4. Final synthesis weighs source credibility in recommendations

## 💾 Saved Output

Each debate saves a JSON file with:

```json
{
  "topic": "Your research topic",
  "timestamp": "2024-12-26T...",
  "participating_agents": ["Agent1", "Agent2", "Agent3"],
  "rounds": [
    {
      "round_num": 1,
      "responses": [
        {
          "agent_name": "Agent1",
          "content": "## Analysis\n...\n## References\n...",
          "model": "claude-3-5-sonnet",
          "tokens_used": 1523
        }
      ]
    }
  ],
  "synthesis": "# Comprehensive Article\n\n## Executive Summary\n...",
  "total_tokens": 8543
}
```

## 🎓 Academic Use Cases

Perfect for:
- **Literature reviews**: Synthesize research papers
- **Technical reports**: Comprehensive analysis with citations
- **Decision documents**: Architecture Decision Records (ADRs)
- **Research proposals**: Background research with sources
- **Blog posts**: Technical articles with verified claims
- **Documentation**: Feature comparisons with benchmarks
- **Course materials**: Teaching resources with references

## ⚖️ Limitations & Considerations

**Strengths:**
- ✅ Comprehensive multi-perspective analysis
- ✅ Source validation and cross-checking
- ✅ Structured academic-style output
- ✅ Technical depth with specifics

**Limitations:**
- ⚠️ LLMs may hallucinate sources (always verify critical citations)
- ⚠️ Cannot access real-time web data (knowledge cutoff applies)
- ⚠️ Source verification is based on LLM knowledge, not live URL checking
- ⚠️ More tokens used = higher cost for paid models

**Best Practice:**
- Use the article as a comprehensive starting point
- Manually verify critical sources before citing in official work
- Cross-reference important claims with actual documentation
- Consider the article as "research assistant output" not "final publication"

## 🚀 Getting Started

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Configure API keys** (or use free tier):
```bash
cp env.example .env
# Edit .env with your keys (or leave empty for free tier)
```

3. **Run example**:
```bash
python examples/research_article_debate.py
```

4. **Review output**: Check the generated JSON files and console output

## 📚 Examples Included

- `examples/research_article_debate.py` - Full demonstration
- `examples/free_cloud_debate.py` - Free tier research (updated)
- `examples/hybrid_free_paid.py` - Mixed approach (updated)

## 🤝 Contributing

Have ideas for improving Research Mode?
- Open an issue on GitHub
- Submit a pull request
- Share your use cases

---

**LLM Council Research Mode** - Where AI agents collaborate to produce comprehensive, citation-backed analysis.

*Built for researchers, developers, and anyone who values thorough, verified information.*

