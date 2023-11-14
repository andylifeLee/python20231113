#function3.py

# function1.py
#1)함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)

#2)호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x 

retValue = swap(3,4)
print(retValue[0], retValue[1])


def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM","SPAM"))


print("---지역,전역변수---")
x = 5   #전역변수
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 10 
    return a+x 

#호출
print(func2(1))

print(globals())
print(dir())


#기본값 셋팅
def times(a=10, b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자(매개변수명 지정)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL


#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="multi.com"))


#가변인자(가변적인 상황 대비)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

# #정의되지 않은 인자(dict)
# def userURIBuilder(server, port, **user):
#     strURL = "http://" + server + ":" + port + "/?"
#     for key in user.keys():
#         strURL += key + "=" + user[key] + "&"
#     return strURL

# #호출
# print(userURIBuilder("multi.com", "80", id="kim", passwd="1234"))
# print(userURIBuilder("multi.com", "80", id="kim", passwd="1234", 
#     name="mike", age="30"))

#람다함수(간단하게 한줄로 함수 정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())

# #람다함수 활용 예제
# lst = [10, 25, 30]
# iterL = filter(lambda x:x>20, lst)
# for item in iterL:
#     print(item)
