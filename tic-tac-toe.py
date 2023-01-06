print("*********************************************************************")
print("*********************************************************************")
print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~TIC TAC TOE~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
print("*********************************************************************")
print("*********************************************************************")


print(" ")
print(" ")

#winning condition:
#a[0]==a[1] && a[0]==a[2]
#a[3]==a[4] && a[3]==a[5]
#a[6]==a[7] && a[6]==a[8]
#a[0]==a[3] && a[0]==a[6]
#a[1]==a[4] && a[4]==a[7]
#a[2]==a[5] && a[2]==a[8]
#a[0]==a[4] && a[0]==a[8]
#a[6]==a[4] && a[6]==a[2]




a = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])
print("************************************************")

t1 = int(input("Enter the number of the box where you want to put cross(0 - 8): "))
a[t1] = "x"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

print("************************************************")


t2 = int(input("Enter the number of the box where you want to put circle(0 - 8): "))

while t2 == t1:
    print("Your typed number is invalid")
    t2 = int(input("Choose an vacant cell: "))
if t2 != t1 :
    a[t2] = "O"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

print("************************************************")


t3 = int(input("Enter the number of the box where you want to put cross(0 - 8): "))

while t3==t1 or t3==t2:
    print("Your typed number is invalid")
    t3 = int(input("Choose an vacant cell: "))
if t3 != t1 :
    a[t3] = "x"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

print("************************************************")

t4 = int(input("Enter the number of the box where you want to put circle(0 - 8): "))

while t4==t1 or t4==t2 or t4==t3:
    print("Your typed number is invalid")
    t4 = int(input("Choose an vacant cell: "))
if t4 != t1 :
    a[t4] = "O"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

print("************************************************")

t5 = int(input("Enter the number of the box where you want to put cross(0 - 8): "))

while t5==t1 or t5==t2 or t5==t3 or t5==t4:
    print("Your typed number is invalid")
    t5 = int(input("Choose an vacant cell: "))
if t5 != t1 :
    a[t5] = "x"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

if a[0]==a[1] and a[0]==a[2]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[3]==a[4] and a[3]==a[5]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[6]==a[7] and a[6]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[6],"'")
    exit() 
elif a[0]==a[3] and a[0]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[1]==a[4] and a[1]==a[7]:
    print("The match has ended")
    print("The winner is the player who had '",a[1],"'")
    exit() 
elif a[2]==a[5] and a[2]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 
elif a[0]==a[4] and a[0]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[2]==a[4] and a[2]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 

print("************************************************")

t6 = int(input("Enter the number of the box where you want to put circle(0 - 8): "))

while t6==t1 or t6==t2 or t6==t3 or t6==t4 or t6==t5:
    print("Your typed number is invalid")
    t6 = int(input("Choose an vacant cell: "))
if t6 != t1 :
    a[t6] = "O"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])


if a[0]==a[1] and a[0]==a[2]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[3]==a[4] and a[3]==a[5]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[6]==a[7] and a[6]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[6],"'")
    exit() 
elif a[0]==a[3] and a[0]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[1]==a[4] and a[1]==a[7]:
    print("The match has ended")
    print("The winner is the player who had '",a[1],"'")
    exit() 
elif a[2]==a[5] and a[2]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 
elif a[0]==a[4] and a[0]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[2]==a[4] and a[2]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 



print("************************************************")

t7 = int(input("Enter the number of the box where you want to put cross(0 - 8): "))

while t7==t1 or t7==t2 or t7==t3 or t7==t4 or t7==t5 or t7==t6:
    print("Your typed number is invalid")
    t7 = int(input("Choose an vacant cell: "))
if t7 != t1 :
    a[t7] = "x"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

if a[0]==a[1] and a[0]==a[2]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[3]==a[4] and a[3]==a[5]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[6]==a[7] and a[6]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[6],"'")
    exit() 
elif a[0]==a[3] and a[0]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[1]==a[4] and a[1]==a[7]:
    print("The match has ended")
    print("The winner is the player who had '",a[1],"'")
    exit() 
elif a[2]==a[5] and a[2]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 
elif a[0]==a[4] and a[0]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[2]==a[4] and a[2]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 

print("************************************************")

t8 = int(input("Enter the number of the box where you want to put circle(0 - 8): "))

while t8==t1 or t8==t2 or t8==t3 or t8==t4 or t8==t5 or t8==t6 or t8==t7:
    print("Your typed number is invalid")
    t8 = int(input("Choose an vacant cell: "))
if t8 != t1 :
    a[t8] = "O"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

if a[0]==a[1] and a[0]==a[2]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[3]==a[4] and a[3]==a[5]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[6]==a[7] and a[6]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[6],"'")
    exit() 
elif a[0]==a[3] and a[0]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[1]==a[4] and a[1]==a[7]:
    print("The match has ended")
    print("The winner is the player who had '",a[1],"'")
    exit() 
elif a[2]==a[5] and a[2]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 
elif a[0]==a[4] and a[0]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[2]==a[4] and a[2]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 


print("************************************************")

t9 = int(input("Enter the number of the box where you want to put cross(0 - 8): "))

while t9==t1 or t9==t2 or t9==t3 or t9==t4 or t9==t5 or t9==t6 or t9==t7 or t9==t8:
    print("Your typed number is invalid")
    t9 = int(input("Choose an vacant cell: "))
if t9 != t1 :
    a[t9] = "x"

print(a[0],"|",a[1],"|",a[2])
print("__ ___ __")
print(a[3],"|",a[4],"|",a[5])
print("__ ___ __")
print(a[6],"|",a[7],"|",a[8])

if a[0]==a[1] and a[0]==a[2]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[3]==a[4] and a[3]==a[5]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[6]==a[7] and a[6]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[6],"'")
    exit() 
elif a[0]==a[3] and a[0]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[3],"'")
    exit() 
elif a[1]==a[4] and a[1]==a[7]:
    print("The match has ended")
    print("The winner is the player who had '",a[1],"'")
    exit() 
elif a[2]==a[5] and a[2]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 
elif a[0]==a[4] and a[0]==a[8]:
    print("The match has ended")
    print("The winner is the player who had '",a[0],"'")
    exit() 
elif a[2]==a[4] and a[2]==a[6]:
    print("The match has ended")
    print("The winner is the player who had '",a[2],"'")
    exit() 


print("************************************************")

print("The match is Draw")






