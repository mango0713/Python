import random

total = int(input("total :"))

sum = 0

for x  in range (total) :
    
     if random.randint (1, 6) == 2 :
  
         sum = sum + 1

print (sum/total)
     
