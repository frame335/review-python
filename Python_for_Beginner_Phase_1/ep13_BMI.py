# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง
# Input / convert to integer
weight = int(input("ป้อนน้ำหนักของคุณ (kg) :"))
height = int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
print("BMI = ",round(weight/(height**2),2))