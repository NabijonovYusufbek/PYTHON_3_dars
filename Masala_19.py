savat = {"non": 4000, "sut": 12000, "tuxum": 18000, "yog‘": 25000}

dastlabki_summa = sum(savat.values())
print(f"Dastlabki summa: {dastlabki_summa} so‘m")

savat["shakar"] = 14000
yangi_summa = sum(savat.values())
print(f"Shakardan keyin: {yangi_summa} so‘m")