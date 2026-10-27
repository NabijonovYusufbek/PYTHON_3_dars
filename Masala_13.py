ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}

print("Umumiy janrlar:",*ali & vali)
print("Faqat bittasiga yoqadi:",*ali ^ vali)