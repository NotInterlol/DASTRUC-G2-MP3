""" Class to make objects and constructors"""
from datetime import datetime

class Pets:
    def __init__(self, pet_id, pet_name, breed, owner_name, severity):
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.breed = breed
        self.owner_name = owner_name
        self.severity = severity
        self.registered_time = datetime.now()

""" Node for Linked List """
class Node:
    def __init__(self, pets):
        self.pets = pets
        self.next = None
