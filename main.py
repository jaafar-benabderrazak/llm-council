"""Main entry point for LLM Council."""
import argparse
from typing import List

from agents import (
    ClaudeAgent, ChatGPTAgent, GeminiAgent, MistralAgent,
    OllamaAgent, GroqAgent, HuggingFaceAgent, DeepSeekAgent, BaseAgent
)
from council import LLMCouncil
from config import Config


def create_council(models: List[str] = None) -> LLMCouncil:
    """
    Create an LLM Council with specified models.
    
    Args:
        models: List of model names to include. If None, uses all available.
        
    Returns:
        Configured LLMCouncil instance
    """
    Config.validate()
    
    available_models = Config.get_available_models()
    
    if models:
        # Use only requested models that are available
        models_to_use = [m for m in models if m in available_models]
    else:
        # Use all available models
        models_to_use = available_models
    
    if len(models_to_use) < 2:
        raise ValueError(
            f"Need at least 2 models. Available: {available_models}. "
            f"Requested: {models}"
        )
    
    agents = []
    
    # Create agents based on available API keys
    # Paid models
    if "claude" in models_to_use:
        if ClaudeAgent is None:
            print("Warning: Claude requested but anthropic package not installed.")
            print("Install with: pip install anthropic")
        else:
            try:
                agents.append(ClaudeAgent(
                    name="Claude",
                    role="Critical Analyst - Questions assumptions and explores edge cases"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize Claude agent: {e}")
    
    if "chatgpt" in models_to_use:
        if ChatGPTAgent is None:
            print("Warning: ChatGPT requested but openai package not installed.")
            print("Install with: pip install openai")
        else:
            try:
                agents.append(ChatGPTAgent(
                    name="ChatGPT",
                    role="Pragmatic Problem Solver - Focuses on practical solutions"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize ChatGPT agent: {e}")
    
    if "gemini" in models_to_use:
        if GeminiAgent is None:
            print("Warning: Gemini requested but google-generativeai package not installed.")
            print("Install with: pip install google-generativeai")
        else:
            try:
                agents.append(GeminiAgent(
                    name="Gemini",
                    role="Research Synthesizer - Integrates diverse perspectives"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize Gemini agent: {e}")
    
    if "mistral" in models_to_use:
        if MistralAgent is None:
            print("Warning: Mistral requested but mistralai package not installed.")
            print("Install with: pip install mistralai")
        else:
            try:
                agents.append(MistralAgent(
                    name="Mistral",
                    role="Devil's Advocate - Challenges consensus and explores alternatives"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize Mistral agent: {e}")
    
    # Free/Open source models
    if "ollama" in models_to_use:
        if OllamaAgent is None:
            print("Warning: Ollama requested but ollama package not installed.")
            print("Install with: pip install ollama")
        else:
            try:
                agents.append(OllamaAgent(
                    name="Llama",
                    role="Local Reasoning Expert - Free local inference"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize Ollama agent: {e}")
    
    if "groq" in models_to_use:
        if GroqAgent is None:
            print("Warning: Groq requested but groq package not installed.")
            print("Install with: pip install groq")
        else:
            try:
                agents.append(GroqAgent(
                    name="Groq",
                    role="Fast Inference Specialist - Ultra-fast free API"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize Groq agent: {e}")
    
    if "huggingface" in models_to_use:
        if HuggingFaceAgent is None:
            print("Warning: HuggingFace requested but huggingface_hub package not installed.")
            print("Install with: pip install huggingface-hub")
        else:
            try:
                agents.append(HuggingFaceAgent(
                    name="HuggingFace",
                    role="Open Source Specialist - Community-driven models"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize HuggingFace agent: {e}")
    
    if "deepseek" in models_to_use:
        if DeepSeekAgent is None:
            print("Warning: DeepSeek requested but openai package not installed.")
            print("Install with: pip install openai")
        else:
            try:
                agents.append(DeepSeekAgent(
                    name="DeepSeek",
                    role="Technical Innovator - Cutting-edge Chinese LLM"
                ))
            except Exception as e:
                print(f"Warning: Could not initialize DeepSeek agent: {e}")
    
    if not agents:
        raise ValueError(
            "No agents could be initialized. Please check your configuration and installed packages."
        )
    
    return LLMCouncil(agents, verbose=True)


def main():
    """Main function with CLI interface."""
    parser = argparse.ArgumentParser(
        description="LLM Council - Multi-Agent AI Discussion Framework"
    )
    parser.add_argument(
        "topic",
        nargs="?",
        help="Topic for the council to discuss"
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=3,
        help="Number of debate rounds (default: 3)"
    )
    parser.add_argument(
        "--models",
        nargs="+",
        choices=["claude", "chatgpt", "gemini", "mistral", "ollama", "groq", "huggingface", "deepseek"],
        help="Models to include in the council (default: all available)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save results to files"
    )
    parser.add_argument(
        "--no-markdown",
        action="store_true",
        help="Don't save Markdown article (JSON only)"
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick mode: single round discussion"
    )
    
    args = parser.parse_args()
    
    # Interactive mode if no topic provided
    if not args.topic:
        print("\n🏛️  Welcome to LLM Council\n")
        print("Available models:", ", ".join(Config.get_available_models()))
        print()
        topic = input("Enter a topic for discussion: ").strip()
        if not topic:
            print("No topic provided. Exiting.")
            return
    else:
        topic = args.topic
    
    # Create council
    try:
        council = create_council(args.models)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Run debate
    if args.quick:
        synthesis = council.quick_discuss(topic)
        print("\n" + synthesis)
    else:
        result = council.debate(
            topic=topic,
            rounds=args.rounds,
            save_results=not args.no_save,
            save_markdown=not args.no_markdown and not args.no_save
        )


if __name__ == "__main__":
    main()

