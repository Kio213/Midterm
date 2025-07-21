numbers = []

for i in range(5):
    num = int(input(f"ป้อนตัวเลขตัวที่ {i+1}: "))
    numbers.append(num)

total = sum(numbers)

average = total / len(numbers)

print("ผลรวม =", total)
print("ค่าเฉลี่ย =", average)
