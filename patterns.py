##basic triangle 
#n=int(input("number of rows: "))
#for i in range(n):
#    for j in range(i + 1):
#        print("*", end="")
#    print()  
#
##inverted triangle
#for i in range(n):
#    for j in range(i,n):
#        print("*", end="")
#    print()  
    
##right sided triangle  1.increasing   
#n=int(input("number of rows: "))
#for i in range(n):
#    for j in range(i,n):
#        print(" ", end="")
#        
#    for k in range (i + 1):
#        print("*", end="")
#    print()
    
#right sided triangle 2.decreasing
n=int(input("number of rows: "))
for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    for l in range (i+1):
        print("*", end="")
    print()

    
    