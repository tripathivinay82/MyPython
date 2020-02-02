# -*- coding: utf-8 -*-
#var = input("Enter Network with Mask:")
var="204.17.5.0/27"
print("User Entered Network/Mask:", var)

var = var.split(".")
list1=["0", "0","0","0"]
list1[0]=var[0]
list1[1]=var[1]
list1[2]=var[2]
list1[3]=var[3]
ipx=list1[3].split("/")
list1[3]=ipx[0]
mask=ipx[1]

print("Final List Based on User Input:",list1)

print("First Oct:",list1[0],"Second Oct:",list1[1], "Third Oct:",list1[2], "Fourth Oct:",list1[3])
print("Mask:", mask)


uhost=32-int(mask)
uhost=2**uhost
print("Available Host:",uhost)
print("Avilable Usable Host:",uhost-2)
psub=256/int(uhost)
print("Total Subnets Possible:",int(psub))

#for class d network
sbits=int(mask)-24
print("Total bits available for subnetting:", sbits)    
print("Printing all available subnets and Host IPs")

x=1
y=1
c1=int(list1[3])

while psub >= x:
    #Get the Subnet
    list1.insert(3,str(c1))
    sub1=list1[0] +  "." + list1[1] + "." + list1[2] + "." + list1[3]
    print("Subnet IP:",sub1)

    while uhost >= y:
        if y >= uhost-1:
            y=1
            break;
        c2=int(list1[3])+1
        list1.insert(3,str(c2))
        sub2=list1[0] +  "." + list1[1] + "." + list1[2] + "." + list1[3]
        print("Usable Host IP:",sub2)
        y=y+1      
    c1=c1+uhost
    print("x",x)
    x=x+1
        

