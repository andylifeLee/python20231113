# Demo.py 

print("hello")

#리스트 형식 연습
colors = ["red","blue","green"]
print(colors)
print(type(colors))
colors.append("black")
colors.insert(1, "pink")
print(colors)
colors += ["red"]
print(colors.index("red"))
colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors)
colors.remove("red")
print(colors)
colors.extend(["yellow","black","green"])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

for item in colors:
    print(item)

# SET 형식 연습(집합연산 시용)
print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Tuple 형식 연습
print("---Tuple 형식---")
tp = (1,2,3)
print(tp)
print(len(tp))
print(type(tp))

#함수 정의
def calc(a, b):
    return a+b, a*b 

#함수 호출
result = calc(3,4)
print(result)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim","김유신"))

args = (5,6)
print(*args)

print("---형식변환---")
#a = set((1,2,3,)) 
a = {1,2,3}
print(a)

b = list(a)
b.append(4)
print(b)


device = {"아이폰":5,"아이패드":10,"원도우타블렛":20}
print(len(device))
print(device)
#검색
print(device["아이폰"])
#입력
device["맥북"] = 15
#삭제
del device["아이패드"]
print(colors)
#수정
print(colors)
device["아이폰"] = 6

for item in device.items():
    print(item)
    
for item in device.items():
    print(item)
    