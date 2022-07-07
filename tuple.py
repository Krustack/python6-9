fruitsTuple = ("apple", "banana", "cherry","kiwi")
fruitsList = ["apple", "banana", "cherry","kiwi"]
print(fruitsTuple[1:])
print(fruitsList[0])
#เปลี่ยนค่าในtuple
fruitsList[1]="mango" #เปลี่ยนในlist
print(fruitsList)
#tupleไม่สามารถเปลี่ยนค่าโดยตรงได้ต้องแปลงเป็นlistก่อน
x = list(fruitsTuple)
x[1]="mango"
fruitsTuple = tuple(x)
print(fruitsTuple)
#เพิ่มค่าในtuple
x = list(fruitsTuple)
x.append("orange")
fruitsTuple = tuple(x)
print(fruitsTuple)
#ลบค่าในtuple
x = list(fruitsTuple)
x.remove("kiwi")
fruitsTuple = tuple(x)
print(fruitsTuple)
x = range(3,20)
for n in x:
    print(n)
x = range(3, 20, 3)
for n in x:
    print("step3:",n)
#ชื่อ เลขที่ ชั้น