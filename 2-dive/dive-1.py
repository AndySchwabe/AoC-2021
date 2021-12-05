def diver(drections: list):
    location = 0
    horiz = 0
    depth = 0

    for rection in drections:
        rection_list = rection.split(" ")
        orientation = rection_list[0]
        spaces = int(rection_list[1])
        if orientation == 'up':
            depth = depth - spaces
        elif orientation == 'down':
            depth = depth + spaces
        elif orientation == 'forward':
            horiz = horiz + spaces
        elif orientation == 'back':
            print("There is no going back")
        else:
            print("Andy is a moron")

    location = horiz * depth

    return location


if __name__ == '__main__':
    # Data from AoC site
    with open('input.txt') as file:
        # Add each line to the depths list as an explicit int
        positional_input = []
        for line in file:
            positional_input.append(line.strip())

    new_loc = diver(drections=positional_input)
    print(new_loc)
