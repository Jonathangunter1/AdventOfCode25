######################### PART 1 #########################
# # input_file  = open('inputs/day3-sample.txt', 'r')
# input_file  = open('inputs/day3-full.txt', 'r')
#
# def get_highest_number(numbers):
#     highest = 0
#     for number in numbers:
#         number = int(number)
#         if number > highest:
#             highest = number
#     print(f"Highest number is : {highest}")
#     if numbers.count(f"{highest}") >= 2:
#         return highest, True
#     return highest, False
#
# total = 0
#
# for line in input_file:
#     highest_possible = ""
#     rest_of_line = ""
#     line = line.strip()
#     print(line)
#     high_num, double = get_highest_number(line)
#     if double:
#         highest_possible = str(high_num) + str(high_num)
#     else:
#         if line.endswith(f"{high_num}"):
#             print("Line ends with highest num.")
#             rest_of_line = line.split(str(high_num))[0]
#             second_high, throw_away = get_highest_number(rest_of_line)
#             highest_possible = str(second_high) + str(high_num)
#         else:
#             # Get the second highest number after the highest
#             rest_of_line = line.split(str(high_num))[1]
#             second_high, throw_away = get_highest_number(rest_of_line)
#             highest_possible = str(high_num) + str(second_high)
#     print(f"Highest possible number is : {highest_possible}")
#     total += int(highest_possible)
# print(f"Total number is : {total}")

######################### PART 2 #########################

pass