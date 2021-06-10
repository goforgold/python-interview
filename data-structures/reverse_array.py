def reverseArray(a):
  start, end = 0, (len(a)-1)
  while start < end:
    a[start], a[end] = a[end], a[start]
    start+=1
    end-=1
  return a


a = [1, 4, 3, 2, 10]

print(reverseArray(a))
