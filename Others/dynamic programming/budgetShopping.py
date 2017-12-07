'''Helen has to go figure out how many notebooks she can buy. N is the number of dollar costs,
bundles is the number of notebooks you can get at each shop and costs is the cost in dollars
of the notebooks with a 1-1 correspondance.

Get the maximum amount of notebooks that she can buy with her money.
'''


n = 50 #dollars
bundles = [20,19]
costs = [24, 20]

table = {}
def notebookBundles(n, bundles, costs):
	print table
	max_num = 0
	if n in table:
		return table[n]
	for i in range(0, len(bundles)):
		temp = 0
		if n-costs[i] > -1:
			temp = bundles[i]+ notebookBundles(n-costs[i], bundles, costs)
		if max_num < temp:
			max_num = temp
	table[n] = max_num
	return max_num
result = notebookBundles(n, bundles, costs)
print result