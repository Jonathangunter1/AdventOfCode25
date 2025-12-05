######################### PART 1 #########################
# input_file  = open('inputs/day2-sample.txt', 'r')
# input_file  = open('inputs/day2-full.txt', 'r')
#
# total_invalid = 0
#
# for line in input_file:
#     line = line.strip()
#     line = line.split(',')
#     for ids in line:
#         ids = ids.split('-')
#         for number in range(int(ids[0]), int(ids[1]) + 1):
#             if len(str(number)) % 2 == 0:
#                 # These are the only possible because they are even
#                 # print(number)
#                 number = str(number)
#                 first_half = number[:int(len(number) / 2)]
#                 second_half = number[int(len(number) / 2):]
#                 # print(f"First half: {first_half}, Second half: {second_half}")
#                 if first_half == second_half:
#                     # print("INVALID!!")
#                     total_invalid += int(number)
# print(f"Total invalid: {total_invalid}")


######################### PART 2 #########################
# input_file  = open('inputs/day2-sample.txt', 'r')
input_file  = open('inputs/day2-full.txt', 'r')

total_invalid = 0

# The numbers never got larger than 10 digits so im going to brute force this
def one_repeat(number):
    number = str(number)
    for char in number:
        if char != number[1]:
            return False
    return True

def two_repeat(number):
    number = str(number)
    if not len(number) % 2 == 0:
        return False
    if not len(number) >= 4:
        return False
    pairs = [number[i:i + 2] for i in range(0, len(number), 2)]
    # print(pairs)
    if len(set(pairs)) == 1:
        return True
    else:
        return False

def three_repeat(number):
    number = str(number)
    if not len(number) >= 6:
        return False
    pairs = [number[i:i + 3] for i in range(0, len(number), 3)]
    # print(pairs)
    if len(set(pairs)) == 1:
        return True
    else:
        return False

def four_repeat(number):
    number = str(number)
    if not len(number) % 2 == 0:
        return False
    if not len(number) >= 8:
        return False
    pairs = [number[i:i + 4] for i in range(0, len(number), 4)]
    # print(pairs)
    if len(set(pairs)) == 1:
        return True
    else:
        return False

def five_repeat(number):
    number = str(number)
    if not len(number) >= 10:
        return False
    pairs = [number[i:i + 5] for i in range(0, len(number), 5)]
    # print(pairs)
    if len(set(pairs)) == 1:
        return True
    else:
        return False


for line in input_file:
    line = line.strip()
    line = line.split(',')
    for ids in line:
        ids = ids.split('-')
        for the_number in range(int(ids[0]), int(ids[1]) + 1):
            the_number = str(the_number)
            # print(the_number)
            if len(the_number) == 1:
                continue
            if one_repeat(the_number):
                # print("One Repeat")
                total_invalid += int(the_number)
                continue
            if two_repeat(the_number):
                # print("Two Repeat")
                total_invalid += int(the_number)
                continue
            if three_repeat(the_number):
                # print("Three Repeat")
                total_invalid += int(the_number)
                continue
            if four_repeat(the_number):
                # print("Four Repeat")
                total_invalid += int(the_number)
                continue
            if five_repeat(the_number):
                # print("Five Repeat")
                total_invalid += int(the_number)
                continue

print(f"Total invalid: {total_invalid}")