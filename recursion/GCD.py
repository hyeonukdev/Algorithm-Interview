'''
최대공약수(유클리드 호제법)
'''

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

print(gcd(48, 60))