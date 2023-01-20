# ===========================================>left triangle with number pattern
for i in range(1,5):
    for j in range(1,5):
        if (j<=i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")
# Output:
# 1       
# 1 2     
# 1 2 3   
# 1 2 3 4 

# ===========================================>Downward inverse right triangle with number pattern

for i in range(1,6):
    k = 6-1;
    for j in range(1,6):
        if (j<=6-i):
            print(k,end=" ")
            k -= 1
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
# 5 4 3 2 1
#   4 3 2 1
#     3 2 1
#       2 1
#         1  

# ===========================================> Downward right triangle with number pattern
for i in range(1,6):
    for j in range(1,6):
        if (j>=i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
# 1 2 3 4 5 
#   2 3 4 5 
#     3 4 5 
#       4 5 
#         5 
