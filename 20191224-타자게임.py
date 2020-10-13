import random
import time

w = ["펭수","김명중","박재영","망고","쥐","똑이","누가 치킨 소리를 내었어","물범","둘리","지구 끝까지 쫓아가서 맴매 할꺼야","오징어","눈치 챙겨","펭하","펭빠"]
n = 1

print ("[타자게임] 준비되면 앤터!!")
input()

start = time.time()
q = random.choice(w)

while n <= 5 :
      print ("문제", n)
      print (q)
      x = input()
      if q == x  :
            print("정답!!")
            n = n+1
            q = random.choice(w)
      else :
            print("땡!!")

end = time.time()
et = end - start
et2 = format(et, ".2f")

print ("타자시간 : ", et2, "초")
