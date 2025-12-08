######################### PART 1 #########################
# # input_file  = open('inputs/day5-sample.txt', 'r')
# input_file  = open('inputs/day5-full.txt', 'r')
#
# fresh_ingredients_ranges = []
# ingredients_to_check = []
# listing_fresh = True
#
# def check_if_in_ranges(all_ranges, number):
#     for the_range in all_ranges:
#         if the_range[0] <= number <= the_range[1]:
#             return True
#     return False
#
#
# for line in input_file:
#     line = line.strip()
#     if line == '':
#         listing_fresh = False
#         continue
#     if listing_fresh:
#         line = line.split('-')
#         fresh_ingredients_ranges.append([int(line[0]), int(line[1])])
#     else:
#         ingredients_to_check.append(int(line))
#
# fresh_ingredients_ranges.sort()
# # print(fresh_ingredients_ranges)
# # print(ingredients_to_check)
#
# total_fresh_ingredients_ranges = 0
# for ingredient in ingredients_to_check:
#     if check_if_in_ranges(fresh_ingredients_ranges, ingredient):
#         total_fresh_ingredients_ranges += 1
# print(f"Total fresh ingredients: {total_fresh_ingredients_ranges}")
import copy

######################### PART 2 #########################

# input_file  = open('inputs/day5-sample.txt', 'r')
input_file  = open('inputs/day5-full.txt', 'r')

fresh_ingredients_ranges = []
listing_fresh = True


def completely_contained(all_ranges, range_to_check):
    tmp_ranges = copy.deepcopy(all_ranges)
    tmp_ranges.remove(range_to_check)
    for the_range in tmp_ranges:
        if the_range[0] <= range_to_check[0] <= the_range[1]:
            if the_range[0] <= range_to_check[1] <= the_range[1]:
                all_ranges.remove(range_to_check)
                return True
    return False

def remove_completely_contained(all_ranges):
    # Check if range completely contained in another. Remove if so
    # print(f"Before Removals : {all_ranges}")
    for the_ranges in all_ranges:
        if completely_contained(all_ranges, the_ranges):
            pass
            # print(f"Range {the_ranges} completely contained in another.")
            # print(f"All ranges : {all_ranges}")

def lower_contained(all_ranges, range_to_check):
    tmp_ranges = copy.deepcopy(all_ranges)
    tmp_ranges.remove(range_to_check)
    range_edited = False
    for the_range in tmp_ranges:
        if the_range[0] <= range_to_check[0] <= the_range[1]:
            if the_range[0] <= range_to_check[1] <= the_range[1]:
                pass
            else:
                # print(f"Old range : {the_range}")
                the_range[1] = range_to_check[1]
                range_edited = True
                # print(f"New range : {the_range}")
    # print(f"Tmp Ranges : {tmp_ranges}")
    if not range_edited:
        return all_ranges
    return tmp_ranges


for line in input_file:
    line = line.strip()
    if line == '':
        listing_fresh = False
        continue
    if listing_fresh:
        line = line.split('-')
        fresh_ingredients_ranges.append([int(line[0]), int(line[1])])
    else:
        pass

fresh_ingredients_ranges.sort()

remove_completely_contained(fresh_ingredients_ranges)

# print("Removed completely contained ranges.\n\n")
# print(f"After Contained Removals : {fresh_ingredients_ranges}")
tmp_all_ranges = []
while True:
    # print(f"\n\nLen tmp_all_ranges : {len(tmp_all_ranges)}, Len fresh_ingredients_ranges : {len(fresh_ingredients_ranges)}")
    for ranges in fresh_ingredients_ranges:
        tmp_all_ranges = lower_contained(fresh_ingredients_ranges, ranges)
        if len(tmp_all_ranges) < len(fresh_ingredients_ranges):
            break
    # print(f"Len tmp_all_ranges : {len(tmp_all_ranges)}, Len fresh_ingredients_ranges : {len(fresh_ingredients_ranges)}")
    # print(f"All Ranges : {fresh_ingredients_ranges}, Tmp All Ranges : {tmp_all_ranges}")

    # Check if range completely contained in another. Remove if so
    remove_completely_contained(tmp_all_ranges)

    if len(tmp_all_ranges) == len(fresh_ingredients_ranges):
        break
    fresh_ingredients_ranges = tmp_all_ranges


# print(f"All Ranges : {fresh_ingredients_ranges}")
final_total = 0
for r in fresh_ingredients_ranges:
    total = (r[1] - r[0]) + 1
    final_total += total
print(f"Final Total : {final_total}")