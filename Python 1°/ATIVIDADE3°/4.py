n = int(input("Informe um Numero: "))
m = int(input("Informe um Segundo Numero: "))
o = int(input("Informe um Teçeiro Numero: "))

if n > m and o:
    print(f"O numero {n} é o Maior")
elif m > n and o:
    print(f"O numero {m} é o Maior")
else:
    print(f"O numero {o} é o Maior")