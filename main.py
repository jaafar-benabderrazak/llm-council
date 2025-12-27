"""Main entry point for LLM Council."""
import argparse
from typing import List

from agents import (
    ClaudeAgent, ChatGPTAgent, GeminiAgent, MistralAgent,
    OllamaAgent, GroqAgent, HuggingFaceAgent, DeepSeekAgent,
    OpenRouterAgent, CometAgent, BaseAgent
)
from council import LLMCouncil
from config import Config


def create_council(models: List[str] = None) -> LLMCouncil:
    """
    Create an LLM Council with specified models.
    
    Args:
        models: List of model names to include. If None, uses all available.
                Supports specific model syntax: "ollama:model-name", "groq:model-name"
                Examples:
                - "ollama" - uses default Ollama model
                - "ollama:llama3.1:8b" - uses specific Ollama model
                - "gemini" - uses default Gemini model
        
    Returns:
        Configured LLMCouncil instance
    """
    Config.validate()
    
    available_models = Config.get_available_models()
    
    # Parse model specifications (support provider:model syntax)
    parsed_models = []
    ollama_models = []  # Track specific ollama models
    comet_models = []  # Track specific comet models or categories
    openrouter_models = []  # Track specific openrouter models
    
    if models:
        for model_spec in models:
            if ":" in model_spec:
                # Specific model: "ollama:llama3.1:8b" or "comet:gpt-5.2" or "comet:advanced"
                parts = model_spec.split(":", 1)
                provider = parts[0]
                specific_model = parts[1] if len(parts) > 1 else None
                
                if provider == "ollama" and specific_model:
                    ollama_models.append(specific_model)
                    parsed_models.append(f"ollama:{specific_model}")
                elif provider == "comet" and specific_model:
                    comet_models.append(specific_model)
                    parsed_models.append(f"comet:{specific_model}")
                elif provider == "openrouter" and specific_model:
                    openrouter_models.append(specific_model)
                    parsed_models.append(f"openrouter:{specific_model}")
                elif provider in available_models:
                    parsed_models.append(provider)
                else:
                    print(f"Warning: Provider '{provider}' not available or not configured")
            else:
                # Simple provider name: "gemini", "claude", "comet", etc.
                if model_spec in available_models:
                    parsed_models.append(model_spec)
                else:
                    print(f"Warning: Model '{model_spec}' not available")
        
        models_to_use = parsed_models
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
    # Handle multiple Ollama agents with different models
    ollama_specs = [m for m in models_to_use if m.startswith("ollama")]
    
    if ollama_specs:
        if OllamaAgent is None:
            print("Warning: Ollama requested but ollama package not installed.")
            print("Install with: pip install ollama")
        else:
            # If no specific models, use default once
            if not any(":" in spec for spec in ollama_specs):
                try:
                    agents.append(OllamaAgent(
                        name="Llama",
                        role="Local Reasoning Expert - Free local inference"
                    ))
                except Exception as e:
                    print(f"Warning: Could not initialize Ollama agent: {e}")
            else:
                # Create agent for each specific Ollama model
                for spec in ollama_specs:
                    if ":" in spec:
                        model_name = spec.split(":", 1)[1]
                        # Derive friendly name from model
                        friendly_name = model_name.split(":")[0].title()
                        try:
                            agents.append(OllamaAgent(
                                name=friendly_name,
                                role=f"Local Expert ({model_name})",
                                model=model_name
                            ))
                        except Exception as e:
                            print(f"Warning: Could not initialize Ollama agent with {model_name}: {e}")
    
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
    
    # Advanced Providers
    # Handle OpenRouter agents
    openrouter_specs = [m for m in models_to_use if m.startswith("openrouter")]
    
    if openrouter_specs:
        if OpenRouterAgent is None:
            print("Warning: OpenRouter requested but openai package not installed.")
            print("Install with: pip install openai")
        else:
            # If no specific models, use default once
            if not any(":" in spec for spec in openrouter_specs):
                try:
                    agents.append(OpenRouterAgent(
                        name="OpenRouter",
                        role="Versatile AI - Access to 100+ models"
                    ))
                except Exception as e:
                    print(f"Warning: Could not initialize OpenRouter agent: {e}")
            else:
                # Create agent for each specific OpenRouter model
                for spec in openrouter_specs:
                    if ":" in spec:
                        model_name = spec.split(":", 1)[1]
                        friendly_name = f"OpenRouter-{model_name.split('/')[-1]}"
                        try:
                            agents.append(OpenRouterAgent(
                                name=friendly_name,
                                role=f"OpenRouter Expert ({model_name})",
                                model=model_name
                            ))
                        except Exception as e:
                            print(f"Warning: Could not initialize OpenRouter agent with {model_name}: {e}")
    
    # Handle Comet agents (with category support)
    comet_specs = [m for m in models_to_use if m.startswith("comet")]
    
    if comet_specs:
        if CometAgent is None:
            print("Warning: Comet requested but openai package not installed.")
            print("Install with: pip install openai")
        else:
            # If no specific models, use default once
            if not any(":" in spec for spec in comet_specs):
                try:
                    agents.append(CometAgent(
                        name="Comet",
                        role="Comet AI Analysis - Versatile and powerful models"
                    ))
                except Exception as e:
                    print(f"Warning: Could not initialize Comet agent: {e}")
            else:
                # Create agent for each specific Comet model or category
                for spec in comet_specs:
                    if ":" in spec:
                        model_or_category = spec.split(":", 1)[1]
                        
                        # Check if it's a category
                        categories = ['advanced', 'opensource', 'free', 'fast']
                        if model_or_category.lower() in categories:
                            # Use category
                            try:
                                agents.append(CometAgent(
                                    name=f"Comet-{model_or_category.title()}",
                                    category=model_or_category.lower(),
                                    role=f"Comet {model_or_category.title()} Analysis"
                                ))
                            except Exception as e:
                                print(f"Warning: Could not initialize Comet with category {model_or_category}: {e}")
                        else:
                            # Use specific model
                            try:
                                agents.append(CometAgent(
                                    name=f"Comet-{model_or_category}",
                                    model=model_or_category,
                                    role=f"Comet Analysis ({model_or_category})"
                                ))
                            except Exception as e:
                                print(f"Warning: Could not initialize Comet with model {model_or_category}: {e}")
    
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
        help=(
            "Models to include in the council (default: all available). "
            "Supports specific model syntax for providers. "
            "Examples: claude, gemini, ollama:llama3.1:8b, ollama:mistral:7b, "
            "comet:advanced, comet:free, comet:gpt-5.2, openrouter:anthropic/claude-3.5-sonnet"
        )
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

