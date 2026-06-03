class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            cnt = [0] * 26
            for j in i:
                cnt[ord(j)-ord('a')]+=1
            res[tuple(cnt)].append(i)
        # print("Value :", list(res.values()))
        return list(res.values())
        