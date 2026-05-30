"""Used for storing, queue priority, treating pets, undoing registration, pet removal, and pet update"""
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, pets):
        index = 0

        # Queue Priority comparison
        while index < len(self.items):
            if pets.severity < self.items[index].severity:
                break
            index += 1
        self.items.insert(index, pets)

    # Serves pet and removes from front of the queue
    def dequeue(self):
        if len(self.items) == 0:
            return None

        return self.items.pop(0)

    # Used to check the current state of the queue
    def peek(self):
        if len(self.items) == 0: # Avoid crashing
            print(f"\n{'=' * 60}")
            print("\nQueue is empty")
            print(f"\n{'=' * 60}")
            return

        for pets in self.items:
            print(f"\n{'=' * 100}")
            print(f"\nPet ID: {pets.pet_id} | "
                  f"Pet Name: {pets.pet_name} | "
                  f"Breed: {pets.breed} | "
                  f"Owner Name: {pets.owner_name} | "
                  f"Severity Level: {pets.severity} | ")
            print(f"\n{'=' * 100}")

    # Used for updating, deleting, and undoing pet registration
    def remove(self, pet_id):
        for i, pet in enumerate(self.items): # Checks the values of the index
            if pet.pet_id == pet_id:
                del self.items[i]
                return True
        return False

    # Check queue size
    def size(self):
        return len(self.items)
