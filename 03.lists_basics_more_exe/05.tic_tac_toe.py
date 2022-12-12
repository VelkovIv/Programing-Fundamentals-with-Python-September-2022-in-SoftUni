first_line = list(map(int,input().split()))
second_line = list(map(int,input().split()))
third_line = list(map(int,input().split()))

line_1, line_2, line_3 = set(first_line), set(second_line), set(third_line)
vert_1 = {first_line[0], second_line[0], third_line[0]}
vert_2 = {first_line[1], second_line[1], third_line[1]}
vert_3 = {first_line[2], second_line[2], third_line[2]}
diag_1 = {first_line[0], second_line[1], third_line[2]}
diag_2 = {first_line[2], second_line[1], third_line[0]}

is_draw = True

for index in range(1,3):
    if line_1 == {index} or line_2 == {index} or line_3 == {index} or vert_1 == {index} or \
            vert_2 == {index} or vert_3 == {index} or diag_1 == {index} or diag_2 == {index} :
        if index == 1:
            is_draw = False
            print('First player won')
            break
        else :
            is_draw = False
            print('Second player won')
            break

if is_draw:
    print('Draw!')

