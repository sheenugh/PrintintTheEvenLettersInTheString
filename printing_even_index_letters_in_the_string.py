

# ----- PSEUDO CODE -----
# - Printing the sentence as "original string is ...."
print("The original string is 'Sheena Mae.'")
print("\n")

# - Printing the sentence "printing only even index number"
print("Printing the even index letters in the string.")

# ------ ACTUAL CODES -----
name = "Sheena Mae"
for i in range(0, 10, 2):
    print(name[i])
    
    
print("\n")
print("---------------")
print("OR")
print("---------------")
print("\n")


for i in range(10):
    if (i%2) == 0:
        print(name[i])
        
# Thus the even index letters in the string are S,e,n,,<space>, and a.
