from lib.diary_class import *

diary = DiaryEntry("Test", "If called again, reading_chunk should return the next chun")

def test_format():
    assert diary.format() == "Test:If called again, reading_chunk should return the next chun"

def test_count_words():
    assert diary.count_words() == 9

def test_reading_time():
    assert diary.reading_time(9) == 1

def test_reading_chunk():
    assert diary.reading_chunk(2, 1) == "If called"
    assert diary.reading_chunk(2,1) == "again, reading_chunk"
