class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)
        res = []

        for s in strs:
            freq_list = [0] * 26
            for c in s:
                freq_list[(ord(c)-97)]+=1

            hash[tuple(freq_list)].append(s)

        for v in hash.values():
            res.append(v)

        return res


        