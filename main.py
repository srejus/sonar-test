USER = "admin"
PASSWORD = "admin"

usr = input("Enter your Username: ")
passw = input("Enter your Password: ")

if usr == USER and PASSWORD == passw:
    print("Logged in")
else:
    print("Incorrect creds!")