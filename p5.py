frase = input('Ingrese una organizacion: ')
n = len(frase)
frase = frase.upper()
i = 0
z = frase[i]
i = 1
while not(i>=(n-1)):
    if (frase[i]==' ' and  not(frase[i+1]=='D')):
        if not(frase[i+1]=='Y'):
            z = "Su acronimo es: "+ z + frase[i+1]
    i = i + 1
print(z)