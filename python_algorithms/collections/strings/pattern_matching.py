class PatternMatch(object):

    # naive string pattern matching
    def naive(self, pat, txt):
        m = len(pat)
        n = len(txt)

        # A loop to slide pat[] one by one
        for i in range(0, n - m + 1):

            # For current index i, check for pattern match
            j = 0
            while(j < m):
                if txt[i + j] != pat[j]:
                    break
                j += 1
            # if pat[0...m-1] = txt[i, i+1, ...i+M-1]
            if j == m:
                print("Pattern found at index {}".format(i))

    # knuth-morris-pratt algorithm for pattern matching strings
    def kmp(self, pat, txt):
        if pat == "":
            return 0  # Immediate match

        # Compute longest suffix-prefix table
        lsp = [0]  # Base case
        for c in pat[1 : ]:
            j = lsp[-1]  # Start by assuming extension of previous LSP

            while j > 0 and c != pat[j]:
                j = lsp[j - 1]

            if c == pat[j]:
                j += 1
            lsp.append(j)
        # Walk through txt
        matches = []
        j = 0  # Num chars matched in pattern
        for i in range(len(txt)):
            while j > 0 and txt[i] != pat[j]:
                j = lsp[j - 1]  # Fall back in the pattern

            if txt[i] == pat[j]:
                j += 1 # Next char matched, increment position

            if j == len(pat):
                matches.append(i - (j - 1))
                j = j-1

        return matches

    # # rubin-karp string pattern matching
    # def rubinKarp(pat, str):


pm = PatternMatch()
n = pm.naive('na', 'banana')
m = pm.naive('oct', 'octagenarian octopus')
print(n)
print(m)

n = pm.kmp('na', 'banana')
m = pm.kmp('oct', 'octagenarian octopus')
print(n)
print(m)
