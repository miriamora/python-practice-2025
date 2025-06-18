"""first_name = input("Enter your name: ")
age = input("Enter our age: ")
print(f"Your name is {first_name} and your age is {age}.")

#write a number that takes 2 numbers and displays the sum of both numbers

a = int(input("What is the first number? :"))
b = int(input("What is the second number? :"))
sum = a + b
print(sum)"""

#write a code to help your client with money transfer. It should ask for user total amount to send in USD
#It should tell how much the receiver will receive in Cameroon --> CFA
#sending fee should be 2%
#sending rate is 655
import os
import time

print("Hello! Welcome to SafeTransfer App")
usd_amount = int(input("Enter how much you want to send - in USD: "))
print("Thank you for your input. Calculating ...")
os.system("sleep 1")
print("Thank you for your patience...")
os.system("sleep 1")
print()
sending_fee_usd = usd_amount*0.02
usd_minus_fee = usd_amount*0.98
final_sent_cfa = usd_minus_fee*655

print(f"The amount due is USD {usd_amount}")
print(f"The sending fee is USD {sending_fee_usd}")
print(f"The amount to send is USD {usd_minus_fee}")
print(f"Amount to be received is CFA {final_sent_cfa:,.2f}")
print()
proceed_to_send = input("Do you want to proceed (yes/no): ")
time.sleep(1.5)
print()
if proceed_to_send == "yes":
    print("Your funds have been transferred")
    print("We appreciate your trust!")
else:
    print("Your transfer has been cancelled")
    print("If you have any questions, please contact 1-800-524-6855")