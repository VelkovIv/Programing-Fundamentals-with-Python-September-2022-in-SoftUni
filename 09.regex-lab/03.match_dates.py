___doc___ = """
Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". 
Use capturing groups in your regular expression.
Compose the Regular Expression
Every valid date has the following characteristics:
•	It always starts with two digits, followed by a separator
•	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
•	After that, it has a separator and exactly 4 digits (for the year).
•	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
•	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). 
Use a group backreference to check for this.
You can follow the table below to help with composing your RegEx:
Match ALL of these	Match NONE of these
13/Jul/1928, 10-Nov-1934, 25.Dec.1937	01/Jan-1951, 23/sept/1973, 1/Feb/2016
Use capturing groups for the day, month, and year.
Since this problem requires more complex RegEx, which includes named capturing groups, 
we will take a look at how to construct it:
•	First off, we do not want anything at the start of our date, so we're going to use a word boundary "\b":
 
•	Next, we are going to match the day by telling our RegEx to match exactly two digits, 
and since we want to extract the day from the match later, we're going to put it in a capturing group:
 
•	Next comes the separator – either a hyphen, period, or forward slash. We can use a character class for this:
 
Since we want to use the separator, we matched here to match the same separator further into the date. 
We're going to put it in a capturing group:
 
•	Next comes the month, which consists of a capital Latin letter and exactly two lowercase Latin letters:
 
•	Next, we are going to match the same separator we matched earlier. We can use a backreference for that:
 
•	Next up, we are going to match the year, which consists of exactly 4 digits:
 
•	Finally, since we do not want to match the date if there's anything else glued to it, 
we're going to use another word boundary for the end:
 
Now it is time to find all the valid dates in the input and 
print each date in the following format: "Day: {day}, Month: {month}, Year: {year}", each on a new line.


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
Output--->
Day: 13, Month: Jul, Year: 1928
Day: 10, Month: Nov, Year: 1934
Day: 25, Month: Dec, Year: 1937

---------------------------------------------------

"""

import re

dates = input()

searched_pattern = r'(\d{2})([/.-])([A-Z][a-z]{2})\2([0-9]{4})'

results = re.findall(searched_pattern,dates)

for match in results:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
