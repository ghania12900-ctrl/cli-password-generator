import pytest
from generator import generate_password


def test_default_password_length():
    """Test that default password length is 12."""
    passwords = generate_password()
    assert len(passwords) == 1
    assert len(passwords[0]) == 12


def test_custom_password_length_and_count():
    """Test custom length (-l 24) and generation count (--count 5)."""
    length = 24
    count = 5
    passwords = generate_password(length=length, count=count)

    assert len(passwords) == count
    for pwd in passwords:
        assert len(pwd) == length


def test_no_symbols_flag():
    """Test that symbols are absent when --no-symbols is used."""
    import string

    passwords = generate_password(no_symbols=True, count=10)
    symbols = string.punctuation

    for pwd in passwords:
        for char in pwd:
            assert char not in symbols


def test_exclude_characters():
    """Test that excluded ambiguous characters do not appear."""
    exclude_list = "0O1lI"
    passwords = generate_password(exclude_chars=exclude_list, length=50, count=5)

    for pwd in passwords:
        for char in pwd:
            assert char not in exclude_list