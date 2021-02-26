# program to calculate factorial
if __name__ == '__main__':
    factorial = 1
    num = int(input())
    if (num<0):
        print("Error: Factorial of a negative number is not defined")
    elif(num == 0):
        print(1)
    else:
        for i in range (1, num+1):
            factorial = factorial*i
        print("The factorial of", num, "is", factorial)