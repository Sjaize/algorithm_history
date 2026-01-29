from itertools import combinations
import sys

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << (ord(char) - ord('a')))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

if K < 5:
    print(0)

else:
    K = K - 5
    bits = list(map(word2bit, words))
    base_bit = word2bit("antic")
    alphabets = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    
    result = 0
    for combination in combinations(alphabets, K):
        mask = sum(combination) | base_bit
        count = 0

        for bit in bits:
            if bit & mask == bit:
                count = count + 1

        result = max(result, count)
    print(result)