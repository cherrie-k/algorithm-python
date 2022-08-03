'''
Basic Loop Problems:
 1) print the odd integers between 1 to N
 2) print the sum of integers between 1 to N
 3) print the divisor(약수) of N
'''
print("1) Print the odd integers between 1 to N")
N = int(input("Enter a positive integer: "))

for i in range(1, N+1):
    if (i % 2 == 1):
        print(i)
    else:
        continue

print()

print("2) Print the sum of integers between 1 to N")
N = int(input("Enter a positive integer: "))
val = 0
for i in range(1, N+1):
    val += i
print(val)

print()

print("3) Print the divisor(약수) of N")
N = int(input("Enter a positive integer: "))
val = 0
for i in range(1, N+1):
    if N%i==0:
        print(i, end = ' ')

print()