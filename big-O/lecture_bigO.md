# 빅오
## 빅오란?
### 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기 방법

---
- 접근적 실행 시간(Asympototic Running Time): 입력값 n이 커질 때, lim 함수의 실행 시간의 추이를 의미
- 다른 말로는 시간 복잡도(Time Complexity)라고 불림
- 시간 복잡도: 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도(Computational Complexity)를 의미
- 그 중 대표적인 것이 빅오임
- 빅오로 시간 복잡도를 표현할 때는 '최고차항'만을 표기하며, 상수항은 무시함 

#### 빅오 표기법 종류
1. O(1)
- 입력값이 아무리 커도 실행 시간은 일정함 
2. O(log n)
- 실행 시간은 입력값에 영향을 받음
- 그러나 로그는 매우큰 입력값에도 큰 영향을 받지 않음
3. O(n)
- 입력값 만큼 실행 시간은 영향을 받음
- 비례 관계임
- 선현 시간(Linear Time) 알고리즘이라고함
- 정렬되지 않은 리스트에서 최댓값 혹은 최솟값 경우가 이에 해당함 
4. O(n log n)
- 병합 정렬등 효율성이 좋은 정렬 알고리즘이 이에 해당함
- 적어도 모든 수에 대해 한 번 이상은 비교해야 하는 비교 기반 정렬 알고리즘은 O(n log n)이 가장 좋음
5. O(n^2)
- 버블 정렬같은 효율적인 정렬 알고리즘이 이에 해당함
6. O(2^n)
- 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당함
7. O(n!)
- TSP(Travelling Salesman Problem) 브루트 포스 풀이가 이에 해당함
- 가장 느린 알고리즘으로 입력값이 조금만 커져도 시간이 길어짐 
---
### 알고리즘은 '시간과 공간이 트레이드 오프' 관계이다

- 빠른 알고리즘은 공간을 많이 사용하고, 공간을 적게 차지하는 알고리즘은 실행 시간이 느림
---
## 상한과 최악

- 빅오(O)는 상한(Upper Bound)를 의미함
- 빅세타(θ)는 평균을 의미함
- 빅오표기법은 주어진(최선/최악/평균) 경우의 수행 시간의 상한을 나타냄