___doc___ = """
Using a dictionary comprehension, write a program that receives country names on the first line, 
separated by comma and space ", ", and their corresponding capital cities on the second line 
(again separated by comma and space ", "). 
Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

--Input--
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London

--Output--
Bulgaria -> Sofia
Romania -> Bucharest
Germany -> Berlin
England -> London
----------------------------------------
--Input--
Bulgaria, Germany, France
Varna, Frankfurt, Paris

--Output--
Bulgaria -> Varna
Germany -> Frankfurt
France -> Paris

"""

countries = input().split(', ')
capitals = input().split(', ')

countries_with_capitals = {countries[i]:capitals[i] for i in range(len(countries))}

for country, capital in countries_with_capitals.items():
    print(f'{country} -> {capital}')