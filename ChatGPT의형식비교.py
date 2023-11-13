# List (리스트) - 수정 가능한 순서가 있는 컬렉션
my_list = [1, 2, 3, 4, 5]
print("List (리스트):", my_list)

# Tuple (튜플) - 수정 불가능한 순서가 있는 컬렉션
my_tuple = (1, 2, 3, 4, 5)
print("Tuple (튜플):", my_tuple)

# Dictionary (사전) - 키-값 쌍을 가지는 수정 가능한 컬렉션
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Dictionary (사전):", my_dict)

# Set (집합) - 중복을 허용하지 않는 수정 가능한 컬렉션
my_set = {1, 2, 3, 4, 5}
print("Set (집합):", my_set)

# List 요소 수정
my_list[0] = 10
print("List 수정:", my_list)

# Tuple은 수정 불가능하므로 요소 수정 시 오류 발생
# my_tuple[0] = 10  # TypeError 발생

# Dictionary 값 수정
my_dict['age'] = 31
print("Dictionary 수정:", my_dict)

# Set에는 인덱스가 없고, 중복된 요소가 자동으로 제거됩니다.
my_set.add(6)
print("Set에 요소 추가:", my_set)
my_set.remove(3)
print("Set에서 요소 제거:", my_set)
