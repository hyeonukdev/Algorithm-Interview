'''
하노이 타워
- A에 있는 n개의 원반 중 맨 아래에 있는 n번재 원반을 제외한 나머지 원반을 B로 옮긴다
- A에 남은 하나의 원반을 C로 옮긴다
- B의 모든 원반을 C로 옮긴다
'''

def hanoi(num, _from, _by, _to):
    if num == 1:
        print("{}에서 {}로 {}번 째 원반 이동".format(_from, _to, num))
        return
    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {}번 째 원반 이동".format(_from, _to, num))
    hanoi(num - 1, _by,  _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반 개수 입력: "))

        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')