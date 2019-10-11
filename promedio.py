
def average_temp(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)


if __name__ == "__main__":
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temp(temps)

    print('La temperatura promedio es: {}'.format(average))
