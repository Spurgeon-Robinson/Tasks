import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt and hash the password
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed
