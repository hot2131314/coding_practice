products = []

while True:
	name = input("請輸入商品名稱： ")
	if name == 'q':
		break
	price = input("請輸入價格： ")
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

print(products[0][1])


#上面 8-10行可以快速寫
p = [name, price]
#或是更快速，連 18 行都不用寫

while True:
	name = input("請輸入商品名稱： ")
	if name == 'q':
		break
	price = input("請輸入價格： ")
	products.append([name, price])
print(products)
