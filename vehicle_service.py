"""Vehicle Service Management System (PS 73)
Concepts: OOP, Dictionaries, File Handling, CRUD
"""

import os

FILE_NAME = "services.txt"
GST_RATE = 1.18

PRICE_LIST = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "Full Service": 4500,
    "Brake Repair": 2200,
}

VALID_STATUSES = ["Pending", "In Progress", "Completed"]


class ServiceRecord:
    def __init__(self, reg_no, owner, vehicle, service, status="Pending"):
        self.reg_no = reg_no
        self.owner = owner
        self.vehicle = vehicle
        self.service = service
        self.status = status

    def calculate_cost(self):
        """Price from the price list plus 18% GST."""
        return PRICE_LIST[self.service] * GST_RATE

    def display(self):
        print(f"{self.reg_no} | {self.service} | "
              f"Cost incl. 18% GST: Rs. {self.calculate_cost():.2f} | "
              f"Status: {self.status}")

    def to_line(self):
        return "|".join([self.reg_no, self.owner, self.vehicle,
                         self.service, self.status])

    @staticmethod
    def from_line(line):
        reg_no, owner, vehicle, service, status = line.strip().split("|")
        return ServiceRecord(reg_no, owner, vehicle, service, status)


records = {}  # key: registration number, value: ServiceRecord object


def load_records():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                rec = ServiceRecord.from_line(line)
                records[rec.reg_no] = rec


def save_records():
    with open(FILE_NAME, "w") as f:
        for rec in records.values():
            f.write(rec.to_line() + "\n")


def match_service(text):
    """Return the proper service name (case-insensitive) or None."""
    for name in PRICE_LIST:
        if name.lower() == text.strip().lower():
            return name
    return None


def add_record():
    reg_no = input("Reg no: ").strip().upper()
    owner = input("Owner: ").strip()
    vehicle = input("Vehicle: ").strip()
    service_input = input("Service: ").strip()

    service = match_service(service_input)
    if service is None:
        print("Invalid service type. Choose from: "
              + ", ".join(PRICE_LIST) + ".")
        return
    if reg_no in records:
        print(f"Record for {reg_no} already exists.")
        return

    rec = ServiceRecord(reg_no, owner, vehicle, service)
    records[reg_no] = rec
    save_records()
    print("Record added.", end=" ")
    rec.display()


def view_records():
    if not records:
        print("No records found.")
        return
    for rec in records.values():
        rec.display()


def update_status():
    reg_no = input("Reg no: ").strip().upper()
    if reg_no not in records:
        print(f"No record found for {reg_no}.")
        return
    new_status = input("New status: ").strip().title()
    if new_status not in VALID_STATUSES:
        print("Invalid status. Choose from: " + ", ".join(VALID_STATUSES) + ".")
        return
    old_status = records[reg_no].status
    records[reg_no].status = new_status
    save_records()
    print(f"Status updated: {old_status} -> {new_status}")


def delete_record():
    reg_no = input("Reg no: ").strip().upper()
    if reg_no in records:
        del records[reg_no]
        save_records()
        print(f"Record for {reg_no} deleted.")
    else:
        print(f"No record found for {reg_no}.")


def main():
    load_records()
    while True:
        print("\n--- Vehicle Service Management ---")
        print("1. Add record")
        print("2. View records")
        print("3. Update status")
        print("4. Delete record")
        print("5. Exit")
        choice = input("Menu: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Enter 1-5.")


if __name__ == "__main__":
    main()
