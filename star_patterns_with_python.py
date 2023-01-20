# # ===========================================>left triangle star pattern###
for i in range(1,5):
    for j in range(1,5):
        if (j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")
# Output:
# *       
# * *     
# * * *   
# * * * * 
# ===========================================>right triangle star pattern:
for i in range(1,5):
    for j in range(1,5):
        if (j >= 5-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")
# output: 
#       * 
#     * * 
#   * * * 
# * * * * 

# ===========================================>downward right triangle star pattern:
for i in range(1,5):
    for j in range(1,5):
        if (j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
# * * * *
#   * * *
#     * *
#       *       

# ===========================================>downward left triangle star pattern:
for i in range(1,5):
    for j in range(1,5):
        if (j<=5-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
# * * * *
# * * *
# * *
# *
# ===========================================>Full triangle star pattern:

for i in range(1,5):
    for j in range(1,8):
        if (j>=5-i and j<=3+i ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
#       *
#     * * * 
#   * * * * *
# * * * * * * *
# ===========================================>Downward Full triangle star pattern:
for i in range(1,5):
    for j in range(1,8):
        if (j>=i and j<=8-i ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------------------------------")

# output:
# * * * * * * *
#   * * * * *
#     * * * 
#       *
# ===========================================>
