### โปรแกรมแปลงอุณหภูมิ

##################################################################################
### farenheit to celsius
from math import degrees


tempareture = input("ป้อนอุณหภูมิ (องศา) : ") # 45C
# print(tempareture)

## เก็บตัวเลของศา
degree  = float(tempareture[:-1]) # เอาทุกตัวที่ไม่ใช่ตัวสุดท้าย => 45

## เก็บหน่วย 
unit = tempareture[-1].upper() # เอาตัวสุดท้ายมาให้ดรั๊ยเล้ย => C

# print(degree," = ",unit)

if unit=="C":
    # แปลงเป็นฟาเรนไฮ
    result = round(((degree * 9) /5) + 32, 2)    
    unit_result = "ฟาเรนไฮน์"
if unit=="F":
    # แปลงเป็นเซลเซียส
    result = round(((degree - 32) *5) / 9, 2)   
    unit_result = "เซลเซียส"

print("แปลงตัวเลข = ",tempareture,"เป็น ",result,"",unit_result)
### celsius to farenheit
##################################################################################