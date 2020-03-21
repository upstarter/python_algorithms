import sys
import re

thismodule = sys.modules[__name__]

# find all functions in current module matching a pattern
funcRegex = re.compile(r".*_to_.*")
funcs = filter(funcRegex.search, dir())
print(funcs)
