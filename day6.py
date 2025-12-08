######################### PART 1 #########################
# # input_file  = open('inputs/day6-sample.txt', 'r')
# input_file  = open('inputs/day6-full.txt', 'r')
#
# numbers_dict = {}
# for line in input_file:
#     line = line.strip()
#     line = line.split()
#     if line.__contains__("*"):
#         last_line = line
#         break
#     print(f"Line: {line}")
#     num_count = 0
#     for num in line:
#         if not num_count in numbers_dict:
#             numbers_dict[num_count] = [int(num)]
#         else:
#             numbers_dict[num_count].append(int(num))
#
#         num_count += 1
#
# print(f"Numbers Dict : {numbers_dict}")
# print(f"Last Line: {last_line}")
#
# totals = {}
# for problem in numbers_dict:
#     print(f"Problem: {problem}")
#     total = None
#     if last_line[problem] == "*":
#         # Multiply
#         for num in numbers_dict[problem]:
#             if not total:
#                 total = num
#             else:
#                 total = total * num
#     elif last_line[problem] == "+":
#         # Add
#         for num in numbers_dict[problem]:
#             if not total:
#                 total = num
#             else:
#                 total = total + num
#     else:
#         print(f"Invalid problem {problem}, last line is {last_line[problem]}")
#         exit(1)
#     totals[problem] = total
# print(f"Totals: {totals}")
#
# final_total = 0
# for probelm_num in totals:
#     final_total += totals[probelm_num]
#
# print(f"Total of all totals : {final_total}")

######################### PART 2 #########################

pass