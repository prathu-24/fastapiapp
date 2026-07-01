from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

payload = {
    "name": "abc",
    "email": "abc+test@example.com",
    "password": "Ab@123",
    "role": "developer"
}

response = client.post('/auth/register', json=payload)
print('status_code =', response.status_code)
print('response_body =', response.text)
print('response_json =', response.json() if response.headers.get('content-type', '').startswith('application/json') else 'not json')
