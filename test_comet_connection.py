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
    "https://api.comet.ml/v1",
    "https://www.comet.ml/api/v1",
]

print("\n🔍 Testing Comet API endpoints...\n")

for base_url in BASE_URLS:
    print(f"Testing: {base_url}")
    try:
        client = OpenAI(api_key=API_KEY, base_url=base_url)
        
        # Try to list models
        print("  → Listing models...")
        models = client.models.list()
        print(f"  ✅ SUCCESS! Found {len(models.data)} models")
        print(f"  Available models: {[m.id for m in models.data[:5]]}")
        
        # Try a simple completion
        print("  → Testing completion...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'test ok'"}],
            max_tokens=10
        )
        print(f"  ✅ Completion: {response.choices[0].message.content}")
        print(f"\n🎉 CORRECT BASE URL FOUND: {base_url}\n")
        print(f"Update agents/comet_agent.py with:")
        print(f"  base_url=\"{base_url}\"")
        break
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg:
            print(f"  ❌ Not found (404)")
        elif "401" in error_msg or "403" in error_msg:
            print(f"  ❌ Authentication error (401/403)")
        elif "Connection" in error_msg or "connection" in error_msg.lower():
            print(f"  ❌ Connection error")
        else:
            print(f"  ❌ Error: {error_msg[:100]}")
        print()

print("\n" + "="*60)
print("If all tests failed, please:")
print("1. Check Comet API documentation for correct endpoint")
print("2. Verify your API key is valid")
print("3. Try: curl -H 'Authorization: Bearer YOUR_KEY' https://api.comet.com/v1/models")
print("="*60)

