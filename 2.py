print("=== ข้อ 2: ผลต่างของ m กับ n ===")
m = int(input("ป้อนค่า m: "))
n = int(input("ป้อนค่า n: "))

print("ผลต่างของ m กับ n คือ:", m - n)

print("\n=== ข้อ 3: สลับค่าระหว่าง a และ b ===")
a = int(input("ป้อนค่า a: "))
b = int(input("ป้อนค่า b: "))

a, b = b, a

print("หลังสลับค่า:")
print("a =", a)
print("b =", b)
