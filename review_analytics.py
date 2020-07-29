data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print("檔案讀取完畢，總共有 ", len(data), " 筆資料")

#刪選留言平均長度小於 100 的
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("留言平均長度是 ", sum_len/len(data))

count = 0
for d in data:
	if len(d) < 100: 
		count += 1
print("總共有 ", count, " 筆小於100")

#或是以下寫法

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有 ", len(new), " 筆留言小於 100")


#搜尋留言裡面有 "good" 字串
good_count = 0
for d in data:
	if "good" in d:
		good_count +=1
print("有 good 的留言總共有 ", good_count, " 筆")

#或是以下寫法
good = []
for d in data:
	if "good" in d:
		good.append(d)
print("總共有 ", len(good), " 筆小於 100 字")

