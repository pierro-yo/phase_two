
def make_snippet(string):
    words = string.split()
    if (len(words)) > 5:
        sentence =  " ".join(words[:5])
        return sentence + "..."
    else:
        return string

print(make_snippet("hello bye hi asas asasa keep"))