import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 10000000]

# 동시성 합계 계산 메인함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포멧
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 실행
if __name__ == '__main__':
    main()