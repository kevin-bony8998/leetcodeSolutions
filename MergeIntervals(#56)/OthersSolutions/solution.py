class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort by start value
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            prev = res[-1]
            #Intervals overlapping
            if start <= prev[1]:
                #Update prev interval's end 
                res[-1][1]=max(prev[1],end)
            #No overlap
            else:
                res.append([start,end])
        return res