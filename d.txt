def average(l):
  return sum(l)/len(l)
def stdev(j):
  import math 
  num=0
  for n in j:
    num+=(n-average(j))**2
  div=len(j)
  return math.sqrt(num/div)
def choice_random():
  import random
  choice_random=random.choice(lista)
  return choice_random
