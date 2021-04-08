'''
가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
대소문자를 구분하지 않으며, 구두점 또한 무시함
'''
import collections
import re

def mostCommonWord(paragraph, banned):
    # \w = 단어 문자를 의미
    # ^는 not을 의미
    # w즉 단어 문자가 아니면 모두 공백으로 치환
    words = [word for word in re.sub(r'[^\w]', '', paragraph)
            .lower().split()
            if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
result = mostCommonWord(paragraph, banned)
print(result)