### Assignment 12: ตัวเลขขั้นบันได

##################################################################################
## เราจะแสดงตัวเลขเป็นขั้นบันได

'''
input = 4
1
12
123
1234
'''

last = int(input("ป้อนตัวเลข : "))

# ใช้ for loop
for row in range(1,last+1):
    for column in range(1,row+1):
        print(column,end='')
    print(" ")

    # print(row)

'''
ป้อน input = 3
row รอบแรก มีค่าเป็น 1
แล้วไปบวกค่าอีก 1 มันจะทำงานสามครั้ง
row = 1,3

column มีช่วงตั้งแต่ 1,1+1
การทำงานเริ่มตั้งแต่ 1,2

row 2
column 1,2+1

row 3
column 1,3+1

'''
##################################################################################