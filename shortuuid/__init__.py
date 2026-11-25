from shortuuid.main import decode
from shortuuid.main import encode
from shortuuid.main import get_alphabet
from shortuuid.main import random
from shortuuid.main import set_alphabet
from shortuuid.main import ShortUUID
from shortuuid.main import uuid

__version__ = "1.0.11"
__all__ = [
    "decode",
    "encode",
    "get_alphabet",
    "random",
    "set_alphabet",
    "ShortUUID",
    "uuid",
]

def prefixed_uuid(prefix: str) -> str:
    """Generate a short UUID with an ASCII alphanumeric prefix."""
    if not prefix.isascii() or not prefix.isalnum():
        raise ValueError("Prefix must contain only ASCII letters and digits.")
    return f"{prefix}-{uuid()}"
