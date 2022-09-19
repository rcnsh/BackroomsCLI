def manilaroom():
    from rich.console import Console
    import os
    clear = lambda: os.system('cls')
    clear()

    console = Console()

    console.print("The Manila Room is an isolated spatial anomaly in the Backrooms, resembling a small square room. "
                  "It is typically considered an extension of Level 0. The room gets its name from the fact that the "
                  "wallpaper and flooring have a similar color to that of manila paper; this color is distinct from "
                  "the mono-yellow of Level 0.", style="bold yellow")
    console.print("WIP", style="bold black")
    exit(1)
