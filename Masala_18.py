shaharlar = {"Toshkent": 3000000, "Farg'ona": 300000, "Samarqand": 600000}

kop_shaharlar = []
eng_kop_shahar = ""
eng_kop_aholi = 0

for shahar, aholi in shaharlar.items():
    if aholi > 500000:
        kop_shaharlar.append(shahar)
    if aholi > eng_kop_aholi:
        eng_kop_aholi = aholi
        eng_kop_shahar = shahar

print(f"500 000 dan ko'p: {', '.join(kop_shaharlar)}")
print(f"Eng ko'p aholi: {eng_kop_shahar}")
