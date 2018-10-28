def wallis_step(i):
  return 4 * i**2 / (4 * i**2 - 1)

def wallis(max_i):
  res = float(wallis_step(1))
  for i in range(2, max_i + 1):
    res = res * float(wallis_step(i))
  return 2 * res

if __name__ == '__main__':
  print('Approximation of PI using Wallis formula')
  print(f"10       => {wallis(10)}")
  print(f"100      => {wallis(100)}")
  print(f"1_000    => {wallis(1_000)}")