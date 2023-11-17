class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.word_count = 0

    def format(self):
        return self.title + ":" + self.contents

    def count_words(self):
        words = self.contents.split()
        # split breaks the content into a list
        return len(words)
        

    def reading_time(self, wpm):
        num_of_words = self.count_words()
        return num_of_words / wpm

    def reading_chunk(self, wpm, minutes):
        readable_words = minutes * wpm
        words = self.contents.split()
        last_word = self.word_count + readable_words
        result = " ".join(words[self.word_count:last_word])
        self.word_count = readable_words
        return result

diary = DiaryEntry("Test", "If called again, reading_chunk should return the next chun")
