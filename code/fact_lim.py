def fact_lim(n,lim):
   sum = 0
   for i in range(1, n+1):
      pivot = 1
      for j in range(i-lim+1,i+1):
          if(j>0):
             pivot=pivot*j
      sum += pivot
   return sum
                 
print fact_lim(5,4)
