#To check weather a number is palindrome or not
#Take the user input
print("Enter your number")
number = int(input())
reverse = 0
temp = number
while(number>0):
    dig = number%10
    reverse = reverse *10 + dig
    number = number//10
if temp==reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")