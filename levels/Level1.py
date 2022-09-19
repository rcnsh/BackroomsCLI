def level1():
    from rich.console import Console
    import os
    clear = lambda: os.system('cls')
    clear()
    console = Console()

    console.print(
        "Level 1 is a massive warehouse with concrete floors and walls, exposed rebar, dim fluorescent lights "
        "placed on the walls and a low-hanging fog with no discernible source. The fog often coalesces into "
        "condensation, forming puddles on the floor in inconsistent areas. Unlike Level 0, this level possesses a "
        "consistent supply of water and electricity, which allows indefinite habitation by wanderers providing that "
        "appropriate precautions are taken. It is also far more expansive, possessing staircases, elevators, "
        "isolated rooms, and hallways.", style="bold yellow")

