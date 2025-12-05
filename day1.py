######################### PART 1 #########################
# input_file  = open('inputs/day1-sample.txt', 'r')
# input_file  = open('inputs/day1-full.txt', 'r')
#
#
# def right(pointer, how_many):
#     print(f"Pointer : {pointer}, Right : {how_many}")
#     for x in range(int(how_many)):
#         if pointer == 99:
#             pointer = 0
#         else:
#             pointer += 1
#     print(f"New Pointer : {pointer}")
#     return pointer
#
#
# def left(pointer, how_many):
#     print(f"Pointer : {pointer}, Left : {how_many}")
#     for x in range(int(how_many)):
#         if pointer == 0:
#             pointer = 99
#         else:
#             pointer -= 1
#     print(f"New Pointer : {pointer}")
#     return pointer
#
# pointer_pos = 50
# total_0_count = 0
#
# for line in input_file:
#     line = line.strip()
#     if line[0] == 'L':
#         pointer_pos = left(pointer_pos, line.split('L')[1])
#     if line[0] == 'R':
#         pointer_pos = right(pointer_pos, line.split('R')[1])
#     if pointer_pos == 0:
#         total_0_count += 1
#
# print(f"Total 0 count : {total_0_count}")


######################### PART 2 #########################

# input_file  = open('inputs/day1-sample.txt', 'r')
input_file  = open('inputs/day1-full.txt', 'r')

pointer_pos = 50
global total_0_count
total_0_count = 0

def right(pointer, how_many):
    global total_0_count
    for _ in range(int(how_many)):
        pointer = (pointer + 1) % 100
        if pointer == 0:
            total_0_count += 1
    return pointer

def left(pointer, how_many):
    global total_0_count
    for _ in range(int(how_many)):
        pointer = (pointer - 1) % 100
        if pointer == 0:
            total_0_count += 1
    return pointer

for line in input_file:
    line = line.strip()
    dir = line[0]
    amount = int(line[1:])

    if dir == 'L':
        pointer_pos = left(pointer_pos, amount)
    else:
        pointer_pos = right(pointer_pos, amount)

print(f"Total 0 count : {total_0_count}")