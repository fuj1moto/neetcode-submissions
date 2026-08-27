class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        seen = []
        for i in range(len(strs)):
                group = [strs[i]]
                if sorted(list(strs[i])) not in seen:
                    seen.append(sorted(list(strs[i])))
                    for j in range(i+1, len(strs)):
                        if sorted(list(strs[j])) == sorted(list(strs[i])):
                            group.append(strs[j])
                    out.append(group)

        return(out)
                
