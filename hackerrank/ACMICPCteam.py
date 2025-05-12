from itertools import combinations

def acmTeam(topic):
    # Write your code here
    
    r = [ {i+1 for i,j in enumerate(s) if j == "1"} for s in topic]
         
    x = [ list(u[0].union(u[1])) for u in combinations(r, r=2) ]
    x = list(map(lambda i: len(i), x))
    
    return [max(x), x.count(max(x))] 
