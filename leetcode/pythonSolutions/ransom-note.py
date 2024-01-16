class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        rand = dict()
        magd = dict()
        ran = list(ransomNote)
        mag = list(magazine)
        flag = False
        for i in mag:
            magd[i] = magd.get(i,0)+1
        for j in ran:
            rand[j] = rand.get(j,0)+1

        for letter in rand:
            if letter not in magd:
                return False
            if rand[letter] <= magd[letter]:
                flag = True
            else: 
                return False

        return flag


        # print(magd, rand) 
