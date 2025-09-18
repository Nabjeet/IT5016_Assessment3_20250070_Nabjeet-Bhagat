counter = 1  

def staff_info():
    global counter
    Date = input("Enter Date (DD/MM/YYYY): ")
    staff_ID = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    
    requisition_ID = 10000 + counter
    counter += 1

    print("\nPrinting Staff Information:")
    print("Date:", Date)
    print("Staff ID:", staff_ID)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_ID)

    return Date, staff_ID, staff_name, requisition_ID


# ---- call the function here ----
staff_info()
