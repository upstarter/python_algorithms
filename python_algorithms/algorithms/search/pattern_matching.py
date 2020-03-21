class PatternMatch(object):

    # naive string pattern matching
    def naive(self, pat, txt):
        m = len(pat)
        n = len(txt)

        # A loop to slide pat[] one by one
        for i in range(0, n - m + 1):

            # For current index i, check for pattern match
            j = 0
            while j < m:
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
        for c in pat[1:]:
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
                j += 1  # Next char matched, increment position

            if j == len(pat):
                matches.append(i - (j - 1))
                j = j - 1

        return matches

    def value(self, letter, power):
        return (26 ** power) * (ord(letter) - 96)

    def rubin_hash(self, prev, start, new, k):
        return (prev - self.value(start, k - 1)) * 26 + self.value(new, 0)

    def rubin_karp(self, pattern, string):
        matches = []
        k = len(pattern)

        pattern_val = 0
        for i, char in enumerate(pattern):
            pattern_val += self.value(char, k - i - 1)

        hash_val = 0
        for i, char in enumerate(string[:k]):
            hash_val += self.value(char, k - i - 1)

        if pattern_val == hash_val:
            if string[:k] == pattern:
                matches.append(0)

        for i in range(len(string) - k):
            hash_val = self.rubin_hash(hash_val, string[i], string[i + k], k)
            if pattern_val == hash_val:
                if string[i + 1 : i + k + 1] == pattern:
                    matches.append(i + 1)

        return matches


pm = PatternMatch()
n = pm.naive("na", "banana")
m = pm.naive("oct", "octagenarian octopus")
print(n)
print(m)

n = pm.kmp("na", "banana")
m = pm.kmp("oct", "octagenarian octopus")
print(n)
print(m)

n = pm.rubin_karp("na", "banana")
m = pm.rubin_karp("oct", "octagenarian octopus")
print(n)
print(m)
