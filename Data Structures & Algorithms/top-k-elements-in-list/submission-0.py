class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq = [[] for i in range(len(nums)+1)]
        print("Freq = ", freq)

        for i in nums:
            count[i] = 1+count.get(i, 0)
        print("Count : ", count)

        for n, c in count.items():
            # print("n :", n)
            # print("c :", c)
            freq[c].append(n)
        print("Freq 2 = ", freq)

        res = []
        for i in range(len(freq)-1, 0, -1):
            print("I is : ",i)
            for n in freq[i]:
                print("n is : ", n)
                res.append(n)
                print("Res :", res)
                if len(res)==k:
                    return res