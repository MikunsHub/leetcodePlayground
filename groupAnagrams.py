from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs):

    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 #a ... z  (idx 0:a,idx 1:b...)

        for c in s: 
            # ord() Returns the Unicode code point(or ascii value) for a one-character string(i.e a,b,A,'1').
            count_idx = ord(c) - ord("a")
            count[ord(c) - ord("a")] += 1
        
        res[tuple(count)].append(s)

    return res.values()


print(groupAnagrams(strs))
print(ord("1"))