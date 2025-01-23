from Fitur.division import calculate_division
from Fitur.sum import calculate_sum
from Fitur.difference import calculate_difference
from Fitur.Product import calculate_product

while True:
  A = int(input("Masukkan A: "))
  B = int(input("Masukkan B: "))

  print("1. Sum\n2. Difference\n3. Product\n4. Division\n5. Stop")
  choice = int(input("Which operation do you want to do?"))

  if choice == 1:
    print(f"Sum result is : {calculate_sum(A,B)}")
  elif choice == 2:
    print(f"Difference result is : {calculate_difference(A, B)}")
  elif choice == 3:
    print(f"Product result is : {calculate_product(A,B)}")
  elif choice == 4:
    print(f"Division result is : {calculate_division(A,B)}")
  elif choice == 5:
    break