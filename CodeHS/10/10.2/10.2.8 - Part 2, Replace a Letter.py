def replace_at_index(string, index, letter): #function that replaces part of the string with a letter
	return string[ :index] + letter + string[index+1: ]
