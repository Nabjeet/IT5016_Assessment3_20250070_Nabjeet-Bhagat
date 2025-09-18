from Task3 import*

def display_requisitions():
    Date, staff_ID, staff_name, requisition_ID, total, status, approval_ref = requisition_approval()
    
    print("\nPrinting Requisitions:")
    print("Date:", Date)
    print("Requisition ID:", requisition_ID)
    print("Staff ID:", staff_ID)
    print("Staff Name:", staff_name)
    print("Total: $", total)
    print("Status:", status)
    if approval_ref:
        print("Approval Reference Number:", approval_ref)

display_requisitions()
