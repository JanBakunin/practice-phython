def remove_loop(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

def remove_set(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print (*a)
print (remove_loop(a))
print (remove_set(a))