"""Main logic of the entire system to provide intended outputs"""
from datetime import datetime
from pets import Pets
from linked_list import LinkedList
from queuing import Queue
from stack import Stack

class VetClinic:
    def __init__(self):
        self.records = LinkedList()
        self.queue = Queue()
        self.undo = Stack()
        self.next_id = 1 # Automatic ID generation

    # Creates unique ID for every pet registered
    def generate_pet_id(self):
        pet_id = f"{self.next_id:03}"
        self.next_id += 1
        return pet_id

    # Error handler if blank inputs
    @staticmethod # static method to remove self parameter
    def string_input(text):
        while True:
            text_input = input(text).strip()
            if text_input != '':
                return text_input
            print("Please input text, try again.")

    # Error handler for invalid values such as string
    @staticmethod
    def int_input(number):
        while True:
            try:
                return int(input(number))
            except ValueError:
                print("Please enter a number. Try again.")

    # Obtains pet information and severity level and registers pet into records
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
            print("\nHigh Severity level detected, pet has been prioritized in the queue!")

        pets = Pets(pet_id, pet_name, breed, owner_name, severity)

        self.records.add_node(pets) # Add record to Linked List
        self.queue.enqueue(pets) # Add to Queue
        self.undo.push(pets) # Push to stack for undo

        print(f"\n{'=' * 30}")
        print("\nPet Registry Successful.")
        print(f"Registered at: {pets.registered_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n{'=' * 30}")

    # Serves pet and remove from queue
    def serve_pet(self):
        pets = self.queue.dequeue()

        if pets is None: # Error handler for crashing
            print(f"\n {'=' * 30}")
            print("\nNo available pets.")
            print(f"\n {'=' * 30}")
            return

        print(f"\n{'=' * 30}")
        print(f"\nTreating current pet: {pets.pet_name}")
        print(f"Treated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n{'=' * 30}")

    # Update pet information through ID
    def update_pet(self):
        print("Input X to return to menu")
        while True:
            pet_id = self.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                return

            pets = self.records.search(pet_id) # Searches the pet ID

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

        self.queue.remove(pet_id) # Removes old information
        self.queue.enqueue(pets) # Reinsert new entry

        print(f"\n{'=' * 30}")
        print("\nPet updated successfully.")
        print(f"Updated Pet Record at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n{'=' * 30}")

    # Undo recently registered pet from pet records and from queue
    def undo_registry(self):
        while True:
            pets = self.undo.pop() # Remove from stack

            if pets is None:
                print(f"\n{'=' * 30}")
                print("\nNo registries to undo.")
                print(f"\n{'=' * 30}")
                return

            if self.records.delete(pets.pet_id): # Remove from Linked List
                self.queue.remove(pets.pet_id) # Remove from Queue
                print(f"\n{'=' * 30}")
                print(f"\nSuccessfully deleted {pets.pet_name} from pet records")
                print(f"Pet record deleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"\n{'=' * 30}")
                return

    def pet_search(self):
        print("Input X to return to menu")
        while True:
            pet_id = self.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                break

            # Searches similar Pet ID
            pets = self.records.search(pet_id)

            if pets:
                print(f"\n{'=' * 100}")
                print(f"\nPet ID: {pets.pet_id} | "
                      f"Pet Name: {pets.pet_name} | "
                      f"Breed: {pets.breed} | "
                      f"Owner Name: {pets.owner_name} | "
                      f"Severity Level: {pets.severity} | "
                      f"Registered Time: {pets.registered_time.strftime('%Y-%m-%d %H:%M:%S')} | ")
                print(f"\n{'=' * 100}")
                break

            else:
                print(f"\n{'=' * 30}")
                print("\nPet not found.")
                print(f"\n{'=' * 30}")

    def delete_pet(self):
        print("Input X to return to menu")
        while True:
            pet_id = self.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                break

            pets = self.records.search(pet_id)

            if pets is None:
                print("Pet not found.")
                continue

            self.records.delete(pet_id)
            self.queue.remove(pet_id)

            print(f"\nSuccessfully deleted {pets.pet_name} from pet records")
            print(f"Pet record deleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
