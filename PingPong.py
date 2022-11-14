import turtle
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

marcadorA = 0
marcadorB = 0

JugadorA = turtle.Turtle()
JugadorA.speed(8)
JugadorA.shape("square")
JugadorA.color("white")
JugadorA.penup()
JugadorA.goto(-350,0)
JugadorA.shapesize(stretch_wid=5, stretch_len=1)

JugadorB = turtle.Turtle()
JugadorB.speed(8)
JugadorB.shape("square")
JugadorB.color("white")
JugadorB.penup()
JugadorB.goto(350,0)
JugadorB.shapesize(stretch_wid=5, stretch_len=1)

pelota = turtle.Turtle()
pelota.speed(8)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 3
pelota.dy = 3

division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0		jugadorB: 0", align="center", font=("Courier", 25, "normal"))

#funciones
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)

def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)

def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)

def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
    JugadorB.sety(y)

#teclado
wn.listen()
wn.onkeypress(JugadorA_up, "w")
wn.onkeypress(JugadorA_down, "s")
wn.onkeypress(JugadorB_up, "Up")
wn.onkeypress(JugadorB_down, "Down")


while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

	#Revisa colisiones con los bordes de la ventana
    if pelota.ycor() > 290:
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.dy *= -1

	# Si la pelota sale por la izq o derecha, esta regresa al centro.
	
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()

        pen.write(f"Jugador A: {marcadorA}		jugadorB: {marcadorB}", align="center", font=("Courier", 25, "normal"))
    if pelota.xcor() < -390:
	    pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
		
		pen.write(f"Jugador A: {marcadorA}		jugadorB: {marcadorB}", align="center", font=("Courier", 25, "normal"))


	#Revisa las colisiones
	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < jugadorB.ycor() + 50
			and pelota.ycor() > jugadorB.ycor() - 50)):
            pelota.dx *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugadorA.ycor() + 50
			and pelota.ycor() > jugadorA.ycor() - 50)):
            pelota.dx *= -1
