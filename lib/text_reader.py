text = "These are examples of the function being called with particular arguments, and what the function should return in each situation. For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address. These are examples of the function being called with particular arguments, and what the function should return in each situation. For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address. These are examples of the function being called with particular arguments, and what the function should return in each situation. For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address."

def word_counter(text):
    words = text.split()
    return len(words)

def reading_time(text):
    number_words = word_counter(text)
    return (number_words / 200)

print(word_counter(text))
print(reading_time(text))

