import sys

a = int(sys.argv[1])

if a % 2 == 0:
    print('El número', a, 'es par.')
else:
    print('El número', a, 'es impar.')