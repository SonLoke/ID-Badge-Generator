print("Please, enter the following info:")
firstname=input("First Name: ")
lastname=input("Last Name: ")
email=input("Email Address: ")
phone=input("Phone Number: ")
job=input("Job Title: ")
id=input("ID Number: ")

hair=input("Hair Color: ")
eyes=input("Eye Color: ")
month=input("Starting Month: ")
training=input("Did you have Advanced Training?: ")

#output=f"\n-----------------------------------\n{lastname.upper()}, {firstname.capitalize()}\n{job.title()}\nID: {id}\n\n{email}\n{phone}\n\nHair: {hair.title()}     Eyes: {eyes.capitalize()}\nMonth: {month.capitalize()}     Training: {training.capitalize()}\n-----------------------------------"
#print(output)

print("\n-----------------------------------")
print(f"{lastname.upper()}, {firstname.capitalize()}")
print(f"{job.title()}")
print(f"ID: {id}")
print(f"\n{email}")
print(f"{phone}")
print(f"\nHair: {hair.title():<15} Eyes: {eyes.title()}")
print(f"Month: {month.capitalize():<14} Training: {training.capitalize()}")
print("-----------------------------------")
