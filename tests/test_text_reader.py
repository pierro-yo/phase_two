from lib.text_reader import *

def test_word_counter():
    text = "Hi my name is Naim"
    assert word_counter(text) == 5

def test_reading_time():
    text = "Hi my name is Naim"
    assert reading_time(text) == 0.025