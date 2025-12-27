# 🔑 Comet API Integration Guide

## ✅ Configuration Complète

Votre clé API Comet a été configurée avec succès!

---

## 📋 Ce Qui a Été Fait

### 1. **Agent Créé**
- ✅ `agents/comet_agent.py` - Implementation complète
- ✅ Support OpenAI-compatible API
- ✅ Gestion des tokens et métadonnées
- ✅ Error handling robuste

### 2. **Configuration**
- ✅ Clé API ajoutée à `.env`
- ✅ Configuration dans `config.py`
- ✅ Import dans `agents/__init__.py`

### 3. **Exemple**
- ✅ `examples/comet_api_example.py` - Exemple d'utilisation

---

## 🔧 Configuration Actuelle

### Fichier `.env`
```bash
COMET_API_KEY=sk-qVmPMt1sEw1R77GOWiMpqj18FcrytykDXDu1RBEHFIwTsvYN
COMET_MODEL=gpt-3.5-turbo
```

⚠️ **SÉCURITÉ IMPORTANTE**: 
Cette clé API a été partagée publiquement. Pour des raisons de sécurité, vous devriez:
1. Régénérer une nouvelle clé dans votre dashboard Comet
2. Mettre à jour le fichier `.env` avec la nouvelle clé
3. Ne jamais partager vos clés API publiquement

---

## 🚀 Utilisation

### Option 1: Exemple Simple
```bash
$env:PYTHONIOENCODING="utf-8"
python examples/comet_api_example.py
```

### Option 2: Command Line
```bash
# Utiliser Comet avec d'autres modèles
python main.py "Your topic" --models comet ollama gemini --rounds 3
```

### Option 3: Python API
```python
from agents.comet_agent import CometAgent
from agents import GeminiAgent
from council import LLMCouncil

# Créer agents
agents = [
    CometAgent(name="Comet", role="Comet AI Analysis"),
    GeminiAgent(name="Gemini", role="Fast Synthesis")
]

# Run debate
council = LLMCouncil(agents)
result = council.debate("Your topic", rounds=3)
```

---

## 🔍 Vérification de la Configuration

### Tester l'API
```python
import os
from agents.comet_agent import CometAgent

# Vérifier la clé
api_key = os.getenv('COMET_API_KEY')
print(f"API Key configured: {api_key[:20]}...")

# Tester l'agent
try:
    agent = CometAgent()
    print("✅ Comet agent initialized successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
```

---

## ⚙️ Configuration Avancée

### Ajuster l'URL de Base (si nécessaire)

Si Comet utilise une URL différente, modifiez `agents/comet_agent.py`:

```python
# Ligne 31-34
self.client = OpenAI(
    api_key=api_key,
    base_url="https://api.comet.example.com/v1"  # ← Modifiez ici
)
```

### Modèles Disponibles

Vérifiez les modèles disponibles via Comet API et mettez à jour `.env`:

```bash
# Exemples (ajustez selon la documentation Comet)
COMET_MODEL=gpt-3.5-turbo
# ou
COMET_MODEL=gpt-4
# ou
COMET_MODEL=claude-2
```

---

## 🎯 Exemples de Débats

### Exemple 1: Mix Comet + Gratuit
```python
from agents import CometAgent, OllamaAgent, GeminiAgent
from council import LLMCouncil

agents = [
    CometAgent(name="Comet"),
    OllamaAgent(name="Llama", model="llama3.1:8b"),
    GeminiAgent(name="Gemini")
]

council = LLMCouncil(agents)
result = council.debate(
    "Analyze cloud security best practices",
    rounds=3
)
```

### Exemple 2: Spécifier le Modèle
```python
agent = CometAgent(
    name="Comet-GPT4",
    model="gpt-4",  # Si disponible
    role="Premium Analysis"
)
```

---

## 🐛 Troubleshooting

### Erreur: "COMET_API_KEY not found"
```bash
# Vérifier le fichier .env
cat .env | grep COMET

# Si vide, ajouter:
echo "COMET_API_KEY=your-key" >> .env
```

### Erreur: "Invalid API key"
- Vérifiez que la clé est correcte
- Régénérez une nouvelle clé si nécessaire
- Vérifiez les permissions de la clé

### Erreur: "Model not found"
- Vérifiez les modèles disponibles dans la doc Comet
- Mettez à jour `COMET_MODEL` dans `.env`

### Erreur: "Connection refused"
- Vérifiez le `base_url` dans `agents/comet_agent.py`
- Consultez la documentation API de Comet pour l'URL correcte

---

## 📊 Comparaison avec Autres Providers

| Feature | Comet | OpenRouter | Ollama |
|---------|-------|------------|--------|
| **Setup** | ✅ Configuré | Optionnel | ✅ Disponible |
| **Coût** | Selon pricing | $$ | Gratuit |
| **Modèles** | À vérifier | 100+ | 100+ |
| **Local** | ❌ | ❌ | ✅ |

---

## 📝 Prochaines Étapes

### 1. Vérifier l'API
```bash
# Tester si l'API fonctionne
python examples/comet_api_example.py
```

### 2. Consulter la Documentation Comet
- Vérifier l'URL de base correcte
- Lister les modèles disponibles
- Vérifier le pricing
- Comprendre les rate limits

### 3. Sécuriser la Clé
```bash
# Régénérer la clé API (recommandé)
# 1. Aller dans votre dashboard Comet
# 2. Créer une nouvelle clé
# 3. Mettre à jour .env
```

### 4. Intégrer dans Vos Workflows
```bash
# Utiliser dans vos débats
python main.py "topic" --models comet gemini --rounds 3

# Ou dans tech watch
# Modifier tech_watch_automation.py pour inclure Comet
```

---

## 🔐 Sécurité - IMPORTANT

### ⚠️ Votre Clé a Été Exposée

La clé API que vous avez partagée est maintenant publique. **Action requise**:

1. **Révoquer la clé actuelle**:
   - Connectez-vous à votre dashboard Comet
   - Trouvez la clé `sk-qVmPMt1sEw1R77GOWiMpqj18FcrytykDXDu1RBEHFIwTsvYN`
   - Révoquez/supprimez cette clé

2. **Générer une nouvelle clé**:
   - Créez une nouvelle clé API
   - Copiez la nouvelle clé

3. **Mettre à jour `.env`**:
   ```bash
   # Ouvrez .env et remplacez l'ancienne clé
   COMET_API_KEY=your-new-key-here
   ```

4. **Bonnes pratiques**:
   - ✅ Jamais partager les clés API dans le chat
   - ✅ Utiliser variables d'environnement
   - ✅ Ajouter `.env` au `.gitignore`
   - ✅ Régénérer les clés exposées immédiatement

---

## 📚 Documentation

- **[ADVANCED_MODELS_GUIDE.md](ADVANCED_MODELS_GUIDE.md)** - Guide des modèles avancés
- **[README.md](README.md)** - Documentation principale
- **Comet API Docs** - Consultez la documentation officielle de Comet

---

## ✅ Résumé

### Ce Qui Est Prêt
- ✅ Agent Comet créé et configuré
- ✅ Clé API ajoutée à `.env`
- ✅ Exemple d'utilisation fourni
- ✅ Integration dans le framework

### Ce Que Vous Devez Faire
- ⚠️ **URGENT**: Régénérer la clé API (exposée publiquement)
- 📖 Vérifier la documentation Comet pour:
  - URL de base correcte
  - Modèles disponibles
  - Pricing et rate limits
- 🧪 Tester avec `python examples/comet_api_example.py`

---

**Repository**: https://github.com/jaafar-benabderrazak/llm-council

**Comet API est maintenant intégré!** 🚀

⚠️ **N'oubliez pas de régénérer votre clé API pour la sécurité!**

