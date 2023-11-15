# DemoFormat.py 

for i in range(1,11):
    URL = "http://multi.com/?page=" + str(i) 
    print(URL)

print("---숫자 출력---")
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))


# #파일 쓰기 
# f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
# f.write("첫번째라인\n두번째라인\n세번째라인\n")
# f.close() 

# #파일 읽기 
# f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
# print(f.read())
# f.close() 


#파일 쓰기 
f = open(r"c:\work\test.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close() 

#파일에 첨부(append, read, write)
f = open(r"c:\work\test.txt", "a+", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close() 

# #파일 읽기 
# f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
# print(f.read())
# f.close() 


#파일 읽기 
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
print(f.read())
#다시 처음으로 리셋
f.seek(0)
result = f.readlines()
for item in result:
    print(item)

#다시 처음
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.close() 