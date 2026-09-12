"""For this challenge you will determine if a stream of digits occurs in a string.
have the function number_stream(str) take the str parameter being passed which will contain the numbers 2 through 9,
and determine if there is a consecutive stream of digits of at least N length where N is the actual digit value.
If so, return the string true, otherwise return the string false. For example: if str is "6539923335" then your program
should return the string true because there is a consecutive stream of 3's of length 3. The input string will always
contain at least one digit."""

"""
traverse the string
have a temp string that will increase if values are consecutive
if the next value is not the same as current consecutive values
break and analyze the length of the temp string
if the length matches the digit value than return true
else continue until the string has been fully traversed
"""

test_one ="5556293383563665"
test_two = "5788888888882339999"
test_three = "6539923335"

def number_stream(value):
	stringed = str(value)
	results = False

	if len(stringed) < 1:
		print(results)

	temp = []
	count = 1

	while len(temp) < len(stringed) :
		for f in stringed:
			temp += [f]
			if len(temp) > 1:
				if temp[-1] == temp[-2] :
					count += 1
					if int(f) == count:
						results = True
				else:
					count = 1

	print(results)

number_stream(test_three)

