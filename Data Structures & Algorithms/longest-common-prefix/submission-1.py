class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            counter = 0
            for s in strs:
                if i >= len(s):
                    return prefix
                
                if s[i] == strs[0][i]:
                    counter += 1
                else:
                    return prefix

            if counter == len(strs):
                prefix += strs[0][i]
             

        return prefix
                
        