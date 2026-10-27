A = (4, 7)
B = (6, 8)
temp = 0
temp1 = 0

for son in A:
    temp += son

for son1 in B:
    temp1 += son1

print("A yig'indisi:",temp)
print("B yig'indisi:",temp1)

if temp > temp1:
    print("A katta")
elif temp < temp1:
    print("B katta")
else:
    print("Yig'indilari teng")


