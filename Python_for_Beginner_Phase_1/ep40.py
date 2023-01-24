### Assignment 15: สร้างขอบตาราง

##################################################################################
'''
xxxx
xxxx
xxxx
xxxx

เอาแค่ขอบ
xxxx
x  x
x  x
xxxx
'''
number = int(input("ป้อนขนาด = "))

for row in range(1,number+1) :
    for column in range(number+1) :
        print("X",end="") if row==1 or row==number or column==1-1 or column==number else print(" ",end="")
    print(" ") # ให้ขึ้นบรรทัดใหม่ เมื่อมันวนลูปแล้ว



##################################################################################