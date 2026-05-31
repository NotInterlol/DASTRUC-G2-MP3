"""Singly Linked List serves as a pet record"""
from pets import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # Used to add a new node at the end of the Linked List
    def add_node(self, pets):
        new_node = Node(pets)

        if self.head is None: # Checks for empty list and assigns the head
            self.head = new_node
            return

        current = self.head # Initiates traversal from the beginning
        while current.next is not None:
            current = current.next
        current.next = new_node # Attach new node to current node

    # Used to display entire pet records of registered pets
    def display_record(self):
        current = self.head

        if current is None: # Initiates during empty list
            print(f"\n{'=' * 20}")
            print("\nNo pets registered")
            print(f"\n{'=' * 20}")
            return

        while current: # Shows every node available in the list
            pets = current.pets # Used to access and assign pet data
            print(f"\n{'=' * 100}")
            print(f"\nPet ID: {pets.pet_id} | "
                  f"Pet Name: {pets.pet_name} | "
                  f"Breed: {pets.breed} | "
                  f"Owner Name: {pets.owner_name} | "
                  f"Severity Level: {pets.severity} | "
                  f"Registered Time: {pets.registered_time.strftime('%Y-%m-%d %H:%M:%S')} | ")
            print(f"\n{'=' * 100}")
            current = current.next # Traversal for Linked List

    # Used to search for a specific pet through ID
    def search(self, pet_id):
        current = self.head

        while current: # Checks every node until ID is matching and returns the pet data else continue traversing
            if current.pets.pet_id == pet_id:
                return current.pets
            current = current.next

        return None

    # Used to delete a specific pet through ID
    def delete(self, pet_id):
        current = self.head
        previous = None # reconnects the nodes if the intermediary is deleted

        while current: # Checks every node until ID is matching and deletes the pet records, else continue traversing
            if current.pets.pet_id == pet_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current # allows for traversal to look for specific id
            current = current.next

        return False
