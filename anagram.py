def check_anagram(string1='Mary', string2='Army'):
	string1_count = {}
	string2_count = {}

	if len(string1) == len(string2):
		for i in range(len(string1)):
			letter = string1[i].lower()
			if letter not in string1_count.keys():
				string1_count[letter] = 1
			else:
				string1_count[letter] =+ 1

			letter = string2[i].lower()
			if letter not in string2_count.keys():
				string2_count[letter] = 1
			else:
				string2_count[letter] =+ 1

		if string1_count == string2_count:
			print("It is Anagram")

	else:
		print("Not An Anagram")

# string1 = "Mary"
# string2= "Army"

string1, string2 = str(input("Enter the 2 strings space separated: ")).split()
check_anagram(string1, string2)
