def levelminus1():
    from simple_console_menu import Menu
    from rich.console import Console
    from random import randint
    from snippets.snippets import clear
    from snippets.snippets import updatenoclip

    console = Console()
    clear()

    console.print("Level -1 is a presumably infinite hallway that has doors on either side. The hallway features "
                  "white painted walls and black painted doors. Each door leads to one of three levels: Level 0, "
                  "Level 2, or almost any Negative Level. This level is one of the safest Negative Levels discovered "
                  "so far, but that's not to say it isn't dangerous.", style="bold yellow")
    exit(1)
