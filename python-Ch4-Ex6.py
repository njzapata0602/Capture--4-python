#Nick Zapata - Ch4 - ex6 - 2/16/18

def computerpay(h,r):
	if h<=40 :
		p = r * h
	else :
		p = r * 40 + (1.5 * r * h (h - 40))
	return p
	
hrs_st = input("Enter Hours: ")
hrs = float(hrs_st)
print (computerpay(hrs, 10.5))
		