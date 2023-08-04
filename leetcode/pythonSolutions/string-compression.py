
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        l,r = 0,0
        dig = len(chars)
        index = 0
        while l<dig:
            r = l
            
            while r<dig and chars[r] == chars[l] :
                r+=1

            count = r-l
            chars[index] = chars[r-1]
            index+=1
            if count>1:
                for i in range(0,len(str(count))):
                    chars[index] = str(count)[i]
                    index+=1
            print(index)
            l = r

        return index
