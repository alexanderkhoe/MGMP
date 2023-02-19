# Using Python 3
Val = input("Masukkan Angka: ") # Baris 1
myInt = int(Val)
count = 0

while myInt>1:
    if myInt%2 == 1:
        myInt = myInt//2
    else:
        myInt = myInt-1
    count=count+1               # Baris 2

print(count)                    # Baris 3
print(myInt)                    # Baris 4


