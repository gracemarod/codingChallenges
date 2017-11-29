''' I was asked to implement a function that given an integer number num, 
it returns the a string representation of the number, comma separated.'''

def seperateNumbersUS(num,sty):
    
	sty = sty.lower()
	oldStr = str(num)[::-1]
	newStr = ""

	for i in range(0,len(oldStr)):
		newStr += oldStr[i]
		if (sty=="us" and (i+1)%3 == 0 and i != len(oldStr)-1):
			newStr += ","
		elif(sty=="indian" and i==2):
			newStr += ","
		elif(sty=="indian" and i >2 and i%2==0 and i != len(oldStr)-1):
		 	newStr += ","

	print "The ", style, " version of the input is: ", newStr[::-1]

num = 111236780
style = "indian"
seperateNumbersUS(num,style)

style = "US"
seperateNumbersUS(num,style)