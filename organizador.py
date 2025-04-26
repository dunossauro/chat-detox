from locale import LC_ALL, setlocale, strxfrm
setlocale(LC_ALL, '')

arquivos = ['palavras.txt', 'frases.txt']


def formata(arquivo):
    with open(arquivo) as file:
        lines = sorted(
            set(line.rstrip().lower() for line in file),
            key=strxfrm
        )

    with open(arquivo, 'w') as file:
        file.writelines(line + '\n' for line in lines)


for arquivo in arquivos:
    formata(arquivo)
