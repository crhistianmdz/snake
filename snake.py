import turtle
import time
import random

posponer=0.1
############
# configuracion de la ventana
############
wn=turtle.Screen()
wn.title("juego")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

############
# Serpiente
############

###cabeza
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
###cuerpo

segmentos=[]

############
# comida
############

comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

############
# texto
############
texto=turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score : 0      High Score:0" ,align='center', font=('courier',24,'normal'))
##Marcador
score=0
high_score=0

############
# Funciones
############
def arriba():
    cabeza.direction="up"

def abajo():
    cabeza.direction="down"

def izquierda():
    cabeza.direction="left"

def derecha():
    cabeza.direction="right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")

while True:
    wn.update()

    # colisiones
    if cabeza.xcor()> 280 or cabeza.xcor() < -280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        time.sleep(1)
        for i in range(0,totalSeg):
            segmentos[i].reset()#limpia los colores en la pantalla
        cabeza.direction="stop"
        cabeza.goto(0,0)
        del segmentos[0:]
        comida.goto(0,100)
        score=0 #limpia variable del marcador
        texto.clear()
        texto.write("Score:{}     High Score:{}".format(score,high_score) ,align='center', font=('courier',24,'normal'))
    
    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            for i in range(0,totalSeg):
                segmentos[i].reset()
            time.sleep(1)
            del segmentos[0:]
            cabeza.direction="stop"
            cabeza.goto(0,0)
            comida.goto(0,100)
            score=0
            texto.clear()
            texto.write("Score:{}     High Score:{}".format(score,high_score) ,align='center', font=('courier',24,'normal'))
            
             

    # logica de comer manzanitas
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        #se crea el la imagen del cuerpo
        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()
        #se guarde en una lista el segmento
        segmentos.append(nuevo_segmento)
        score+=10
        if score > high_score:
            high_score=int(score)
        texto.clear()
        texto.write("Score:{}     High Score:{}".format(score,high_score) ,align='center', font=('courier',24,'normal'))

    #se ordenan una detras de otra    
    totalSeg=len(segmentos)

    for index in range(totalSeg-1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    #el primer segmento isgue a la cabeza de la serpiente
    if totalSeg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)

    
    mov()
    time.sleep(posponer)