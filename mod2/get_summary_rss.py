def get_summary_rss(output_file):
    with open(output_file) as file:
        word = ['B', 'KiB', 'MiB', 'GiB']
        sum = 0
        div = 0
        for line in file.readlines()[1:]:
            column = line.split()[5]
            sum += int(column)
        while(sum >= 1024):
            div += 1
            sum = sum / 1024
        print(round(sum, 3), word[div])

if __name__ == '__main__':
    get_summary_rss('output.txt')