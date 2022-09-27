
from curses.ascii import isdigit


t = input("Digite o tempo em (segundos): ")

if t.isdigit():
    t = int(t)
else: 
    print("Entrada inválida!")
    quit()

while
    minutes, seconds = divmod(t, 60)
    timer = f"{minutes}:{seconds}"
    print(timer, end="\r")
    t = t -1


