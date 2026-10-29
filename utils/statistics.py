def calculate_average(numbers):#среднее арифметическое
    sum=0
    for chisla in numbers:
        sum+=chisla
    return sum/len(numbers)



def find_min(numbers):#минимальое
    mini=numbers[0]
    for chisla in numbers:
        if chisla<mini:
            mini=chisla
    return mini


def find_max(numbers):
    maxi=numbers[0]
    for chisla in numbers:
        if chisla>maxi:
            maxi=chisla
    return maxi