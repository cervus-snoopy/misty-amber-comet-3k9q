#!/usr/bin/env python3
"""Gate helpers for the time-machine warning label entry.

This module holds the gate rules the entry enforces: a warning label
must be real text, and it must fit inside the competition's character
budget. The entrypoint keeps its own copies of the same rules so it can
run standalone; this module is the readable source those rules were
built from, kept here for reuse and for testing.
"""

MAX_LABEL_CHARS = 120


def is_valid_label(label):
    """Return True when *label* passes every gate rule.

    A label passes when it is a string, it is not empty, it is not
    only whitespace, and its length stays inside the character budget.
    """
    if not isinstance(label, str):
        return False
    if not label:
        return False
    if not label.strip():
        return False
    return len(label) <= MAX_LABEL_CHARS


def label_length(label):
    """Return the character count of *label*, or -1 when it is no text."""
    if not isinstance(label, str):
        return -1
    return len(label)


def remaining_budget(label):
    """Return how many characters of the budget a label leaves unused.

    A label that is no text leaves nothing: the answer is -1. A label
    over the budget leaves a negative number, so callers can tell how
    far over it went without counting twice.
    """
    if not isinstance(label, str):
        return -1
    return MAX_LABEL_CHARS - len(label)
