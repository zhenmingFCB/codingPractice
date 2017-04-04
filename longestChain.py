"""
Find longest chain within a set of words,
eg. 'a', 'b', 'ba', 'bca', 'bda', 'bdca' return length=4
"""

def longestChain(words):
    memo = dict()
    res = 0
    for w in words:
        res = max(res, dfs(words, w, memo))
    return res

def dfs(words, w, memo):
    res = 1
    for i in range(len(w)):
        candidate = w[:i] + w[i+1:]
        if candidate in words:
            if candidate in memo:
                res = max(res, memo[candidate]+1)
            else:
                res = max(res, dfs(wors, candidate, memo)+1)
    memo[w] = res
    return res

if __name__ == '__main__':
    words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
    print(longestChain(words))
