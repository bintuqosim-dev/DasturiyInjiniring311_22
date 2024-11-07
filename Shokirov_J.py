import numpy as np

def Fibona(n):
  A=np.array([1,1])
  if n<0:
    return "Iltimos 0 dan katta son kiriting"
  elif n==0:
    return (np.nan)
  elif n==1:
    return 1
  elif n==2:
    return np.array([1,1])
  else:
    for i in range(n-2):
      A=np.append(A,A[i]+A[i+1])
    return A
try:
  n=int(input("Nechta fibonanchi sonlarni ko'rmoqchisiz? "))
  print(Fibona(n))
except:
  print("Butun son kiriting")