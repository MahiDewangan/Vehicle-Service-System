# Vehicle Service Management System

**PS No:** 73  
**Course:** B.Tech Computer Science and Engineering  
**University:** Rungta International Skills University, School of Computer Science and Engineering  
**Language:** Python 3  
**Concepts:** OOP, Dictionaries, File Handling, CRUD

## About the Project

A console-based Python program for a vehicle service centre. It lets the user add, view, update and delete vehicle service records. Each record is stored as an object of the `ServiceRecord` class, kept in a dictionary keyed by registration number, and saved to a text file (`services.txt`) so data persists between runs.

The service cost is taken from a fixed price list and increased by 18% GST.

| Service | Price (before GST) | Cost with GST (x 1.18) |
|---|---|---|
| Oil Change | Rs. 1500 | Rs. 1770.00 |
| Wheel Alignment | Rs. 800 | Rs. 944.00 |
| Full Service | Rs. 4500 | Rs. 5310.00 |
| Brake Repair | Rs. 2200 | Rs. 2596.00 |

## Features

- **Add** a service record (registration number, owner, vehicle type, service type)
- **View** all service records with the GST-inclusive cost
- **Update** the status of a record: `Pending`, `In Progress` or `Completed`
- **Delete** a record by registration number
- Input validation for invalid service types, unknown registration numbers and duplicate records
- Records saved to `services.txt` after every change and reloaded at startup

## Project Structure

```
.
├── vehicle_service.py   # main program
├── services.txt         # data file (created automatically)
├── README.md
└── SUMMARY.md           # project summary / report
```

## How the Code Is Organised

| Part | Purpose |
|---|---|
| `PRICE_LIST`, `GST_RATE`, `VALID_STATUSES` | Constants for prices, tax and allowed statuses |
| `class ServiceRecord` | Holds one record. Methods: `calculate_cost()`, `display()`, `to_line()`, `from_line()` |
| `records = {}` | Dictionary of all records, key = registration number |
| `load_records()` / `save_records()` | File handling (read at start, write after each change) |
| `add_record()`, `view_records()`, `update_status()`, `delete_record()` | CRUD operations |
| `main()` | Menu loop |

## How to Run

1. Install Python 3 (https://www.python.org/downloads/).
2. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
3. Run the program:
   ```bash
   python vehicle_service.py
   ```
4. Choose an option from the menu:
   ```
   1. Add record
   2. View records
   3. Update status
   4. Delete record
   5. Exit
   ```

> To repeat the test cases from scratch, delete `services.txt` before running.

## Test Cases

Run in order, starting from an empty `services.txt`.

**Test Case 1: Normal input**

| Input | Output |
|---|---|
| Menu: Add record, Reg no: `MH12AB1234`, Owner: Rohit Patil, Vehicle: Car, Service: Oil Change | `Record added. MH12AB1234 \| Oil Change \| Cost incl. 18% GST: Rs. 1770.00 \| Status: Pending` |

**Test Case 2: Boundary / minimum input**

| Input | Output |
|---|---|
| Menu: Update status, Reg no: `MH12AB1234`, New status: Completed | `Status updated: Pending -> Completed` |

**Test Case 3: Invalid input**

| Input | Output |
|---|---|
| (a) Add record, `MH14ZZ0001`, Asha Nair, Car, service Painting | `Invalid service type. Choose from: Oil Change, Wheel Alignment, Full Service, Brake Repair.` |
| (b) Delete record, `KA01ZZ9999` | `No record found for KA01ZZ9999.` |

**Test Case 4: Different valid scenario**

| Input | Output |
|---|---|
| (a) Add record, `CG07XY4321`, Amit Das, Bike, Full Service | `Record added. CG07XY4321 \| Full Service \| Cost incl. 18% GST: Rs. 5310.00 \| Status: Pending` |
| (b) Delete record, `CG07XY4321` | `Record for CG07XY4321 deleted.` |

All four test cases pass.

## Sample Data File Format

Each line of `services.txt` holds one record, fields separated by `|`:

```
MH12AB1234|Rohit Patil|Car|Oil Change|Completed
```

## Author

- **Name:** _your name_
- **Enrollment No.:** _your enrollment number_
- **Program:** B.Tech CSE, Rungta International Skills University
