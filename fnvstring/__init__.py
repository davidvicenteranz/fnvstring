"""fnvstring package.

A hash implementation of the Fowler–Noll–Vo non-cryptographic function 
for python 3.
"""

from fnvstring.hasher import DEFAULT_SALT
from fnvstring.hasher import Fvn64StringHasher as Hash

__all__ = (
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
)

__copyright__ = "Copyright 2021 David Vicente"

# This package version is auto-managed by scm 
import importlib_metadata

metadata = importlib_metadata.metadata("fnvstring")


__title__ = metadata["name"]
__summary__ = metadata["summary"]
__uri__ = metadata["home-page"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__email__ = metadata["author-email"]
__license__ = metadata["license"]

# Fvn64StringHasher sortcut to statics methods
def hash(string, salt=None):
    """Return a FNV hash of string."""
    return Hash.as_base64(string, salt=salt)

def random(): 
    """Return random hash formated as base64 with a length of 11"""
    return Hash.random()

class Fvn64SaltedHasher:
    """Fnv64 Hasher with specific salt."""

    salt: str = DEFAULT_SALT

    def __init__(self, salt: str = None):
        if salt:
            self.salt = salt

    def hash(self, string: str, salt: str = None) -> str:
        """Return a base64 string of a length of 11."""
        salt = salt if salt else self.salt
        return Hash.as_base64(string, salt=salt)
