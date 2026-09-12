def find_unit_clause(clauses):
    """Finds a unit clause in the list of clauses."""
    for clause in clauses:
        if len(clause)==1:
            return clause[0]
        return None
def simplify_clauses(clauses,literal):
    """Simplifies the list of clauses by setting the given literal to True."""
    simplified==[]
    for clause in clauses:
        if literal in clause:
            continue
        new_clause=[1 for 1 in clause if 1!=-literal]
        if not new_clause:
            return None
        simplified.append(new_clause)
        return simplified
def dpll(clauses,assignments):
    """Implements the DPLL algorithm for propositional model checking."""
    unit=find_unit_clause(clsuses)
    while unit is not None:
        assignment.append(unit)
        clauses=simply_clauses(clauses,unit)
        if clauses is None:
            return False
        unit = find_unit_clause(clauses)
if not clauses:
    return True
literal = clauses[0][0]
new_clauses = simplify_clauses(clause,literal)
if new_clauses is not None and dpll(new_clauses,assignment+[literal]):
    return True
new_clauses= simplify_claues(clause,-literal)
if new_clauses is not None and dpll(new_clauses,assignments+[-literal]):
    return True
  return False
def main():
    A,B,C =1,2,3
    clauses=[[A,B],[-A,C],[-B,-C]]
    assignment=[]
    if dpll(clauses,assignmnets):
        print("SATISFIABLE with assignment:",assignments)
    else:
        print("UNSATISFIABLE")
if__name__=="__main__":
    main()
