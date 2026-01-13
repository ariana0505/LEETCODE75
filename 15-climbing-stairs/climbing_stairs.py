n = 3
uno = 1
dos = 1
for i in range(n - 1):
    temp = uno 
    uno = dos + uno
    dos = uno
print(uno)