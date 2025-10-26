#solution 1 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sortedfreq=sorted(freq.items(),key= lambda x: x[1],reverse=True)
        result=[]
        for key,value in sortedfreq[:k]:
            result.append(key)
        return result

        
