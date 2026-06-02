# src/hello.py

"""Demo module for the CORE audit gate.

Every public symbol below carries a ``# ID: <uuid>`` comment as
required by CORE's symbol-tracking rules. Removing one of these
comments is the easiest way to demonstrate a constitutional
violation that the audit gate will flag and merge-block.
"""

from __future__ import annotations


# ID: 6c8a1b7e-9d4f-4c2a-8e3b-1f5c7d2a9b0e
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


# ID: 4f7d9c3a-2b8e-4a1d-9c6f-3e8a5b7c2d1f
def shout(message: str) -> str:
    """Return the message in uppercase with an exclamation point."""
    return f"{message.upper()}!"
