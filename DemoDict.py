# DemoDict.py 
colors = {"apple":"red", "banana":"yellow"}
print(colors)
print(len(colors))
#검색
print(colors["apple"])
#입력
colors["kiwi"] = "green"
print(colors)
#삭제
del colors["apple"]
print(colors)

#반복구문 
#디버깅셋팅(내부를 탐색할 때 사용)
#디버깅할 때 중단점(Break Point)
for item in colors.items():
    print(item)



print("---주소록---")
#전화번호 저장 
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)

#참조를 전달
p = phone
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone))
print(id(p))




for item in phone.items():
    print(item)

print(phone["kim"])
print("park" in phone)




#참조만 복사(같은 객체)
p = phone

p["kang"] = "1234"
print(id(phone))
print(id(p))

print("moon" not in p)

print("---논리식---")
print(1 < 2)
print(1 != 2)
print(1 == 2)
#and(~이면서, ~이고) or(~이거나)
print(True and True and True)
print(True and True and False)
print(True or False or False)
#파이썬 참 판단 근거
print(bool(0))
print(bool(-1))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool(None))
print(bool([1,2,3]))

print("---얕은복사---")
a = [1,2,3]
b = a 
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

print("---깊은복사---")
a = [1,2,3]
b = a[:] 
a[0] = 38
print(a)
print(b)
print(id(a), id(b))
