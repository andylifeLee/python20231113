class MyClass:
    #초기화 메서드(초기화)
    def __init__(self, value):
        self.Value = value 
        print("Class is created! Value = ", value)
    #소멸자 메서드(정리작업)    
    def __del__(self):
        print("Class is deleted!")
        

c = MyClass(5)
#del d
print("전체코드 실행 종료")
#c_copy = c
#del c 
#del c_copy
