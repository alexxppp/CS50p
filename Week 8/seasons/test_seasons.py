from seasons import get_minutes
import pytest


def test_invalid_format():
    with pytest.raises(SystemExit):
        get_minutes("February 28, 2012")
