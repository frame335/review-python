## Pass

age = int(input("ป้อนอายุของคุณ :"))

if age<=15:
    if age==15:
        print("ต้องไปทำบัตรประชาชน")
    elif age==14:
        pass
    else:
        print("ประถมศึกษา")
else: 
    print("ม.ปลาย")

print("จบโปรแกรม")