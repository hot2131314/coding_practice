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





#列印商品和價格
for p in products:
	print(p[0]) #會印出每一個商品名稱
	print(p[0], '的價格是', p[1])

#底下的 'pruduct_write.txt' 不一定要先建立，他會自動建立這檔案
#CSV 檔通常都用逗號做區隔
with open('product_write.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')#這樣寫，會產生亂碼，所以才要加 encoding = utf-8
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

#讀取  .split() 切割完的結果是 list
products = []
with open('product_write.csv', 'r', encoding='utf-8') as f:
	for line in f:
		s = line.strip().split(',')
		print(s)

#以上的寫法可以用更簡單方法寫：
products = []
with open('product_write.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)