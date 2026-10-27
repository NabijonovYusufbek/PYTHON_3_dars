xarajat=int(input("Xarajat: "))
count=0
temp = xarajat
while xarajat != 0:
    count += 1
    xarajat=int(input("Xarajat: "))
    temp += xarajat

OrtachaQimat = temp / count
print("Jami:",temp)
print("Kiritilgan xarajatlar soni:",count)
print(f"O'rtacha qiymat: {OrtachaQimat:.2f}")