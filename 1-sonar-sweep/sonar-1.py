def broomer(depths: list):
    counter = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[(i + 1)]:
            counter = counter + 1
    return counter


if __name__ == '__main__':
    # Data from AoC site
    with open('input.txt') as file:
        # Add each line to the depths list as an explicit int
        depth_input = []
        for line in file:
            depth_input.append(int(line.strip()))

    depth_count = broomer(depths=depth_input)
    print(depth_count)
