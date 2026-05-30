from vetclinic import VetClinic

clinic = VetClinic()

while True:
    print("\n===== Veterinary Clinic System =====")
    print("\n1. Register Pet")
    print("2. Serve Pet")
    print("3. Update Pet")
    print("4. Undo Recently Registered Pet")
    print("5. Display Pet Records")
    print("6. Display Queue")
    print("7. Search Pet")
    print("8. Delete Pet")
    print("9. Total Waiting Pets")
    print("10. Exit")
    print("\n====================================")

    choice = clinic.int_input("\nEnter Choice: ")

    if choice == 1:
        clinic.pet_registry()
    elif choice == 2:
        clinic.serve_pet()

    elif choice == 3:
        clinic.update_pet()

    elif choice == 4:
        clinic.undo_registry()

    elif choice == 5:
        clinic.records.display()

    elif choice == 6:
        clinic.queue.peek()

    elif choice == 7:
        print("Input X to return to menu")
        while True:
            pet_id = clinic.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                break

            # Searches similar Pet ID
            pets = clinic.records.search(pet_id)

            if pets:
                print(f"\n{'=' * 100}")
                print(f"\nPet ID: {pets.pet_id} | "
                      f"Pet Name: {pets.pet_name} | "
                      f"Breed: {pets.breed} | "
                      f"Owner Name: {pets.owner_name} | "
                      f"Severity Level: {pets.severity} | ")
                print(f"\n{'=' * 100}")
                break

            else:
                print("Pet not found.")

    elif choice == 8:
        print("Input X to return to menu")
        while True:
            pet_id = clinic.string_input("Enter Pet ID: ")
            if pet_id.lower() == "x":
                break

            if clinic.records.delete(pet_id):
                clinic.queue.remove(pet_id)
                print(f"\n{'=' * 30}")
                print("\nSuccessfully deleted pet")
                print(f"\n{'=' * 30}")
                break

            else:
                print(f"\n{'=' * 30}")
                print("\nPet not found.")
                print(f"\n{'=' * 30}")

    elif choice == 9:
        print("Total waiting pets:", clinic.queue.size())

    elif choice == 10:
        print(f"\n{'=' * 30}")
        print("\nExiting Program")
        print(f"\n{'=' * 30}")
        break

    # Error handler for invalid choices
    else:
        print("\nInvalid choice, please try again.")

    # Avoids Flooding in the CLI
    print(f"\n{'=' * 36}")
    input(f"\nPress Enter to Continue...")
