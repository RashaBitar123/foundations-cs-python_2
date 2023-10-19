# Write a function that takes an integer from the user and calculates its factorial.

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n - 1)
n = input("Enter a number to calculate its factorial: ")
print(n+"! =",factorial(int(n))) 

# Write a function that takes an integer as an input from the user and finds all its divisors and stores them in a list.

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
num = input("Enter a number to find its divisors: ")
print("Divisors of "+num+" are",divisors(int(num)))

# Write a function called reverseString that takes a string as input from the user and returns the string reversed.

def reverseString(s):
    return s[::-1]
input_string = input("Enter a string to reverse: ")  
print("Reversed String: ",reverseString(input_string))

# Write a function that takes a list of integers as input from the user and returns a new list containing only the even numbers from the original list, in the same order.

def evenNumbers(n):
    evenNumbers = []
    for i in n:
        if i % 2 == 0:
            evenNumbers.append(i)
    return evenNumbers
  
input_string = input("Enter a list of integers separated by spaces: ")
input_list = [int(item) for item in input_string.split()]
print("Input List:", input_list)
print("Even Numbers:", evenNumbers(input_list))

# Write a function that takes a string as input and checks whether it meets the requirements for a strong password.A strong password should be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character (a special character is either #, ?, !, $).

def check_password_strength(password):
  if (len(password) >= 8) and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "#?!$" for c in password):
      return "Strong password"
  else:
      return "Weak password"

input_pass = input("Enter a password: ")  
print(check_password_strength(input_pass))


# Write a function that takes a string as input andchecks whether it is a valid IPv4 address. A valid IPv4 address is a string of four numbers separated by periods, where each number is between 0 and 255. 
def check_ipv4(ip):
    
        ip = ip.split(".")
        if len(ip) != 4:
            return False
        for i in ip:
            if not i.isdigit() or int(i) < 0 or int(i) > 255:
                return False
        return True

ip = input("Enter an IPv4 address: ")
print(check_ipv4(ip))

  