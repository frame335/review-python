# ตัวดำเนินการทางตรรกศาสตร์

# and , or , not
# AND = และ
# OR = หรือ
# NOT = ไม่
# คำตอบที่ได้ => จริง / เท็จ

# การประยุกต์ใช้งาน
x = (5>10) # ค่า x = bool
# y = (10==5) # ค่า y = bool
y = (10!=5)
print(x)
print(y)

# z = (5>10)  and (10!=5)
z = x and y
print(z)
print(not z)

# n = (5>10) or (10!=5)
n = x or y
print(n)

