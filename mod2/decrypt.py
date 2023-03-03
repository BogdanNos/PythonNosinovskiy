import sys
def decrypt(line):
    newLine = ''
    i = 0
    while i < len(line) - 1:
        if(line[i] != '.'):
            newLine += line[i]
        if(line[i] == line[i+1] == '.'):
            newLine = newLine[0:len(newLine) - 1]
            i+=1
        i+=1
    print(newLine + (line[-1] if line[-1] != '.' else ''))

if __name__ == '__main__':
    decrypt(sys.stdin.read())