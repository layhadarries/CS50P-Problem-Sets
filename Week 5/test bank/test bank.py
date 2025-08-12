from bank import value


def test_input_hello():
    assert value("Hello") == 0


def test_input_h():
    assert value("hi") == 20
    assert value("hey") == 20


def test_input_other():
    assert value("Wassup") == 100
    assert value("Good Evening") == 100
