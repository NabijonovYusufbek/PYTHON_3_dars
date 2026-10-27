ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}
Jami = 0
kop=ombor["olma"]
kam=ombor["olma"]

for meva, i in ombor.items():
    Jami += i
    if kop < i:
        kop = i
    if kam > i:
        kam = i

print(f"Eng kop: {kop}")
print(f"Eng kam; {kam}")
print(f"Jami mahsulot: {Jami}")