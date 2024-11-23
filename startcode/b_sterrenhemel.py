import random
import turtle

from sterren_module import *
kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

for _ in range(30):
    x = random.randint(-350,350)
    y = random.randint(-300,300)
    kleur = random.choice(kleuren) #kies random kleur uit kleuren
    teken_ster(x,y,kleur)

turtle.exitonclick()