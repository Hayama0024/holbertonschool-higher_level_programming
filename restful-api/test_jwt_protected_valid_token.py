# test_jwt_protected_valid_token.py
import requests

# ログインしてトークンを取得
response = requests.post("http://127.0.0.1:5000/login", json={
    "username": "admin1",
    "password": "password"
})
token = response.json().get("access_token")

# トークンを使って保護されたルートにアクセス
headers = {"Authorization": f"Bearer {token}"}
protected = requests.get("http://127.0.0.1:5000/jwt-protected", headers=headers)

print("Protected:", protected.json())

admin = requests.get("http://127.0.0.1:5000/admin-only", headers=headers)
print("Admin:", admin.json())
