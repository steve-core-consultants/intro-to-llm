import pytest
import string

from src.utils.clean_text import clean_text


def test_clean_text_lowercase():
    assert clean_text("LOWERCASE") == "lowercase"


def test_clean_text_remove_punctuation():
    assert clean_text("Hello, world!") == "hello world"


def test_clean_text_remove_spaces():
    assert clean_text("  leading trailing  ") == "leading trailing"


def test_clean_text_special_characters():
    assert clean_text("H!e@l#l$o") == "hello"


def test_clean_text_digits():
    assert clean_text("1hello2world3") == "helloworld"


def test_clean_text_only_special_chars():
    assert clean_text(string.punctuation) == ""


def test_clean_text_only_numbers():
    assert clean_text("1234567890") == ""


def test_clean_text_combined():
    assert clean_text(" H@ell1o W$or%^ld!  ") == "hello world"


def test_clean_text_empty_string():
    with pytest.raises(ValueError) as e_info:
        clean_text("")
    assert str(e_info.value) == "Input text should not be empty"


def test_clean_text_none():
    with pytest.raises(ValueError) as e_info:
        clean_text(None)
    assert str(e_info.value) == "Input text should not be None"


def test_clean_text_non_string_input():
    with pytest.raises(AttributeError):
        clean_text(12345)
