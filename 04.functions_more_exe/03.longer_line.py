def coordinate_check(point_x1, point_y1, point_x2, point_y2, point_x3, point_y3, point_x4, point_y4) :
    check_list = []
    p1 = abs(point_x1) + abs(point_y1)
    check_list.append(p1)
    p2 = abs(point_x2) + abs(point_y2)
    check_list.append(p2)
    p3 = abs(point_x3) + abs(point_y3)
    check_list.append(p3)
    p4 = abs(point_x4) + abs(point_y4)
    check_list.append(p4)
    check_list.sort(reverse=True)
    if check_list[0] == p1 :
        x2 = point_x1
        y2 = point_y1
    elif check_list[0] == p2 :
        x2 = point_x2
        y2 = point_y2
    elif check_list[0] == p3 :
        x2 = point_x3
        y2 = point_y3
    else :
        x2 = point_x4
        y2 = point_y4
    if check_list[1] == p1 :
        x1 = point_x1
        y1 = point_y1
    elif check_list[1] == p2 :
        x1 = point_x2
        y1 = point_y2
    elif check_list[1] == p3 :
        x1 = point_x3
        y1 = point_y3
    else :
        x1 = point_x4
        y1 = point_y4

    return f'({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})'


point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
point_x3 = float(input())
point_y3 = float(input())
point_x4 = float(input())
point_y4 = float(input())
print(coordinate_check(point_x1, point_y1, point_x2, point_y2, point_x3, point_y3, point_x4, point_y4))
