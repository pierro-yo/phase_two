from lib.to_do_list import *

def test_add_to_list():
    test = ToDoList()
    result = test.add_to_list("buy sugar")
    assert result == ["buy sugar"]

def test_mark_complete_and_remove():
    test = ToDoList()
    add_test = test.add_to_list("buy sugar")
    result = test.mark_complete_and_remove("buy sugar")
    assert result == []