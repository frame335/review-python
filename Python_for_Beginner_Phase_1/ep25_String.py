### เจาะลึก String ตอนที่ 1 # ช่องของตัวอักษร

name = "John Tik" # index เริ่มต้นที่ 0

print(name[0:3]) # ก่อนถึงจุดสุดท้าย

print(name[:4]) # เขียนแบบนี้ก็ได้

print(name[:6]) # รวมเอาช่องว่างด้วย

print(name[4])

print(name[-1]) # นับจากด้านหลัง

print(name[-2])

print(name[-3:])

###### หาความยาวด้วย len
name=" john "

print(len(name))

## ลบช่องว่างซ้ายขวา

name=name.strip()
print(name)

################################
# ลบช่องว่างที่อยู่ด้านซ้ายมือ
name=" john "

name=name.lstrip()
print(name)
print(len(name))
################################

################################
# ลบช่องว่างที่อยู่ด้านขวามือ
name=" john "

name=name.rstrip()
print(name)
print(len(name))
################################

################################
### แปลง case ของ string ให้เป็นตัวพิมพ์ใหญ่
name="john"
print(name.upper())
################################

################################
### แปลง case ของ string ให้เป็นตัวพิมพ์เล็ก
name="John"
print(name.lower())
################################

################################
### แปลง case ของ string ให้ตัวแรกเป็นตัวพิมพ์ใหญ่
name="johnTik"
print(name.capitalize())
################################

################################
### การแทนที่ replace
name = "johntik"
name = name.replace(name,"Mr.John Tik")
# print(name.replace("johntik","Mr.John Tik"))
print(name)

name_2 = "john tik อารายๆก็ไม่รู้อยู่ชั้น ป 4 ปีที่ 4 ซอย 4"
# name_2 = name_2.replace("4","3.5",1) # บอกว่าแก้กี่จุด
# name_2 = name_2.replace("4","3.5",2)
name_2 = name_2.replace("4","3.5",3)
print(name_2)
################################

################################
### การเช็คข้อความ => true, false
name = "ไปซื้อข้าวและอาหารที่ตลาด"

x = "ข้าว" in name
y = "ไข่" in name
z = "อาหาร" not in name # เขียนในรูปตรงข้าม

print(x)
print(y)
print(z)

if x:
    name = name.replace("ข้าว","ขนมอะไรก็ได้โว้ย")

print(name)

if z:
    name = name.replace("อาหาร","อะไรก็ได้แหล่ะ")

print(name)

################################