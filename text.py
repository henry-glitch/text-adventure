# import only system from os 
from os import system, name 
from os import startfile
import random
import time 
# import sleep to show output for some time period 
from time import sleep 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def menu(): 
#title
    print("        ,----,                                                                                                                                          ")
    print("      ,/   .`|                                                                                                                                          ")
    print("    ,`   .'  :  ,---,                         ,---,                                                   ,--,                                              ")
    print("  ;    ;     /,--.' |                        '  .' \      ,-.----.                                  ,--.'|             ,-.----.                         ")
    print(".'___,/    ,' |  |  :                       /  ;    '.    \    /  \    ,---.                        |  | :             \    /  \                        ")
    print("|    :     |  :  :  :                      :  :       \   |   :    |  '   ,'\                       :  : '             |   :    |  .--.--.              ")
    print(";    |.';  ;  :  |  |,--.   ,---.          :  |   /\   \  |   | .\ : /   /   |   ,---.     ,--.--.  |  ' |        .--, |   | .\ : /  /    '     ,---.   ")
    print("`----'  |  |  |  :  '   |  /     \         |  :  ' ;.   : .   : |: |.   ; ,. :  /     \   /       \ '  | |      /_ ./| .   : |: ||  :  /`./    /     \  ")
    print("    '   :  ;  |  |   /' : /    /  |        |  |  ;/  \   \|   |  \ :'   | |: : /    / '  .--.  .-. ||  | :   , ' , ' : |   |  \ :|  :  ;_     /    /  | ")
    print("    |   |  '  '  :  | | |.    ' / |        '  :  | \  \ ,'|   : .  |'   | .; :.    ' /    \__\/: . .'  : |__/___/ \: | |   : .  | \  \    `. .    ' / | ")
    print("    '   :  |  |  |  ' | :'   ;   /|        |  |  '  '--'  :     |`-'|   :    |'   ; :__   ,\" .--.; ||  | '.'|.  \  ' | :     |`-'  `----.   \'   ;   /|")
    print("    ;   |.'   |  :  :_:,''   |  / |        |  :  :        :   : :    \   \  / '   | '.'| /  /  ,.  |;  :    ; \  ;   : :   : :    /  /`--'  /'   |  / | ")
    print("    '---'     |  | ,'    |   :    |        |  | ,'        |   | :     `----'  |   :    :;  :   .'   \  ,   /   \  \  ; |   | :   '--'.     / |   :    | ")
    print("              `--''       \   \  /         `--''          `---'.|              \   \  / |  ,     .-./---`-'     :  \  \`---'.|     `--'---'   \   \  / ")
    print("                           `----'                           `---`               `----'   `--`---'                \  ' ;  `---`                 `----'   ")
    print("                                                                                                                  `--`                                  ")
    print("\n")
    #introduction


    print(" _ __ ___   ___ _ __  _   _ ")
    print("| '_ ` _ \ / _ \ '_ \| | | |")
    print("| | | | | |  __/ | | | |_| |")
    print("|_| |_| |_|\___|_| |_|\__,_|")
    print("1) new game")
    print("2) instructions")
    print("3) quit")
    q = input()
    if q == "1":
        start()
    elif q == "2":
        print("to play the game you must enter your choise of charecter and try and mmake it to the base!")
    elif q == "3":
        quit()

    
def shop(reason):
    print("youy go to the shop looking for reason")
    random3 = random.randint(1,10)
    if random3 == 1:
        item == "Cheese"
    elif random3 == 2:
        item == "Pump shotgun"
    elif random3 == 3:
        item == "lanyard"
    elif random3 == 4:
        item == "water"
    elif random3 == 5:
        item == "sleeping bag"
    elif random3 == 6:
        item == "oats"
    elif random3 == 7:
        item == "knife"
    elif random3 == 8:
        item == "firework"
    elif random3 == 9:
        item == "16th century sword"
    elif random3 == 9:
        item == "skittles"
    elif random3 == 9:
        item == "skittles"
        
    print("                                   .-.,-.")
    print("                                  _|_||_|_")
    print("                                ,'|--'  __|")
    print("                                |,'.---'-.'")
    print("  ___                            |:|] .--|")
    print(" (__ ```----........_________...-|-|__'--|-........_________.....")
    print("  \._,```----........__________..::|--' _|--........_________....")
    print("  :._,._,._,._,._,._,._,._,._,._,\\|___'-|._,._,._,._,._,._,._,._")
    print("  |._,._,._,._,._,._,._,._,._,._,.`'-----'._,._,._,._,._,._,._,._")
    print("  |._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._")
    print("  |._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._")
    print("  ;._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._")
    print(" /,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._,._")
    print(" )________)________)________)________)________)________)_______)_")
    print("  |::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.-")
    print("  |_|_  .----._     ___.-_-__-_-.--.-'          __.-.-_-__-_-. '-")
    print("  |---' '--.-'-'.  '-.-||_|__|_||--'           '--'-||_|__|_||_")
    print("  |        '----'    '-|| |  | ||             ____.-|| |  | ||-'")
    print("  |                   [||-|--|-||_           '--.-'-||-|--|-||")
    print("  |-.____              ||_|__|_||-'-.           '---||_|__|_||_ _")
    print("  |-'-.--'       ___.--||_|__|_||---' ___.--.       ||_|__|_||_'-")
    print("  |---'         '---'--'--------'    '---'--'       '--------'")
    print("  ;--.______________________________________________,--._________")
    print("  :(o))---------------------------------------------:(o))--------")
    print("  |`-: \//|[_  /,.\|| |,\|[_  ((_ |[]|/,.\|o)|o)|[_ |`-: ((_ ||| ")
    print("  |__| // |[_  \`'/|'-|`/|[_   _))|[]|\`'/|| || |[_ |__|  _))|||`")
    print("  |--|____________________________________________  |--|  _______")
    print("  |  |       |`-||__|--|__|--|__|--|__|--|__|--|__| |__| ||__|--|")
    print("  |  |_____  |._|.-------..-------..-------..----.| |  | |.------")
    print("  |  |.-.-.| |  ||::'    ||::'    ||::'    ||:'  || |  | ||:'")
    print("  |  || | || |  ||'      ||'      ||'      ||    || |  | ||____.:")
    print("  |  ||-|-|| |  ||       ||       ||       ||    || |  | |.------")
    print("  |  || | || |  ||      .||      .||      .||    || |  | ||:'")
    print("  |__|'-'-'|/:._||___..::||___..::||___..::||__.:|| |__| ||____.:")
    print("  |  |     || `-|---------------------------------.'|  |'.-------")
    print(" _|__|-----''-..| ________________________________|_|__|_|_______")
    delay(2)


#death message
def death():
    print("                                 _____  _____                           ")
    print("                                <     `/     |                          ")
    print("                                 >          (                           ")
    print("                                |   _     _  |                          ")
    print("                                |  |_) | |_) |                          ")
    print("                                |  | \ | |   |                          ")
    print("                                |            |                          ")
    print("                 ______.______%_|            |__________  _____         ")
    print("               _/                                       \|     |        ")
    print("              |               D U M B   A S S                  <        ")
    print("              |_____.-._________              ____/|___________|        ")
    print("                                | * 10/9/30  |                          ")
    print("                                |            |                          ")
    print("                                |            |                          ")
    print("                                |            |                          ")
    print("                                |   _        <                          ")
    print("                                |__/         |                          ")
    print("                                 / `--.      |                          ")
    print("                               %|            |%                         ")
    print("                           |/.%%|          -< @%%%                      ")
    print("                           `\%`@|     v      |@@%@%%                    ")
    print("                         .%%%@@@|%    |    % @@@%%@%%%%                 ")
    print("                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%             ")

#room3
def followman():
    print("the man says that he knows a base three miles south of here")
    print("do you either")
    print("a)follow him")
    print("b)spend the night alone")
    c =input("enter a or b")
    if c == "a":
        print("")
        randint =random.randint(1,2)
        if randint == 1:
            print("You end up cornered in an alleyway")
            print("cornered against the wall the man calls out to you saying that this is it")
            print("Do you either")
            print("a)leave him behind")
            print("b)try and take him with you")
            random1 = random.randint(1,2)
            if c == "b" & random2 == 1:
                print("You pull him up he struggles and falls victim to the hord of zombies")
                death()
        else:
            print("you make camp in ")
    elif c == "b":
        print("a group of hunters pins you up against the wall and asks you if you have any food or weapons")
        for index, item in enumerate(items):
            henry.pop() 
        
        
        random2 =random.randint(1,2)
        if random2 == 1:
            print("The man takes your stuff then shoots you")
            print("          ^ ")        
            print("         | |  ")      
            print("       @#####@  ")    
            print("     (###   ###)-. ") 
            print("   .(###     ###) \ ")
            print("  /  (###   ###)   )")
            print(" (=-  .@#####@|_-- 	GET riggidy recked son")
            print(" /\    \_|l|_/ (\   	")
            print("(=-\     |l|    /   ")
            print(" \  \.___|l|___/    ")
            print(" /\      |_|   /    ")
            print("(=-\._________/\    ")
            print(" \             /    ")
            print("   \._________/     ")
            print("     #  ----  #     ")
            print("     #   __   #      ") 
            print("     \########/     ") 
            death()
            delay(5)
            clear()
    else:
        print("They let you go on one condition that you find and kill the man that aimed a crossbow at your head")
        killman = True
            
    
    

#room2


def man():
    print("you run towards the  warehouse and slam the door behind yourself The man jolts around and aims a crossbow at our head")
    print("            .-.        ")
    print("           /  \\       ")                      
    print("      .---/-+--||      ")                      
    print("     |  K=====++->     ")                       
    print("      '---\-+--||      ")                         
    print("           \  //       ")                         
    print("            `-'        ")
    print("Do you Either")
    print("a) talk to him")
    print("b) Go and try and kill the man")
    b = input("Enter a or b: ")
    if b == "a":
        print("you call out to him explaining you cause no harm")
        followman()
        if name == ross:
          print("your lack of any social skills concludes with you ")
          print("messing up  and being shot")
          print("                                                       |")
          print("                                                        \.")
          print("                                                        /|.")
          print("                                                      /  `|.")
          print("                                                    /     |.")
          print("                                                  /       |.")
          print("                                                /         `|.")
          print("                                              /            |.")
          print("                                            /              |.")
          print("                                          /                |.")
          print("     __                                 /                  `|.")
          print("      -\                              /                     |.")
          print("        \\                          /                       |.")
          print("          \\                      /                         |.")
          print("           \|                   /                           ||")
          print("             \#####\          /                             ||")
          print("         ==###########>     /                               ||")
          print("          \##==      \    /                                 ||")
          print("     ______ =       =|__/___                                ||")
          print(" ,--' ,----`-,__ ___/'  --,-`-==============================##==========>")
          print("\               '        ##_______ ______   ______,--,____,=##,__")
          print(" `,    __==    ___,-,__,--'#'  ==='      `-'              | ##,-/")
          print("   `-,____,---'       \####\              |        ____,--\_##,/")
          print("       #_              |##   \  _____,---==,__,---'         ##")
          print("        #              ]===--==\                            ||")
          print("        #,             ]         \                          ||")
          print("         #_            |           \                        ||")
          print("         ##_       __/'             \                      ||")
          print("           ####='     |                \                    |/")
          print("            ###       |                  \                  |.")
          print("            ##       _'                    \                |.")
          print("           ###=======]                       \              |.")
          print("          ///        |                         \           ,|.")
          print("          //         |                           \         |.")
          print("                                                   \      ,|.")
          print("                                                     \    |.")
          print("                                                       \  |.")
          print("                                                         \|.")
          print("                                                         /.")
          print("                                                        |")
          death1()
          quit()
    
    elif b == "b":
        print("The last thing you ever fell is cold metal slide through your head")
        print("\n")
        death()
        sleep(5)
        quit()
    else:
        print("That was not an option.  Game Over")
        quit()





def start():                                  
    print("The year was 2036 a new Pathogen was released by a terrorist organization wanting to create a new world  ")
    print("order it was spread from across the world before anyone noticed.The virus had a rabies gene that lead humans")
    print("2 months later the world is in collapse business, governments and civilization fell into collapse the people")
    print("Who are still alive search in the shadows for what is left trying to rebuild there reality.")
    print("\n")
    print("\n")
    print("choose your character")
    print("a)Harry")
    print("abilities) neckback")
    print("disability)low 1Q ,no parents")
    print("    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(" XXXXXXXXXXXXXXXXXX         XXXXXXXX")
    print("XXXXXXXXXXXXXXXX              XXXXXXX")
    print("XXXXXXXXXXXXX                   XXXXX")
    print(" XXX     _________ _________     XXX")     
    print("  XX    I  _xxxxx I xxxxx_  I    XX")        
    print(" ( X----I         I         I----X )")          
    print("( +I    I      00 I 00      I    I+ )")
    print(" ( I    I    __0  I  0__    I    I )")
    print("  (I    I______ /   \_______I    I)")
    print("   I           ( ___ )           I")
    print("   I    _  :::::::::::::::  _    i")
    print("    \    \___ ::::::::: ___/    /")
    print("     \_      \_________/      _/")
    print("       \        \___,        /")
    print("         \                 /")
    print("          |\             /|")
    print("          |  \_________/  |")
    sleep(5)
    clear()
    print("b) Ross ")
    print("abilities) High IQ")
    print("disability) socially awkward")
    print("                        ;;\\/;;;;;;;;")
    print("                   ;;;;;;;;;;;;;;;;;")
    print("                ;;;;;;;;;;;;     ;;;;;")
    print("               ;;;;;    ;;;         \;;")
    print("              ;;;;;      ;;          |;")
    print("             ;;;;         ;          |")
    print("            ;;;                     |")
    print("             ;;                     )")
    print("               \    ~~~~ ~~~~~~~    /")
    print("                \    ~~~~~~~  ~~   /")
    print("              |\ \                / /|")
    print("               \\| %%%%%    %%%%% |//")
    print("              [[====================]]")
    print("               | |  ^          ^  |")
    print("              | | :@: |/  \| :@: | |")
    print("                \______/\  /\______/")
    print("                 |     (@\/@)     |")
    print("                /                  |")
    print("               /  ;-----\  ______;  |")
    print("               \         \/         /")
    print("                )                  (")
    print("               /                    |")
    print("               \__                  /")
    print("                \_                _/")
    print("                 \______/\/\______/")
    print("                  |               | ")
    sleep(5)
    clear()
    print("c) henry")
    print("abilities) Strong , stamina ")
    print("disabilities) cake")
    print("                 ,#####,")
    print("                 #_   _#")
    print("                 |0` `0|")
    print("                 |  u  |")
    print("                 \  =  /")
    print("                 |\___/|")
    print("        ___ ____/:     :\____ ___")
    print("      .'   `.-===-\   /-===-.`   '.")
    print("     /      .-....._.-....-.      |")
    print("    /'             =:=             '|")
    print("  .'  ' .:    o   -=:=-   o    :. '  `.")
    print("  (.'   /'. '-.....-'-.....-' .'\   '.)")
    print("  /' ._/   ..     --:--     ..   \_. '|")
    print(" |  .'|      ..  ---:---  .      |'.  |")
    print(" |  : |       |  ---:---  |       | :  |")
    print("  \ : |       |_____._____|       | : /")
    print("  /   (       |----|------|       )   |")
    print(" /... .|      |    |      |      |. ...|")
    print("|::::/''     /     |       \     ''\::::|")
    print("'....       /'    .L_      `\       ....'")
    print("           /'-.,__/` `\__..-'|")
    print("          ;      /     \      ;")
    print("          :     /       \     |")
    print("          |    /         \.   |")
    print("          |`../           |  ,/")
    print("         ( _ )            |  _)")
    print("          |   |           |   |")
    print("          |___|           \___|")
    print("          :===|            |==|")
    print("           \  /            |__|")
    print("           /\/\           /....--")
    print("           |oo|           \__.//___)")
    print("           |==|")
    print("           \__/")
    henry = {
      "Weapon": "Katana",
      "food": "bread",
      "money": 1987,
    }
    sleep(5)
    clear()
    name = input("choose your charecter")
    harry = "a"
    ross = "b"
    room1()
    henry = "c"
    room1()
    if name == harry:
        print("your retard self gets wheelchair stuck in the ")
        print("gutter you dont last long before the zombie's get to you ")
        print("you start bluffing relising how crippled you are and that your only")
        print("achievement was knowing henry in secondary school")
        print("your life flashes before your eyes you see ")
        print("the day his mum was so ugly his dad had a husband")
        print("your brains lied on the floor ")
        print("      .__---~~~~~-_.")
        print("   _-'  \) -~~- \) _-- ")
        print("  (  ( `-,_..`.,_--_ '_,\)_")
        print(" (  -_\)  ( -_-~  -_ `,    )")
        print(" (_ -_ _-~-__-~`, ,' )__-'))--___--~~~--__--~~--___--__..")
        print(" _ ~`_-'( (____;--==,,_))))--___--~~~--__--~~--__----~~~'`=__-~+_-_.")
        print("(@) (@) `````      `-_(())_-~  ")
        death1()
        sleep(5)
        clear()
        quit()

    
#room 1
def room1():
    print("You Sprint down the street running from the zombies,you hear voices coming from inside a abondened warehouse.")
    print("Do you Either")
    print("a) keep on running.")
    print("b) Go  and investigate")
    x = input("Enter a or b: ")
    if x == "a":
        print("The zombies hunt you down and trap you against the wall You died")
        print("The zombies to your brain")
        
        sleep(5)
        clear()
    elif x == "b":
        print("You go in to investigate.")
        print("A man dressed in tattered old clothing turns around aims his crossbow at your head")
        man()
        sleep(5)
        clear()
    else:
        print("That was not an option.  Game Over")
        print("question your life choises")
        death()
        sleep(5)
        clear()
menu()

