for index in range(1,11,1):
    print(index)

#loop กับ list
List1 = ['Wisanu','Jojo','Jotaro']
for element in List1:
    print(element)

#loop กับ dic
Dic = {'name':'joseph','age':50,'job':'mage'}
for key,value in Dic.items():
    print(key,':',value)
List2=[{'name':'joseph','age':50,'job':'mage'},
       {'name':'Wisanu','age':18,'job':'popstar'},
       {'name':'soranun','age':25,'job':'teacher'},
       {'name':'Tuu','age':70,'job':'soldier'},]
for element in List2:
    for key,value in element.items():
        print(key,value)
i = 1
while i<10:
    print(i)
    i+=1
name = input("ชื่อ:")
print(name)
