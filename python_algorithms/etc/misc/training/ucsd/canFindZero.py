
def can_find_zero(lst, i=0):
	
	# is first elem 0?
	# if not move lft/rt according to value
	# is new value == 0?
	# if not continue process above until 0 found else False

	found = False

	while lst[i] != 0 and not found:
		elem = lst[i]
		if elem == 0:
			found = True
		else:
			found = recurse_elems(lst, i )

	return found

def recurse_elems(lst, i):
		found = False
		el = lst[i]
		lft = i - list[i]
		rt = i + lst[i]
		if el == 0:
			return True
		else:
			if lft < 0 or rt > lst[len(lst)-1]:
				return False
			found = recurse_elems(lst, lft)
			if found:
				return True
			found = recurse_elems(lst, rt)
			if found:
				return True


		return found

canFindZero([3, 7, 0, 2, 8, 3, 7, 6]) == True


def shouldSave(userData):
	avail_bal = userData['accounts']['balance']['available']

	transactions = userData['transactions']
	summ = 0
	for t in transactions:
		amt = t['amount']
		summ += amt

	pct = summ/avail_bal
	if avail_bal >= summ:
		return True
	else:
		return False
