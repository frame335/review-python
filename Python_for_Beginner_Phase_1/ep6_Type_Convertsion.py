# การแปลงชนิดข้อมูล
# Type Conversion

x = 10
y = 3.14
z = "20"

print(type(x))
print(type(y))
print(type(z))

# บวกเลข
result = x + y
print(result) 

# String => int
int(z)
result2 = x + int(z)
print(result2)

# int => string
result3 = str(x) + z
print(result3)
print(type(result3))

# string => float
result4 = y + float(z)
print(result4)

# float => string
result5 = str(y)
print(result5)
print(type(result5))

print(float(x))
print(int(y))

# z = float(z)
# print(type(z))