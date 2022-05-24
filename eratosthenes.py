while True:
    teto = input('Qual o teto do cálculo?')
    try:
        teto = int(teto)
    except ValueError:
        continue
    else:
        if teto < 2:
            continue
        break
crivo = {x: True for x in range(2,teto+1)}      # Números a serem crivados
for numero in crivo:
    if numero**2 > teto:          #Só precisamos testar até sqrt(teto)
        break
    if not crivo[numero]:
        continue
    for key in range(numero**2,teto+1,numero):
        if crivo[key]:
            crivo[key] = False
lista = []
for key in crivo:
    if crivo[key]:
        lista += [key]
print('Primos: ',lista)
