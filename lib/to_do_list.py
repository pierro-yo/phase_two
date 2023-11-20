
class ToDoList():
    def __init__(self):
        # self.string = string
        self.list = []
    
    def add_to_list(self,string):
        self.list.append(string)
        return self.list

    def mark_complete_and_remove(self,string):
        self.list.remove(string)
        return self.list


test = ToDoList()

test.add_to_list("buy milk")
# print(test.add_to_list("walk dog"))
print(test.mark_complete_and_remove("buy milk"))

