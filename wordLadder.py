def findLadders(beginWord, endWord, wordlist):
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """
    """
    BFS Solution
    """
    from collections import deque, defaultdict
    visited = defaultdict(list)
    visited[beginWord] = [beginWord]
    levels = dict()
    levels[beginWord] = 1
    queue = deque()
    queue.append(beginWord)
    length = 1
    found = False
    res = []
    while queue:
        if found:
            break
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            for i,c in enumerate(curr):
                for new_c in 'abcdefghijklmnopqrstuvwxyz':
                    if new_c == c:
                        continue
                    newWord = curr[:i]+new_c+curr[i+1:]
                    if newWord == endWord:
                        found = True
                        if curr not in visited[newWord]:
                            visited[newWord].append(curr)
                            
                    elif newWord in wordlist:
                        if newWord in levels and length+1>levels[newWord]:
                            continue
                        if curr not in visited[newWord]:
                            visited[newWord].append(curr)
                        levels[newWord] = length+1
                        queue.append(newWord)
        length+=1
    
    for word in wordlist:
        print word, visited[word]
    # back tracking path
    def addPath(word, path, res):
        if word == beginWord:
            res.append([word]+[p for p in reversed(path)])
        else:
            path.append(word)
            for pre in visited[word]:
                addPath(pre, path, res)
            path.pop()
            
    res = []
    path = []
    addPath(endWord, path, res)
    
    return res

print findLadders("red","tax",["ted","tex","red","tax","tad","den","rex","pee"])