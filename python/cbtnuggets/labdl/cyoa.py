global xp
xp = 0

def help():
    print("Use the keyboard to make a choice.")
    print("Example: Press a, b, c, or d.")
    print
    return

def start():
    print('''CHOOSE YOUR OWN ADVENTURE IN NETWORKING
You are asked to repair a computer that is suspected of
being infested with malware. You are at the customer's site.''')


start()

def opener():
    global xp
    print('''\nThe customer, Susan, leads you to the family computer
    and says "Here you are--have at it!"

    Actions (You can use lowercase or uppercase letters; press h for help):

    a - Option 1
    b - Option 2
    c - Option 3
    ''')
    prompt_opener()

def prompt_opener():
    global xp
    prompt_o = input("Type a command: ").lower()
    try:
        if prompt_o == "a":
            print("You selected choice a")
        elif prompt_o == "b":
            print("You selected choice b")
        elif prompt_o == "c":
            print("You selected choice c")
        elif prompt_o == "d":
            print("You selected choice d")
        elif prompt_o == "h":
            help()
        else:
            print("That command is invalid")
            print
            prompt_opener()
    except ValueError:
        print("That command is invalid")
        print
        prompt_opener()
            
opener()    
