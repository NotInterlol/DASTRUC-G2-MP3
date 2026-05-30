from pets import Pets
from linked_list import LinkedList
from queuing import Queue
from stack import Stack

class VetClinic:
    def __init__(self):
        self.records = LinkedList()
        self.queue = Queue()
        self.undo = Stack()
        self.next_id = 1

    def generate_pet_id(self):
        pet_id = f"{self.next_id:03}"
        self.next_id += 1
        return pet_id

    @staticmethod # static method to remove self parameter
    def string_input(text):
        while True:
            text_input = input(text).strip()
            if text_input != '':
                return text_input
            print("Please input text, try again.")

    @staticmethod
    def int_input(number):
        while True:
            try:
                return int(input(number))
            except ValueError:
                print("Please enter a number. Try again.")

    def pet_registry(self):
        pet_id = self.generate_pet_id()
        print(f"\nGenerated Pet ID: {pet_id}")

        pet_name = self.string_input("Pet Name: ")
        breed = self.string_input("Breed: ")
        owner_name = self.string_input("Name of Owner: ")

        while True:
            severity = self.int_input("Severity Level (1-5): ")

            if severity < 1 or severity > 5:
                print("Invalid Severity Level, please try again")
                continue
            break

        if severity == 1:
            print(f"\n{'=' * 30}")
            print("\nHigh Severity level detected, pet has been moved to front of queue!")
            print(f"\n{'=' * 30}")

        pets = Pets(pet_id, pet_name, breed, owner_name, severity)

        self.records.add_node(pets)
        self.queue.enqueue(pets)
        self.undo.push(pets)

        print(f"\n{'=' * 30}")
        print("\nPet Registry Successful.")
        print(f"\n{'=' * 30}")

    def next_pet(self):
        pets = self.queue.dequeue()

        if pets is None:
            print(f"\n {'=' * 30}")
            print("\nNo available pets.")
            print(f"\n {'=' * 30}")
            return

        print(f"\n{'=' * 30}")
        print(f"\nTreating current pet: {pets.pet_name}")
        print(f"\n{'=' * 30}")

    def update_pet(self):
        print("Input X to return to menu")
        while True:
            pet_id = self.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                return

            pets = self.records.search(pet_id)

            if pets:
                break
            print("Pet not found. Try again.")

        pets.pet_name = self.string_input("New Pet Name: ")
        pets.breed = self.string_input("New Breed: ")
        pets.owner_name = self.string_input("New Owner Name: ")

        while True:
            severity = self.int_input("New Severity (1-5): ")

            if 1 <= severity <= 5:
                pets.severity = severity
                break

            print("Invalid Severity Level")

        self.queue.remove(pet_id)
        self.queue.enqueue(pets)

        print(f"\n{'=' * 30}")
        print("\nPet updated successfully.")
        print(f"\n{'=' * 30}")

    def undo_registry(self):
        pets = self.undo.pop()

        if pets is None:
            print(f"\n{'=' * 30}")
            print("\nNo registries to undo.")
            print(f"\n{'=' * 30}")
            return

        self.records.delete(pets.pet_id)
        self.queue.remove(pets.pet_id)
        print(f"\n{'=' * 30}")
        print("\nSuccessfully removed pet registration.")
        print(f"\n{'=' * 30}")
