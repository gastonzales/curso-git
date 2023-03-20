a=5/2 #esto es un ejemplo 23
print (f"hola {a}")

rica=int (input ("ingrese edad de la hembra: "))

if rica>15:
    print("con pelito")
else: 
    print("sin pelito")

# for variable in lista:
num=0
for num in range(5):
    num+=1
    print(f"{num}")

print("\n")
num=0
while num <5:
    print(num)
    num+=1

def saluda():
    print("hola ")
    

saluda()

def valor():
    return 5
val=valor()
print(val)