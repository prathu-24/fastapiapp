import random
import string
from routers import auth
from schemas.users import UserCreate
from database import get_db

email = f"test{''.join(random.choices(string.digits, k=6))}@example.com"
user_data = UserCreate(name="abc", email=email, password="Ab@123", role="developer")

db = next(get_db())
try:
    result = auth.register_user(user_data, db)
    print('success', result)
except Exception as exc:
    print('error', type(exc).__name__, exc)
finally:
    db.close()
