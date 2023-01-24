### Assignment 16: เกมทายเลขลูกเต๋า

##################################################################################
# 1,2,3,4,5,6
# ให้ผู่เล่นเดาค่าที่สุ่มออกมา ถ้าถูกก็ให้ค่าถูก ผืดก็ให้ค่าผิด

# import random

# myrandom = random.randrange(1,6+1) # สุ่มตั้งแต่ค่า 1 ถึง สิบ

# # ใช้ loop while
# while True:
#     number=int(input("ป้อนคำตอบของคุณ = "))
#     if number<0:
#         break
#     print("สุ่มค่ามาได้ถูกต้อง") if (number==myrandom) else print("สุ่มค่ามายังไม่ถูกนะจ๊ะ")

# print("สุ่มเลขได้ ",myrandom)
##################################################################################

##################################################################################
## เขียนตามตัวอย่าง
import random

myrandom = random.randrange(1,6+1) # สุ่มตั้งแต่ค่า 1 ถึง สิบ
print(myrandom)
k=1
print("คุณมีโอกาสทายได้ 3 ครั้ง \n")
correct=False

while True:
    number=int(input("ป้อนคำตอบของคุณ = "))
    # correct=(number==myrandom)
    if number<myrandom:
        print("ยังน้อยไปครับ")
    elif number>myrandom :
        print("ยังมากไปครับ")
    elif number==myrandom :
        print("ยินดีด้วยครับ คุณตอบถูก รับไปเลย 1 ล้านบาท")
        break

    if number<0 or k==3:
        break
    k+=1
    # if not correct:
    #     if (number>myrandom) :
    #         print("ใบนิดนึงว่า ค่าที่ทายมามันน้อยไปครับ")
    #     elif (number<myrandom) :
    #         print("ใบนิดนึงว่า ค่าที่ทายมามันมากไปครับ")

if number!=myrandom :
    print("เสียใจด้วยนะครัช คุณทายครบ 3 ครั้งแล้ว")

print("เฉลยนะครับ เลขที่ถูกต้องก็คือ ",myrandom," ครับผม")
##################################################################################