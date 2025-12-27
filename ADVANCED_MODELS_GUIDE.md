# 🚀 Guide: Utiliser des Modèles LLM Avancés

## Vue d'Ensemble

Ce guide vous montre comment ajouter et utiliser des modèles LLM avancés dans votre LLM Council:

- 🌐 **OpenRouter** - Accès à 100+ modèles (GPT-4, Claude 3, Llama 3 70B, etc.)
- 🤝 **Together AI** - Modèles open-source rapides et abordables
- 🔄 **Replicate** - Modèles ML à la demande
- 🦙 **LM Studio** - Interface locale pour modèles Llama, Mistral, etc.
- 🔥 **Fireworks AI** - Inference ultra-rapide
- 💎 **Cohere** - Modèles Command optimisés
- 🌟 **Perplexity** - Modèles avec recherche web intégrée

---

## Table des Matières

1. [Modèles Avancés Ollama](#modèles-avancés-ollama)
2. [OpenRouter (100+ modèles)](#openrouter)
3. [Together AI](#together-ai)
4. [LM Studio](#lm-studio)
5. [Autres Providers](#autres-providers)
6. [Créer un Nouvel Agent](#créer-un-nouvel-agent)
7. [Modèles Recommandés](#modèles-recommandés)

---

## 1. Modèles Avancés Ollama

### Modèles Gratuits de Haute Qualité

Ollama supporte 100+ modèles open-source. Voici les meilleurs:

#### **Modèles de Code (Recommandés pour la sécurité)**
```bash
# DeepSeek Coder (Excellent pour code & sécurité)
ollama pull deepseek-coder:6.7b
ollama pull deepseek-coder:33b      # Plus puissant

# CodeLlama (Meta)
ollama pull codellama:7b
ollama pull codellama:13b
ollama pull codellama:34b

# Qwen Coder (Alibaba)
ollama pull qwen2.5-coder:7b
```

#### **Modèles Généraux (Meilleure qualité)**
```bash
# Llama 3.1 (Meta - Recommandé)
ollama pull llama3.1:8b
ollama pull llama3.1:70b           # Très puissant mais lent

# Llama 3.3 (Dernière version)
ollama pull llama3.3:70b

# Mistral (Excellent raisonnement)
ollama pull mistral:7b
ollama pull mixtral:8x7b           # Mixture of Experts

# Phi-3 (Microsoft - Rapide et efficace)
ollama pull phi3:mini
ollama pull phi3:medium

# Gemma 2 (Google)
ollama pull gemma2:9b
ollama pull gemma2:27b

# Qwen (Alibaba - Multilingue)
ollama pull qwen2.5:7b
ollama pull qwen2.5:14b
ollama pull qwen2.5:32b
```

#### **Modèles Spécialisés**
```bash
# Mathématiques & Raisonnement
ollama pull deepseek-math:7b

# Vision (comprend les images)
ollama pull llava:7b
ollama pull llava:13b

# Multilingue (Français excellent)
ollama pull qwen2.5:7b
ollama pull mistral:7b
```

### Utilisation
```bash
# Un seul modèle avancé
python main.py "topic" --models ollama:llama3.1:70b gemini --rounds 3

# Plusieurs modèles avancés
python main.py "topic" --models \
  ollama:deepseek-coder:33b \
  ollama:llama3.1:70b \
  ollama:mixtral:8x7b \
  gemini \
  --rounds 4
```

---

## 2. OpenRouter

### Pourquoi OpenRouter? 🌟

- ✅ Accès à **100+ modèles** via une seule API
- ✅ GPT-4, GPT-4 Turbo, GPT-4o
- ✅ Claude 3 (Haiku, Sonnet, Opus)
- ✅ Llama 3 70B, Llama 3.1 405B
- ✅ Mistral Large, Mixtral 8x22B
- ✅ Et bien plus...
- ✅ Prix compétitifs
- ✅ Pas de file d'attente

### Installation

```bash
pip install openai  # OpenRouter utilise l'API OpenAI
```

### Configuration

Ajoutez à votre `.env`:
```bash
OPENROUTER_API_KEY=your-openrouter-api-key
# Obtenir une clé: https://openrouter.ai/keys

# Modèles disponibles (exemples)
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
# Ou: openai/gpt-4-turbo
# Ou: meta-llama/llama-3.1-70b-instruct
# Ou: mistralai/mixtral-8x22b-instruct
```

### Créer l'Agent OpenRouter

Créez `agents/openrouter_agent.py`:

```python
"""OpenRouter agent implementation - Access to 100+ models."""
from typing import Optional, List
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class OpenRouterAgent(BaseAgent):
    """Agent powered by OpenRouter (100+ models)."""
    
    def __init__(
        self, 
        name: str = "OpenRouter",
        role: str = "Advanced Multi-Model Agent",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        if OpenAI is None:
            raise ImportError("OpenAI package required. Install: pip install openai")
        
        api_key = Config.OPENROUTER_API_KEY if hasattr(Config, 'OPENROUTER_API_KEY') else None
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        self.model = model or getattr(Config, 'OPENROUTER_MODEL', 'anthropic/claude-3.5-sonnet')
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using OpenRouter."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=getattr(Config, 'MAX_TOKENS', 2000)
            )
            
            content = response.choices[0].message.content
            tokens_used = response.usage.total_tokens if response.usage else None
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={
                    "input_tokens": response.usage.prompt_tokens if response.usage else None,
                    "output_tokens": response.usage.completion_tokens if response.usage else None,
                    "provider": "openrouter"
                }
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
```

### Mise à Jour de config.py

Ajoutez à `config.py`:
```python
# OpenRouter (100+ models)
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL: str = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")
```

### Utilisation

```python
from agents.openrouter_agent import OpenRouterAgent
from council import LLMCouncil

# Utiliser différents modèles via OpenRouter
agents = [
    OpenRouterAgent(name="Claude-3.5", model="anthropic/claude-3.5-sonnet"),
    OpenRouterAgent(name="GPT-4", model="openai/gpt-4-turbo"),
    OpenRouterAgent(name="Llama-70B", model="meta-llama/llama-3.1-70b-instruct"),
    GeminiAgent()  # Toujours inclure un modèle gratuit
]

council = LLMCouncil(agents)
result = council.debate("Your topic", rounds=3)
```

### Modèles OpenRouter Recommandés

#### **Meilleure Qualité**
```python
"anthropic/claude-3-opus"           # Le meilleur (cher)
"anthropic/claude-3.5-sonnet"       # Excellent rapport qualité/prix
"openai/gpt-4-turbo"                # Très bon
"openai/gpt-4o"                     # Rapide et puissant
```

#### **Bon Rapport Qualité/Prix**
```python
"anthropic/claude-3-haiku"          # Rapide et abordable
"openai/gpt-3.5-turbo"              # Économique
"meta-llama/llama-3.1-70b-instruct" # Puissant et abordable
"mistralai/mixtral-8x7b-instruct"   # Excellent
```

#### **Open-Source Puissants**
```python
"meta-llama/llama-3.1-405b-instruct" # Le plus puissant open-source
"meta-llama/llama-3.1-70b-instruct"
"mistralai/mixtral-8x22b-instruct"
"qwen/qwen-2.5-72b-instruct"
```

---

## 3. Together AI

### Pourquoi Together AI?

- ✅ Modèles open-source rapides
- ✅ Prix très compétitifs
- ✅ Inference optimisée
- ✅ Llama 3, Mistral, Qwen, etc.

### Installation

```bash
pip install together
```

### Configuration

Ajoutez à `.env`:
```bash
TOGETHER_API_KEY=your-together-api-key
# Obtenir: https://api.together.xyz/settings/api-keys
TOGETHER_MODEL=meta-llama/Llama-3-70b-chat-hf
```

### Créer l'Agent Together

Créez `agents/together_agent.py`:

```python
"""Together AI agent implementation."""
from typing import Optional, List
try:
    from together import Together
except ImportError:
    Together = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class TogetherAgent(BaseAgent):
    """Agent powered by Together AI."""
    
    def __init__(
        self, 
        name: str = "Together",
        role: str = "Fast Open-Source Models",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        if Together is None:
            raise ImportError("Together package required. Install: pip install together")
        
        api_key = Config.TOGETHER_API_KEY if hasattr(Config, 'TOGETHER_API_KEY') else None
        if not api_key:
            raise ValueError("TOGETHER_API_KEY not found")
        
        self.client = Together(api_key=api_key)
        self.model = model or getattr(Config, 'TOGETHER_MODEL', 'meta-llama/Llama-3-70b-chat-hf')
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Together AI."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            full_prompt = f"{system_prompt}\n\n{prompt}"
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=getattr(Config, 'MAX_TOKENS', 2000)
            )
            
            content = response.choices[0].message.content
            tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else None
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                tokens_used=tokens_used,
                metadata={"provider": "together"}
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
```

### Modèles Together Recommandés

```python
"meta-llama/Llama-3-70b-chat-hf"
"meta-llama/Llama-3.1-70B-Instruct-Turbo"
"mistralai/Mixtral-8x7B-Instruct-v0.1"
"Qwen/Qwen2.5-72B-Instruct"
"deepseek-ai/deepseek-coder-33b-instruct"
```

---

## 4. LM Studio

### Pourquoi LM Studio?

- ✅ Interface graphique pour modèles locaux
- ✅ Serveur API local compatible OpenAI
- ✅ Facile à utiliser
- ✅ Supporte GGUF, GGML
- ✅ GPU acceleration

### Installation

1. Télécharger: https://lmstudio.ai/
2. Télécharger un modèle (Llama 3, Mistral, etc.)
3. Démarrer le serveur local (Settings → Server)
4. Port par défaut: `http://localhost:1234`

### Configuration

Ajoutez à `.env`:
```bash
LMSTUDIO_BASE_URL=http://localhost:1234/v1
LMSTUDIO_MODEL=llama-3-70b  # Nom du modèle dans LM Studio
```

### Créer l'Agent LM Studio

Créez `agents/lmstudio_agent.py`:

```python
"""LM Studio agent implementation."""
from typing import Optional, List
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base_agent import BaseAgent, AgentResponse
from config import Config


class LMStudioAgent(BaseAgent):
    """Agent powered by LM Studio local server."""
    
    def __init__(
        self, 
        name: str = "LMStudio",
        role: str = "Local High-Quality Models",
        temperature: float = 0.7,
        model: str = None
    ):
        super().__init__(name, role, temperature)
        if OpenAI is None:
            raise ImportError("OpenAI package required")
        
        base_url = Config.LMSTUDIO_BASE_URL if hasattr(Config, 'LMSTUDIO_BASE_URL') else "http://localhost:1234/v1"
        
        self.client = OpenAI(
            api_key="lm-studio",  # LM Studio doesn't need real key
            base_url=base_url
        )
        self.model = model or getattr(Config, 'LMSTUDIO_MODEL', 'local-model')
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using LM Studio."""
        try:
            system_prompt = self.get_system_prompt(context, round_num)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=getattr(Config, 'MAX_TOKENS', 2000)
            )
            
            content = response.choices[0].message.content
            
            return AgentResponse(
                agent_name=self.name,
                content=content,
                model=self.model,
                metadata={"provider": "lmstudio", "local": True}
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
```

---

## 5. Autres Providers

### Cohere

```python
# agents/cohere_agent.py
import cohere
from .base_agent import BaseAgent, AgentResponse

class CohereAgent(BaseAgent):
    def __init__(self, name="Cohere", role="Command Models", temperature=0.7):
        super().__init__(name, role, temperature)
        self.client = cohere.Client(Config.COHERE_API_KEY)
        self.model = "command-r-plus"  # ou "command-r"
    
    def generate_response(self, prompt, context=None, round_num=1):
        system_prompt = self.get_system_prompt(context, round_num)
        response = self.client.chat(
            model=self.model,
            message=prompt,
            preamble=system_prompt,
            temperature=self.temperature
        )
        return AgentResponse(
            agent_name=self.name,
            content=response.text,
            model=self.model
        )
```

### Perplexity

```python
# agents/perplexity_agent.py
from openai import OpenAI
from .base_agent import BaseAgent, AgentResponse

class PerplexityAgent(BaseAgent):
    def __init__(self, name="Perplexity", role="Search-Augmented AI"):
        super().__init__(name, role)
        self.client = OpenAI(
            api_key=Config.PERPLEXITY_API_KEY,
            base_url="https://api.perplexity.ai"
        )
        self.model = "llama-3.1-sonar-large-128k-online"
    
    def generate_response(self, prompt, context=None, round_num=1):
        system_prompt = self.get_system_prompt(context, round_num)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return AgentResponse(
            agent_name=self.name,
            content=response.choices[0].message.content,
            model=self.model,
            metadata={"citations": response.citations if hasattr(response, 'citations') else None}
        )
```

---

## 6. Créer un Nouvel Agent

### Template Générique

Créez `agents/your_provider_agent.py`:

```python
"""Your Provider agent implementation."""
from typing import Optional, List
from .base_agent import BaseAgent, AgentResponse
from config import Config


class YourProviderAgent(BaseAgent):
    """Agent powered by Your Provider."""
    
    def __init__(
        self, 
        name: str = "YourProvider",
        role: str = "Your Description",
        temperature: float = 0.7
    ):
        super().__init__(name, role, temperature)
        
        # Initialize your client
        # self.client = YourProviderClient(api_key=Config.YOUR_API_KEY)
        # self.model = Config.YOUR_MODEL
    
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[AgentResponse]] = None,
        round_num: int = 1
    ) -> AgentResponse:
        """Generate response using Your Provider."""
        try:
            # Get system prompt
            system_prompt = self.get_system_prompt(context, round_num)
            
            # Call your provider's API
            # response = self.client.generate(
            #     prompt=prompt,
            #     system=system_prompt,
            #     temperature=self.temperature
            # )
            
            # Return formatted response
            return AgentResponse(
                agent_name=self.name,
                content="response content here",
                model=self.model,
                tokens_used=None,  # if available
                metadata={"provider": "your_provider"}
            )
            
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
```

### Étapes pour Ajouter un Nouveau Provider

1. **Créer l'agent**: `agents/your_provider_agent.py`
2. **Ajouter config**: Dans `config.py`
   ```python
   YOUR_PROVIDER_API_KEY: str = os.getenv("YOUR_PROVIDER_API_KEY", "")
   YOUR_PROVIDER_MODEL: str = os.getenv("YOUR_PROVIDER_MODEL", "model-name")
   ```

3. **Mettre à jour `agents/__init__.py`**:
   ```python
   try:
       from .your_provider_agent import YourProviderAgent
   except ImportError:
       YourProviderAgent = None
   
   __all__ = [
       # ... existing agents
       'YourProviderAgent',
   ]
   ```

4. **Utiliser**:
   ```python
   from agents import YourProviderAgent
   agent = YourProviderAgent()
   ```

---

## 7. Modèles Recommandés par Use Case

### Pour la Sécurité & Code
```python
# Top 3
1. "deepseek-coder:33b" (Ollama) - GRATUIT
2. "anthropic/claude-3.5-sonnet" (OpenRouter) - Payant
3. "deepseek-ai/deepseek-coder-33b" (Together) - Abordable
```

### Pour le Raisonnement Général
```python
# Top 3
1. "anthropic/claude-3-opus" (OpenRouter) - Meilleur
2. "llama3.1:70b" (Ollama) - GRATUIT
3. "openai/gpt-4-turbo" (OpenRouter) - Excellent
```

### Pour la Rapidité
```python
# Top 3
1. "gemini-2.5-flash" (Google) - GRATUIT & Rapide
2. "anthropic/claude-3-haiku" (OpenRouter) - Rapide & Bon
3. "phi3:mini" (Ollama) - GRATUIT & Très rapide
```

### Pour le Multilingual (Français)
```python
# Top 3
1. "qwen2.5:7b" (Ollama) - GRATUIT & Excellent français
2. "mistral:7b" (Ollama) - GRATUIT & Bon français
3. "mistralai/mixtral-8x7b" (OpenRouter) - Excellent
```

### Pour la Recherche Académique
```python
# Top 5
1. "anthropic/claude-3-opus" (OpenRouter) - Le meilleur
2. "llama3.1:70b" (Ollama) - GRATUIT & Puissant
3. "meta-llama/llama-3.1-405b" (OpenRouter) - Le plus puissant
4. "mixtral:8x7b" (Ollama) - GRATUIT & Excellent
5. "gemini-2.5-flash" (Google) - GRATUIT & Rapide
```

---

## 8. Configuration Multi-Providers

### Exemple: Mix Gratuit + Payant

```python
from agents import (
    OllamaAgent, GeminiAgent,  # Gratuits
    OpenRouterAgent  # Payant mais puissant
)

agents = [
    # Gratuits (bulk du travail)
    OllamaAgent(name="DeepSeek", model="deepseek-coder:33b"),
    OllamaAgent(name="Llama70B", model="llama3.1:70b"),
    GeminiAgent(name="Gemini"),
    
    # Payant (validation finale)
    OpenRouterAgent(name="Claude", model="anthropic/claude-3.5-sonnet"),
]

council = LLMCouncil(agents)
```

### Exemple: 100% Gratuit Maximum Quality

```python
agents = [
    OllamaAgent(name="DeepSeek33B", model="deepseek-coder:33b"),
    OllamaAgent(name="Llama70B", model="llama3.1:70b"),
    OllamaAgent(name="Mixtral", model="mixtral:8x7b"),
    OllamaAgent(name="Qwen72B", model="qwen2.5:72b"),
    GeminiAgent(name="Gemini"),
]
# 5 modèles puissants, 0$ de coût!
```

---

## 9. Comparaison des Providers

| Provider | Coût | Qualité | Vitesse | Modèles | Setup |
|----------|------|---------|---------|---------|-------|
| **Ollama** | ⭐⭐⭐⭐⭐ Gratuit | ⭐⭐⭐⭐ | ⭐⭐⭐ | 100+ | Facile |
| **Gemini** | ⭐⭐⭐⭐⭐ Gratuit | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 3 | Très facile |
| **OpenRouter** | ⭐⭐⭐ Payant | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 100+ | Facile |
| **Together AI** | ⭐⭐⭐⭐ Abordable | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 50+ | Facile |
| **LM Studio** | ⭐⭐⭐⭐⭐ Gratuit | ⭐⭐⭐⭐ | ⭐⭐⭐ | 100+ | Moyen |
| **Groq** | ⭐⭐⭐⭐ Gratuit | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 5 | Facile |

---

## 10. Next Steps

### Commencez Maintenant

1. **Modèles Ollama avancés** (gratuit):
   ```bash
   ollama pull llama3.1:70b
   ollama pull deepseek-coder:33b
   ollama pull mixtral:8x7b
   ```

2. **OpenRouter** (accès à tout):
   - Inscrivez-vous: https://openrouter.ai/
   - Créez l'agent (code ci-dessus)
   - Testez différents modèles

3. **Together AI** (open-source rapide):
   - Inscrivez-vous: https://api.together.xyz/
   - Créez l'agent (code ci-dessus)

---

## Documentation Complète

- **[README.md](README.md)** - Documentation principale
- **[SPECIFIC_MODELS_GUIDE.md](SPECIFIC_MODELS_GUIDE.md)** - Sélection de modèles
- **[TECH_WATCH_GUIDE.md](TECH_WATCH_GUIDE.md)** - Veille technologique

---

**Repository**: https://github.com/jaafar-benabderrazak/llm-council

**Vous avez maintenant accès à 100+ modèles LLM!** 🚀

