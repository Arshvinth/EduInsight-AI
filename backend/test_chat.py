import requests
import json

base = "http://127.0.0.1:8000"

# Register (ignore failures if user exists)
try:
    r = requests.post(f"{base}/auth/register", json={"username":"tester","email":"tester@example.com","password":"password123","role":"student"})
    print("register", r.status_code, r.text)
except Exception as e:
    print("register error", e)

# Login
r2 = requests.post(f"{base}/auth/login", json={"username":"tester","password":"password123"})
print("login", r2.status_code, r2.text)

token = None
try:
    token = r2.json().get("access_token")
except Exception as e:
    print("token parse error", e)

headers = {"Authorization": f"Bearer {token}"} if token else {}

# Call chat
r3 = requests.post(f"{base}/ai/chat", json={"query": "what is Polymorphism?"}, headers=headers)
print("chat", r3.status_code, r3.text)
