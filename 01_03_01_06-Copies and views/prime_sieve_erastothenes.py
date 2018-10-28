import numpy as np

#  Input: an integer n > 1.
 
#  Let A be an array of Boolean values, indexed by integers 2 to n,
#  initially all set to true.
 
#  for i = 2, 3, 4, ..., not exceeding √n:
#    if A[i] is true:
#      for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
#        A[j] := false.
 
#  Output: all i such that A[i] is true.

is_prime = np.ones((100), dtype=bool)
# 0 & 1 are not prime
is_prime[:2] = False
N_max = int(np.sqrt(len(is_prime) - 1))
for i in range(2, N_max + 1):
  if is_prime[i]:
    for j in range(i**2, len(is_prime), i):
      is_prime[j] = False

print(np.nonzero(is_prime))

