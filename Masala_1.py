pul=int(input("Boshlangich pul: "))
hafta=int(input("Haftalik qo'shimcha: "))
count=0

while pul < 500000:
    pul += hafta
    count += 1

print("Kerakli hafta:",count)

   