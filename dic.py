car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car['brand'])
#แสดงคีย์
print(car.keys())
#เพิ่มค่าในdic
car["color"] = "red"
print(car.keys())
print(car)
#แก้ไขค่าในdic
car["year"] = 2018
print(car)
#ลบค่าในdic
car.pop('color')
print(car)
#copyค่าไปdicอื่น
vel =dict(car)
print('velDic:',vel)
#เก็บlist ในdic
car["part"] = ["body","wheel","light","etc..."]
print('listPart :',car)
#เพิ่มค่าdicแบบ  Nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child3']['year'])
#ชื่อเลขที่
