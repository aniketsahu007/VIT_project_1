a = int(input("Enter the number you want to print upto :   "))
num = [ ]
for i in range(1,a):
    if i <= 9:
        num.append(i)
    else:
        b = str(i)
        for j in b:
            m =  int(j)
            num.append(m)
print(num)
o = int( input("enter the digit you want to find : "))
n = num[o]
print(f"The digit at {o} place is : {n} \nand it comes from  the number  : ", end=" ")
if o%2 == 0 : 
    g,p = num[o] , num[o+1]
    print(g,end="")
    print(p)
else: 
    g,p = num[o] , num[o-1]
    print(p,end="")
    print(g)