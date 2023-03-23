import pytest


def always_returns_true():
    variable = True
    return variable


def test_always_returns_true():
    assert always_returns_true()
