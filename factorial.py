n = int(input("Enter an integer: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)
