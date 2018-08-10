import pytest
import kellersensortelegrambot


def test_project_defines_author_and_version():
    assert hasattr(kellersensortelegrambot, '__author__')
    assert hasattr(kellersensortelegrambot, '__version__')
