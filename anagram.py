class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfrequency={}
        if (len(s)!=len(t)):
            return False
        for i in s:
            if (i not in sfrequency):
                sfrequency[i]=1
            else:
                sfrequency[i]+=1

        tfrequency={}
        for i in t:
            if (i not in tfrequency):
                tfrequency[i]=1
            else:
                tfrequency[i]+=1
       
        if sfrequency==tfrequency:
            return True
        else:
            return False
