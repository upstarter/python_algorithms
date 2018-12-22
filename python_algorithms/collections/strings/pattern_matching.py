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

    # # knuth-morris-pratt algorithm for pattern matching strings
    # def knp(pat, str):
    #
    # # rubin-karp string pattern matching
    # def rubinKarp(pat, str):


pm = PatternMatch()
n = pm.naive('na', 'banana')
m = pm.naive('oct', 'octagenarian octopus')
print(n)
print(m)
