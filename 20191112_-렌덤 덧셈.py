import random

a = random.randint (1, 100)
b = random.randint (1, 100)

print (a, "+", b , "=")

c = int (input("answer?"))

if a + b == c :
      print ("정답입니다^^.")
else :
      print ("축하합니다.바보입니다.")
