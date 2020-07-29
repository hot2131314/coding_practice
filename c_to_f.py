import random

r = random.randint(1, 100)
count = 0

while True:
	count +=  1

	num = input("請猜數字: ")
	num = int(num)
	print("正確答案是：", r)
	if r == num:
		print("終於答對了")
		print("你總共猜了 ", count, " 次！")
		break
	elif num > r:
			print("你猜的數字比答案大")
	elif num < r:
			print("你猜的數字比答案小")
	print("你總共猜了 ", count, " 次！")

