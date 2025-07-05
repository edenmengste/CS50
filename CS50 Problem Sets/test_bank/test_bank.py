import pytest
from bank import value

def test_hello_greetings():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, world!") == 0

def test_h_only_greetings():
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("How do you do?") == 20
    assert value("hey") == 20
    assert value("h") == 20 
    
def test_other_greetings():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Adieu") == 100
    assert value("123 Hello") == 100 # Starts with a number
    assert value("") == 100 # Empty string
    assert value("  hello") == 100
    
