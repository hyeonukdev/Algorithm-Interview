'''
로그 파일 재정렬
- 로그의 가장 앞 부분은 식별자
- 문자로 구성된 로그가 숫자 로그보다 앞에 옴
- 식별자는 순서에 영향을 끼치진 않지만, 문자가 동일한 경우 식별자 순으로 함
- 숫자 로그는 입력 순서대로 함

ex1)
입력 : logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
출력 : ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
'''

# isdigit() : 숫자 여부 판별

def reorderLogfiles(logs):
    letters, digits = [], []
    for log in logs:
        # print("log.split()[1]: {}".format(log.split()[1]))
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = reorderLogfiles(logs)
print(result)