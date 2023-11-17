
def capital_first_letter(string):
    user_string = string
    if user_string[0].isupper():
        return "Grammar is correct"
    else:
        return "capital letter needed"
# print(capital_first_letter('Hello'))

def sentence_ending(string):
    special_chars = ".!?"
    user_string = string[-1]
    if any(char in special_chars for char in user_string):
        return "grammar is correct"
    else:
        return "need either ! ? ."
# print(sentence_ending("hello."))
