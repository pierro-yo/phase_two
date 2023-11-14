from lib.diary import *

def test_make_snippet_less_than_five():
    string = "hello my name is piers"
    result = make_snippet(string)
    assert result == string


def test_make_snippet_more_than_five():
    string = "hello my name is piers piers"
    result = make_snippet(string)
    assert result == "hello my name is piers..."

def test_count_two_words():
    string = "hello there"
    assert count_words(string) == 2

def test_count_five_words():
    string = "hello my name is piers"
    assert count_words(string) == 5