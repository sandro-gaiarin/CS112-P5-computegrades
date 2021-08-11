#Keys: 'Name', 'Projects', 'Homeworks', 'zyBooks', 'Quizzes', 'Midterm', 'Final'

def grades_to_str(grades):
	final_str = '' #return value. 
	#final_str += 'whatever bits of string need to be added'

	for key in grades: #step through keys
		final_str += str(key + ': ' + str(grades[key]) + '\n')
		# build out the returns string from the keys and their
		# associated values, with a newline in between.

	return(final_str)




def projects_weighted_avg(grades):

	project_grades = list(grades['Projects'])
	project_grades.sort()
	# get the project grades into a list of their own, then sort them
	# in ascending order.

	total_grade = (len(project_grades) * 100) - 100
	# total value of all grades added up. len provides the number of
	# assignments, times 100, minus 100 to account for the halved grades.

	project_grades[0] /= 2
	project_grades[1] /= 2
	#divide the two lowest scores by 2 and adjust them

	final_grade = 0 #number of all grades added up

	for grade in project_grades:
		final_grade += grade
		#add up all the grades in the list

	return((final_grade/total_grade) * 100) 
	#return the weighted average grade




def homeworks_weighted_avg(grades):

	homework_grades = list(grades['Homeworks'])
	homework_grades.sort()
	# get the homework grades into a list, sort in ascending order

	total_grade = (len(homework_grades) - 1) * 100
	# total value of homework grades. subtract 1 from len because
	# the lowest grade is dropped.

	del homework_grades[0] #removes the lowest homework grade

	final_grade = 0 #all grades added up

	for grade in homework_grades:
		final_grade += grade

	return((final_grade/total_grade) * 100)
	#return weighted average




def zybooks_weighted_avg(grades):

	zy_grades = list(grades['zyBooks'])
	zy_grades.sort()

	total_grade = (len(zy_grades) - 2) * 100
	# subtract 2 from len because the two lowest grades are dropped.

	del zy_grades[0]
	del zy_grades[0] #delete the two lowest values

	final_grade = 0 #all grades added up

	for grade in zy_grades:
		final_grade += grade

	return((final_grade/total_grade) * 100)
	#return weighted average




def quiz_weighted_avg(grades):

	quiz_grades = list(grades['Quizzes'])
	quiz_grades.sort()

	total_grade = (len(quiz_grades) - 2) * 100
	# subtract 2 from len because the two lowest grades are dropped.

	del quiz_grades[0]
	del quiz_grades[0] #delete two lowest grades

	final_grade = 0

	for grade in quiz_grades:
		final_grade += grade

	return((final_grade/total_grade) * 100)
	#return weighted average




def compute_final_grade(grades):

	#Using previous functions, get all the average grades together.
	project_grade = projects_weighted_avg(grades) #40%
	homework_grade = homeworks_weighted_avg(grades) #7%
	zy_grade = zybooks_weighted_avg(grades) #5%
	quiz_grade = quiz_weighted_avg(grades) #10%
	midterm = grades['Midterm'] #13%
	final_exam = grades['Final'] #25%

	if final_exam > midterm: 
	#Replace midterm grade with final if final is better.
		midterm = final_exam
		# The project sheet states, under Final, 'May replace
		# if midterm is better', but I think it's a typo,
		# as replacing the final exam grade with the midterm
		# grade causes the tester to fail.

	final_grade = ((project_grade * .4) + (homework_grade * .07) + 
					(zy_grade * .05) + (quiz_grade * .1) + 
					(midterm * .13) + (final_exam * .25))
		#add up all the grades, multiplying them by their weighted percentage

	return(final_grade)




def read_grades_file(filename):

	grades_dict = {} #dictionary to build upon

	file = open(filename) #open the file
	file_str_list = file.readlines()
	# get a list of the contents of the file, each line becoming
	# a string inside the file_str_list list
	

	#--------------------------------------------------------------------------
	# FILE READLINES: List of strings. Each string contains elements of a line.
	#--------------------------------------------------------------------------
	# file_str_list:
	#============================
	# Keys:			Index Value:
	#============================
	# Name			0
	# Projects  	1
	# Homeworks 	2
	# zyBooks 		3
	# Quizzes 		4
	# Midterm 		5
	# Final 		6
	#
	# For the Projects, Homeworks, zyBooks, and Quizzes, the strings have
	# to be split, then each individual string has to be converted into
	# a float value.


	#--------------------------------------------------------------------------
	# Name:
	#--------------------------------------------------------------------------
	name_list = file_str_list[0]
	name_list = name_list.split('\n')
	#reading from the file adds a newline after the name. this removes "\n"


	grades_dict['Name'] = name_list[0]
	# since removing from the end adds an empty string to the list containing
	# the name, we pull from index 0 so we don't include the empty string.

	#--------------------------------------------------------------------------
	# Projects:
	#--------------------------------------------------------------------------
	project_str_list = file_str_list[1] 
	#puts the string of project grades into its own list
	project_str_list = project_str_list.split() 
	#splits the list by whitespace

	project_list = []

	for string in project_str_list: #go through the strings
		xfloat = float(string) #change them to floats
		project_list.append(xfloat) # add them to the final list

	grades_dict['Projects'] = project_list

	#--------------------------------------------------------------------------
	# Homeworks:
	#--------------------------------------------------------------------------
	homework_str_list = file_str_list[2] 
	#puts the string of homework grades into its own list
	homework_str_list = homework_str_list.split() 
	#splits the list by whitespace

	homework_list = []

	for string in homework_str_list: #go through the strings
		xfloat = float(string) #change to floats
		homework_list.append(xfloat) #add floats to the final list

	grades_dict['Homeworks'] = homework_list

	#--------------------------------------------------------------------------
	# zyBooks:
	#--------------------------------------------------------------------------
	zy_str_list = file_str_list[3]
	#puts string of zybooks grades into their own list
	zy_str_list = zy_str_list.split()
	#splits the list by whitespace

	zy_list = []

	for string in zy_str_list: #go through the strings
		xfloat = float(string) #change to floats
		zy_list.append(xfloat) #add floats to the final list

	grades_dict['zyBooks'] = zy_list

	#--------------------------------------------------------------------------
	# Quizzes:
	#--------------------------------------------------------------------------
	quiz_str_list = file_str_list[4]
	#puts string of quiz grades into their own list
	quiz_str_list = quiz_str_list.split()
	#splits list by whitespace

	quiz_list = []

	for string in quiz_str_list: #go through strings
		xfloat = float(string) #change to floats
		quiz_list.append(xfloat) #add floats to final list

	grades_dict['Quizzes'] = quiz_list

	#--------------------------------------------------------------------------
	# Midterm:
	#--------------------------------------------------------------------------
	grades_dict['Midterm'] = float(file_str_list[5])
	#turn the string of midterm grade to a float, then add it to grades_dict

	#--------------------------------------------------------------------------
	# Final:
	#--------------------------------------------------------------------------
	grades_dict['Final'] = float(file_str_list[6])
	#turn the string of the final grade to a float, then add it to grades_dict

	return(grades_dict)

# I should have used a helper function for Projects, Homeworks, zyBooks, 
# and Quizzes, but I didn't think of it until I was finished. Whoops.



def write_grades_file(filename, grades):

	gradefile = open(filename, 'w') #opens the file for writing

	for key in grades: #step through keys
		if type(grades[key]) == list:
			# some of the key values are lists, 
			# we want to print strings instead
			for x in grades[key]:
				gradefile.write(str(x) + ' ')
				# steps through the values in the list, then
				# adds them to the file with a space in between.
				# also changes the x values from floats to strings.

		else: #this one's for everything that's not a list
			gradefile.write(str(grades[key]))

		if key != 'Final': 
		#'Final' is the last key, and shouldn't have a newline after it!
			gradefile.write('\n')
			#end each loop with a newline to prep for the next loop
