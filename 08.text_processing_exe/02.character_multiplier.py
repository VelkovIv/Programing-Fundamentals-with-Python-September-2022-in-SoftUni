___doc___ = """
Create a program that receives two strings on a single line separated by a single space. 
Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] 
and add the result to the total sum, then continue with the next two characters. 
If one of the strings is longer than the other, add the remaining character codes to the total sum 
without multiplication.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
George Peter
Output--->
52114
---------------------------------------------------
--->Input
123 522
Output--->
7647
---------------------------------------------------
--->Input
a aaaa
Output--->
9700
---------------------------------------------------
"""


def characters_multiplier_func(left_string, right_string):
    total_sum = 0
    if len(left_string) == len(right_string):
        for index in range(len(left_string)):
            total_sum += ord(left_string[index]) * ord(right_string[index])

    elif len(left_string) > len(right_string):
        for index in range(len(right_string)):
            total_sum += ord(left_string[index]) * ord(right_string[index])

        second_pass = len(left_string) - len(right_string)

        for index in range(second_pass):
            new_index = len(right_string) + index
            total_sum += ord(left_string[new_index])
    else:
        for index in range(len(left_string)):
            total_sum += ord(left_string[index]) * ord(right_string[index])

        second_pass = len(right_string) - len(left_string)

        for index in range(second_pass):
            new_index = len(left_string) + index
            total_sum += ord(right_string[new_index])

    return total_sum


strings = input().split()

left_string, right_string = strings[0], strings[1]

total_sum = characters_multiplier_func(left_string, right_string)
print(total_sum)
