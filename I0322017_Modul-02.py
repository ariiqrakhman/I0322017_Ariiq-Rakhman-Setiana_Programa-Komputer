nama = input("Masukkan nama: ")
print("Halo, " + nama)

# challenge 1
# masukkan id pada input sesuai dengan tipe data yang sudah ditentukan
id = int(input("Masukkan ID: "))
print("ID: " + str(id))

print ("=====================")
nama = "POSI"
tahun = 2020
print(type(nama))
print(type(tahun))
print(type("TI UNS"))

print ("=====================")
a = 10
b = 5
print(a + b)
print(a - b)

print ("=====================")
x = 10
user = int(input("Enter a number: "))

while user != x:
    if user > x:
        print("Too high")
    elif user < x:
        print("Too low")
    else:
        print("Number correct")
    user = int(input("Enter a number: "))
    
print ("=====================")
# challenge 2
x =5
y = 3

command = 5(input("Masukkan command: "))
if command == 1:
    print(f"{x} pangkat {5} = {x ** y}") # output seharusnya 1000
else:
    print("Command tidak dikenali")