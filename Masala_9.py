natijalar = (12, 18, 15)
katta = natijalar[0]
temp = 0

for natija in natijalar:
    temp += natija
    if katta < natija:
        katta = natija

print("Jami:",temp)
print("Eng yaxshi urinish",natijalar.index(max(natijalar)))
print("Eng yaxshi natija:",katta)