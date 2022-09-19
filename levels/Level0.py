def level0():
    from simple_console_menu import Menu
    from rich.console import Console
    from random import randint
    from snippets.snippets import clear
    from snippets.snippets import updatenoclip
    from snippets.snippets import updatehealth
    from snippets.snippets import updatealmond

    console = Console()
    clear()

    console.print(
        "[bold yellow]Level 0 is an expansive non-Euclidean space, resembling the back rooms of a retail outlet. All "
        "rooms in Level 0 share the same superficial features, such as worn mono-yellow wallpaper, old moist carpet, "
        "scattered electrical outlets, and inconsistently-placed fluorescent lighting. Aside from these common "
        "features, no two rooms within the level are identical.[/bold yellow]")
    console.print("[bold red]What will you do?[/bold red]")

    noclipfile = open("profileData/noclip.txt", "r")

    noclip = noclipfile.read()

    options = Menu.SimpleConsoleMenuBlock('Options:', ["Enter the room to your left", "Enter the room to your right",
                                                       "Enter the room ahead of you", "Enter the room behind you",
                                                       f"Noclip out of the room: {noclip} remaining"], "Option: ", 76)

    if options == 1:
        console.print("You enter the room to your left...\n", style="blink green")
        console.print("The room looks the same as the previous one, with the same [bold yellow]faded yellow[/bold "
                      "yellow] wallpaper\n", style="blink green")
        randomgen = randint(1, 100)
        if randomgen > 80:
            console.print("You spot a small door in the corner...", style="bold yellow")
            options = Menu.SimpleConsoleMenuBlock('Options:',
                                                  ["Enter", "Don't enter",
                                                   f"Noclip out of the room: {noclip} remaining"], "Go through the "
                                                                                                   "door? ", 76)
            if options == 1:
                from levels.theManilaRoom import manilaroom
                manilaroom()

            elif options == 2:
                console.print("You decide not to enter the room for now and turn away from it. A second later, "
                              "you glance back and the door has vanished...", style="bold yellow")
            elif options == 3:

                updatenoclip()
                from levels.Level1 import level1
                level1()

        options = Menu.SimpleConsoleMenuBlock('Options:', ["Enter the room to the left", "Enter the room to the right",
                                                           "Enter the room ahead of you",
                                                           f"Noclip out of the room: {noclip} remaining"], "Option: ",
                                              76)
        from levels.Level1 import level1
        if options == 1:
            level1()
        elif options == 2:
            level1()
        elif options == 3:
            level1()
        elif options == 4:
            updatenoclip()
            from levels.Levelminus1 import levelminus1
            levelminus1()

    if options == 2:
        console.print("You enter the room to your right...\n", style="blink green")
        console.print("The room looks the same as the previous one, with the same [bold yellow]faded yellow[/bold "
                      "yellow] wallpaper\n\n", style="blink green")
        console.print("There appears a bottle of water lying on the floor... You pick it up cautiously...",
                      style="blink green")

        options = Menu.SimpleConsoleMenuBlock('Options:',
                                              ["Drink the water", "Don't drink the water", "Store the water for later"],
                                              "Drink the water?: ", 76)

        if options == 1:
            console.print("You take a sip of the bottle of water...", style="bold blue")
            randomgen = randint(1, 100)
            if randomgen > 50:
                console.print("The substance in the bottle turned out to be almond water! This miracle drink acts as "
                              "a healing potion, revitalising you and your strength!", style="bold yellow")
                updatehealth(20)
                console.print("You gained [bold red]20HP[/bold red]!")
            else:
                console.print("The substance in the bottle turned out to be LIQUID PAIN! This liquid acts as a deadly "
                              "poison in large quantities, sapping your strength and putting you in great amounts of "
                              "pain!", style="bold red")
                updatehealth(-20)
                console.print("You lost [bold red]20HP[/bold red]!")
        elif options == 2:
            console.print("You decide to leave the bottle and not risk it.", style="bold green")

        elif options == 3:
            console.print("You decided to stash the bottle for later use and put it in your backpack...")
            updatealmond(1)

        options = Menu.SimpleConsoleMenuBlock('Options:',
                                              ["Enter the room to your left", "Enter the room to your right",
                                               "Enter the room ahead of you",
                                               f"Noclip out of the room: {noclip} remaining"], "Option: ", 76)
        from levels.Level1 import level1
        if options == 1:
            level1()
        elif options == 2:
            level1()
        elif options == 3:
            level1()
        elif options == 4:
            from levels.Levelminus1 import levelminus1
            levelminus1()

    if options == 3:
        console.print("You enter the room ahead of you...\n", style="blink green")

        console.print("The room looks the same as the previous one, with the same [bold yellow]faded yellow[/bold "
                      "yellow] wallpaper\n\n", style="blink green")

        console.print("In the middle of the room on the floor is a singular stick of [bold red]dynamite[/bold red].",
                      style="bold yellow")

        options = Menu.SimpleConsoleMenuBlock('Options:',
                                              ["Use it", "Don't use it"], "Use the dynamite?: ", 76)
        if options == 1:
            console.print("You activate the dynamite and step back quickly. After a few seconds, it explodes "
                          "violently, ripping a hole in the middle of the floor of the room.\n", style="blink green")

            console.print("\nAfter the dust settles, you approach the crater and look at it. It seems that the "
                          "dynamite has created a hole into a sort of [bold black]void, or endless abyss...[/bold "
                          "black]", style="bold yellow")

            options = Menu.SimpleConsoleMenuBlock('Options:', ["Jump into the hole...",
                                                               "Enter the room to your left",
                                                               "Enter the room to your right",
                                                               "Enter the room ahead of you",
                                                               "Enter the room behind you",
                                                               f"Noclip out of the room: {noclip} remaining"],
                                                  "Option: ", 76)

            from levels.Level1 import level1
            if options == 1:
                from levels.Level27 import level27
                level27()
            elif options == 2:
                level1()
            elif options == 3:
                level1()
            elif options == 4:
                level1()
            elif options == 5:
                level1()
            elif options == 6:
                updatenoclip()
                from levels.Levelminus1 import levelminus1
                levelminus1()

        elif options == 2:
            console.print("You decided not to use the dynamite...", style="blink green")
            options = Menu.SimpleConsoleMenuBlock('Options:', [
                                                               "Enter the room to your left",
                                                               "Enter the room to your right",
                                                               "Enter the room ahead of you",
                                                               "Enter the room behind you",
                                                               f"Noclip out of the room: {noclip} remaining"],
                                                  "Option: ", 76)

            from levels.Level1 import level1
            if options == 1:
                level1()
            elif options == 2:
                level1()
            elif options == 3:
                level1()
            elif options == 4:
                level1()
            elif options == 5:
                updatenoclip()
                from levels.Levelminus1 import levelminus1
                levelminus1()

    if options == 4:
        console.print("You enter the room to your left...\n", style="blink green")
        console.print("The room looks the same as the previous one, with the same [bold yellow]faded yellow[/bold "
                      "yellow] wallpaper\n", style="blink green")
        console.print("It doesn't look like there is anything interesting in this room....", style="bold yellow")

        options = Menu.SimpleConsoleMenuBlock('Options:', [
            "Enter the room to your left",
            "Enter the room to your right",
            "Enter the room ahead of you",
            "Enter the room behind you",
            f"Noclip out of the room: {noclip} remaining"],
                                              "Option: ", 76)

        from levels.Level1 import level1
        if options == 1:
            level1()
        elif options == 2:
            level1()
        elif options == 3:
            level1()
        elif options == 4:
            level1()
        elif options == 5:
            updatenoclip()
            from levels.Levelminus1 import levelminus1
            levelminus1()

    if options == 5:
        from levels.Levelminus1 import levelminus1
        levelminus1()

    exit(1)