#!python3
#PhoneEmailExtractor.py - finds phone and email addresses on the clipboard

import re, pyperclip

def Extractor():
#phone number regex pattern		
		phoneRegex = re.compile(r'''(
			(\d{3}|\(\d{3}\))?				 #areacode
			(\s|-|\.)?						 #separator
			(\d{3})							 #first 3 numbers
			(\s|-|\.)						 #separator
			(\d{4}) 						 #last 4 digits
			(\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
			)''',re.VERBOSE)
#email regex
		emailRegex = re.compile(r'''(
			[a-zA-Z0-9.+_%-]+  #username
			@                  #@ symbol
			[a-zA-Z0-9.-]+     #domain name
			(\.[a-zA-Z]{2,4})  #dot-something
			)''',re.VERBOSE)

		twitterRegex = re.compile(r'^Twitter:@')

#find matching regex in clipboard
		text = str(pyperclip.paste())

		match = []
		for groups in phoneRegex.findall(text):
			phoneNum = '-'.join([groups[1], groups[3], groups[5]])
			if groups[8] !='':
				phoneNum +='x' + groups[8]
			match.append(phoneNum)


		for groups in emailRegex.findall(text):
			match.append(groups[0])

		for groups in twitterRegex.findall(text):
			match.append(groups[0])
		
#copy results to clipboard
		if len(match) > 0:
			pyperclip.copy('\n'.join(match))
			print('Results found include:')
			print('\n'.join(match))
		else:
			print('No Phone Numbers or Emails Extracted ')


Extractor()		
