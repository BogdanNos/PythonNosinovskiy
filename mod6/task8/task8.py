import re
letter = {
"2":"[a|b|c]",
"3":"[d|e|f]",
"4":"[g|h|i]",
"5":"[j|k|l]",
"6":"[m|n|o]",
"7":"[p|q|r|s]",
"8":"[t|u|v]",
"9":"[w|x|y|z]"
}
file = '\n' + open('words.txt').read().lower() + '\n'

def my_t9(numbers):
    combination = '[\n]'
    for number in numbers:
        combination += letter[number]
    combination += '[\n]'
    return re.findall(combination, file)


if __name__ == '__main__':
    print(*my_t9('22736368'))