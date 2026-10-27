ballar = (78, 92, 65, 88, 74)
max=ballar[0]
min=ballar[1]
temp=0
sum=0

for ball in ballar:
    if max < ball:
        max = ball
    if min > ball:
        min = ball
    temp += ball
    sum += 1

print(f"Eng yuqori: {max}")
print(f"Eng past: {min}")
print(f"O'rtacha: {temp / sum:.1f}")
    
