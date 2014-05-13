# data: list of tuples
# tuple = (t1, t2)
# t1 = probability that instance is positive
# t2 = true class label either "P" (positive) or "N" (negative)
def roc(data):
	# sort by score
	s = sorted(data, key = lambda x: x[0], reverse = True)
	n = 0 # number of negatives
	p = 0 # number of positives
	for i in s:
		if i[0] < 0 or i[0] > 1:
			raise Exception("invalid value for probability")
		# count number of negatives and positives instances
		if i[1] == "P": 
			p += 1
		elif i[1] == "N": 
			n += 1
		else: 
			raise Exception("unexpected value for category")
	if p == 0 or n == 0:
		raise Exception("at least one example for each category is required")
	f = -1.0
	tp = 0
	fp = 0
	tpr = []
	fpr = []
	for i in s:
		pr = i[0]
		classlabel = i[1] # P/N
		if pr != f:
			fpr.append(float(fp) / n)
			tpr.append(float(tp) / p)
			f = classlabel
		if classlabel == "P":
			tp += 1
		else:
			fp += 1
	fpr.append(float(fp) / n)
	tpr.append(float(tp) / p)
	return [fpr, tpr]

if __name__ == "__main__":
	data = []
	data.append([0.1, "P"])
	data.append([0.2, "P"])
	data.append([0.2, "N"])
	data.append([0.3, "P"])
	data.append([0.3, "P"])
	data.append([0.4, "P"])
	data.append([0.5, "P"])
	data.append([0.6, "N"])
	data.append([0.7, "N"])
	data.append([0.9, "N"])
	fpr, tpr = roc(data)
	for i in zip(fpr, tpr):
		print (i)
