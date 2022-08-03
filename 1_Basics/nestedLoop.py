'''Nested Loop Trees'''

print("1)")
for i in range(7):
    for j in range(i+1):
        print("*", end='')
    print()
    
print()    

print("2)")
for i in range(7):
    for j in range(7-i):
        print("*", end='')
    print()
    

