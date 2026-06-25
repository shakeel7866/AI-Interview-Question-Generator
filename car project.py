# Car Parking Management System

cars = []
fee = 100

while True:
    print("\nCAR PARKING MANAGEMENT SYSTEM ")
    print("1. Add/Park Car")
    print("2. View Parking")
    print("3. Remove Parking")
    print("4. Total Income")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        car = input("Enter car number: ")
        cars.append(car)
        print("Car parked successfully!")

    elif choice == "2":
        if len(cars) == 0:
            print("Parking is empty.")
        else:
            print("\nParked Cars:")
            for i, car in enumerate(cars, start=1):
                print(f"{i}. {car}")

    elif choice == "3":
        car = input("Enter car number to remove: ")
        if car in cars:
            cars.remove(car)
            print("Car removed successfully!")
        else:
            print("Car not found.")

    elif choice == "4":
        total_cars = len(cars)
        income = total_cars * fee
        print(f"\nTotal cars parked: {total_cars}")
        print(f"Total income = {fee} x {total_cars} = {income}")

    elif choice == "5":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")