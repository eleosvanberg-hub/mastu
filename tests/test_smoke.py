"""Trivial check that the test suite and src package are wired up correctly."""

from src import config


def test_config_importable():
    assert config.RANDOM_SEED == 42
