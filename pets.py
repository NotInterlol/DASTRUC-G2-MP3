""" Used as a storage to register and undo registration"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, pets):
        self.items.append(pets)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None
