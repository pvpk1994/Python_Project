'''
Regular Expressions in Python
Author: Pavan Kumar Paluri
'''

import re

# Aim: TO EXTRACT WORD "CAT"
given_str = "an example word: cat!!!"
matcher = re.search(r'word:\s+(\w\w\w)', given_str)
if matcher:
    print(f"match found is: {matcher.group(1)}")  # group(1) posts the content after '+'
else:
    print(f"match not found")

# periods search
given_word = 'piig'
match = re.search(r"...g", given_word)  # the number of .'s represent # of periods
print(match.group())

# Integer searches
match = re.search(r'p\d\d\dg', 'p123g')
print(match.group())

# Character Searches
match = re.search(r'\W\W\W', "@@@abs")  # \W => extracts any char, \w=> extracts a char in word
print(match.group())

# Repetitions
match = re.search(r'pi+', 'piiiig')  # i+ - one/more i's
print(match.group())

match = re.search(r'pi+', "piiigiiiii")  # i+ - only until a breaking char is found
print(match.group())

# * - Extract only Numbers with variable number of spaces
match = re.search(r'\d\s*\d\s*\d\s*\d', "xx 1  3 7  9  xxxxxx")
print(match.group())

# ^ - Matches only with the start of the string
match = re.search(r"b\w+", "foobar")   # match should only return bar
print(str(match.group()))  # convert res into a string

# Emails Examples - Pattern Matching
given_email_id = "purple pvpk1994@google.com money dishwasher stuff"
# In the given text, task is to find out the valid email id i.e., {alice-b@google.com}

# Attempt - 1
match = re.search(r"\w@\w", given_email_id)
print(match.group())  # only prints d@g

# Attempt - 2
match = re.search(r"\w+@\w+", given_email_id)
print(match.group())  # Only prints bsd@google but we want whole email ID

# Final Attempt
match = re.search(r'[\w.-]+@[\w.-]+', given_email_id)
print(match.group())

# Group Extractions - Extract the username of the user from his emailID
given_str = "pvpk1994-bsd@gmail.com"
match = re.search(r'([\w-]+)@([\w.]+)', given_str)
print(f"Username of the user is {str(match.group(1))}")
print(f"Email Server is {str(match.group(2))}")

# Findall - re.search() returns the first match of a pattern,
#           However, findall() finds ALL matches and returns them as list of strings with
#           each string representing one match
# Sample: A txt with lot of email Addresses
given_email_list = "1. pvpk199423sdc@hotmail.com 2. asunsus8@live.com 3. daniel_vista@gmail.com"
email_matcher = re.findall(r'[\w-]+@[\w.]+', given_email_list)  # Extracts all the email-IDs into a list
for email in email_matcher:
    print(email)


# Findall with Files
'''
1. Instead of iterating through every line in file and then using findall() in each line is 
    rather cumbersome, 
2. Easier approach is to use re.findall(r'', f.read())
'''
filer = open('emails.txt', 'r')
# find all email-IDs
email_matcher = re.findall(r'[\w.-]+@[\w.-]+', filer.read())
for email in email_matcher:
    print(f"email is {email}")
filer.close()

# Findall and Groups - Grp 1 has usernames and Grp2 has hosts
strn = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w.-]+)@([\w.-]+)', strn)  # Produces list of tuples
for tup in tuples:
    print(tup[0])  # Username
    print(tup[1])  # Host
