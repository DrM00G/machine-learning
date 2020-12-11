def exclam(number):
  if number == 0:
    return 1
  else:
    result=1
    for n in range(number):
      result=result*(n+1)
    return result

def choose(n,r):
  return (exclam(n)/(exclam(n-r)))

print(choose(20,2))
print((choose(20,4)*choose(30,6))/choose(50,10))
print((choose(20,0)*choose(30,10)+choose(20,1)*choose(30,9)+choose(20,2)*choose(30,8))/choose(50,10))