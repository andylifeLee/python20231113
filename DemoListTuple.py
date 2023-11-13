# DemoListTuple.py 
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
print(colors.pop(1))
colors.extend(["yellow","black","white"])
colors.sort()
print(colors)
colors.reverse()
print(colors)
colors.remove("blue")
print(colors)


print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---Tuple형식---")
tp = (1,2,3)
print(tp)
print(len(tp))
print(type(tp))

#함수 정의
def calc(a,b):
    return a+b, a*b 

#함수 호출
result = calc(3,4)
print(result)

print("id:%s, name:%s" % ("kim","김유신"))

args = (5,6)
print(*args)

print("---형식변환---")
a = {1,2,3}
b = list(a)
b.append(4)
print(b)
