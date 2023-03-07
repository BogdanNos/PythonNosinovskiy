import sys
def get_mean_size(data):
    sum = 0
    count = 0
    div = 0
    word = ['B', 'KiB', 'MiB', 'GiB']
    for line in data.readlines()[1:]:
        column = line.split()[4]
        sum += int(column)
        count += 1
    if(count == 0):
        print('Нет файлов')
    else:
        result = sum / count
        while (result >= 1024):
            div += 1
            result = result / 1024
        print(round(result, 2), word[div])

if __name__ == '__main__':
    get_mean_size(sys.stdin)