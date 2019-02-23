total_legs = 94
total_heads = 35
for hens in range(1,total_heads):
	goats = 35-hens
	if 2*hens + 4*goats == total_legs:
		print("Hens : {}\nGoats : {}".format(hens,goats))
