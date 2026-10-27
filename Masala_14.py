ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}

print("Ruxsat etilgan:",*ruxsat & tanlangan)
print("Ryxsat etilmagan:",*tanlangan - ruxsat)