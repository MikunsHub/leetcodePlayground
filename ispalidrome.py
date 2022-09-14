
s = "A man, a plan, a canal: Panama"

cvrt_list = []

for char in s:
    if not char.isalnum():
        continue
    cvrt_list.append(char.lower())
print(cvrt_list)

l = 0
r = len(cvrt_list) - 1

while l < r:
    if cvrt_list[l] == cvrt_list[r]:
        l += 1
        r -= 1
    else:
        break
print(False)
