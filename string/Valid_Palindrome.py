# 유효한 팰린드롬
'''
팰린드롬이란?
- 앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장.

주어진 문자열이 팰린드롬인지 확인하라.
대소문자를 구분하지 않으며, 영뭄자와 숫자만을 대상으로 한다.

ex1)
입력 : "A man, a plan, a canal: Panama"
출력 : true
ex2)
입력 : "race a car"
출력 : false

https://leetcode.com/problems/valid-palindrome/
'''

def isPalindrome(s):
    strs = []
    for char in s:
        # isalnum : 글자 또는 숫자로 구성되어있으면 : True 아니면 False 값 반환
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# ---------------------------------
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))