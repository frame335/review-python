# โครงสร้างแบบควบคุมเลือก if...else

'''
โครงสร้างควบคุม (Control Structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ
'''

'''
if boolean expression:
    statement
'''

age = int(input("ป้อนอายุของคุณ :"))
name = "John Tik"

# print(type(age==15))
# print(name=="John Tik")

# if age >= 15:
#     print("คำนำหน้าเป็น นาย/นางสาว")
#     print("จบโปรแกรมด้านใน if")

# print("จบการทำงาน")

'''
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''

# if age >= 15:
#     print("คำนำหน้าเป็น นาย/นางสาว")
# else :
#     print("คำนำหน้าเป็น เด็กชาย / เด็กหญิง")

# print("จบโปรแกรม")

if age>=15:
    print("วัยรุ่น")
elif age>=20:
    print("วัยผู้ใหญ่")
elif age>=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")