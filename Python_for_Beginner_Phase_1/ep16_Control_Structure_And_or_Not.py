# การใฃ้ And Or Not

# 15 - 20 => วัยรุ่น
# 21 - 29 => วัยผู้ใหญ่
# 30 - 39 => วัยทำงาน
age=int(input("ป้อนอายุของคุณ :"))

if (age>=15 and age<=20):
    print("วัยรุ่น")
elif (age>20 and age<=30):
    print("วัยผู้ใหญ่")
elif (age>=30 and age<=39):
    print("วัยทำงาน")
elif (age >=65) :
    print("วัยชรา")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")