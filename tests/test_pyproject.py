"""Verify the library top-level functionality."""
import pyproject


def test_version():
    """Verify we have updated the package version."""
    assert pyproject.__version__ == "21.1.1"
