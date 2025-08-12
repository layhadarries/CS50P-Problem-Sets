from plates import is_valid


def test_length():
    assert is_valid("HI") is False
    assert is_valid("CS50") is True


def test_first_two_char():
    assert is_valid("45CS05") is False
    assert is_valid("CSPY05") is True


def test_end_char():
    assert is_valid("CS50P") is False
    assert is_valid("CSP50") is True


def test_isalpha():
    assert is_valid("PI3.14") is False
    assert is_valid("PIE314") is True
