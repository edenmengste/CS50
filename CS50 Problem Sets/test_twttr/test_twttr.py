from twttr import shorten

def test_no_vowels():
    """Test a word with no vowels."""
    assert shorten("rhythm") == "rhythm"
    assert shorten("sky") == "sky"

def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_mixed_case_word():
    assert shorten("hello") == "hll"
    assert shorten("WORLD") == "WRLD"
    assert shorten("pyThon") == "pyThn"


def test_word_with_punctuation():

    assert shorten("apple!") == "ppl!"
    assert shorten("test?") == "tst?"
    assert shorten("CS50") == "CS50"


