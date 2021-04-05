# 리스트
- 순서대로 저장하는 시퀀스이자 변경 가능한 목록
- 내부적으로는 동적 배열로 구현
- list()
- 추가 : append()
- 추출 : pop()
  - pop(0) : 첫 번째 요소 추출
  - 큐의 연산이므로 복사가 필요
- 인덱스 : a[i]
- 길이 : len(a)
- 조회 : a[i:j]; i~j까지 슬라이스의 길이만큼 k개의 요소를 가져옴
- 존재 확인 : elem in a
- 개수 : a.count(elem)
- 정렬 : a.sort()
- 최소/최대 : min/max(a)
- 역순 : reverse()
---
### 리스트 활용 방법
- a = list()
- a = []
- append는 뒤에 추가


    a = [1, 2, 3]
    a.append(4)
    -> [1, 2, 3, 4]

- insert는 지정 추가

    
    # 3번째 인덱스에 5를 삽입
    a.insert(3,5)
    -> [1, 2, 3, 5, 4]

- 리스트에 숫자 외에도 문자와 불리언등 다양한 자료형 사용 가능

- 가져오려면 a[3] 로 인덱싱을 주면 됨
- 시작 인덱스 생략 가능 a[:3]; 처음 부터 인덱스 3까지
- 종료 인덱스 생략 가능 a[4:]; 인덱스 4부터 끝까지

- 예외처리
    - IndexError 발생 가능이라면
    - try-catch로 잡기
    
- 뒤에서 하나 지우기 : del
- 지정해서 지우기 : remove
---
### 리스트 특징
- 연속된 공간에 요소를 배치하는 배열의 장점을 갖음
- 다양한 타입을 연결해 배치하는 연결 리스트의 자점을 갖음
- 다양한 타입을 동시에 관리할 수 있는 단일 리스트임
- 그렇기 때문에 각기 다른 자료형의 크기로 인해 연속된 메모리 공간에 할당하는 것이 불가
- 따라서 인덱스 조회시 속도가 느림