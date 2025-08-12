from twttr import shorten


def test_upper():
    assert shorten("tweet") == "twt"


def test_lower():
    assert shorten("TWEET") == "TWT"
