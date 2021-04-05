# 자료형
### 파이썬3 표준 타입 계층 구조
- None(class None Type)
    - 숫자
        - 정수형 
        1. 정수(class int)
        2. 불리언(class bool)
        - 실수(class float)
    - 집합형
        1. 집합(class set)
    - 시퀀스
        - 불변
        1. 문자열(class str)
        2. 튜플(class tuple)
        3. 바이트(class bytes)
        - 가변
        1. 리스트(class list)
    
### 매핑
- 키와 자료형으로 구성된 복합 자료형
- 딕셔너리가 유일

### 집합
- 중복된 값을 갖지 않는 자료형


    a = set()
    type(a)
    => <class 'set>
  
- 딕셔너리는 키/값 형태이지만 집합은 값만 선언
- 입력 순서가 유지 되지 않으며, 중복된 값이 있을 경우 하나의 값만 유지

### 시퀀스
- 수열과 같은 의미
- 대상의 순서 있는 나열
- list라는 시퀀스 타입이 사실상 배열의 역할을 수행
- str, tuple, bytes로 선언되는 타입은 불변
- list는 가변 즉, 추가/삭제 가능한 동적 배열임

### 객체
- 파이썬에서는 모든 것이 객체임
- 크게 불변 객체(immutable Object)와 가변 객체(Mutable Object)로 구분
- 불변 객체
    - bool
    - int
    - float
    - tuple
    - str
- 가변 객체
    - list
    - set
    - dict
    
### is와 ==
    if a is None
        pass
- == 는 비교 연산자
- is는 id()를 비교하는 함수
- None은 값 자체가 정의 되지 않기 때문에 비교 불능
