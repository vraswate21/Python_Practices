age = int(input("Enter your age: "))
print("You are eligbile for ")
print("Birth Certificate \nAadhaar Card \nPassport \nPAN Card \nBank/Post Office Passbook")
if age >= 18:
    print("Voter ID Card (EPIC) \nDriving License")
if age >= 60:
    print("Senior Citizen Card")