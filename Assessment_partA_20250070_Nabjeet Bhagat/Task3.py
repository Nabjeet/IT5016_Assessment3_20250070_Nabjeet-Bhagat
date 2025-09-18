from Task2 import *

def requisition_approval():
    Date, staff_ID, staff_name, requisition_ID, total = requisitions_total()

    status = "Pending"
    approval_ref = None  

    if total < 500:
        status = "Approved"
        approval_ref = staff_ID + str(requisition_ID)[-3:]
    else:
        status = "Not Approved"

    print(f"\nTotal: $ {total}")
    print(f"Status: {status}")
    if approval_ref:
        print(f"Approval Reference Number: {approval_ref}")

    return Date, staff_ID, staff_name, requisition_ID, total, status, approval_ref

requisition_approval()
