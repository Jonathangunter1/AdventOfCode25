######################### PART 1 #########################
# input_file  = open('inputs/day7-sample.txt', 'r')
# # input_file  = open('inputs/day7-full.txt', 'r')
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
# whole_map = {}
# line_count = 0
#
# # Crete the map
# for line in input_file:
#     line = line.strip()
#     line_list = []
#     for char in line:
#         line_list.append(char)
#     whole_map[line_count] = line_list
#     line_count += 1
#
# beam_splits = 0
#
# for row in whole_map:
#     if row == 0:
#         pass
#     else:
#         position = 0
#         for char in whole_map[row]:
#             # Up Center
#             row_to_check = row - 1
#             position_to_check = position
#             if within_bounds(row_to_check, position_to_check, whole_map):
#                 up_center = whole_map[row_to_check][position_to_check]
#                 if up_center == "S":
#                     whole_map[row][position] = "|"
#                 elif up_center == "|":
#                     if whole_map[row][position] == "^":
#                         whole_map[row][position - 1] = "|"
#                         whole_map[row][position + 1] = "|"
#                         beam_splits += 1
#                     elif whole_map[row][position] == ".":
#                         whole_map[row][position] = "|"
#             position += 1
#
# print_map(whole_map)
# print(f"Beam splits: {beam_splits}")
######################### PART 2 #########################

pass