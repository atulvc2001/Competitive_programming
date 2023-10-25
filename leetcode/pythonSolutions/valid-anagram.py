
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = dict()
        dt = dict()
        for i in s:
            print(i)
            if i not in ds:
                ds[i] = ds.get(i,0)+1
            else:
                ds[i] = ds.get(i)+1
        print(ds)
        for j in t:
            if j not in dt:
                dt[j] = dt.get(j,0)+1
            else:
                dt[j] = dt.get(j)+1

        print(dt)
        return ds==dt
