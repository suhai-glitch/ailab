import itertools
class propositional Logic:
    def__init__(self):
        self.clause=[]
    def add_clause(self,clause):
        self.clauses.append(clause)
    def pl_resolution(self):
        """ Perform propositional logic resolution to determine satisfiability."""
        new = set()
        while True:
            n=len(self.clauses)
            pairs =[(self.clauses[i],self.clauses[j]) for i in range(n) for j in range(i+1,n)]
            for(ci,cj) in pairs:
                resolvents=self.pl_reslove(ci,cj)
                if [] in resolvents:
                    return False
                for res in resolvents:
                    new.add(tuple(res))
            if new.issubset(set(map(tuple,self.clauses))):
                return True
            for clause in new:
                if list(clause) not in self.clause:
                    self.clause.append(list(clause))
            new =set()
    def pl_resolve(self,ci,cj):
        """Resolve two clauses to produce a set of resolvents."""
        resolvents=[]
        for di in ci:
            for di in cj:
                if di==-dj:
                    resolvent=list(set(ci)-{dj})+list(set(cj)-{dj})
                    resolvents.append(resolvent)
        return resolvents
    pl= Propositional Logic()
    pl.add_clause([1,2])
    pl.add_clause([-1,3])
    pl.add_clause([-2,-3])
    is_satisfiable=pl.pl_resolution()
    if is_satisfiable:
        print("the knowledge base is satisfiable.")
    else:
        print("the knowledge base is not satisfiable.")
            
