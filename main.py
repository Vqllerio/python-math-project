from Fitur.division import calculate_division
from Fitur.sum import calculate_sum

A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

print("1. Sum\n4. Division")
choice = int(input("Which operation do you want to do?")


if choice == 1:
  print(f"Sum : {calculate_sum(A,B)}")
division_result = calculate_division(A, B)
print(f"division result is: {division_result}")

