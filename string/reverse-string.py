'''
# 문자열 뒤집기
- 입력값은 문자 배열이며
- 리턴 없이 리스트 내부를 직접 조작하기

ex1)
입력 : ["h", "e", "l", "l", "o"]
출력 : ["o", "l", "l", "e", "h"]

'''

def reverseString(s):
    print(s)
    s.reverse()
    print(s)


s = ["h", "e", "l", "l", "o"]
reverseString(s)