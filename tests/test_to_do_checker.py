
from lib.to_do_checker import *

def test_check_if_strings_contain_todo():
    text = "Collect parcel #TODO"
    assert check_if_strings_contain_todo(text) ==  "Collect parcel #TODO - Don't forget to do this!"
