s = "anagram"
t = "nagaram"

def isAnagram(s:str,t:str) -> bool:

    if len(s) != len(t):
        return False
    
    countS , countT = {}, {}

    for i in range(len(s)):

        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for letter in countS:
        if countS[letter] != countT.get(letter,0):
            return False
    return True

print(isAnagram(s,t))