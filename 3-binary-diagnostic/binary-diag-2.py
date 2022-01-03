def diagnoser(gobbledygook: list):
    gamma_rate = []
    epsilon_rate = []
    power_rate = 0

    # gamma == ox
    ox_list = gobbledygook
    # epsilon = c02
    co2_list = gobbledygook

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

        for x in ox_list:
            if x[i] != gamma_rate[i]:
                print("hi")
                if len(ox_list) != 1:
                    ox_list.remove(x)
            else:
                if len(co2_list) != 1:
                    co2_list.remove(x)

    gamma = int(''.join([str(gamma_bit) for gamma_bit in gamma_rate]), 2)
    epsilon = int(''.join([str(epsilon_bit) for epsilon_bit in epsilon_rate]), 2)
    power_rate = gamma * epsilon

    print(ox_list)
    print(co2_list)

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
