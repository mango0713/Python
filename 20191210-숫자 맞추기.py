import random

def make_question() :
      
      a = random.randint(1, 20)
      b = random.randint(1, 20)
      op = random.randint(1, 3)
      

      q = str(a)

      if op == 1 :
            q = q + "+"
      if op == 2 :
            q = q + "-"
      if op == 3 :
            q = q + "*"

      q = q + str(b)
       
      return q


sc1 = 0
sc2 = 0

for x in range (10) :
      q = make_question()
      print (q)
      r = int(input("="))
              
      if eval(q) == r :
              print("정답")
              sc1 = sc1 + 1

      else :
            print("틀였오.....")
            sc2 = sc2 + 1


print ("정답 : ", sc1, "오답 :", sc2)   
      
            
