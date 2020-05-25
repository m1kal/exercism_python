def sum_of_multiples(limit, factors):
    return sum(x for x in range(1,limit) if any(x%e==0 for e in factors if e>0))
