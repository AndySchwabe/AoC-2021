def broomer_return_to_the_depths(depths: list):
    counter = 0

    for i in range(len(depths) - 3):
        first_three = depths[i] + depths[i + 1] + depths[i + 2]
        second_three = depths[i + 1] + depths[i + 2] + depths[i + 3]
        if first_three < second_three:
            counter = counter + 1
    return counter


if __name__ == '__main__':
    # Data from AoC site
    with open('input.txt') as file:
        # Add each line to the depths list as an explicit int
        depth_input = []
        for line in file:
            depth_input.append(int(line.strip()))

    depth_count = broomer_return_to_the_depths(depths=depth_input)
    print(depth_count)
