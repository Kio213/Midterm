import math
hour = int(input("ชั่วโมง: "))
minute = int(input("นาที: "))
if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    total_minutes = hour *60 + minute
    if total_minutes <= 60:
        cost = 0
    else:
        remining_minutes = total_minutes - 60
        extra_hours = math.ceil(remining_minutes / 60)
        cost = extra_hours * 30
    print("ค่าจอดรถคือ", cost, "บาท")
