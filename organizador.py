with open('palavras.txt') as file:
    lines = file.readlines()

with open('palavras.txt', 'w') as file:
    file.writelines(sorted(set(lines)))
