print "What school do you want to know about?" 
school = raw_input("> ")

checker = 0 #used to check if the input is in the database
while checker = 0: 
	for schoolName in database:  #schoolName and database need to be figured out to read through every school name
		if school = schoolName:
			checker = 1
	if checker = 0:
		print "Sorry! Doesn't look like we have that school. Try again?"
		school = raw_input("> ")
#Guarantee now exists that the school entered by user has a match in the database.