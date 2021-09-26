from keys import *
import io
import tweepy
import requests
import pyautogui
import pytesseract as ocr
from PIL import Image
import time
import winsound


def steam(codigo):
    # abrir o navegador
    pyautogui.click(643, 750)
    # clicar na aba da steam
    pyautogui.click(66, 22)
    # inserir o código
    pyautogui.click(399,484)
    pyautogui.write(codigo)
    # confirmar (click)
    pyautogui.click(751, 514)
    # Recarregar a página pra começar de novo
    time.sleep(3)
    pyautogui.press('F5')
    time.sleep(3)
    pyautogui.click(643, 750)


def roblox(codigo):
    # abrir o navegador
    pyautogui.click(643, 750)
    # clicar na aba do roblox
    pyautogui.click(249, 16)
    # inserir o código
    pyautogui.click(832, 266)
    pyautogui.write(codigo)
    # resgatar o código (1 tab)
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    # Recarregar a página pra começar de novo
    time.sleep(3)
    pyautogui.press('F5')
    time.sleep(3)
    pyautogui.click(643, 750)


def uber(codigo):
    # abrir o navegador
    pyautogui.click(643, 750)
    # clicar na aba do uber
    pyautogui.click(476, 10)
    # clicar no meio da tela pra funcionar os tabs
    pyautogui.click(663, 200)
    # inserir o código (1 tab)
    pyautogui.press('TAB')
    pyautogui.write(codigo)
    # resgatar código (1 tab)
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    # Recarregar a página pra começar de novo
    time.sleep(3)
    pyautogui.press('F5')
    time.sleep(5)
    pyautogui.click(612, 401)
    time.sleep(3)
    pyautogui.click(643, 750)


def googlePlay(codigo):
    # abrir o navegador
    pyautogui.click(643, 750)
    # clicar na aba do google play
    pyautogui.click(705, 15)
    # inserir o código
    pyautogui.write(codigo)
    # resgatar o código (3 tabs)
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    for c in range(0, 10):
        pyautogui.click(856, 503)
    # Recarregar a página pra começar de novo
    pyautogui.sleep(3)
    pyautogui.press('F5')
    pyautogui.sleep(3)
    pyautogui.click(58, 514)
    time.sleep(3)
    pyautogui.click(643, 750)


def lol(codigo):
    # abrir o lol
    pyautogui.click(683, 752)
    # clicar em alguma parte da tela pros TABS funcionarem
    pyautogui.click(583, 138)
    # inserir código
    pyautogui.press('TAB')
    pyautogui.write(codigo)
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    time.sleep(3)
    pyautogui.click(683, 752)


def abrirLojaLol():
    # abrir o lol
    pyautogui.press('ESC')
    pyautogui.click(683, 752)
    time.sleep(0.5)
    # fechar a janela de resgate de código
    pyautogui.click(1119, 116)
    # abrir a janela de resgate de código novamente
    time.sleep(1.5)
    pyautogui.click(207, 256)
    time.sleep(5)
    # clicar em uma parte da tela pros tabs funcionarem
    pyautogui.click(583, 138)
    time.sleep(0.5)
    # inserir as informações novamente
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.write('Your name')
    pyautogui.press('TAB')
    pyautogui.write('Your last name')
    pyautogui.press('TAB')
    pyautogui.write('Your CPF')
    pyautogui.press('TAB')
    pyautogui.write('Your birthday')
    time.sleep(0.5)
    # clicar pra sair da tela do lol depois de preencher as informações
    pyautogui.click(683, 752)


def ifood(codigo):
    # abre o emulador android
    pyautogui.click(718, 754)
    time.sleep(0.1)
    # imprime o codigo no input do ifood
    pyautogui.click(680, 266)
    pyautogui.write(codigo, interval=0.045)
    # ativa o código
    pyautogui.click(676, 679)
    # confirmar (spam de click pra garantir)
    for c in range(0, 50):
        pyautogui.click(676, 695)
    # sair do emulador
    pyautogui.click(718, 754)


def encontraCodigo(tweets):
    achou = False
    for info in tweets[:1]:
        tweet = info.full_text.replace('\n', ' ')
        palavras = tweet.split(' ')
        for palavra in palavras:
            palavra = palavra.replace('.', '')
            if palavra.replace('-', '').isalnum() and not palavra.replace('-', '').isalpha() and len(palavra.replace('-', '')) >= 10:  # Verificação do código
                achou = True
                codigo = palavra
                print(f'Achou código: {codigo}')
                break
    if achou:
        return achou, codigo # se achou no texto, retornamos o código agora, senão, procuro o código nas imagens anexadas ao tweet
    else:
        achouImagem = False # começo a verificação supondo que o tweet não tem imagem
        for info in tweets[:1]:
            for media in info.entities.get("media", [{}]):
                if media.get("type", None) == "photo":
                    conteudo_imagem = requests.get(media["media_url"])
                    achouImagem = True
                    break
        if achouImagem:
            #ocr.pytesseract.tesseract_cmd = r'Your tesseract directory goes here'
            imagem = Image.open(io.BytesIO(conteudo_imagem.content))
            palavrasImagem = ocr.image_to_string(imagem, lang='por')
            palavrasImagem = palavrasImagem.replace('\n', ' ')
            palavrasImagem = palavrasImagem.split(' ')
            for palavra in palavrasImagem:
                palavra = palavra.replace('.', '')
                if palavra.replace('-', '').isalnum() and not palavra.replace('-', '').isalpha() and len(palavra.replace('-', '')) >= 10:
                    achou = True
                    codigo = palavra
                    print(f'Achou código (imagem): {codigo}')
                    break
        if achou:
            return achou, codigo
        else:
            return achou, 0


def primeiraExecucao():
    tweets = api.user_timeline(screen_name=userID,
                               count=1,  # Número de tentativas (200 é o máximo)
                               include_rts=False,  # Não incluir retweets, apenas tweets feitos pelo usuário
                               tweet_mode='extended'  # Necessário para pegar o tweet inteiro
                               )
    for info in tweets[:1]:
        idTweetAntigo = info.id
    return idTweetAntigo


def verificaCodigo(codigo):
    if achou:
        if len(codigo) == 20 or len(codigo) == 28:
            lol(codigo)
        elif len(codigo) == 10:
            roblox(codigo)
        elif len(codigo) == 17:
            steam(codigo)
        elif len(codigo.replace('-', '')) == 21 or len(codigo.replace('-', '')) == 19:
            ifood(codigo)
        elif len(codigo) == 16:
            if codigo[0:3].upper() == 'NAA':
                uber(codigo)
            else:
                googlePlay(codigo)



def getTweetID(tweets):
    for info in tweets[:1]:
        idTweet = info.id
    return idTweet

userID = 'twitter user id you want to scrap the gift cards codes'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
# não estourar o limite pra não dar erro
api = tweepy.API(auth, wait_on_rate_limit=True, retry_count=10, retry_delay=5, retry_errors=set([503]))

tweetAntigo = primeiraExecucao() # Recebe o ID do primeiro tweet verificado
pyautogui.keyUp('SHIFT') # soltar o shift depois de reiniciar o programa
#abrirLojaLol() # COMENTE ESSA LINHA CASO ESTEJA COM O LOL FECHADO
contador = 0
while True:
    time.sleep(1)
    tweets = api.user_timeline(screen_name=userID,
                               count = 1, # Número de tentativas (200 é o máximo)
                               include_rts = False, # Não incluir retweets e apenas tweets feitos pelo usuário
                               tweet_mode = 'extended' # Necessário para pegar o tweet inteiro
                               )
    idTweet = getTweetID(tweets) # Pega o id do tweet mais recente
    if tweetAntigo != idTweet: # Compara se os 2 ids são iguais para otimização de processamento
        tweetAntigo = idTweet
        achou = encontraCodigo(tweets)[0]
        if achou:
            codigo = encontraCodigo(tweets)[1]
            verificaCodigo(codigo)

    contador += 1
    if contador % 1800 == 0: # sistema de reiniciamento automático do script para evitar erros
        # abrir o pycharm
        # pyautogui.click(867, 752)
        print('Reiniciando...')
        time.sleep(30)
        # reiniciar o código
        pyautogui.keyDown('SHIFT')
        pyautogui.press('F10')
    if contador % 300 == 0: # Caso esteja com o LOL fechado, comente essa sessão
        print('Abrindo loja do LOL')
        winsound.Beep(500, 3000)
        abrirLojaLol()
