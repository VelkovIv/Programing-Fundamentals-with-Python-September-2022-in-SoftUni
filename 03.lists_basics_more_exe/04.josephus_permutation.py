list_for_permutaion = input().split()
permutation_factor = int(input())
execution_list = []
start_index = 0

while list_for_permutaion != [] :
    start_index = (start_index + permutation_factor - 1) % len(list_for_permutaion)
    execution_list.append(list_for_permutaion.pop(start_index))

print(f"[{', '.join(execution_list)}]")
