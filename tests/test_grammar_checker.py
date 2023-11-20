from lib.grammar_checker import *

def test_capital_first_letter():
    test_string = "Hello"
    assert capital_first_letter(test_string) == "Grammar is correct"

def test_sentence_ending():
    test_string = "Hello!"
    assert sentence_ending(test_string) == "grammar is correct"