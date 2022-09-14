s = "abcabcbb"

def lengthOfLongestSubstring(s: str) -> int:
        leftptr = 0
        seen = []
        max_len = 0
        for rightptr in range(len(s)):
            while s[rightptr] in seen:
                seen.remove(s[leftptr])
                leftptr += 1
            seen.append(s[rightptr])
            max_len = max((rightptr - leftptr)+1,max_len)
        return max_len

print(lengthOfLongestSubstring(s))