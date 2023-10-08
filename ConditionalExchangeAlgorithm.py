
a = float(input("Veuillez entrer la première donnée (a) : "))
b = float(input("Veuillez entrer la deuxième donnée (b) : "))
c = 0.0  

if (a > 0 and b > 0) or (a < 0 and b < 0):
    c = a
    a = b
    b = c
else:
    c = a
    a = a + b
    b = c * b


print("Après la modification :")
print("a =", a)
print("b =", b)
