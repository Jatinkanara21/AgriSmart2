from app.core.security import hash_password, verify_password, create_access_token, decode_access_token
def test_password_hash_roundtrip():
 password="AgriSmart-Test-123!"; stored=hash_password(password)
 assert stored!=password; assert verify_password(password,stored); assert not verify_password("wrong-password",stored)
def test_jwt_roundtrip():
 token=create_access_token(123,"farmer@example.com"); payload=decode_access_token(token)
 assert payload["sub"]=="123"; assert payload["email"]=="farmer@example.com"
