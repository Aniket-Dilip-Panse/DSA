#A Python3 Program to check if the given
#string is a pangram or not
# pangram string means a string which contains all the aplhabet from 'a' to 'z' the alphabet should not be repeated and must be distinct example:- ethier 'a' or 'A' will be present in string
#Returns true if the string is pangram else false
def checkPangram(string):
	# Initialize a set of characters
	char_set = set()
	
	for ch in string:
		# If the character is already
		# a lowercase character
		if ch >= 'a' and ch <= 'z':
			char_set.add(ch)
	
		# In case of a uppercase character
		if ch >= 'A' and ch <= 'Z':
			# convert to lowercase
			ch = ch.lower()
			char_set.add(ch)

	# check if the size is 26 or not
	return len(char_set) == 26

#Driver Program to test above functions
string = "The quick brown fox jumps over the lazy dog"
if checkPangram(string) == True:
	print("It is a Pangram")
else:
	print("It is Not a Pangram")
