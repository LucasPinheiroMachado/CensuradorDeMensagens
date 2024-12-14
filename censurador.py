import string

def censura(mensagem, palavrasCensuradas):
    palavras = mensagem.split()
    mensagemSensurada = ''
    censura = ''
    for palavra in palavras:
        palavraLimpa = palavra.strip(string.punctuation).lower()
        if palavraLimpa in palavrasCensuradas:
            for i in range(len(palavra)):
                censura += '*'
            mensagemSensurada += censura + ' '
            censura = ''
        else:
            mensagemSensurada += palavra + ' '
    return mensagemSensurada