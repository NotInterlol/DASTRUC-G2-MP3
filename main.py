""" Main Console for choosing specific options """
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
    print("0. Exit")
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
        clinic.records.display_record()

    elif choice == 6:
        clinic.queue.display_queue()

    elif choice == 7:
        clinic.pet_search()

    elif choice == 8:
        clinic.delete_pet()

    elif choice == 9:
        print("Total waiting pets:", clinic.queue.size())

    elif choice == 0:
        print(f"\n{'=' * 30}")
        print("\nExiting Program")
        print(f"\n{'=' * 30}")
        break

    # Error handler for invalid choices
    else:
        print("\nInvalid choice, please try again.")

    # Avoids Flooding in the CLI
    input(f"\nPress Enter to Continue...")
