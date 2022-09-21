from levels.Level0 import level0
from simple_console_menu import Menu
from rich import console
import os

console = console.Console()

healthFile = open("./profileData/health.txt", "w")
healthFile.write("100")
healthFile.close()

noclipFile = open("./profileData/noclip.txt", "w")
noclipFile.write("3")
noclipFile.close()

nameFile = open("./profileData/name.txt", "w")
ageFile = open("./profileData/age.txt", "w")

almondFile = open("./profileData/almondWater.txt", "w")
almondFile.write("0")
almondFile.close()

while True:
    options = Menu.SimpleConsoleMenuBlock('Options:', [
        "Start Game",
        "Enter Name and Age",
        "View Credits",
        "Exit"], "Option: ", 76)

    if options == 1:
        level0()
        exit()
    elif options == 2:
        name = input("Please enter your name: ")
        nameFile.write(name)
        nameFile.close()

        age = input("Please enter your age: ")
        ageFile.write(age)
        ageFile.close()
        os.system('cls')

    elif options == 3:
        console.print(
            "Credits: [bold red]Lead Programmer:\n[/bold red] [bold blue]Jacob Wiltshire[/bold blue]\n\n[bold "
            "pink]Mental support:\n[/bold pink][bold yellow]Luc Smith\nHenry Smith\nMr Brown\nMr Veli\nKaleb "
            "Hirshfield\nThomas Hawkins\nLouisa Safo\nFin Stevens\nLucas Done\nMy Parents and Family\n\n and"
            "you for playing the game![/bold yellow]\n")
        input("Press enter to continue...")
        os.system('cls')
    elif options == 4:
        exit()
