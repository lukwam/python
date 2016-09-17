# Enter your code here. Read input from STDIN. Print output to STDOUT 
import math
import sys

# find all equally-lengthed pairs of staff pieces that can be made from the original
[input, ] = sys.stdin
input=str(input)
fullLength = len(input)

def reverse(string):
	l=len(string)
	if l <= 1:
		return string
	newstring=string[l-1]+reverse(string[0:l-1])
	return newstring

# start with the longest equally-lengthed pairs and cycle through all of them until they've all been tested or the longest one has been found

def weight(string):
	s=str(string)
	weight=0
	i=0
	while i < len(s) and s[i] != '<':
		count=i+1
		char=s[i]
		weight += int(char) * int(count)
		i+=1
	return weight


# find the longest possible half-staff
length = int(math.floor(fullLength/2))
found = 0
# starting with the longest, for each length of staff, find all the possible pairs of staffs of that length
while (length>0):
    
    # starting with index 0 find a half staff of the current length
    index1=0
    while (index1+length+length <= fullLength):
        staff1 = input[index1:index1+length]
    
        index2=index1+length
        while (index2+length) < fullLength:
            staff2 = input[index2:index2+length]
	    print staff1,staff2
            if weight(staff1) == weight(staff2):
		found = 1
                break
            elif weight(staff1) == weight(reverse(staff2)):
		found = 1
                break
            elif weight(reverse(staff1)) == weight(staff2):
		found = 1
                break
            elif weight(reverse(staff1)) == weight(reverse(staff2)):
		found = 1
                break
    	    if found:
    		print 'Index1: '+str(index1)+', Index2: '+str(index2)+', Length: '+str(length)+'\n'
		print 'Original string ('+str(fullLength)+'): '+input
		print 'String 1: '+staff1+' '+str(weight(staff1))
		print 'String 2: '+staff2+' '+str(weight(staff2))
		sys.exit(0)

            index2+=1
        index1+=1
    length-=1


