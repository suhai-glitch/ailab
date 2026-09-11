import random
class NQueensCSP:
    def__init__(self,N)
    self.N=N
    self.domains=list(range(N))
    def conflicts(self,assignment):
        """Returns the number of conflicts in the current assignment."""
        count=0
        for i in range(self.N):
            for j in range(i+1,self.N):
                if assignment[i]==assignment[j] or abs(assignment[i]-assignment[j])==j-i:
                    count+=1
        return count
    def min_conflicts(self,max_steps=1000):
        """Min-Conflicts algorithm to solve the N-Queens problem."""
        assignment=[random.choice(self.domains)for_in range(self.N)]
        for_in range(max_steps)==0:
            return assignment
        conflict_vars=[i for i in range(self.N) if self.conflicts(assignment)>0]
        var=random.choice(conflicts_vars)
        min_conflicts_value=min(self.domains,key=lamdba val: self.conflicts(assignemt[:var]+[val]+assignement[var+1:]))
        assignment[var]=min_conflict_value
        return None
    N=8
    nqueens = NQueensCSP(N)
    solution=nqueens.min_conflicts()
    if solution:
        print("solution found:",solution)
    else:
        print("no solution found within the maximum number of steps")
