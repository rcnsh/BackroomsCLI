def manilaroom():
    from rich.console import Console
    import os
    from simple_console_menu import Menu
    from rich.console import Console
    from random import randint
    from snippets.snippets import clear
    from snippets.snippets import updatenoclip
    from snippets.snippets import updatehealth
    from snippets.snippets import updatealmond

    console = Console()

    console.print("The Manila Room is an isolated spatial anomaly in the Backrooms, resembling a small square room. "
                  "It is typically considered an extension of Level 0. The room gets its name from the fact that the "
                  "wallpaper and flooring have a similar color to that of manila paper; this color is distinct from "
                  "the mono-yellow of Level 0.", style="bold yellow")
    console.print("\nWhat will you do?", style="bold yellow")

    noclipfile = open("profileData/noclip.txt", "r")

    noclip = noclipfile.read()

    options = Menu.SimpleConsoleMenuBlock('Options:',
                                          ["Sleep on the floor", "Exit the room", f"Noclip out of the room: {noclip} remaining"], "Options: ", 76)

    if options == 1:
        randomgen = randint(1,100)
        if randomgen > 95:
            from levels.Level994 import level994
            level994()
            exit()
        else:
            console.print("You wake up feeling refreshed...", style="bold blue")
            updatehealth(20)
            console.print("You gained [bold red]20HP[/bold red]!", style="bold yellow")
            options = Menu.SimpleConsoleMenuBlock('Options:',
                                                  ["Exit the room",
                                                   f"Noclip out of the room: {noclip} remaining"], "Options: ", 76)
            if options == 1:
                from levels.Level0 import level0
                level0()
                exit()
            elif options == 2:
                updatenoclip()
                from levels.Level1 import level1
                level1()
                exit()
    if options == 2:
        from levels.Level0 import level0
        level0()
        exit()
    if options == 3:
        from levels.Level1 import level1
        level1()
        exit()



