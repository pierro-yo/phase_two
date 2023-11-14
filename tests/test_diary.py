from lib.diary import *

def test_make_snippet_less_than_five():
    string = "hello my name is piers"
    result = make_snippet(string)
    assert result == string


def test_make_snippet_more_than_five():
    string = "hello my name is piers piers"
    result = make_snippet(string)
    assert result == "hello my name is piers..." 