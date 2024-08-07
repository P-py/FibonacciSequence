#Importando as bibliotecas necessárias
import time
from tkinter import *
import matplotlib.pyplot #pip install matplotlib
import turtle #pip install turtle
import math
import pygame #pip install pygame
import os
import colorsys
from math import sqrt, cos, sin

lista_termos = [] #Lista de termos, usada para a função de demonstrar termos da sequência até um certo termo.
numero_termos = []

#Definindo variáveis para as principais cores que usei
colorPallete1 = "#ff4a36" 
colorPallete2 = "#272f3d" 

#Função que demonstra o gráfico de crescimento da sequência e uma certa quantidade de termos baseada em um input do usuário
def executarFibonacci():
    def fibonacci():
        def sequência_fibonacci():
            #configurando a janela que mostra a quantidade de termos
            top2 = Toplevel()
            top2.configure(bg=colorPallete2)
            anterior = 0
            proxima = 1
            soma = 1
            final = int(qntidadetermosEntry.get())
            numTermo = 1
            for n in range(0, final+1):
                time.sleep(.5)
                termoLabel = Label(top2, text=anterior, bg=colorPallete2, fg=colorPallete1, font="roboto 12 bold italic")
                termoLabel.pack()
                lista_termos.append(anterior)
                numero_termos.append(numTermo)
                numTermo += 1
                soma = proxima+anterior
                anterior = proxima
                proxima = soma
            #linhas usadas para fazer com que o matplotlib mostre o gráfico de crescimento
            matplotlib.pyplot.plot(numero_termos, lista_termos) #montando o gráfico
            matplotlib.pyplot.title("Sequência de fibonacci") #dando título para o gráfico
            matplotlib.pyplot.show() #mostrando
        #Configurando os widgets necessários para a função
        qntidadetermosEntry = Entry(top)
        qntidadetermosEntry.place(rely=.35, relx=.5, anchor=CENTER)
        qntidadetermosLabel = Label(top, text="Qual a quantidade de termos que deseja visualizar?", font="roboto 11 bold italic", fg=colorPallete1, bg=colorPallete2)
        qntidadetermosLabel.place(rely=.25, relx=.5, anchor=CENTER)
        resultadoButton = Button(top, text="Resultado", font="roboto 12 bold italic", command=sequência_fibonacci, bg=colorPallete1)
        resultadoButton.place(rely=.45, relx=.5, anchor=CENTER)
    #Função de desenhar a proporção de ouro
    def desenhar():
        #Configurando a tela base do turtle
        wn = turtle.Screen()
        wn.setup(1000, 800) #Tamanho da janela base
        wn.bgcolor(colorPallete2) #Cor do fundo
        myturtle = turtle.Turtle()
        myturtle.pencolor(colorPallete1) #cor da "caneta"
        myturtle.pensize(3) #grossura da caneta usada para desenhar
        myturtle.speed(5) #velocidade com que o "turtle" executa o desenho
        def main():
            valueOne = 0
            valueTwo = 1
            fib = 1
            for i in range(8):
                myturtle.right(90)
                drawSq(fib*20)
                fib = valueOne + valueTwo
                valueOne = valueTwo
                valueTwo = fib
        def drawSq(sides):
            for n in range(6):
                myturtle.forward(sides)
                myturtle.left(90)
        #Função que faz o espiral
        def spiral():
            r = 20
            angle = 90
            myturtle.right(90)
            myturtle.penup()
            myturtle.setpos(0, 0)
            myturtle.pendown()
            arc(20, angle)                         # call arc function  1 * 20 = 20
            arc(20, angle)                         # call arc function  1 * 20 = 20
            arc(40, angle)                         # call arc function  2 * 20 = 40
            arc(60, angle)                         # call arc function  3 * 20 = 60
            arc(100, angle)                        # call arc function  5 * 20 = 100
            arc(160,angle)                         # call arc function 8 * 20 = 160
            arc(260,angle)                         # call arc function 13 * 20 = 260
            arc(420,angle)
        def arcLine(n, length, angle):
            for i in range(n):
                myturtle.forward(length)
                myturtle.left(angle)
        def arc(r, angle):
            arc_length = 2 * math.pi * r * abs(angle) / 360
            n = int(arc_length / 4) + 1
            step_length = arc_length / n
            step_angle = float(angle) / n
            # Before starting making a slight left turn.
            myturtle.left(step_angle/2)
            arcLine(n, step_length, step_angle)
            myturtle.right(step_angle/2)
        main() #Função principal que faz os quadros
        spiral() #Função que faz o espiral
        wn.exitonclick() #Só sair quando clickado para
    #Função que faz a filotaxia
    def Phyllotaxis():
        os.environ["SDL_VIDEO_CENTERED"]='1'

        color = (39, 47, 61)
        
        width, height = 1920, 1080
        size = (width, height)
        pygame.init()
        pygame.display.set_caption("Phyllotaxis")
        screen = pygame.display.set_mode(size)
        screen.fill(color)
        fps = 30
        clock = pygame.time.Clock()

        font = pygame.font.Font('freesansbold.ttf', 14)

        rotation_angle = 0
        white, black = (240, 240, 240), (15, 15, 15)
        hue = 0

        n = 0
        c = 20
        cube_position = [width//2, height//2]
        scale = 20
        points = []
        counter = False
        class Point:
            def __init__(self, x, y, color):
                self.x = x
                self.y = y
                self.points= [[x], [y], [1]]
                self.color = color

        def hsv2rgb(h, s, v):
            return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


        def fibonnaci_numbers(r):
            fib_list = []
            i, j = 1, 1
            for _ in range(r):
                fib_list.append(i)
                i, j = j, i + j
            return fib_list

        def matrix_multiplication(a, b):
            columns_a = len(a[0])
            rows_a = len(a)
            columns_b = len(b[0])
            rows_b = len(b)

            result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
            if columns_a == rows_b:
                for x in range(rows_a):
                    for y in range(columns_b):
                        sum = 0
                        for k in range(columns_a):
                            sum += a[x][k] * b[k][y]
                        result_matrix[x][y] = sum
                return result_matrix
            else:
                print("error!")
                return None

        run = True
        while run:
            clock.tick(fps)
            screen.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            angle = n * 137.5
            r = c * sqrt(n)

            x = r * cos(angle)
            y = r * sin(angle)

            rotation_z =[[cos(rotation_angle), -sin(rotation_angle), 0],
                            [sin(rotation_angle), cos(rotation_angle), 0 ],
                            [0, 0, 1]]
            if n < 700:
                # coloring type hsv2rgb(hue, 1, 1) for a rainbow pattern
                # hsv2rgb(angle/255, 1, 1) for a spiral rainbow pattern
                p = Point(int(x), int(y), hsv2rgb(angle/255, 1, 1))
                points.append(p)

            for point in points:
                rotated_2d = matrix_multiplication(rotation_z, point.points)

                distance = 20
                z = 1/(distance - rotated_2d[2][0])
                projection_matrix = [[z, 0, 0],
                                    [0, z, 0]]
                projected2d = matrix_multiplication(projection_matrix, rotated_2d)
                x_pos = int(projected2d[0][0] * scale) + cube_position[0]
                y_pos = int(projected2d[1][0] * scale) + cube_position[1]
                pygame.draw.circle(screen, point.color, (x_pos, y_pos), 8)

            text = font.render(str(int(r)), True, white)
            textRect = text.get_rect()
            textRect.center = (50, 100)
            screen.blit(text, textRect)
            pygame.display.update()

            n += 1
            hue += 0.002
            rotation_angle += 0.01
        pygame.quit()
    #Configurando a base da janela que contém os botões
    top = Toplevel()
    top.geometry("450x300") #Tamanho da janela
    top.title(" Fibonacci") #Título da janela
    top.configure(bg=colorPallete2) #Cor de fundo da janela

    #Botão que executa a função de gráfico e termos
    FibonacciButton = Button(top, text=" Executar", font="Helvetica 13 bold italic", width=10, height=2, bg=colorPallete1, command=fibonacci)
    FibonacciButton.place(rely=.1, relx=.5, anchor=CENTER)
    
    #Botão que desenha a proporção de ouro
    DesenharButton = Button(top, text="Desenhar", font="Helvetica 13 bold italic", width=10, height=2, bg=colorPallete1, command=desenhar)
    DesenharButton.place(rely=.6, relx=.5, anchor=CENTER)
    
    #Botão que executa a função de filotaxia
    FilotaxiaButton = Button(top, text="Filotaxia", font="Helvetica 13 bold italic", width=10, height=2, bg=colorPallete1, command=Phyllotaxis)
    FilotaxiaButton.place(rely=.8, relx=.5, anchor=CENTER)
    top.mainloop()

#Configurando a janela raiz, a mais básica
root = Tk()
root.title(" Fibonacci") #Título
root.geometry("500x300") #Tamanho

#Configurando o fundo dessa janela base
canva = Canvas(root, bg=colorPallete2)
canva.place(relwidth=1.0, relheight=1.0)

#Configurando o botão que abre a janela com as 3 funções
ExecButton = Button(canva, text=" Fibonacci", font="Helvetica 20 bold italic", command=executarFibonacci, bg=colorPallete1)
ExecButton.place(rely=.5, relx=.5, anchor=CENTER)

#Loop
root.mainloop()
