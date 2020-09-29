with open('palavras.txt') as file:
    lines = sorted(set(line.rstrip().lower() for line in file))

with open('palavras.txt', 'w') as file:
    file.writelines(line + '\n' for line in lines)
