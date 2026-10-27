baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}
count = 0
Jami = 0
kop = baholar["Ali"]

for odam, baho in baholar.items():
    Jami += baho
    count += 1
    if kop < baho:
        kop = baho

print(f"Yuqori ball olganlar: {kop}")
print(f"O'rtacha ball: {Jami / count:.2f}")