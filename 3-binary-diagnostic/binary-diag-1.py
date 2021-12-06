def diagnoser(gobbledygook: list):
    gamma_rate = []
    epsilon_rate = []
    power_rate = 0

    for i in range(len(gobbledygook[0])):
        count_of_zero = 0
        count_of_one = 0
        for gobbledy in gobbledygook:
            if int(gobbledy[i]) == 0:
                count_of_zero = count_of_zero + 1
            elif int(gobbledy[i]) == 1:
                count_of_one = count_of_one + 1
            else:
                print("Non-binary digit found")

        if count_of_zero > count_of_one:
            gamma_rate.append(0)
            epsilon_rate.append(1)
        elif count_of_zero < count_of_one:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            print("Things are equal")

    gamma = int(''.join([str(gamma_bit) for gamma_bit in gamma_rate]), 2)
    epsilon = int(''.join([str(epsilon_bit) for epsilon_bit in epsilon_rate]), 2)
    power_rate = gamma * epsilon

    return power_rate


if __name__ == '__main__':
    # Data from AoC site
    with open('input.txt') as file:
        # Add each line to the depths list as an explicit int
        binary_message = []
        for line in file:
            binary_message.append(line.strip())

    power_consumption = diagnoser(gobbledygook=binary_message)
    print(power_consumption)
