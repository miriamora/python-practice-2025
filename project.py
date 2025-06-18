#project 1
"""
email_address=input("What is your email address?: ")

if "@" in email_address:
    print("You have entered a valid email address")

else:
    print ("Email address is not valid")

#project 2

user_name=input("What is your username?: ")
pass_word=input("What is your password?: ")

if user_name == "admin" and pass_word == "admin":
    print("You have signed in sucessfully!")

else:
    print ("Wrong credentials, please try again")
"""
#project 3
zip_code=input("What is your zip code?: ").strip()

if len(zip_code) == 5 and zip_code.isdigit():
    print("You have entered a valid zip code")

else:
    print ("Zip code is not valid")
