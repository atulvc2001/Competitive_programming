#Contains Dupicates

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        print("Hashset is the set")
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
