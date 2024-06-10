
DESCRIPTOGRAFAR= 0
CRIPTOGRAFAR = 1

alfabeto =  'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ!@#$%¨&*{}[]()=+-_1234567890.,:;?/\<>' 



def cifra(dado, chave, modo):
    novodado = ''
    for c in dado:
        posicao = alfabeto.find(c)
    if posicao == -1:
        novodado += c
    else:
        novaposicao = posicao + chave if modo == CRIPTOGRAFAR else posicao - chave
        novaposicao = novaposicao % len(alfabeto)
        novodado += alfabeto[novaposicao:novaposicao+1]
    return novodado

#A chave é o deslocamento que a letra terá no alfabeto
def inicio():

    qtd= len(alfabeto)
    print('A quantidade atual de caracteres no alfabeto é: ', qtd)

    chave = int(input('Selecione uma chave: '))
    textooriginal = input('Selecione seu texto a ser criptografado ou descriptografado: ')
    metodo= input('Selecione seu método desejado: \n0 = Descriptografar\n1 = Criptografar\n--> ')

    if metodo == '0':
        print('Descriptografia realizada com sucesso!')
        print('Texto original: ', textooriginal)
        textodescriptografado = cifra(textooriginal, chave, DESCRIPTOGRAFAR)
        print('Texto Descriptografado: ', textodescriptografado)

    elif metodo == '1':
        print('Criptografia realizada com sucesso!')
        print('Texto original: ', textooriginal)
        textocriptografado = cifra(textooriginal, chave, CRIPTOGRAFAR)
        print('Texto Criptografado: ', textocriptografado)
    escolha()

def escolha():
    print('Continuar?')
    resposta=input('S=Sim \nN=Não \n--->')
    if resposta=='S':
        inicio()
    elif resposta=='N':
        print('Obrigado e até breve')
    else:
        print('Resposta inválida')
    escolha()
inicio()
