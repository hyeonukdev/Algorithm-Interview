# 람다 표현식
- 식별자 없이 실행 가능한 함수
- 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현 가능


    lamda 인자 : 표현식

ex1)

    >>> def hap(x, y):
    ...   return x + y
    ...
    >>> hap(10, 20)
    30

람다식

    >>> (lambda x,y: x + y)(10, 20)
    30  


ex2)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

원래
    
    def func(x):
        return x.split()[1], x.split()[0]
