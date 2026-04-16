def solve(n):
    res = []
    def backtrack(s, l, r):
        if len(s) == 2*n:
            res.append(s)
            return
        if l < n:
            backtrack(s+'(', l+1, r)
        if r < l:
            backtrack(s+')', l, r+1)
    backtrack('', 0, 0)
    return res

print(solve(3))
