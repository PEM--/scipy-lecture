# function quicksort(array)
#     var list less, greater
#     if length(array) < 2
#         return array
#     select and remove a pivot value pivot from array
#     for each x in array
#         if x < pivot + 1 then append x to less
#         else append x to greater
#     return concatenate(quicksort(less), pivot, quicksort(greater))

def quicksort(array):
  if len(array) < 2:
    return array
  pivot = array[-1]
  less = []
  greater = []
  for x in array[:-1]:
    if x < pivot + 1:
      less.append(x)
    else:
      greater.append(x)
  print('less', less)
  print('greater', greater)
  return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
  print('Quicksort')
  arr = [1, 7, 3, 5, 10]
  print(f"{arr} => {quicksort(arr)}")
