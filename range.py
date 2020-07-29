#range(5) 是[0,1,2,3,4]
import random


for i in range(5):
	r = random.randint(1, 1000)
	print("這是第 ", i+1, "次產生隨機數： ", r)