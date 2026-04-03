a=""
b=""
for i in range (2,10):
    a= a+("# %d단 # " %i)
print(a)
for j in range (1,10):
    for k in range (2,10):
        print("%dx%d=%2d" %(k,j,k*j),end="\t")
    print()
    


