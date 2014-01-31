#Text Adventure.py
#By Chris O'Leary
# Found here: http://www.daniweb.com/forums/thread55140.html

global gold
global gotGold_reading
global gotGold_SQ
global gotGold_liv
global gotGold_draw
global gotGold_din
gold=0
gotGold_reading = 0
gotGold_SQ = 0
gotGold_liv = 0
gotGold_draw = 0
gotGold_din = 0

def help1():
    print "look, examine (object), n, w, e, s, take (item)"
    print "Examples: examine chair, take gold"
    print
def start():
    print '''
        ADVENT HOUSE v1.1
    You find yourself in the foyer of a large house. You
    have no idea how you got there. You look around, and see the front door.
    It is locked and barred, and the bar is nailed down. There is
    no way to open it. There are three other doors in the area. A voice says
    '50 gold is what you need,
    to escape my grasp, of this take heed!'

    Note: All instructions can be typed in lower or upper case letters.'''
    print
    
def foyer():
    global gold
    print "     Current Gold = ",gold
    print '''    You are in the Foyer. The walls are lined with trophy cabinets
    and suits of armour. The exits are (N)orth, (E)ast and (W)est.
    Type 'help' for a full list of commands.'''
    print
    prompt_foy()

def foy_desc():
    print '''    The walls are lined with trophy cabinets and suits of armour.
    The exits are (N)orth, (E)ast and (W)est.'''
    print
    prompt_foy()
    
def prompt_foy():
    global gold
    prompt_f = raw_input("Type a command: ").lower()
    try:
        if prompt_f == "w":
            reading_room()
        elif prompt_f == "e":
            servants_quarters()
        elif prompt_f == "help":
            help()
            prompt_foy()
        elif prompt_f == "examine armour":
            print "The armour is rusted, and not of any use."
            print
            prompt_foy()
        elif prompt_f == "examine cabinet":
            print '''    The cabinet is lined with trophies, dating back to the 1800s.
            Seems this was a talented family.'''
            print
            prompt_foy()
        elif prompt_f == "look":
            foy_desc()
        elif prompt_f == "s":
            if gold < 50:
                print "You can't get out untill you have 50 gold."
                print
                prompt_foy()
            elif gold == 50:
                ending()
        elif prompt_f == "n":
            main_hall()
        else:
            print "That command is invalid"
            print
            prompt_foy()
    except ValueError:
        print "That command is invalid"
        print
        prompt_foy()

def reading_room():
    global gold
    print "      Current Gold = ",gold
    print '''    You are in an large reading room. The room is stuffed with novels
    and poetry books on every shelf. There is a large table in the middle
    of the room. It has a reading lamp, and a cluster of books scattered about
    on top. The exits are (n)orth and (e)ast. Type 'help' for a full list of
    commands.'''
    print
    prompt_rea()

def rea_desc():
    print '''    The room is stuffed with novels and poetry books on
    every shelf. There is a large table in the middle of the room.
    It has a reading lamp, and a cluster of books scattered about
    on top. The exits are (n)orth and (e)ast.'''
    print
    prompt_rea()
    
def prompt_rea():
    global gold
    global gotGold_reading
    prompt_r = raw_input("Type a command: ").lower()
    try:
        if prompt_r == "e":
            foyer()
        elif prompt_r == "n":
            drawing_room()
        elif prompt_r == "help":
            help()
            prompt_rea()
        elif prompt_r == "examine table":
            if gotGold_reading == 0:
                print "You see 30 gold pieces on the table."
                print
                prompt_rea()
            elif gotGold_reading == 1:
                print "The table is cluttered with books."
                print
                prompt_rea()
        elif prompt_r == "look":
            rea_desc()
        elif prompt_r == "take gold":
            if gotGold_reading==0:
                print "You get 30 gold!"
                print
                gold=gold+30
                gotGold_reading=1
                reading_room()
            elif gotGold_reading==1:
                print "No gold in here"
                print
                prompt_rea()
        elif prompt_r == "examine shelves":
            print '''    There are numerous bookshelves and countless books,
            and some novels are scattered under the reading lamp. Obviously
            they were terrible housekeepers.'''
            print
            prompt_rea()
        else:
            print "That command is invalid"
            print
            prompt_rea()
    except ValueError:
        print "That command is invalid"
        print
        prompt_rea()
def servants_quarters():
    global gold
    print "Current Gold = ",gold
    print '''    You are in a small room, with a large, old bed. There is an open
    wardrobe in the corner with a small amount of clothes still in it.
    Obviously a servant used to sleep here.

    Type 'help' for a full list of commands.'''
    print
    prompt_SQ()
def serv_desc():
    print '''    There is an open wardrobe in the corner with
    a small amount of clothes still in it. There is a large bed.'''
    print
def prompt_SQ():
    global gold
    global gotGold_SQ
    prompt_s = raw_input("Type a command: ").lower()
    try:
        if prompt_s == "w":
            foyer()
        elif prompt_s == "n":
            living_room()
        elif prompt_s == "help":
            help1()
            prompt_SQ()
        elif prompt_s == "examine bed":
            if gotGold_SQ == 0:
                print '''    There are no bedclothes. The mattress is old and motheaten. You
                see a hole with gold pieces in it. There are five.'''
                print
                prompt_SQ()
            elif gotGold_SQ == 1:
                print '''    There are no bedclothes. The mattress is old and motheaten. There
                is a hole in the matress.'''
                print
                prompt_SQ()
        elif prompt_s == "examine wardrobe":
            print "The door is ajar. You see a maid's uniform, but there is nothing of interest."
            print
            prompt_SQ()
        elif prompt_s == "take gold":
            if gotGold_SQ == 0:
                print "You get 5 gold!"
                print
                gold = gold+5
                gotGold_SQ = 1
                servants_quarters()
            elif gotGold_SQ == 1:
                print "There is no gold here."
                print
                prompt_SQ()
        elif prompt_s == "look":
            serv_desc()
        else:
            print "That command is invalid"
            print
            prompt_SQ()
    except ValueError:
        print "That command is invalid"
        print
        prompt_SQ()
def living_room():
    global gold
    print "Current Gold = ",gold
    print '''    You are in a large room. There is an old, decaying sofa and
    a chair that has fallen into disrepair. Both are covered in cobwebs.
    There is an old, dusty fireplace, with a large chimney. The logs and carpet
    are caked with soot, presumably recent. It appears to have been a living
    room at some point. There are exits (n)orth, (w)est and (s)outh.

     Type 'help' for a full list of instructions.'''
    print
    prompt_liv()
def liv_desc():
    print '''    There is an old, decaying sofa and a chair that has
    fallen into disrepair. Both are covered in cobwebs. There is an old,
    dusty fireplace, with a large chimney. The logs and carpet are caked
    with soot, presumably recent.'''
    print
    prompt_liv()
    
def prompt_liv():
    global gold
    global gotGold_liv
    print
    prompt_l = raw_input("Type a command: ").lower
    try:
        if prompt_l == "s":
            servants_quarters()
        elif prompt_l =="n":
            conservatory()
        elif prompt_l == "examine sofa":
            print '''    The sofa is in disrepair, there are springs poking
            out everywhere.'''
            print
            prompt_liv()
        elif prompt_l == "help":
            help1()
            prompt_liv()
        elif prompt_l == "w":
            mail_hall()
        elif prompt_l == "examine fireplace":
            if gotGold_liv == 0:
                print "There are ten, slightly sooty, gold pieces in the hearth."
                print
                prompt_liv()
            elif gotGold_liv == 1:
                print "The hearth is a mess."
                print
                prompt_liv()
        elif prompt_l == "examine chair":
            print "The chair is in awful condition. The cushions have rising damp."
            print
            prompt_liv()
        elif prompt_l == "take gold":
            if gotGold_liv == 0:
                print "You got 10 gold!"
                print
                gold = gold+10
                gotGold_liv = 1
                living_room()
            elif gotGold_liv == 1:
                print "There is no gold here."
                print
                prompt_liv()
        elif prompt_l == "look":
            liv_desc()
        else:
            print "That command is invalid"
            print
            prompt_liv()
    except ValueError:
        print "That command is invalid"
        print
        prompt_liv()

def main_hall():
    global gold
    print "Current Gold = ",gold
    print '''    You are in the main hall. You see a staircase, however it has
    collapsed. There are three portraits surrounding you, captioned with names:
    Master Daniel Redwood, Mistress Stephanie Redwood and Mister Ivan Redwood.
    There are four exits, (n)orth, (s)outh, (e)ast and (w)est.'''
    print
    prompt_main()
def main_desc():
    print '''    You see a staircase, however it has
    collapsed. There are three portraits surrounding you, captioned with names:
    Master Daniel Redwood, Mistress Stephanie Redwood and Mister Ivan Redwood.'''
    print
    prompt_main()
def prompt_main():
    prompt_m = raw_input("Type a command: ").lower()
    try:
        if prompt_m == "s":
            foyer()
        elif prompt_m == "e":
            living_room()
        elif prompt_m == "w":
            drawing_room()
        elif prompt_m == "n":
            kitchen()
        elif prompt_m == "help":
            help1()
            prompt_main()
        elif prompt_m == "look":
            main_desc()
        elif prompt_m == "examine pictures":
            print '''    The family look happy in their respective photos.
            They are wearing champion ribbons.'''
            prompt_main()
        elif prompt_m == "examine staircase":
            print "The stairs are totally destroyed."
            prompt_main()
        else:
            print "That command is invalid"
            print
            prompt_main()
    except ValueError:
        print "That command is invalid"
        print
        prompt_main()
def drawing_room():
    global gold
    print "Current gold = ",gold
    print '''    You are in the drawing room. There is a table with documents
    scattered all over it. There is a single painting, a portrait of the wife,
    on the south wall. The bookshelves here are filled with diaries.

    The exits are (n)orth, (s)outh and (e)ast.'''
    print
    prompt_draw()
def draw_desc():
    print '''    There is a table with documents scattered all over it.
    There is a single painting, a portrait of the wife, on the south wall.
    The bookshelves here are filled with diaries.'''
    print
    prompt_draw()
def prompt_draw():
    global gold
    global gotGold_draw
    prompt_d = raw_input("Type a command: ").lower()
    try:
        if prompt_d == "s":
            reading_room()
        elif prompt_d == "e":
            main_hall()
        elif prompt_d =="n":
            dining_room()
        elif prompt_d == "look":
            draw_desc()
        elif prompt_d == "examine bookshelves":
            print "The shelves are cluttered with diaries."
            print
            prompt_draw()
        elif prompt_d == "examine table":
            print '''    The floor plans are detailed here. The ground floor is layed out
            in a three-by-three grid.'''
            print
            prompt_draw()
        elif prompt_d == "examine portrait":
            if gotGold_draw == 0:
                print '''    She was hauntingly beautiful. There is a single
                gold piece adorning the frame.'''
                print
                prompt_draw()
            elif gotGold_draw == 1:
                print "She was hauntingly beautiful."
                print
                prompt_draw()
        elif prompt_d == "take gold":
            if gotGold_draw == 0:
                print "You got 1 gold!"
                gold = gold+1
                gotGold_draw = 1
                prompt_draw()
            elif gotGold_draw == 1:
                print "There is no gold here"
                print
                prompt_draw()
        elif prompt_d == "help":
            help1()
            prompt_draw()
        else:
            print "That command is invalid"
            print
            prompt_draw()
    except ValueError:
            print "That command is invalid"
            print
            prompt_draw()
def conservatory():
    global gold
    print "Current gold = ",gold
    print '''    You are in a large glass conservatory. There are plants everywhere.
    There is a set of garden furniture right in the centre, and an assortment of
    plants, potted around the edge. There are exits to the (s)outh and (w)est.

    Type 'help' for a full list of commands.'''
    print
    prompt_con()
def con_desc():
    print '''    You are in a large glass conservatory. There are plants everywhere.
    There is a set of garden furniture right in the centre, and an assortment of
    plants, potted around the edge.'''
    print
def prompt_con():
    prompt_c = raw_input("Type a command: ").lower()
    try:
        if prompt_c == "s":
            living_room()
        elif prompt_c == "w":
            kitchen()
        elif prompt_c == "examine plants":
            print '''    There are several varieties of flowers and vines planted
            in various locations in the conservatory.'''
            print
            prompt_con()
        elif prompt_c == "look":
            con_desc()
        elif prompt_c == "examine furniture":
            print '''    The furniture is a complete set. It is white. There are
            three tables and a chair.'''
            print
            prompt_con()
        elif prompt_c == "help":
            help1()
            prompt_con()
        else:
            print "That command is invalid"
            print
            prompt_con()
    except ValueError:
        print "That command is invalid."
        print
        prompt_con()

def kitchen():
    global gold
    print "Current Gold = ",gold
    print '''    You are in a large kitchen. The sideboard is solid mahogany,
    but hopelessly scratched. There is a large rusted gas stove in the corner
    with what looks like a mouldy roast inside. The knife rack has a large
    and menacing array of pointy things, but in stark contrast the cupboards
    are all bare. The exits are (s)outh, (e)ast and (w)est.

    Type help for a full list of commands.'''
    print
    prompt_kit()
def kit_desc():
    print '''    The sideboard is solid mahogany, but hopelessly scratched.
    There is a large rusted gas stove in the corner with what looks like
    a mouldy roast inside.The knife rack has a large and menacing array of
    pointy things, but in stark contrast the cupboards are all bare.'''
    print
    prompt_kit()
def prompt_kit():
    prompt_k = raw_input("Type a command: ").lower()
    try:
        if prompt_k == "s":
            main_hall()
        elif prompt_k == "e":
            conservatory()
        elif prompt_k == "w":
            dining_room()
        elif prompt_k == "look":
            kit_desc()
        elif prompt_k == "examine sideboard":
            print '''    The sideboard has been badly scratched. The wood is
            worn away to almost nothing'''
            print
            prompt_kit()
        elif prompt_k == "examine stove":
            print "The stove is broken."
            print
            prompt_kit()
        elif prompt_k == "examine roast":
            print "Eeeeewwww!"
            print
            prompt_kit()
        elif prompt_k == "examine rack":
            print "The rack is full of sharp objects. Better stay away!"
            print
            prompt_kit()
        elif prompt_k == "examine cupboard":
            print "Empty"
            print
            prompt_kit()
        elif prompt_k == "help":
            help1()
            prompt_kit()
        else:
            print "That command is invalid!"
            print
            prompt_kit()
    except ValueError:
        print "That command is invalid!"
        print
        prompt_kit()

def dining_room():
    global gold
    print "Current Gold = ",gold
    print '''    There is a large oak table in the centre of the room. It, unlike
    the rest of the house, is in good condition. There are 6 chairs around the table
    that must have been used for the family and their friends. There is a large vase
    in the corner that is decorated with a Salvador Dali work involving melting
    clocks. On the north wall is a family photo containing not just the father, mother
    and children but other family members too. On the west wall is a tapestry
    depicting a great battle.
    The Exits are (s)outh and (e)ast.

    Type 'help' for a full list of commands.'''
    print
    prompt_din()
def din_desc():
    print '''    There is a large oak table in the centre of the room. It, unlike
    the rest of the house, is in good condition. There are 6 chairs around the table
    that must have been used for the family and their friends. There is a large vase
    in the corner that is decorated with a Salvador Dali work involving melting
    clocks. On the north wall is a family photo containing not just the father, mother
    and children but other family members too. On the west wall is a tapestry
    depicting a great battle.'''
    print
    prompt_din()
def prompt_din():
    global gotGold_din
    global gold
    prompt_di=raw_input("Type a command: ").lower()
    try:
        if prompt_di == "e":
            kitchen()
        elif prompt_di == "s":
            drawing_room()
        elif prompt_di == "help":
            help1()
            prompt_din()
        elif prompt_di == "examine table":
            print "The table is untarnished. Strange..."
            print
            prompt_din()
        elif prompt_di == "examine chairs":
            print "There are enough for the whole family and three guests"
            print
            prompt_din()
        elif prompt_di == "examine vase":
            if gotGold_din == 0:
                print "There are 4 gold pieces in the vase."
                print
                prompt_din()
            elif gotGold_din == 1:
                print "It has a picture by Salvador Dali on it."
                print
                prompt_din()
        elif prompt_di == "examine photo":
            print "An old family photo. How sweet."
            print
            prompt_din()
        elif prompt_di == "examine tapestry":
            print "It depicts a ferocious war in the year... Let's see... 26BC."
            print
            prompt_din()
        elif prompt_di == "take gold":
            if gotGold_din == 0:
                print "You got 4 gold"
                gotGold_din = 1
                gold=gold+1
                print
                dining_room()
            elif gotGold_din == 1:
                print "No gold here"
                print
                prompt_din()
        else:
            print "That command is invalid"
            print
            prompt_din()
    except ValueError:
        print "That command is invalid"
        print
        prompt_din()
def ending():
    print '''    You place the coins on the doormat. The voice rings out again:
    "I thank you for gathering these coins that I lost. I need them to fix the stairs.
    I can't get upstairs if the stairs are gone, and that is where I pay my bills.
    You may go now." And with that, the bolt disintegrates, allowing the door to swing
    open and you to leave.

    THE END'''

    dummy = raw_input("Press any button to quit.")
    
start()
foyer()
