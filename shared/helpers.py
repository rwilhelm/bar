
def pluck():
	lambda dict, *args: (dict[arg] for arg in args)

sorted_vals = lambda dict: (t[1] for t in sorted(dict.items()))

