import time
import math

number = int(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

time.sleep(delay / 1000)

sqrt_value = math.sqrt(number)

print(f"Square root of {number} after {delay} milliseconds is {sqrt_value}")
