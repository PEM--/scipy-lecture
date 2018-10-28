from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(i):
  if i == 0:
    return 0
  if i == 1:
    return 1
  return fibonacci(i - 1) + fibonacci(i - 2)

if __name__ == '__main__':
  print('Fibonacci')
  print(f"3  => {fibonacci(3)}")
  print(f"10 => {fibonacci(10)}")
  print(f"15 => {fibonacci(15)}")