def equal_columns(m):
  '''Given an NxM matrix of integers,
  return true iff it has two identical
  columns
  '''
  return False


assert equal_columns([[1, 2, 3], [3, 2, 1]])
assert not equal_columns([[1, 2], [2, 1]])
assert not equal_columns([[]])
assert not equal_columns(
  [
    [1, 3, 4, 5, 1],
    [2, 4, 6, 2, 2],
    [7, 2, 3, 2, 7]
  ]
)
