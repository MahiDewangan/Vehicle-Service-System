# Project Summary: Vehicle Service Management System (PS 73)

## 1. Problem Statement

A service centre needs a simple program to add, view, update and delete vehicle service records. The cost of each service comes from a price list plus 18% GST, each record has a status (Pending, In Progress or Completed), and all records must be saved to a file.

## 2. Objective

To build a Python 3 console application using a `ServiceRecord` class that performs CRUD operations, stores records in a dictionary keyed by registration number, and saves them to a text file.

## 3. Approach

1. **Understand the requirements.** Identify the data (registration number, owner, vehicle, service, status), the operations (CRUD) and the rules (price list, 18% GST, valid statuses).
2. **Design the class.** `ServiceRecord` holds one record's attributes and has methods for cost calculation and display, plus two helpers to convert a record to and from a line of text.
3. **Choose the data structure.** A dictionary keyed by registration number gives fast lookup, update and delete, and prevents duplicate keys.
4. **Add file handling.** Records are loaded from `services.txt` at startup and the whole file is rewritten after every add, update or delete, so the data is never out of sync.
5. **Add validation.** Invalid service types, unknown registration numbers, duplicate registrations and invalid statuses are rejected with clear messages.
6. **Build the menu.** A `while` loop shows the menu and calls the matching function until the user exits.
7. **Test.** All four given test cases were run in order from an empty `services.txt`.

## 4. Concepts Used

| Concept | Where it is used |
|---|---|
| OOP | `ServiceRecord` class with attributes and methods |
| Dictionaries | `PRICE_LIST` (service to price) and `records` (reg no to object) |
| File handling | `load_records()` and `save_records()` using `open()` in read/write mode |
| CRUD | `add_record`, `view_records`, `update_status`, `delete_record` |
| String handling | `strip()`, `upper()`, `lower()`, `title()` to clean input |
| Control flow | Menu loop with `if/elif/else`, input validation |

## 5. Key Logic

- **Cost calculation:** `cost = base price x 1.18`. For example, Oil Change = 1500 x 1.18 = Rs. 1770.00 and Full Service = 4500 x 1.18 = Rs. 5310.00.
- **Initial status:** every new record starts as `Pending`.
- **Registration numbers** are converted to upper case, and service names are matched ignoring case, so slightly different typing still works.

## 6. Test Results

| Test Case | Scenario | Result |
|---|---|---|
| 1 | Add MH12AB1234 (Oil Change) | Pass: record added, Rs. 1770.00, Pending |
| 2 | Update MH12AB1234 to Completed | Pass: `Pending -> Completed` |
| 3a | Add with invalid service "Painting" | Pass: invalid service error shown |
| 3b | Delete non-existent KA01ZZ9999 | Pass: no record found |
| 4a | Add CG07XY4321 (Full Service) | Pass: record added, Rs. 5310.00, Pending |
| 4b | Delete CG07XY4321 | Pass: record deleted |

## 7. Conclusion

The program meets all the minimum requirements: it is written in Python 3 in a single `.py` file, uses a `ServiceRecord` class with cost calculation and display methods, stores records in a dictionary keyed by registration number, saves them to a file, supports Add, View, Update status and Delete, and passes all four test cases.

## 8. Possible Improvements

- Validate the registration number format (for example `MH12AB1234`).
- Search or filter records by status or owner.
- Store data as JSON or in a database instead of a text file.
- Add a total revenue report for completed services.
- Build a graphical interface.
