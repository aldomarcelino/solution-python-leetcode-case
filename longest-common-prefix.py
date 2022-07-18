def longestCommonPrefix(list):
    pre = ""
    for i in range(len(list[0])):
        for temp in list:
            if i == len(temp) or temp[i] != list[0][i]:
                return pre
        pre += list[0][i]
    return pre


strs = ["flower", "flow", "flight"]

for x in range(len(strs)):
    print(strs[x])
print(longestCommonPrefix(strs))
