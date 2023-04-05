class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict()
        tempsum = 0
        for i in range(0,len(list1)):
            for j in range(0,len(list2)):
                if list1[i] == list2[j]:
                    tempsum = i+j
                    name = list2[j]
                    d[name] = tempsum

        min_val = min(d.values())
        min_keys = [k for k,v in d.items() if v == min_val]
        return min_keys
