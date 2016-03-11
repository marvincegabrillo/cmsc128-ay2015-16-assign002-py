def getHammingDistance(str1, str2):
	distance = 0;
	
	if type(str1) != str or type(str2) != str:     #Error Checking
		return "Error: Invalid Arguments"
	if len(str1) != len(str2):
		return "Length of strings are not equal"
	for i in range (0, len(str1)):
		if str1[i]!=str2[i]:						#if the two charcters from each string are not equal increment the distance
			distance = distance + 1
	return distance
	


def	countSubsPattern(str1,str2):
	if type(str1) != str or type(str2) != str:		#Error checking
		return "Error: Invalid Arguments"
	start = 0
	end = len(str2)									
	count = 0
	for i in range(0,len(str1)):
		if str2 == str1[start:end]:					#Range splice the string accdg to the length of the substring			
			count = count + 1						#then if the spliced string is equal to the substring increment
		start = start + 1							#Then move to the next splice
		end = end +1
	return count

def isValidString(str1,alph):
	if type(str1) != str or type(str2) != str:  	#Error checking
		return "Error: Invalid Arguments"
	check = 0
	for i in range(0,len(str1)):					#Check per charcter the string and compare it it to each charcter in the alphabet
		for j in range(0,len(alph)):				#if found increment checker variable(check)
			if(str1[i] == alph[j]):					
				check = check + 1;
				break
	if(check != len(str1)):							#if checker is not equal to the length of the string atleast one of it is not in the
		return False								#the alphabet
	else:
		return True	

def getSkew(str1,index):
	if type(str1) != str or type(index) != int:
		return "Error: Invalid Arguments"				#Error Checking
	if index < 1 or index > len(str1):
		return "Error: Index invalid"
	numG = 0 
	numC = 0
	for i in range(0,index):
		if(str1[i] == "G"):							#Count the G and C 's  up to the given index
			numG = numG + 1							#Then get their difference
		elif(str1[i] == "C"):
			numC = numC + 1
	skew = numG - numC			
	return skew	

def getMaxSkewN(str1,index):
	if type(str1) != str or type(index) != int:
		return "Error: Invalid Arguments"
	if index < 1 or index > len(str1):
		return "Error: Index invalid"	
	maxList = []
	for i in range(1,index+1):					#Repeatedly call getSkew up to the given index and store each in a list
		maxList.append(getSkew(str1,i))			#Return the maximum value in list
	return max(maxList)	
	
def getMinSkewN(str1,index):
	if type(str1) != str or type(index) != int:
		return "Error: Invalid Arguments"
	if index < 1 or index > len(str1):
		return "Error: Index invalid"	
	minList = []
	for i in range(1,index+1):					#Same as before call getSkew up to the given index then return
		minList.append(getSkew(str1,i))			#Minimum value
	return min(minList)		


	
