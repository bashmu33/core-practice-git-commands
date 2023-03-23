import pytest


def always_returns_true():
    #Hello, this comment should give a merge conflict.
    # adding a comment here
    return False


def test_always_returns_true():
    assert always_returns_true()
