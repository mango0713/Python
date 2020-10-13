a = input ("숫자를 입력하세요")
a2 = int (a)

for x in range (1, 10001) :
      if a2%x == 0 :
            print (x,"는", a2 ,"의 약수 입나다")
      else :
            print (x, "는 약수가 아닙니다" )
 
