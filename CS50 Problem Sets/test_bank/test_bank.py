import pytest
from bank import value # Import the 'value' function from bank.py

def test_hello_greetings():
    """
    Tests greetings that should return $0.
    Includes various cases of "hello" (case-insensitive).
    """
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, world!") == 0

def test_h_only_greetings():
    """
    Tests greetings that should return $20.
    Includes greetings starting with 'h' but not "hello" (case-insensitive).
    """
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("How do you do?") == 20
    assert value("hey") == 20
    assert value("h") == 20 # Edge case: just 'h'

def test_other_greetings():
    """
    Tests greetings that should return $100.
    Includes greetings not starting with 'h' or "hello".
    """
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Adieu") == 100
    assert value("123 Hello") == 100 # Starts with a number
    assert value("") == 100 # Empty string
    assert value("  hello") == 100 # Leading spaces (though problem says "assume no leading spaces" for value function, good to test if it passes through main)
    