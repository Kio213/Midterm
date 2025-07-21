print("ข้อ 4.1: พิมพ์ตัวเลขจาก 0 ถึง 100")
i = 0
while i <= 100:
    print(i)
    i += 1
print("\nข้อ 4.2: พิมพ์ตัวเลขจาก 1000 ถึง 0")
i = 1000
while i >= 0:
    print(i)
    i -= 1
print("\nข้อ 4.3: หาค่าจำนวนจริงที่น้อยที่สุด")

min_value = None
while True:
    user_input = input("ป้อนจำนวนจริง (หรือพิมพ์สิ่งที่ไม่ใช่ตัวเลขเพื่อหยุด): ")
    try:
        num = float(user_input)
        if min_value is None or num < min_value:
            min_value = num
    except:
        break

if min_value is not None:
    print("จำนวนจริงที่น้อยที่สุดคือ:", min_value)
else:
    print("ไม่มีจำนวนจริงที่ป้อนเข้ามาเลย")
