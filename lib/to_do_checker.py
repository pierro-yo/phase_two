
def check_if_strings_contain_todo(string):
    catch_phrase = "#TODO"
    user_string = string.split()
    sentence = " ".join(user_string)

    if any(phrase in catch_phrase for phrase in user_string):
        return f"{sentence} - Don't forget to do this!"
    else:
        print("nothing to do")

