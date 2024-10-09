import hashlib
import hmac
import base64

def create_session_token(username, server_secret):
    session_id = base64.b64encode(username.encode()).decode()

    # Create signature using HMAC SHA256
    hmac_signature = hmac.new(server_secret.encode(), session_id.encode(), hashlib.sha256)
    signature = hmac_signature.hexdigest()
    
    return f"{session_id}.{signature}"

# Using the provided username and server secret
username = "admin"
server_secret = "super_secret_key_123"

print(create_session_token(username, server_secret))