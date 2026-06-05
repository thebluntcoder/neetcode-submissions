class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for each in strs:
            t = ''
            t = str(len(each))+'#'+each
            print("t is :", t)
            s = s+t
        print("S is :", s)
        return s

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
