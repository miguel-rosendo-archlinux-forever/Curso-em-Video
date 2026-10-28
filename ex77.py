palavras = ('curso', 'vídeo', 'python', 'aprenda', 'progamar', 'guanabara', 'gustavo')
for p in palavras:
    print(f'na palavra "{p.upper()}" temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)