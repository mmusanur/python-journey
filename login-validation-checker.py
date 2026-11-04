user_name = input("enter your username ")
user_password = input("enter your password")

correct_username = "admin"
correct_password = "1234"

login_success = user_name == correct_username and user_password == correct_password
print("Login Successfull" ,login_success)