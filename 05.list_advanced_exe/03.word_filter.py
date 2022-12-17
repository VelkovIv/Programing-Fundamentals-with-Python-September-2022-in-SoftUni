text = input().split(' ')
new_list = [text[index] for index in range(len(text)) if len(text[index]) % 2 == 0]
print(* new_list, sep='\n')