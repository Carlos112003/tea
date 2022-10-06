c = "X-DSPAM-Confidence:0.8475"

s1 = c.find(":")
print("Inicia en el Indice: "+ str(s1))

s2 = c.find("5")
print("Termina en: "+ str(s2))

final = len(c)
st = c[s1+1:final]
numero = float(st)

print(numero)
print(type(numero))