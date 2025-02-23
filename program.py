# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Calculate the sum of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 3. Find the square of a number.
num = int(input("Enter a number: "))
print("Square:", num ** 2)

# 4. Accept the user's name and greet them with it.
name = input("Enter your name: ")
print("Hello, " + name + "!")

# 5. Check whether a number is even or odd.
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# 6. Return a new list with unique elements of the first list.
lst = input("Enter list elements separated by space: ").split()
lst = [int(i) for i in lst]  # Converting to integers without map()
unique_lst = list(set(lst))
print("Unique elements:", unique_lst)

# 7. Convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 8. Calculate the area of a circle.
import math
radius = float(input("Enter the radius of the circle: "))
print("Area:", math.pi * radius ** 2)

# 9. Reverse a given string.
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# 10. Check if a number is a prime number.
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print(num, "is a prime number" if is_prime else "is not a prime number")
else:
    print(num, "is not a prime number")

# 11. Calculate the factorial of a number.
import math
num = int(input("Enter a number: "))
print("Factorial:", math.factorial(num))

# 12. Find the largest item from a given list.
lst = input("Enter list elements separated by space: ").split()
lst = [int(i) for i in lst]  # Converting to integers without map()
print("Largest item:", max(lst))

# 13. Check whether a number is in a given range.
num = int(input("Enter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
print(f"{num} is in range" if start <= num <= end else f"{num} is not in range")

# 14. Count uppercase and lowercase letters in a string.
s = input("Enter a string: ")
upper_count = sum(1 for c in s if c.isupper())
lower_count = sum(1 for c in s if c.islower())
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)



