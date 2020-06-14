class py_solution:
    def __init__(self,nums):
        self.list=nums
        self.subset=[]
        self.threes=[]
        
    def sub_sets(self):
        sset=self.list
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

    def find_threes(self):
        for x in self.subset:
            if len(x)==3:
                if x[0]+x[1]+x[2]==0:
                    self.threes.append(x)

                         

nums=py_solution([4,5,6,7])
nums.subset=nums.sub_sets()
print(nums.subset)


nums2=py_solution([-25, -10, -7, -3, 2, 4, 8, 10])
nums2.subset=nums2.sub_sets()
print(nums2.subset)
nums2.find_threes()
print(nums2.threes)
