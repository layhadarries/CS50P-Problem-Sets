from fuel import convert, gauge


def test_convert():
    assert convert("0/5") == 0
    assert convert("5/5") == 100
    assert convert("4/5") == 80


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(80) == "80%"


def test_error():
    with pytest.raises(TypeError):
        assert convert("cat")

    with pytest.raises(ValueError):
        assert convert("5/4")

    with pytest.raises(ValueError):
        assert convert("-4/-5")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")
