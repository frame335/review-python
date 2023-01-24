# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง
# Input / convert to integer
weight = int(input("ป้อนน้ำหนักของคุณ (kg) :"))
height = int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
# print("BMI = ",round(weight/(height**2),2))

'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1
>30.0 = โรคอ้วนระดับอันตราย
'''

bmi = round(weight/(height**2),2)

result = "ไม่ทราบค่าที่ชัดเจน" # ค่าเริ่มต้น
if bmi>=0.0 and bmi<18.0:
    result="ผอม"
elif bmi>=18.5 and bmi<=22.99:
    result="สมส่วน"
elif bmi>=23.0 and bmi<=24.99:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.99:
    result="โรคอ้วนระดับหนึ่ง"
elif bmi>=30.0:
    result="โรคอ้วนระดับอันตราย"   
else:
    result="ไม่ทราบค่าที่ชัดเจน"

print("ค่า bmi = ",bmi,"ทำนายว่า =",result)