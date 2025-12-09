######################### PART 1 #########################
# input_file  = open('inputs/day9-sample.txt', 'r')
input_file  = open('inputs/day9-full.txt', 'r')

all_red_spots = []
# Crete the map
for line in input_file:
    line = line.strip().split(",")
    line[0] = int(line[0])
    line[1] = int(line[1])
    print(f"Line : {line}")
    all_red_spots.append(line)
print(all_red_spots)

max_area = 0
points = []
for spot in all_red_spots:
    for other_spot in all_red_spots:
        w = abs(spot[0] - other_spot[0]) + 1
        l = abs(spot[1] - other_spot[1]) + 1
        area = w * l
        if area > max_area:
            max_area = area
            points = [spot, other_spot]
print(f"Max Area : {max_area}")
print(f"Points : {points}")


######################## PART 2 #########################

pass