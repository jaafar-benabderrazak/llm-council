# 🚀 Guide d'Utilisation CLI - Comet API

## ✅ Fonctionnalité Activée !

Le support CLI pour les catégories Comet et les modèles spécifiques est maintenant **complètement opérationnel**.

---

## 📋 Syntaxes Supportées

### 1. **Par Catégorie** (Recommandé)

```bash
# Catégorie Advanced (Premium)
python main.py "Your research question" --models comet:advanced gemini --rounds 3

# Catégorie Open-Source (Équilibré)
python main.py "Your research question" --models comet:opensource gemini --rounds 3

# Catégorie Free (Économique)
python main.py "Your research question" --models comet:free ollama:llama3.1:8b --rounds 3

# Catégorie Fast (Ultra-Rapide)
python main.py "Your research question" --models comet:fast ollama --rounds 2
```

### 2. **Par Modèle Spécifique**

```bash
# Modèle GPT-5.2
python main.py "Complex analysis" --models comet:gpt-5.2 gemini --rounds 4

# Modèle Llama-3.1-70b
python main.py "Technical analysis" --models comet:llama-3.1-70b ollama --rounds 3

# Modèle Claude-3-Opus
python main.py "Critical review" --models comet:claude-3-opus gemini --rounds 3
```

### 3. **Multiple Comet Agents**

```bash
# Mix de catégories
python main.py "Comprehensive research" \
  --models \
    comet:advanced \
    comet:opensource \
    comet:free \
    ollama:llama3.1:8b \
  --rounds 4

# Mix de modèles spécifiques
python main.py "Deep dive analysis" \
  --models \
    comet:gpt-5.2 \
    comet:llama-3.1-70b \
    comet:gpt-3.5-turbo \
    gemini \
  --rounds 5
```

---

## 🎯 Catégories Disponibles

| Catégorie | Modèles | Usage | Coût |
|-----------|---------|-------|------|
| **advanced** | gpt-5.2, gpt-4-turbo, gpt-4, claude-3-opus, claude-3-sonnet | Recherche critique, analyses complexes | $$$$ |
| **opensource** | llama-3.1-70b, llama-3-70b, mixtral-8x7b, mistral-large, qwen-72b | Usage général, production | $$ |
| **free** | gpt-3.5-turbo, claude-3-haiku, llama-3-8b | Tâches rapides, prototypes | $ |
| **fast** | gpt-3.5-turbo, claude-3-haiku, gemini-pro | Réponses urgentes, validations | $ |

---

## 💡 Exemples Pratiques

### **Exemple 1: Recherche Premium**
```bash
# Windows PowerShell
$env:PYTHONIOENCODING="utf-8"

python main.py "Advanced cryptography patterns with zero-trust architecture" `
  --models comet:advanced comet:opensource ollama:deepseek-coder:6.7b `
  --rounds 5
```

**Utilisation**: Analyses critiques nécessitant la meilleure qualité.

### **Exemple 2: Équilibré (Qualité/Coût)**
```bash
python main.py "Design patterns for microservices in Kubernetes" `
  --models comet:opensource comet:free ollama:llama3.1:8b gemini `
  --rounds 4
```

**Utilisation**: Production, analyses techniques standard.

### **Exemple 3: Économique (100% Gratuit)**
```bash
python main.py "Quick overview of GraphQL vs REST" `
  --models comet:free ollama:llama3.1:8b ollama:mistral:7b `
  --rounds 2
```

**Utilisation**: Prototypes, tests rapides, veille technologique.

### **Exemple 4: Ultra-Rapide**
```bash
python main.py "What is the difference between JWT and OAuth2?" `
  --models comet:fast ollama:llama3.1:8b `
  --rounds 1 `
  --no-markdown
```

**Utilisation**: Validation rapide, questions urgentes.

---

## 🔧 Configuration Avancée

### **1. Variables d'Environnement (.env)**

```bash
# Comet API Key
COMET_API_KEY=your_comet_api_key_here

# Modèle par défaut (utilisé si aucune catégorie/modèle spécifié)
COMET_MODEL=gpt-3.5-turbo

# Base URL (si différent de la valeur par défaut)
COMET_BASE_URL=https://api.comet.com/llm/v1
```

### **2. Vérifier les Modèles Disponibles**

```bash
python -c "from config import Config; print(Config.get_available_models())"
```

**Sortie attendue**:
```
['gemini', 'deepseek', 'ollama', 'groq', 'huggingface', 'comet']
```

### **3. Tester la Connexion Comet**

```bash
python examples/comet_api_example.py
```

---

## ⚠️ Problèmes Courants & Solutions

### **Problème 1: `Connection error` pour Comet**

**Cause**: Base URL incorrect ou API key invalide.

**Solution**:
1. Vérifiez votre `.env`:
```bash
COMET_API_KEY=sk-your-actual-key-here
```

2. Vérifiez le base URL dans `agents/comet_agent.py`:
```python
base_url="https://api.comet.com/llm/v1"  # Ou l'URL correcte
```

3. Testez la connexion:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.comet.com/llm/v1/models
```

### **Problème 2: `Unknown Comet model category: xxx`**

**Cause**: Catégorie invalide.

**Solution**: Utilisez une des catégories valides:
- `advanced`
- `opensource`
- `free`
- `fast`

### **Problème 3: `Need at least 2 models`**

**Cause**: Un seul modèle spécifié.

**Solution**: Ajoutez un deuxième modèle:
```bash
# ❌ INCORRECT
python main.py "Question" --models comet:free

# ✅ CORRECT
python main.py "Question" --models comet:free ollama:llama3.1:8b
```

---

## 📊 Comparaison des Approches

| Approche | Commande | Avantages | Inconvénients |
|----------|----------|-----------|---------------|
| **Catégorie** | `--models comet:advanced` | Simple, auto-sélection | Moins de contrôle sur le modèle exact |
| **Modèle spécifique** | `--models comet:gpt-5.2` | Contrôle total | Besoin de connaître les noms exacts |
| **Mix** | `--models comet:advanced comet:free` | Meilleur compromis qualité/coût | Plus de tokens utilisés |

---

## 🎓 Workflows Recommandés

### **Workflow 1: Veille Technologique**
```bash
# Quotidien - Économique
python main.py "Latest trends in Kubernetes 2025" \
  --models comet:free ollama:llama3.1:8b \
  --rounds 2
```

### **Workflow 2: Décision d'Architecture**
```bash
# Hebdomadaire - Équilibré
python main.py "Microservices vs Monolith for fintech platform" \
  --models comet:opensource comet:free gemini \
  --rounds 4
```

### **Workflow 3: Recherche Critique**
```bash
# Mensuel - Premium
python main.py "Security patterns for zero-trust architecture with references" \
  --models comet:advanced comet:opensource ollama:deepseek-coder:6.7b \
  --rounds 6
```

### **Workflow 4: Validation Rapide**
```bash
# À la demande - Ultra-rapide
python main.py "Quick: Pros and cons of gRPC vs REST" \
  --models comet:fast ollama \
  --rounds 1 \
  --no-markdown
```

---

## 📚 Documentation Complète

- **Installation**: `README.md`
- **Catégories Comet**: `COMET_MODELS_CATEGORIES.md`
- **Configuration API**: `COMET_API_GUIDE.md`
- **Exemples**: `examples/comet_categories_example.py`

---

## ✅ Vérification du Support

Pour vérifier que tout fonctionne:

```bash
# Test rapide
python main.py "Test: What is REST API?" \
  --models comet:free ollama:llama3.1:8b \
  --rounds 1 \
  --no-markdown
```

**Sortie attendue**:
```
│ Topic: Test: What is REST API?    │
│ Rounds: 1                          │
│ Participants: Llama3.1, Comet-Free │  ← Comet-Free visible ici!
```

---

## 🚀 Prochaines Étapes

1. ✅ **Support CLI activé** - `comet:category` et `comet:model` fonctionnent
2. ⚠️ **Connexion Comet** - Vérifier le base URL et l'API key
3. 📊 **Tests complets** - Tester avec votre API key réelle
4. 📝 **Documentation** - Tous les guides créés

---

**💡 Astuce**: Commencez par `comet:free` pour tester sans coût, puis évoluez vers `comet:opensource` ou `comet:advanced` selon vos besoins.

