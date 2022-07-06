def num_pair(l, k):
  ''' Given a list of integers l and an integer k,
  return True iff there are at least two integers
  in l such that their sum is equal to k
  '''
  return False


assert num_pair([1, 2, 3, 4], 7)
assert num_pair([1, 2], 3)
assert not num_pair([1], 1)
assert not num_pair([], 0)
