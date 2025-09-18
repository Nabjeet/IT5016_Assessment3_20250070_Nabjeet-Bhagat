from Task1 import *

def requisitions_total():
    Date, staff_ID, staff_name, requisition_ID = staff_info()

    Coffee = int(input("Enter Coffee price: "))
    Paper  = int(input("Enter Paper price: "))
    Pen    = int(input("Enter Pen price: "))

    total = Coffee + Paper + Pen

    print("\nRequisition Summary:")
    print("Date:", Date)
    print("Staff ID:", staff_ID)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_ID)
    print("Total Cost:", total)

    return Date, staff_ID, staff_name, requisition_ID, total

requisitions_total()
