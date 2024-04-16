# -*- coding: utf-8 -*-
# !/usr/bin/python
from Tkinter import *
import random
import os, glob

# PENDENTE
# tratar ranking usuários diferentes
# gerar icone do aplicativo

# VARIÁVEIS PARA INICIALIZAÇÃO DO APLICATIVO
borda_carta = 10
largura_carta = 100
altura_carta = 130

contador = 1
img_anterior = ""
indice_anterior = ""
acertos = 0

lista_img = range(1, 13)
lista_carta = range(1, 13)
lista_aberta = []
lista_img_ok = range(1, 13)

usuario_atual = os.popen('whoami').read().strip();

pointsX = [10, 120, 230, 10, 120, 230, 10, 120, 230, 10, 120, 230]
pointsY = [10, 10, 10, 150, 150, 150, 290, 290, 290, 430, 430, 430]


#########################FUNÇÕES#################################
def coluna1(e):
    if e.x >= borda_carta and e.x <= (largura_carta + borda_carta):
        return True


def coluna2(e):
    if e.x >= largura_carta + (borda_carta * 2) and e.x <= (largura_carta * 2) + (borda_carta * 2):
        return True


def coluna3(e):
    if e.x >= (largura_carta * 2) + (borda_carta * 3) and e.x <= (largura_carta * 3) + (borda_carta * 3):
        return True


def linha1(e):
    if e.y <= (altura_carta + borda_carta) and e.y >= borda_carta:
        return True


def linha2(e):
    if e.y <= (altura_carta * 2) + (borda_carta * 2) and e.y >= (altura_carta) + (borda_carta * 2):
        return True


def linha3(e):
    if e.y <= (altura_carta * 3) + (borda_carta * 3) and e.y >= (altura_carta * 2) + (borda_carta * 3):
        return True


def linha4(e):
    if e.y <= (altura_carta * 4) + (borda_carta * 4) and e.y >= (altura_carta * 3) + (borda_carta * 4):
        return True


def clica(e):
    # LINHA 1
    if coluna1(e) and linha1(e):
        desvira(0)
    if coluna2(e) and linha1(e):
        desvira(1)
    if coluna3(e) and linha1(e):
        desvira(2)

    # LINHA 2
    if coluna1(e) and linha2(e):
        desvira(3)
    if coluna2(e) and linha2(e):
        desvira(4)
    if coluna3(e) and linha2(e):
        desvira(5)

    # LINHA 3
    if coluna1(e) and linha3(e):
        desvira(6)
    if coluna2(e) and linha3(e):
        desvira(7)
    if coluna3(e) and linha3(e):
        desvira(8)

    # LINHA 4
    if coluna1(e) and linha4(e):
        desvira(9)
    if coluna2(e) and linha4(e):
        desvira(10)
    if coluna3(e) and linha4(e):
        desvira(11)


def vira():
    global lista_aberta
    for indice, valor in enumerate(lista_carta):
        if not indice in lista_aberta:
            canLeft.create_image(pointsX[indice], pointsY[indice], image=fundo_carta, anchor=NW)


def desvira(indice_carta):
    global lista_img_ok, lista_aberta, lista_carta, lista_img, img_anterior, indice_anterior, contador, acertos

    if contador % 2 == 0 and acertos <= 6 and not indice_carta in lista_aberta and indice_carta != indice_anterior:
        lb_tentativas.config(text=(contador / 2))
        if img_anterior == lista_carta[indice_carta]:
            lista_aberta.append(indice_anterior)
            lista_aberta.append(indice_carta)
            canLeft.create_image(pointsX[indice_carta], pointsY[indice_carta], image=lista_img_ok[indice_carta],
                                 anchor=NW)
            canLeft.create_image(pointsX[indice_anterior], pointsY[indice_anterior],
                                 image=lista_img_ok[indice_anterior], anchor=NW)
            acertos += 1
        else:
            if not indice_carta in lista_aberta:
                canLeft.create_image(pointsX[indice_carta], pointsY[indice_carta], image=lista_img[indice_carta],
                                     anchor=NW)
        contador += 1
    else:
        if not indice_carta in lista_aberta and indice_carta != indice_anterior:
            contador += 1
            vira()
            canLeft.create_image(pointsX[indice_carta], pointsY[indice_carta], image=lista_img[indice_carta], anchor=NW)

    if acertos == 6:
        lb_parabens.config(text="Parabéns, você acertou todas!")
        log_tentativa()

    img_anterior = lista_carta[indice_carta]
    indice_anterior = indice_carta


def log_tentativa():
    global contador
    if not os.path.lexists("game-log.txt"):
        log = open("game-log.txt", "w")
        log.write("")
        log.close()

    text_log = ""
    log = open("game-log.txt", "rt")
    meta_data = []
    # list_user = []

    for line in log:
        line_data = line.split(' -*- ')
        # list_user[0] =  line_data[0]
        if (contador / 2) != int(line_data[1]):
            meta_data.append(int(line_data[1]))

    meta_data.sort()
    text_label = ""
    for indice, line in enumerate(meta_data):
        if indice < 3:
            text_log += line_data[0] + " -*- " + str(line) + "\n"
    log.close()

    if len(text_log):
        lb_ranking.config(text="Ranking:")
        lb_ranking1.config(text=text_log)
        log = open("game-log.txt", "w")
        log.write(text_log)
        log.close()


def comecar():
    global lista_img_ok, lista_aberta, lista_carta, lista_img, img_anterior, indice_anterior, contador, acertos

    # MISTURA TODAS AS CARTAS
    lista_carta = range(1, 13)
    lista_img = range(1, 13)
    random.shuffle(lista_carta)
    print
    "reset..."

    # CRIA AS CARTAS NA TELA
    for indice, valor in enumerate(lista_carta):
        if valor > 6:
            valor = valor - 6
        lista_img[indice] = PhotoImage(file="src/temas/" + tema + "/carta%d.png" % valor)
        lista_img_ok[indice] = PhotoImage(file="src/temas/" + tema + "/carta%d_ok.png" % valor)
        lista_carta[indice] = valor

    vira()
    img_anterior = ""
    indice_anterior = ""
    contador = 1
    acertos = 0
    lista_aberta = []
    lb_tentativas.config(text="0")
    lb_parabens.config(text="")


###############################ÍNICIO#######################
janela = Tk()
janela.title("Jogo da Memória")
janela.geometry("680x570+10+10")

# LADO ESQUERDO DA TELA
canLeft = Canvas()
canLeft.pack(side=LEFT, fill="y")
fundo_carta = PhotoImage(file="src/fundo_carta.png")
canLeft.bind("<Button-1>", clica)

# LADO DA DIREITO DA TELA
canRight = Canvas()
canRight.pack(side=RIGHT, fill="y")
canRight.create_text(100, 30, text="Jogo da Memória", font="Arial 18")

temas = []
for arquivo in glob.glob('src/temas/*'):
    if os.path.isdir(arquivo):
        temas.append(arquivo.split("/")[2])

tema = temas[random.randint(0, 2)]

bt_fechar = Button(text="FECHAR", command=janela.quit, foreground="red")
rt_jogador = Label(font="Arial 16", text="Jogador:", foreground="blue")
rt_tentativas = Label(font="Arial 16", text="Tentativas:", foreground="blue")
lb_jogador = Label(font="Arial 16", text=usuario_atual, foreground="#333")
lb_tentativas = Label(font="Arial 16", text="0", foreground="#333")
lb_parabens = Label(font="Arial 12", text="", foreground="green")

lb_ranking = Label(font="Arial 16", text="", foreground="blue")
lb_ranking1 = Label(font="Arial 16", text="", foreground="#333")

bt_comecar = Button(text="COMEÇAR", command=comecar)

canRight.create_window(10, 70, window=bt_comecar, anchor=NW)
canRight.create_window(100, 70, window=bt_fechar, anchor=NW)
canRight.create_window(10, 150, window=rt_tentativas, anchor=NW)
canRight.create_window(10, 120, window=rt_jogador, anchor=NW)
canRight.create_window(100, 120, window=lb_jogador, anchor=NW)
canRight.create_window(120, 150, window=lb_tentativas, anchor=NW)
canRight.create_window(10, 180, window=lb_parabens, anchor=NW)
canRight.create_window(10, 220, window=lb_ranking, anchor=NW)
canRight.create_window(10, 250, window=lb_ranking1, anchor=NW)

#########DEVELOPED################
lb_site = Label(font="Arial 12", text="www.graciomar.com.br", foreground="#790547")

logomarca = PhotoImage(file="src/logomarca.png")
canRight.create_image(10, 480, image=logomarca, anchor=NW)
canRight.create_window(80, 500, window=lb_site, anchor=NW)

comecar()
log_tentativa()
janela.mainloop()