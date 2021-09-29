data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('Finished Reading Data', 'Total', len(data), 'reviews')

sum_len = 0
for review in data:
	sum_len = sum_len + len(review)

print('The average amount of word in the each reviews is ', sum_len/len(data))