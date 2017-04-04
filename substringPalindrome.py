"""
Find the number of palindromic substrings.

DP: O(n^2)
"""

def substringPalindrome(s):
    n = len(s)
    dp = [[False]*n for i in range(n)]

    count = 0

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                dp[i][j] = True
                count += 1

    return count

if __name__ == '__main__':
    s = 'abcdcba'
    print(substringPalindrome(s))
