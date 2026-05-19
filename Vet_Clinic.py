from Linked_List import LinkedList
from Pet_Node import PetNode
from Queuing import PriorityQueue
from Stack import Stack

class VetClinic:
    def __init__(self):
        self.records = LinkedList()
        self.queue = PriorityQueue()
        self.undo_stack = Stack()
        self._id_counter = 1000

    def _next_id(self):
        pid = f"P{self._id_counter}"
        self._id_counter += 1
        return pid

    @staticmethod
    def _get_input(prompt, allow_blank=False):
        while True:
            val = input(prompt).strip()
            if val or allow_blank:
                return val
            print("  Input cannot be blank. Please try again.")

    @staticmethod
    def _get_int(prompt, lo, hi):
        while True:
            raw = input(prompt).strip()
            if not raw.isdigit():
                print(f"  Please enter a whole number between {lo} and {hi}.")
                continue
            val = int(raw)
            if lo <= val <= hi:
                return val
            print(f"  Value must be between {lo} and {hi}.")

    def register_pet(self):
        print("\n  ── Register New Pet ──")
        name = self._get_input("  Pet Name   : ")
        breed = self._get_input("  Breed      : ")
        owner = self._get_input("  Owner Name : ")
        severity = self._get_int("  Severity (1=Emergency … 5=Least severe): ", 1, 5)

        pet_id = self._next_id()
        new_pet = PetNode(pet_id, name, breed, owner, severity)

        self.records.insert(new_pet)
        self.queue.enqueue(new_pet)
        self.undo_stack.push(pet_id)

        print(f"\n  {name} has been registered successfully! (ID: {pet_id})")

    def serve_next(self):
        print("\n  ── Serve Next Animal ──")
        if self.queue.is_empty():
            print("  The consultation queue is empty. No pets to serve.")
            return
        pet = self.queue.dequeue()
        print(f"""

    NOW SERVING                     

    ID       : {pet.pet_id:<22}     
    Name     : {pet.name:<22}       
    Breed    : {pet.breed:<22}
    Owner    : {pet.owner:<22}   
    Severity : {pet.severity:<22}
  """)

    def undo_registration(self):
        print("\n  ── Undo Last Registration ──")
        if self.undo_stack.is_empty():
            print("  Nothing to undo. Undo history is empty.")
            return
        pet_id = self.undo_stack.pop()
        removed = self.records.delete(pet_id)
        if removed:
            self.queue.remove_by_id(pet_id)
            print(f"  Registration of '{removed.name}' (ID: {pet_id}) has been undone.")
        else:
            print(f"  Pet ID {pet_id} was already removed (may have been served).")

    def delete_pet(self):
        print("\n  ── Delete Pet Record ──")
        if self.records.is_empty():
            print("  No records to delete.")
            return
        pet_id = self._get_input("  Enter Pet ID to delete: ").upper()
        removed = self.records.delete(pet_id)
        if removed:
            self.queue.remove_by_id(pet_id)
            print(f"  Pet '{removed.name}' (ID: {pet_id}) deleted successfully.")
        else:
            print(f"  Pet ID '{pet_id}' not found.")

    def search_pet(self):
        print("\n  ── Search Pet ──")
        if self.records.is_empty():
            print("  No records to search.")
            return
        pet_id = self._get_input("  Enter Pet ID to search: ").upper()
        pet = self.records.search(pet_id)
        if pet:
            print(f"""
  Pet Found
  ID       : {pet.pet_id}
  Name     : {pet.name}
  Breed    : {pet.breed}
  Owner    : {pet.owner}
  Severity : {pet.severity}
""")
        else:
            print(f" No pet found with ID '{pet_id}'.")

    def update_pet(self):
        print("\n  ── Update Pet Record ──")
        if self.records.is_empty():
            print("  No records to update.")
            return
        pet_id = self._get_input("  Enter Pet ID to update: ").upper()
        pet = self.records.search(pet_id)
        if pet is None:
            print(f"  No pet found with ID '{pet_id}'.")
            return

        print(f"  Updating record for: {pet.name} (leave blank to keep current value)")
        name = self._get_input(f"  New Pet Name  [{pet.name}]  : ", allow_blank=True) or None
        breed = self._get_input(f"  New Breed     [{pet.breed}] : ", allow_blank=True) or None
        owner = self._get_input(f"  New Owner     [{pet.owner}] : ", allow_blank=True) or None

        sev_raw = input(f"  New Severity  [{pet.severity}] (1-5, blank to skip): ").strip()
        sev = None
        if sev_raw:
            if sev_raw.isdigit() and 1 <= int(sev_raw) <= 5:
                sev = int(sev_raw)
                self.queue.remove_by_id(pet_id)
                self.records.update(pet_id, name, breed, owner, sev)
                self.queue.enqueue(pet)
                print(f" Record updated and queue position refreshed.")
                return
            else:
                print(" Invalid severity – other fields will still be saved.")

        self.records.update(pet_id, name, breed, owner, sev)
        print(f"  Record for '{pet.name}' updated successfully.")

    def display_all_pets(self):
        print("\n  ── All Registered Pets ──")
        self.records.display()

    def display_queue(self):
        print("\n  ── Consultation Queue ──")
        self.queue.display()
        print(f"\n  Total pets waiting: {self.queue.size()}")


def print_menu():
    print("""

VETERINARY CLINIC MANAGEMENT SYSTEM

[1] Register New Pet 
[2] Serve Next Animal
[3] Undo Last Registration
[4] Delete Pet Record
[5] Search Pet
[6] Update Pet Record
[7] Display All Registered Pets
[8] Display Consultation Queue
[0] Exit 
""")


def main():
    clinic = VetClinic()
    print("\n  Welcome to the Veterinary Clinic Management System!")

    while True:
        print_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            clinic.register_pet()
        elif choice == "2":
            clinic.serve_next()
        elif choice == "3":
            clinic.undo_registration()
        elif choice == "4":
            clinic.delete_pet()
        elif choice == "5":
            clinic.search_pet()
        elif choice == "6":
            clinic.update_pet()
        elif choice == "7":
            clinic.display_all_pets()
        elif choice == "8":
            clinic.display_queue()
        elif choice == "0":
            print("\n  Thank you for using the Vet Clinic System. Goodbye!\n")
            break
        else:
            print("\n  Invalid option. Please enter a number from the menu.")

        input("\n  Press Enter to continue...")

if __name__ == "__main__":
    main()