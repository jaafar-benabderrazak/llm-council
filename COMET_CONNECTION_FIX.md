# 🔧 Guide Rapide: Résoudre l'Erreur de Connexion Comet API

## ⚠️ Problème Actuel

```
Error generating response: Connection error.
```

L'agent Comet est créé correctement (`Comet-Free` visible dans les participants), mais la connexion à l'API échoue.

---

## 🔍 Diagnostic

### **1. Vérifier l'API Key**

```powershell
# Vérifier que la clé est bien chargée
cd "C:\Users\Utilisateur\Desktop\projects\LLM Council"
python -c "from config import Config; print(f'Comet API Key: {Config.COMET_API_KEY[:10]}...' if Config.COMET_API_KEY else 'NOT SET')"
```

**Attendu**:
```
Comet API Key: sk-qVmPMt1...
```

**Si "NOT SET"**, ajoutez dans votre `.env`:
```bash
COMET_API_KEY=sk-qVmPMt1sEw1R77GOWiMpqj18FcrytykDXDu1RBEHFIwTsvYN
```

### **2. Vérifier le Base URL**

Le fichier `agents/comet_agent.py` utilise actuellement:
```python
base_url="https://api.comet.com/llm/v1"
```

**Ce base URL est probablement incorrect.**

---

## 🛠️ Solutions Possibles

### **Option 1: Trouver le Bon Base URL**

Comet API peut utiliser différents endpoints. Vérifiez la documentation Comet ou essayez ces URLs:

1. **OpenAI-compatible endpoint** (le plus probable):
   ```
   https://api.comet.com/v1
   ```

2. **LLM endpoint spécifique**:
   ```
   https://api.comet.com/api/v1
   ```

3. **Autre variante**:
   ```
   https://www.comet.com/api/llm/v1
   ```

### **Option 2: Modifier le Code**

Si vous trouvez le bon endpoint, modifiez `agents/comet_agent.py`:

```python
# Ligne ~25-30
self.client = OpenAI(
    api_key=Config.COMET_API_KEY,
    base_url="https://api.comet.com/v1"  # ← Mettez le bon URL ici
)
```

### **Option 3: Variable d'Environnement**

Ajoutez le base URL dans `.env`:

```bash
# Dans .env
COMET_BASE_URL=https://api.comet.com/v1
```

Puis modifiez `agents/comet_agent.py`:

```python
from config import Config

# Dans __init__
self.client = OpenAI(
    api_key=Config.COMET_API_KEY,
    base_url=os.getenv("COMET_BASE_URL", "https://api.comet.com/llm/v1")
)
```

---

## 🧪 Tester la Connexion Manuellement

Créez un script de test `test_comet_connection.py`:

```python
"""Test Comet API connection with different base URLs."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COMET_API_KEY")
if not API_KEY:
    print("❌ COMET_API_KEY not set in .env")
    exit(1)

print(f"✅ API Key found: {API_KEY[:10]}...")

# Test different base URLs
BASE_URLS = [
    "https://api.comet.com/v1",
    "https://api.comet.com/llm/v1",
    "https://api.comet.com/api/v1",
    "https://www.comet.com/api/v1",
]

for base_url in BASE_URLS:
    print(f"\n🔍 Testing: {base_url}")
    try:
        client = OpenAI(api_key=API_KEY, base_url=base_url)
        
        # Try to list models
        print("  Trying to list models...")
        models = client.models.list()
        print(f"  ✅ SUCCESS! Found {len(models.data)} models")
        print(f"  Available models: {[m.id for m in models.data[:5]]}")
        
        # Try a simple completion
        print("  Trying a test completion...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'test ok'"}],
            max_tokens=10
        )
        print(f"  ✅ Completion test: {response.choices[0].message.content}")
        print(f"\n🎉 CORRECT BASE URL: {base_url}")
        break
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg:
            print(f"  ❌ Not found (404)")
        elif "401" in error_msg or "403" in error_msg:
            print(f"  ❌ Authentication error")
        elif "Connection" in error_msg:
            print(f"  ❌ Connection error")
        else:
            print(f"  ❌ Error: {error_msg[:100]}")
```

**Exécuter**:
```powershell
$env:PYTHONIOENCODING="utf-8"
python test_comet_connection.py
```

---

## 📞 Contacter le Support Comet

Si aucune URL ne fonctionne:

1. **Vérifier la documentation Comet**:
   - Cherchez "API endpoint" ou "base URL" dans leur documentation
   - Regardez les exemples de code

2. **Vérifier l'état de l'API**:
   ```bash
   curl -H "Authorization: Bearer sk-qVmPMt1sEw1R77GOWiMpqj18FcrytykDXDu1RBEHFIwTsvYN" https://api.comet.com/v1/models
   ```

3. **Contacter le support**:
   - Email: support@comet.com
   - Question: "What is the correct OpenAI-compatible API endpoint for LLM inference?"

---

## 🔄 Alternative: Utiliser OpenRouter à la Place

Si Comet ne fonctionne pas immédiatement, vous pouvez utiliser OpenRouter qui a le même objectif:

```bash
# Dans .env
OPENROUTER_API_KEY=your_openrouter_key_here

# CLI
python main.py "Question" --models openrouter:anthropic/claude-3.5-sonnet ollama --rounds 3
```

OpenRouter donne accès à 100+ modèles avec un seul API key.

---

## ✅ Checklist de Dépannage

- [ ] API key dans `.env` (vérifiée)
- [ ] Base URL correct trouvé
- [ ] Test manuel avec `test_comet_connection.py`
- [ ] Modification de `agents/comet_agent.py` avec bon base URL
- [ ] Test avec CLI: `python main.py "Test" --models comet:free ollama --rounds 1`
- [ ] Connexion réussie !

---

## 💡 Astuce

En attendant de résoudre le problème Comet, utilisez les autres providers gratuits:

```bash
# Débat 100% gratuit sans Comet
python main.py "Your question" \
  --models ollama:llama3.1:8b ollama:deepseek-coder:6.7b groq \
  --rounds 3
```

Tous ces modèles sont gratuits et fonctionnent immédiatement !

---

## 📧 Si Vous Trouvez la Solution

Si vous trouvez le bon base URL Comet, merci de:
1. Me le partager pour que je mette à jour le code
2. Créer un issue sur GitHub pour aider les autres utilisateurs

---

**Note**: Le support CLI fonctionne parfaitement, c'est juste la configuration du endpoint API qui nécessite la bonne URL de Comet.

