for i in range(100,0,-1):
	if i == 1:
		print("\n" + str(i) + "  bottle of beer on the wall, " + str(i) + " bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
	else:
		print("\n" + str(i) + "  bottles of beer on the wall, " + str(i) + " bottles of beer. Take one down and pass it around, " + str(i - 1) + " bottles of beer on the wall.")