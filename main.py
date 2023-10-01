from Dialogue import Dialogue
from Dialogue import Option
import os

if __name__ == "__main__":
    playerItems = []
    isWarlord = False
    familyMurdered = False
    slaveTraded = False
    prisonered = False
    examScore = 0
    
    def reset():
        global playerItems
        global isWarlord
        global examScore
        global slaveTraded
        global prisonered
        global familyMurdered
        playerItems = []
        isWarlord = False
        familyMurdered = False
        slaveTraded = False
        prisonered = False
        examScore = 0
        
    def warlord():
        global isWarlord
        isWarlord = True
        
        game.RemoveOption("5,2", 0)
        game.AddOption("5,2", Option("Try bribing them and tell them about your warlord slaughters.", "5,2,1"))

    def slaveTrader():
        global slaveTraded
        slaveTraded = True
        
    def prisoner():
        global prisonered
        prisonered = True
        
    def familyMurder():
        global familyMurdered
        familyMurdered = True
    
    game = Dialogue()
    
    game.AddNode("death", "You died!", [
        Option("Restart", "0", reset)
    ])
    game.AddNode("slavery", "You have been enslaved and have been forced to work till your death.", [
        Option("aww man", "0", reset)
    ])

# Exam
    def score():
        global examScore
        examScore+=1
        if examScore >= 2:
            game.RemoveNode("0,5")
            game.AddNode("0,5", "The exam results are back: You PASSED.", [
                Option("Take the ship keys and fly off into space towards your eventual doom and death.", "1"),
            ])

    game.AddNode("0", "Welcome to the best pilot exam in the whole universe. I am your host Dickinson today we are pleased to announce the start of the shortest flight exam. And we want you as our student to pick your own subject at the reception.", [
        Option("Go to the reception.", "0,1"),
        Option("Wait and try to befriend people.", "0,2"),
        Option("Go the hangar and look at ships.", "0,3"),
        Option("Keep listening to Dickinson.", "0,4"),
    ])
    game.AddNode("0,1", "You have arrived at the reception", [
        Option("Choose your subjects.", "0,1,1"),
        Option("Ask where the toilet is.", "0,1,2"),
    ])
    game.AddNode("0,2", "You waited for 1 hour but no one came to talk to you. You should have realized you were destined to be a loner from the beginning. Sigh 눈_눈", [
        Option("Go to reception and choose your subject.", "0,1,1"),
    ])
    game.AddNode("0,3", "You took too long looking at the beautiful ships that you almost forgot to choose your subjects. (¬_¬)", [
        Option("Go to reception and choose your subject.", "0,1,1"),
    ])
    game.AddNode("0,4", "You kept listening but nothing important came out of his mouth.", [
        Option("Go to the reception and choose your subject.", "0,1,1"),
    ])
    # options 0,1,1
    game.AddNode("0,1,1", "You can choose between the following subject branches.", [
        Option("Meth, Botanical nature and Flying.", "0,1,1,1"),
        Option("Meth, Flying and Languages.", "0,1,1,2"),
        Option("Meth, Informatica and Flying.", "0,1,1,3"),
    ])
    # meth botanical nature
    game.AddNode("0,1,1,1", "You chose Meth, Botanical nature and Flying. You passed the practical exam. Next are the theoretical Questions. Question 1: Do penguins fly?", [
        Option("Yes.", "0,1,1,1,1"),
        Option("No.", "0,1,1,1,1", score),
    ])
    game.AddNode("0,1,1,1,1", "Question 2: What is the poppy plant mostly used for?", [
        Option("Medical purposes.", "0,5"),
        Option("trading purposes.", "0,5"),
        Option("recreational purposes", "0,5", score),
    ])
    # meth language
    game.AddNode("0,1,1,2", "You chose Meth, Flying and Languages. You passed the practical exam. Next are the theoretical Questions. Question 1: Do you ever pick your nose when you think nobody is watching?", [
        Option("Yes.", "0,1,1,2,1", score),
        Option("No.", "0,1,1,2,1", score),
    ])
    game.AddNode("0,1,1,2,1", "Question 2: muraho mute mukora abantu", [
        Option("byiza (yes)", "0,5", score),
        Option("oya (no)", "0,5"),
    ])
    # meth informatica
    game.AddNode("0,1,1,3", "You chose Meth, Informatica and Flying. You chose Informatica really? Are you mad. Question 1: What did jesse wanna do?", [
        Option("Dance.", "0,1,1,3,1"),
        Option("Cook.", "0,1,1,3,1", score),
    ])
    game.AddNode("0,1,1,3,1", "Question 2: what is x in: 'x=1; x+=x++;'?", [
        Option("x=4", "0,5"),
        Option("x=6", "0,5"),
        Option("x=3", "0,5", score),
    ])
    # options 0,1,2
    game.AddNode("0,1,2", "After going to the toilet you arrived at the main hall. Where mister Dickinson is still talking.", [
        Option("Ignore him and go back to the reception.", "0,1,1"),
        Option("Keep listening.", "0,1,2,2"),
    ])
    game.AddNode("0,1,2,2", "you kept listening but nothing important came out of his mouth.", [
        Option("Go to reception and choose your subject.", "0,1,1"),
    ]) 
    # results
    game.AddNode("0,5", "The exam results are back: You FAILED.", [
        Option("Try to steal a ship.", "0,5,1"),
    ])
    game.AddNode("0,5,1", "You succeeded in stealing the ship. They stopped the chase since they didn't think you would make it anyway.", [
        Option("Continue.", "1"),
    ])
# Xarpoh
    def steal():
        pass
        # playerItems.append("200.000 xorza")
        # playerItems.append("200 food rations")
        
    game.AddNode("1", "You land on a planet called Xarpoh, the people living there ask for your help to defend against invaders.", [
        Option("You help the people of Xarpoh.", "1,1"),
        Option("You help the invaders take over Xarpoh.", "1,2"),
        Option("You leave as fast as you can.", "1,3"),
    ])
    game.AddNode("1,1", "You help the people but the invaders are too strong.", [
        Option("Leave as fast as you can in your space ship", "1,1,1"),
        Option("Keep fighting the invaders", "1,1,2"),
        Option("You steal some supplies from Xarpoh and leave the planet", "1,1,3"),
    ])
    game.AddNode("1,1,1", "You left the planet safely and got away.", [
        Option("Continue", "2")
    ])
    game.AddNode("1,1,2", "The invaders are too strong and kill you.", [
        Option("Continue", "death")
    ])
    game.AddNode("1,1,3", "You stole some stuff and got away safely.", [
        Option("Continue", "2", steal)
    ])
    game.AddNode("1,2", "You fly towards the invaders and greet them, they don't mind the help and welcome you to their ship. They ask you to help them in strategy.", [
        Option("Recommend a suprise attack from the inside out.", "1,2,1"),
        Option("Recommend a massive push going straight for their main defenses.", "1,2,2"),
    ])
    game.AddNode("1,2,1", "The suprise attack failed drasticly, you luckily didn't go with them but they are now mad at you and chase you out of the system.", [
        Option("Continue", "2")
    ])
    game.AddNode("1,2,2", "The attack worked and you and the invaders took over the planet. Now branded as warlord you proceed on your adventures.", [
        Option("Continue", "2", warlord)
    ])
    game.AddNode("1,3", "You leave the planet Xarpoh as fast as you can but the invaders are following your every move.", [
        Option("Shoot at the invaders.", "1,3,1"),
        Option("Keep flying away.", "1,3,2"),
    ])
    game.AddNode("1,3,1", "You shoot at the enemies but miss every shot. They got scared and stopped the pursuit.", [
        Option("Continue", "2")
    ])
    game.AddNode("1,3,2", "You kept flying away. You have no idea where they are and got away safely for now.", [
        Option("Continue", "2")
    ])
# Ganon
    game.AddNode("2", "You landed in an icy biome in search of food and happen to come across the inhabiants of the planet.", [
        Option("Beg for food.", "2,1"),
        Option("Plunder and kill all inhabitants.", "2,2", warlord),
    ])
    game.AddNode("2,1", "The inhabitants are greedy and wont give you food no matter how much you beg.", [
        Option("You decide they are not worth begging to and kill and plunder them all", "2,2", warlord),
        Option("You have wasted too much time and decide to leave on an empty stomach in search of food.", "2,1,2"),
    ])
    game.AddNode("2,1,2", "After you left you stumble upon a cave where one of the inhabitants was mining resources.", [
        Option("You help him with mining.", "2,1,2,1"),
        Option("You ask him for food and leave the planet with food for 1 week.", "3"),
    ])
    game.AddNode("2,1,2,1", "After you mined together, You formed a great bond and get invited to eat at their home.", [
        Option("You eat your stomach full and leave while getting food for the journey and you get a teddy bear for along the way from their daughter. You leave the planet with enough food to last 2 weeks.", "3"),
        Option("You still decide you want to murder and plunder everyone after all the hours you had to beg.", "2,2"),
    ])
    
    game.AddNode("2,2", "You plunder and kill everyone you see.", [
        Option("You plunder and murder everyone you see and leave with enough food to last 4 weeks.", "3"),
        Option("You leave with the minimum requirements to survive out of guilt.", "3"),
    ])
# Harlan
    game.AddNode("3", "You landed on a small island enriched in water. You don't see anything with your binoculars and decide to get on the island. You take out you water-meter and start taking samples of the water to see if it's drinkable. The water is drinkable.", [
        Option("You fully fill the water-tank in your spaceship and decide to leave.", "3,1"),
        Option("While the water is filling you decide to explore the island.", "3,2"),
    ])
    game.AddNode("3,1", "After filling the water you get in your spaceship and leave.", [
        Option("Continue", "4")
    ])
    game.AddNode("3,2", " While exploring the island you get bit by a poisonous snake in you leg. You continue to explore more of the island in hope you find an antidote. Suddenly a 8 feet tall inhabitant is standing behind you.", [
        Option("You muster up the courage to ask for help by pointing at the place where you got bit.", "3,2,1"),
        Option("You get shocked and don't move an inch.", "3,2,2"),
    ])
    game.AddNode("3,2,1", "The inhabitants starts licking your leg at the place you got bit and puts something in your mouth. after that he start picking up leaves and vines and start dressing your leg. After dressing your wound the inhabitant leaves and you hurry back to your ship, Afraid you might get bitten again.", [
        Option("Continue", "4")
    ])
    game.AddNode("3,2,2", "The inhabitant leaves after a while. and you hurry back to your ship.", [
        Option("Leave the planet as fast as you can in hopes of finding civilization on another planet.", "3,2,2,1"),
        Option("Kill yourself.", "3,2,2,2"),
    ])
    game.AddNode("3,2,2,1", "While searching for a civilized planet you get struck by immense headache and start turning blue. Since you have no more option left you start bickering about your life while you are slowly dying. And think back about how you should have just asked the inhabitant if he knew a way to treat it. But you were to dumb and braindead to realise.", [
        Option("Continue", "death")
    ])
    game.AddNode("3,2,2,2", "You ready your gun.", [
        Option("Pull trigger.", "death")
    ])
# Ship
    game.AddNode("4", "You leave planet Harlan and just autopilot through space on to the next planet. While autopiloting you decide to take a rest.", [
        Option("Go to the sleeping chambers and take a nap.", "4,1"),
        Option("Go to the main hall and lie down on a sofa.", "4,2"),
    ])
    game.AddNode("4,1", "You took a nap.", [
        Option("Eat.", "4,1,1"),
        Option("Shower.", "4,1,2"),
    ])
    game.AddNode("4,1,1", "After having eaten, you decide to take a shower.", [
        Option("Shower.", "4,1,1,1"),
    ])
    game.AddNode("4,1,1,1", "After taking a shower, you decide to go to another planet.", [
        Option("Pilot the ship.", "5"),
    ])
    game.AddNode("4,1,2", "After having showered, you decide to eat.", [
        Option("Eat.", "4,1,2,1"),
    ])
    game.AddNode("4,1,2,1", "After having eaten, you decide to go to another planet.", [
        Option("Pilot the ship.", "5"),
    ])
    game.AddNode("4,2", "After lying down on the sofa, you decide to:", [
        Option("Eat.", "4,2,1"),
        Option("Shower.", "4,2,2"),
    ])
    game.AddNode("4,2,1", "After having eaten, you decide to take a shower.", [
        Option("Shower.", "4,2,1,1"),
    ])
    game.AddNode("4,2,1,1", "After taking a shower, you decide to go to another planet.", [
        Option("Pilot the ship.", "5"),
    ])
    game.AddNode("4,2,2", "After having showered, you decide to eat.", [
        Option("Eat.", "4,2,2,1"),
    ])
    game.AddNode("4,2,2,1", "After having eaten, you decide to go to another planet.", [
        Option("Pilot the ship.", "5"),
    ])
# EB-57806G
    # Add nodes and options for the EB-57806G scenario
    game.AddNode("5", "After a long travel you arrive at the planet EB-57806G. The onboard computer tells you that it has 29 billion inhabitants living on this planet and one of the strongest security systems.", [
        Option("Try to sneakily land on one of the landing pads.", "5,1"),
        Option("Request docking access using the onboard computer.", "5,2"),
    ])
    game.AddNode("5,1", "You got caught by the security. They bring you into a room for questioning. The first question they ask is 'Do you have a piloting license?'", [
        Option("No", "5,1,1"),
        Option("Yes", "5,1,2"),
    ])
    game.AddNode("5,1,1", "Even if you did, it wouldn't matter. We will lock you up anyway. Enjoy rotting away on Ezkbla, the prison planet. They drag you off to one of the transport vehicles heading to Ezkbla prison.", [
        Option("Continue", "6"),
    ])
    game.AddNode("5,1,2", "So why would you sneak in? We will lock you up since you're just kind of a creep. Enjoy rotting away on Ezkbla, the prison planet. They drag you off to one of the transport vehicles heading to Ezkbla prison.", [
        Option("Continue", "6"),
    ])



    game.AddNode("5,2", "Your docking access got denied.", [
        Option("Try bribing them.", "5,1"),
        Option("Force a landing on the landing pad.", "5,1"),
    ])
    
    

    game.AddNode("5,2,1", "They realize you are a warlord, and they become scared of you. They take your bribe and let you go free. You land your ship and step out, taking in the fresh air.", [
        Option("Go into the city and buy some food.", "5,2,1,1"),
        Option("Stay near the landing pad watching over the city.", "5,2,2"),
    ])

    game.AddNode("5,2,1,1", "After buying some food, you return to your ship and fly off into space.", [
        Option("Continue", "7"),
    ])

    game.AddNode("5,2,2", "A thief tries to steal your ship, but you caught him in the act.", [
        Option("Kill the thief and hide the body.", "5,2,2,1"),
        Option("Kill the thief and devour the body.", "5,2,2,2"),
    ])

    game.AddNode("5,2,2,1", "After killing the thief, you tried to hide the body as best as you can.", [
        Option("Continue", "6"),
    ])

    game.AddNode("5,2,2,2", "You took the body to your ship and ate him bit by bit until only a small pile of bones was left.", [
        Option("Continue", "7"),
    ])
# Ezkbla
    game.AddNode("6", " You found yourself on Ezkbla, a dreaded prison planet known for its unforgiving conditions and brutal guards. The planet's surface was a desolate wasteland, and the towering penitentiary complex loomed in the distance, surrounded by layers of security.", [
        Option("Attempt to escape.", "6,1", prisoner),
        Option("Bide your time.", "6,2", prisoner),
    ])
    game.AddNode("6,1", " Desperation and a desire for freedom gnawed at your every waking moment. You knew you had to make a daring escape from Ezkbla. There were two ways you could try:", [
        Option("Infiltrate the prison's underground network.", "6,1,1"),
        Option("Incite a prison riot.", "6,1,2"),
    ])
    game.AddNode("6,1,1", " You had heard rumors of a secret network of tunnels and rebels hiding beneath the prison. With stealth and cunning, you decided to search for a way into it. you decided to incite a rebellion and escape the planet.", [
        Option("Continue", "7"), 
    ])
    game.AddNode("6,1,2", " You incite a riot among the inmates, causing chaos that might distract the guards long enough for you to make your move and leave the planet with your ship.", [
         Option("Continue", "7"),
    ])
    game.AddNode("6,2", "Survival on Ezkbla was not just about escaping; it was about avoiding attention and staying alive. You chose to bide your time, keeping a low profile and observing the daily routines of the guards and prisoners.", [
        Option("Forge alliances with other inmates.", "6,2,1"),
    ])
    game.AddNode("6,2,1", " You knew that having allies on the inside could be your ticket to survival and possibly escape. You started building connections with other prisoners, seeking those who shared your desire for freedom to then attempt to escape.", [
        Option("Betray your allies escape on your own.", "6,2,1,1"),
        Option("Make a plan together with your allies to escape the prison.", "6,2,1,2"),
    ])
    game.AddNode("6,2,1,1", " You give away important information to the guards and tell them about a group which is trying to escape. When the guards go searching for the inmates you sneak past the control room and make your way to the hangar and escape.", [
        Option("Continue", "7"),
    ])
    game.AddNode("6,2,1,2", " One of you allies smugled a phone in through their a**. with that phone you and your allies order a ton of dynamite and ask for it to be dropped near the prison so you can escape while the guards are distracted. while escaping you get sprayed by the guards.", [
        Option("Because you are the faster than your allies you outrun and betray them.", "6,2,1,2,1"),
        Option("Because you are the faster than your allies you outrun and open the door.", "6,2,1,2,2"),
    ])
    game.AddNode("6,2,1,2,1", " Since you are the fastest among your allies you close the door of the ship and escape on you own leaving your allies to die.", [
        Option("Continue", "7"),
    ])
    game.AddNode("6,2,1,2,2", " since you arrived at the ship faster than your allies you leave the door open and provide supressing fire for you allies. The guards stopped supressive firing and started murdering your allies one by one leaving only you alive. Seeing them die in front of you triggerred effeminacy within you so you close the door and and escape, leaving your allies body in the cold.", [
        Option("Continue", "7"),   
    ])
# DeepSpace
    game.AddNode("7", "You are calmly traveling in deep space, not a planet or star in sight. There is no light in this part of space. You encounter a stranded ship with people on board but no fuel left.", [
        Option("Help them.", "7,1"),
        Option("Slaughter them.", "7,2", familyMurder),
    ])
    game.AddNode("7,1", "You have decide to help the suvivors of the stranded ship.", [
        Option("Give them a part of your fuel without docking.", "7,1,1"),
        Option("Give them a part of your fuel while docking.", "7,1,2"),
    ])
    game.AddNode("7,1,1", "You gave the stranded ship enough fuel to atleast make it to a busier part of space.", [
        Option("Leave deepspace.", "8"),
    ])
    game.AddNode("7,1,2", "You have docked your ship to theirs.", [
        Option("Invite them over for food.", "7,1,2,1"),
        Option("Pull out your weapon to murder the men and sell the women as slaves to another planet.", "7,1,2,2", slaveTrader),
    ])
    game.AddNode("7,1,2,1", "You invite them over for food. As you give them a warm greeting they pull out their taser and electrocute you and steal the ship. Luckily you have a gun in you pocket which they didn't seem to notice.", [
        Option("Give them your ship and live like a slave.", "slavery"),
        Option("Murder the bloody thieves.", "7,1,2,1,2"),
    ])
    game.AddNode("7,1,2,1,2", "You take out your gun and start spraying them whilst shouting for NOXUS. After murdering them you clean the ship and are ready to leave.", [
        Option("Quickly undock their ship and leave without looting.", "8"),
        Option("Loot and leave.", "7,2,2"),
    ])
    game.AddNode("7,1,2,2", "You enslaved the women and killed most of the men.", [
        Option("Loot their ship.", "7,2,2"),
        Option("Loot and leave.", "8"),
    ])
    game.AddNode("7,2", "You dock to their ship. While smiling you invite them for food in the main hall. You brutally slaughter the people and loot a taser from one of their pockets.", [
        Option("Undock the ship and leave.", "8"),
        Option("Loot their ship.", "7,2,2"),
    ])
    game.AddNode("7,2,2", "You looted the ship and found 10 ship components.", [
        Option("Repair your own ship.", "7,2,2,1"),
        Option("Leave deepspace.", "8"),
    ])
    game.AddNode("7,2,2,1", "You used 10 ship components to armor your ship.", [
        Option("Leave deepspace.", "8"),
    ])

#warpgate  
    game.AddNode("8", "You open a warpgate to leave deepspace. ", [
        Option("Initiate warpgate.", "8,1"),
    ])
    game.AddNode("8,1", "Just when you were going to press the button you feel an exhilirating pain in you lungs. You realise you dont have much oxygen left so you try to escape deepspace as fast as possible to find a planet to breath on.", [
        Option("Search on map for a planet.", "8,1,1"),
    ])
    game.AddNode("8,1,1", "You managed to find a small planet named Earth 100000 lightyears away from you.  ", [
        Option("Initiate warpgate.", "8,1,1,1"),
    ])
    game.AddNode("8,1,1,1", "while warping your ship hits an astroid in between the warp gate slowing time. As you're trying to look for anything that works so you could potentialy fix the gate. but nothing seems work even the tv is frozen on the same news. even the water doesn't run and you dont feel anything anymore even the pain is gone now.  ", [
        Option("...", "9"),
    ])

# Death
    def generateTvShow():
        game.RemoveNode("9,1")
        title = ""
        if prisonered:
            title += "Escaped "
        if slaveTraded:
            title += "Slave Trader "
        if isWarlord:
            title += "Warlord "
        if familyMurdered:
            title += "Murdered a whole family left stranded in deep space."
            
        if not prisonered and not slaveTraded and not isWarlord and not familyMurdered:
            title = "You"
            
        game.AddNode("9,1", f"You turn on the tv and sit down. The old news from 3 weeks ago is up. Its talking about some guy: '{title}' and the horrible acts committed", [
            Option("Give it one last try.", "9,1,1"),
            Option("Give up.", "9,1,2"),
        ])
        
    game.AddNode("9", "You lay there, on the floor of your ship. Dying alone in time and space. Time has been stopped for weeks now, its weird since only the other living beings have been affected. You are running out of food and time, even though you cant die you can still move and think. Existence is a terrible experience but infinite lives is even worse.", [
        Option("Turn on tv.", "9,1", generateTvShow),
    ])
    game.AddNode("9,1", "You turn on the tv and sit down. The old news from 3 weeks ago is up. Its talking about some serial killer on the loose and the horrible acts they committed", [
        Option("Give it one last try.", "9,1,1"),
        Option("Give up.", "9,1,2"),
    ])
    game.AddNode("9,1,1", "Do you really think that would work? You tried it over 500 times already why would it be different now? Are you going insane?", [
        Option("Try it anyway.", "9,2"),
        Option("Give up.", "9,1,2"),
    ])
    game.AddNode("9,1,2", "You pick up your space laser and attempt to shoot yourself. Only to realize time has stopped and bullets wont move. What now? What will the player of my game do now?", [
        Option("Try to save yourself from this doom. Giving it one last try.", "9,2"),
        Option("Give up.", "9,1,2"),
    ])
    game.AddNode("9,2", "You turn your ship around so that you are slowly getting pulled back into the wormhole, a painful experience but is it worth it? You wont know yet but if you return here again you certainly didn't learn your lesson.", [
        Option("...", "0"),
    ])


# gameloop
    game.SetCurrentNode("0")
    while True:
        print("\n\n\n----------------------------------------------------------------------------\n", game.currentNode["text"], "\n----------------------------------------------------------------------------")
        for idx, option in enumerate(game.currentNode["options"]):
            print(f"{idx+1}: {option.text}")
        ip = input("\nEnter option (x to exit): ")
        if ip.lower() == "x":
            break
        try:
            option = int(ip)
        except:
            continue
        
        if game.GetChoice(option) is not None and game.GetChoice(option).nextNode is None:
            break
        game.Step(option)
        if len(game.currentNode["options"]) == 0:
            break