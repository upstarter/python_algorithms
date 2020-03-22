def absSort(arr):
	"""
	@param arr: int[]
	@return: int[]
  [-2, 0, 1]
  [-2, 0, -2, 2, 7]
	"""

  return sorted(arr, key=lambda x: abs(x))
