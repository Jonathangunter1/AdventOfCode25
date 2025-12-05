######################### PART 1 #########################
# # input_file  = open('inputs/day4-sample.txt', 'r')
# input_file  = open('inputs/day4-full.txt', 'r')
#
# def print_map(the_map):
#     for the_row in the_map:
#         print(the_map[the_row])
#
# def within_bounds(the_row, the_pos, the_map):
#     if the_row < 0 or the_row >= len(the_map):
#         # print(f"ROW {the_row}, Position {the_pos} out of bounds")
#         return False
#     if the_pos < 0 or the_pos >= len(the_map[the_row]):
#         # print(f"Row {the_row}, POSITON {the_pos} out of bounds")
#         return False
#     # print(f"Row {the_row}, Position {the_pos} in bounds")
#     return True
#
# def how_many_stacks_surrounding(ul, uc, ur, sl, sr, dl, dc, dr):
#     total_stacks = 0
#     the_points = [ul, uc, ur, sl, sr, dl, dc, dr]
#     # print(f"The Points: {the_points}")
#     for point in the_points:
#         if point and point != '.':
#             total_stacks += 1
#     return total_stacks
#
#
# whole_map = {}
# line_count = 0
# total_accessible = 0
#
# # Crete the map
# for line in input_file:
#     line = line.strip()
#     line_list = []
#     for char in line:
#         line_list.append(char)
#     whole_map[line_count] = line_list
#     line_count += 1
# print_map(whole_map)
#
# # Check how many can be accessed
# for row in whole_map:
#     # print(whole_map[row])
#     position = 0
#     for value in whole_map[row]:
#         # print(f"Position is ({row},{position}), Value is {value}")
#
#         if value != ".":
#             up_left = up_center = up_right = same_left = same_right = down_left = down_center = down_right = None
#
#             # Up Left
#             row_to_check = row - 1
#             position_to_check = position - 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 up_left = whole_map[row_to_check][position_to_check]
#
#             # Up Center
#             row_to_check = row - 1
#             position_to_check = position
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 up_center = whole_map[row_to_check][position_to_check]
#
#             # Up Right
#             row_to_check = row - 1
#             position_to_check = position + 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 up_right = whole_map[row_to_check][position_to_check]
#
#             # Left Same Row
#             row_to_check = row
#             position_to_check = position - 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 same_left =  whole_map[row_to_check][position_to_check]
#
#             # Right Same Row
#             row_to_check = row
#             position_to_check = position + 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 same_right = whole_map[row_to_check][position_to_check]
#
#             # Down Left
#             row_to_check = row + 1
#             position_to_check = position - 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 down_left = whole_map[row_to_check][position_to_check]
#
#             # Down Center
#             row_to_check = row + 1
#             position_to_check = position
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 down_center = whole_map[row_to_check][position_to_check]
#
#             # Down Right
#             row_to_check = row + 1
#             position_to_check = position + 1
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 down_right = whole_map[row_to_check][position_to_check]
#
#             # print(f"{up_left} {up_center} {up_right}")
#             # print(f"{same_left} !{value}! {same_right}")
#             # print(f"{down_left} {down_center} {down_right}")
#
#             total_surrounding_stacks = how_many_stacks_surrounding(up_left, up_center, up_right, same_left, same_right, down_left, down_center, down_right)
#             # print(f"Total surrounding stacks: {total_surrounding_stacks}")
#             if total_surrounding_stacks < 4:
#                 whole_map[row][position] = 'X'
#                 total_accessible += 1
#
#         position += 1
# print_map(whole_map)
# print(f"Total accessible: {total_accessible}")

######################### PART 2 #########################

# input_file  = open('inputs/day4-sample.txt', 'r')
input_file  = open('inputs/day4-full.txt', 'r')

def print_map(the_map):
    for the_row in the_map:
        print(the_map[the_row])

def within_bounds(the_row, the_pos, the_map):
    if the_row < 0 or the_row >= len(the_map):
        # print(f"ROW {the_row}, Position {the_pos} out of bounds")
        return False
    if the_pos < 0 or the_pos >= len(the_map[the_row]):
        # print(f"Row {the_row}, POSITON {the_pos} out of bounds")
        return False
    # print(f"Row {the_row}, Position {the_pos} in bounds")
    return True

def how_many_stacks_surrounding(ul, uc, ur, sl, sr, dl, dc, dr):
    total_stacks = 0
    the_points = [ul, uc, ur, sl, sr, dl, dc, dr]
    # print(f"The Points: {the_points}")
    for point in the_points:
        if point and point == '@':
            total_stacks += 1
    return total_stacks

def count_xs_in_map(the_map):
    x_count = 0
    for the_row in the_map:
        the_pos = 0
        for _ in the_map[the_row]:
            if the_map[the_row][the_pos] == 'X':
                x_count += 1
            the_pos += 1
    return x_count



whole_map = {}
line_count = 0

# Crete the map
for line in input_file:
    line = line.strip()
    line_list = []
    for char in line:
        line_list.append(char)
    whole_map[line_count] = line_list
    line_count += 1

def check_accesses(the_whole_map):
    total_accessible = 0
    # Check how many can be accessed
    for row in the_whole_map:
        # print(the_whole_map[row])
        position = 0
        for value in the_whole_map[row]:
            # print(f"Position is ({row},{position}), Value is {value}")

            if value != ".":
                up_left = up_center = up_right = same_left = same_right = down_left = down_center = down_right = None

                # Up Left
                row_to_check = row - 1
                position_to_check = position - 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    up_left = the_whole_map[row_to_check][position_to_check]

                # Up Center
                row_to_check = row - 1
                position_to_check = position
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    up_center = the_whole_map[row_to_check][position_to_check]

                # Up Right
                row_to_check = row - 1
                position_to_check = position + 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    up_right = the_whole_map[row_to_check][position_to_check]

                # Left Same Row
                row_to_check = row
                position_to_check = position - 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    same_left =  the_whole_map[row_to_check][position_to_check]

                # Right Same Row
                row_to_check = row
                position_to_check = position + 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    same_right = the_whole_map[row_to_check][position_to_check]

                # Down Left
                row_to_check = row + 1
                position_to_check = position - 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    down_left = the_whole_map[row_to_check][position_to_check]

                # Down Center
                row_to_check = row + 1
                position_to_check = position
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    down_center = the_whole_map[row_to_check][position_to_check]

                # Down Right
                row_to_check = row + 1
                position_to_check = position + 1
                if within_bounds(row_to_check, position_to_check, the_whole_map):
                    down_right = the_whole_map[row_to_check][position_to_check]

                # print(f"{up_left} {up_center} {up_right}")
                # print(f"{same_left} !{value}! {same_right}")
                # print(f"{down_left} {down_center} {down_right}")

                total_surrounding_stacks = how_many_stacks_surrounding(up_left, up_center, up_right, same_left, same_right, down_left, down_center, down_right)
                # print(f"Total surrounding stacks: {total_surrounding_stacks}")
                if total_surrounding_stacks < 4:
                    the_whole_map[row][position] = 'X'
                    total_accessible += 1
            position += 1
    print(f"Map after this run : ")
    print_map(whole_map)
    print("#"*200)
    return total_accessible

total_after = 1
total_before = 0

while total_after > total_before:
    total_before = count_xs_in_map(whole_map)
    run_total = check_accesses(whole_map)
    print(f"Run total : {run_total}")
    total_after = count_xs_in_map(whole_map)

