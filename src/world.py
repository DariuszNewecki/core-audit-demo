# src/world.py

"""Demonstrates a constitutional violation for the CORE audit gate.

This file intentionally contains a public function that lacks the
required ``# ID: <uuid>`` comment on the line above its ``def``
keyword. The CORE audit gate (running on this PR) flags it as a
finding, surfaces an inline annotation in the diff view, and the
workflow's non-zero exit code blocks the merge button.

To clear the violation (and re-enable merge), uncomment the ID line
below or remove the ``add`` function entirely.
"""

from __future__ import annotations


# Intentional violation: the `add` function is public but missing the
# `# ID: <uuid>` marker that CORE's rules require. The audit will
# annotate the `def` line below.
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
