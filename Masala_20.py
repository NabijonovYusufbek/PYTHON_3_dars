ovozlar = {"Ali": "Python", "Vali": "JavaScript", "Madina": "Python", "Jasur": "C++", "Aziza": "Python", "Sardor": "JavaScript"}

til_ovozlari = {}
for til in ovozlar.values():
    til_ovozlari[til] = til_ovozlari.get(til, 0) + 1
golib = ""
max_ovoz = 0
for til, ovoz in til_ovozlari.items():
    print(f"{til}: {ovoz} ta ovoz")
    
    if ovoz > max_ovoz:
        max_ovoz = ovoz
        golib = til

print(f"G'olib: {golib}")