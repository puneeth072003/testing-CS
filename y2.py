from q1 import factorial

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))