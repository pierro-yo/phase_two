
def make_snippet(string):
    words = string.split()
    if (len(words)) > 5:
        sentence =  " ".join(words[:5])
        return sentence + "..."
    else:
        return string

# print(make_snippet("hello bye hi asas asasa "))


def count_words(string):
    words = string.split()
    return len(words)


print(count_words("hello my name is piers piers"))

