#TimeComplexity:O(N*M) 
#SpaceComplexity: O(N)
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No
class Solution:
         
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates==None:
            return None
        self.output=[]
        self.candidates=candidates
        self.recur(target,[],0,0)
        return self.output 
    def recur(self,target,path,curSum,index):
        if curSum>target or index==len(self.candidates):
            return
        if curSum==target:
            self.output.append(path)
        for i in range(index,len(self.candidates)):
            self.recur(target,path+[self.candidates[i]],curSum+self.candidates[i],i)
    
'''
    def recur(self,target,path,index,sum):
        if sum>target or index==len(self.candidates):
            return
        if sum==target:
            self.output.append(copy.deepcopy(path))
            return
        for i in range(index,len(self.candidates)):
            path.append(self.candidates[i])
            self.recur(target,path,i,sum+self.candidates[i])
            path.pop()        
'''
                