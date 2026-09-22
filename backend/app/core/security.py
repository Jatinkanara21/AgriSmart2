import hashlib
import hmac
from datetime import datetime, timedelta, timezone
import jwt
from .config import settings

def hash_password(password: str) -> str:
    salt = hashlib.sha256(settings.jwt_secret.encode()).digest()[:16]
    digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
    return "scrypt$sha256$" + salt.hex() + "$" + digest.hex()

def verify_password(password: str, stored: str) -> bool:
    try:
        _, _, salt_hex, digest_hex = stored.split("$", 3)
        digest = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), n=2**14, r=8, p=1)
        return hmac.compare_digest(digest.hex(), digest_hex)
    except (ValueError, TypeError):
        return False

def create_access_token(user_id: str, email: str) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": str(user_id), "email": email, "exp": expires}, settings.jwt_secret, algorithm=settings.jwt_algorithm)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
