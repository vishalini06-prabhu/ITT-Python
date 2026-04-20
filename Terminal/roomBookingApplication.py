class HotelRoom:
    def __init__(self, roomnumber, roomtype, price):
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.price = price
        self.isbooked = False
        self.guestname = None

    def getroomnumber(self):
        return self.roomnumber

    def getroomtype(self):
        return self.roomtype

    def getprice(self):
        return self.price

    def isbookedstatus(self):
        return self.isbooked

    def getguestname(self):
        return self.guestname

    def setguestname(self, name):
        self.guestname = name

    def setisbooked(self, status):
        self.isbooked = status

    def bookroom(self, guestname):
        try:
            if self.isbooked:
                raise Exception(f"Room {self.roomnumber} is already booked.")
            self.setguestname(guestname)
            self.setisbooked(True)
            print(f"Room {self.roomnumber} successfully booked for {guestname}.")
            print("Thank You for Booking. Have a happy stay.")
        except Exception as e:
            print("Booking failed:", e)

    def checkout(self):
        try:
            if not self.isbooked:
                raise Exception(f"Room {self.roomnumber} is not currently booked.")
            print(f"{self.guestname} has checked out of Room {self.roomnumber}.")
            self.setguestname(None)
            self.setisbooked(False)
        except Exception as e:
            print("Checkout failed:", e)

    def showstatus(self):
        status = "Booked" if self.isbooked else "Available"
        print(f"Room {self.roomnumber} ({self.roomtype}) - {status}")

    def displaydetails(self):
        print("Room Number:", self.roomnumber)
        print("Room Type:", self.roomtype)
        print("Price:", self.price)
        print("Booking Status:", "Booked" if self.isbooked else "Available")
        if self.isbooked:
            print("Guest Name:", self.guestname)
        print("-" * 30)

print("---------------Welcome to Lini Hotel-----------------")
rooms = [
    HotelRoom(101, "Standard", 3000),
    HotelRoom(102, "Standard", 3200),
    HotelRoom(103, "Standard", 3500),
    HotelRoom(104, "Deluxe", 4000),
    HotelRoom(105, "Deluxe", 4500),
    HotelRoom(106, "Deluxe", 4800),
    HotelRoom(107, "Executive", 6000),
    HotelRoom(108, "Executive", 6300),
    HotelRoom(109, "Suite", 8000),
    HotelRoom(110, "Suite", 8500),
]

def findroombynumber(number):
    for room in rooms:
        if room.getroomnumber() == number:
            return room
    return None

while True:
    print("\n--- Hotel Management System ---")
    print("1. Show all room status")
    print("2. Book a room")
    print("3. Checkout")
    print("4. Show room details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        for r in rooms:
            r.showstatus()

    elif choice == '2':
        print("\n--- Please read the booking rules ---")
        print("1. Valid ID proof is required at check-in.")
        print("2. Check-in time is 12:00 PM, and check-out is 11:00 AM.")
        print("3. Pets are not allowed.")
        print("4. Smoking is strictly prohibited inside the room.")
        print("5. Full payment must be made at the time of check-in.")
        print("---------------------------------------------")

        try:
            num = int(input("Enter room number to book: "))
            room = findroombynumber(num)
            if room:
                if room.isbookedstatus():
                    print("This room is already booked.")
                    continue

                print(f"The price for Room {room.getroomnumber()} is Rs.{room.getprice()}")
                confirm = input("Do you want to proceed with the payment and booking? (yes/no): ").strip().lower()
                if confirm == "yes":
                    name = input("Enter guest name: ")
                    room.bookroom(name)
                else:
                    print("Booking cancelled.")
            else:
                print("Invalid room number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '3':
        try:
            num = int(input("Enter room number to checkout: "))
            room = findroombynumber(num)
            if room:
                room.checkout()
            else:
                print("Invalid room number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '4':
        try:
            num = int(input("Enter room number to view details: "))
            room = findroombynumber(num)
            if room:
                room.displaydetails()
            else:
                print("Invalid room number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '5':
        print("Thank you for Visiting Lini Hotel! . Have a great day!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
