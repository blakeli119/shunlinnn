class solution(object):
    def mergesort(self,nums): 
        final= []
        if len(nums) < 2:
            return nums 
    
        else:
            mid = int(len(nums)/2)
            a = mergesort(nums[:mid]) 
            b = mergesort(nums[mid:]) 
        self.mergesort(a)
        self.mergesort(b)
        while (len(a) > 0) or (len(b) > 0):
            if len(a) > 0 and len(b) > 0:
                if a[0] > b[0]:
                    final.append(b[0]) 
                    b.pop(0)
                else:
                    final.append(a[0])
                    a.pop(0)
            elif len(b) > 0:
                for i in b:
                    final.append(i) 
                    b.pop(0)
            else:
                for i in a:
                    final.append(i) 
                    a.pop(0)
        return final
