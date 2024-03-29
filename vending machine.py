a = int(input("물건 가격: "))
b = int(input("지불 가격: "))


if b>a:
  c = b - a
  value1 = c//1000
  c -= 1000*value1
  value2  = c//500
  c -= 500*value2
  value3  = c //100






else:
  print("돈을 더 넣으세요")
