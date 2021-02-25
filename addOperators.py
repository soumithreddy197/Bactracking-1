#TimeComplexity:O(N*M) NOT SURE EXACTLY
#SpaceComplexity: O(N)
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No
class Solution:
    def backtracking(self,num,index,target,prevSum,prevAddition,exp):
        if index>=len(num):
            if prevSum==target:
                self.output.append(exp)
            return
        
        for i in range(index,len(num)):
            if num[index] == '0' and i != index:
                continue
            currElem=int(num[index:i+1])
            if index==0:
                self.backtracking(num,i+1,target,prevSum+currElem,currElem,exp+str(currElem))
            else:            
                self.backtracking(num,i+1,target,prevSum+currElem,currElem,exp+'+'+str(currElem))
                self.backtracking(num,i+1,target,prevSum-currElem,currElem*-1,exp+'-'+str(currElem))
                self.backtracking(num,i+1,target,prevSum-prevAddition+prevAddition*currElem,prevAddition*currElem,exp+'*'+str(currElem))
        
        
    def addOperators(self, num: str, target: int) -> List[str]:
        
        self.output=[]
        self.backtracking(num,0,target,0,0,'')
        
        return self.output
    