### โครรงสร้างควบคุมทำซ้ำ (For Loop)

##################################################################################
## โครงสร้างของ loop for
'''
# i เป็นตัวนับรอบ
for i in range(start,stop,step) #กำหนดรอบว่าให้ทำกี่รอบ
'''

# แสดง Hello World 3 รอบ
# ค่าเริ่มต้นของ range คือเริ่มต้นที่ 0

for i in range(5):
    print("Hello World","รอบที่ ", i+1 ,)
print("End")

for i in range(1,6,2): # รอบที่ 1 ถึง 5 เลข 6-1 = 5 , 
    # เลข 2 เป็น Step การเพิ่ม ==> (start,stop-1,step) ถ้าค่าเริ่มเป็น 1
    # ถ้าไม่บอก Step มันจะเพิ่ม step เป็นทีละ 1
    print("รอบที่ = ", i ,"Hello World")
print("End")
##################################################################################

##################################################################################
summation = 0 # กำหนดค่าเริ่มต้น
count=int(input("ระบุจำนวนรอบ : "))


for i in range(1,count+1):
    summation+=i
    print("รอบที่ ",i,"Hello Tik","sum = ",summation)
    average=summation/count

average = summation / count    
print("ผลรวม = ",summation)

print("ค่าเฉลี่ย = ",average)
print("End")

for i in range(-10,-4,2):
    print("ค่า = ",i)
print("End")

### ลดค่า
for i in range(10,-1,-1):
    print("ค่า = ",i)
print("End")
##################################################################################