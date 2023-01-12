#import libraries

import random
#provides random number generator

import time
#provides timer function

import sys
#provides exit function and kill program

#Variables

characterName = str(input("Characters name: "))
#the name of the character
characterNameUpper = characterName.upper()
#the characters name i all caps

characterAge = int(input("Characters age (no older than 15): "))
#the age of the character

randomItem = str(input("Random item: "))
#a random item to be used later in the story

#check age, if less than 0 then exit program
if characterAge <= 0:
  print ("Invalid age.")
  time.sleep(1)
  print ("try again")
  time.sleep(1)
  print ("Goodbye!")
  time.sleep(1)
  sys.exit()

#Generate random story value between 1 - 2 since the 3rd isn't done
#each value corresponds to different story

storyNumber = random.randint(1,2)
#print ("the random number is "+ str(storyNumber))
#debug 
#Generate story based on age and random number
#picks the possible story based on age and story value

if characterAge <= 15:
  if storyNumber == 1: # bank hiest 

    print ("person 1 whispers: you sure about this? he looks a bit young for this.")
    time.sleep(3)
    print ("person 2 whispers: don't worry about him, i've heard good things. hes got a fair bit of experience")
    time.sleep(3)
    print ("person 1: hey uhh... " + characterName + " right? my name is Alex, we'll be working together. So... i-")
    time.sleep(3)
    print ("person 2: Alex!")
    time.sleep(3)
    print ("person 2: we don't have the time. " + characterName + " Im the one that's organising this. I'd tell you my name but im not trying to get burned... you know? in case your a cop..." )
    time.sleep(3)
    print ("person 2: ...your not a cop right? yeah, you don't look like a cop")
    time.sleep(3)
    print ("Alex: Anyways we got a special job, good pay and comes with benifits... ")
    time.sleep(3)
    print ("Alex: but theres major health risks... major...")
    time.sleep(3)
    print ("person 2 and Alex: You in?")
    continueStory = str(input("YES (Y) or NO (N)"))    

    #if N is picked stop story

    if continueStory == "N" or "n":
      time.sleep(1)
      print ("Alex: Well...")
      time.sleep(3)
      print ("Person 2 Whispers: Hes gotta go i guess...")
      time.sleep(3)
      print ("Alex whispers: Yeah that sucks, what a shame...")
      time.sleep(3)
      print ("Person 2: Well...")
      time.sleep(1)
      print ("BANG!")
      sys.exit()
  
    #congratulations on not dying
    print ("Person 2: Good choice")
    time.sleep(3)
    print ("Person 2: So... ")
    time.sleep(3)
    print ("Person 2: Hmmm...")
    time.sleep(3)
    print ("Alex: The job?")
    time.sleep(3)
    print ("Person 2: The job... well, we're robbing a bank")
    time.sleep(3)
    print ("Person 2: We have 3 main roles that need to be filled: Get away driver, Gunman and the guy that'll hold the duffle bag with cash.")
    time.sleep(3)
    print ("Person 2: each have their ups and downs, but it's equal work i'd say")
    time.sleep(3)
    print ("Alex: Definitely")
    #ask role
    role = str(input("Driver (D), Gunmam (G) or Cash (C)"))

  #story branch based on role
  #driver role
    if role == "D" or "d":
      print ("Alex: Driver huh? ... are you even old enough to dr- ... you know what? never mind")
      time.sleep(3)
      print ("Alex: Alright " + characterName + " let's see what you got first.")
      time.sleep(2)
      print ("")
      print (characterName + " does test drive*")
      print ("")
      time.sleep(3)
      print ("Alex: Not bad... not bad especially for a " + str(characterAge) + " year old")
      time.sleep(3)
      print ("Alex: so the plan is you drive us there, leave then come pick us up at the EAST exit... EAST.")
      time.sleep(3)
      print ("Alex: then we drive off... simple.")
      time.sleep(3)
      print ("Alex: anyways... that's it... i'll see you on the big day")
      time.sleep(3)
      print ("")
      print ("Hiest Day")
      print ("")
      print ("person 2: you tought him everything? good...")
      time.sleep(3)
      print ("Alex: Here...")
      time.sleep(2)
      print ("Alex: We...")
      time.sleep(2)
      print ("Alex: Go")
      time.sleep(3)
      print ("Person 2 yelling: MEET BACK IN 30!")
      time.sleep(3)
      print ("Distant gun shots as " + characterName + " drives off.")
      time.sleep(3)
      print ("")
      print ("30 min later...")
      print ("")
      time.sleep(3)
      print ("Alex: Oh am i glad to see you " + characterName)
      time.sleep(3)
      print ("driving off")
      time.sleep(3)
      print ("Alex: Not much of a talker are you " + characterName + " ?")
      time.sleep(3)
      print (characterName + ": ...")
      time.sleep(3)
      print ("Alex: Yeah alright...")
      time.sleep(2)
      print ("Distant siren")
      time.sleep(3)
      print ("Person 2: Hold on... you hear that?")
      time.sleep(3)
      print ("Alex and Person 2: COPS!")
      time.sleep(3)
      print ("person 2: Alright it's your time to shine")
      time.sleep(3)
      
      #dircetion
      directionOne = str(input("Turn lefft (L) or Right (R)"))
      time.sleep(3)
      print ("Alex: Good thinking " + characterName + " but they're still on us.")

      directionTwo = str(input("Turn lefft (L) or Right (R)"))
      time.sleep(3)
      print ("Person 2: we're loosing them! ")
      time.sleep(3)
      print ("Alex: A couple more turns and we'll loose em for sure")

      #use random item

      directionThree = str(input("Turn left (L) or Right (R)"))
      time.sleep(3)
      print ("Person 2: They're catching up!")
      time.sleep(3)
      print ("Person 2: Alex do you have anything that could help us?") 
      time.sleep(3)
      print ("Alex: No, not really... what about you " + characterName + " ?")
      time.sleep(3)
      print (characterName + ": what about this " + randomItem + "?")
      time.sleep(3)
      print ("Alex: Really a " + randomItem + " ?")
      time.sleep(3)
      print ("Person 2: Just throw it or somthing!")
      time.sleep(3)
      print ("Alex: Another turn coming up!")


      directionFour = str(input("Turn lefft (L) or Right (R)"))
      time.sleep(3)
      print ("Person 2: They're barely in veiw!")
      time.sleep(3)
      print ("Either your a great driver or that " + randomItem + " was bad luck... Slowing us down.")

      directionFive = str(input("Turn lefft (L) or Right (R)"))
      time.sleep(3)
      print ("Alex: Great they're gone!") 

    #ending

      time.sleep(3)
      print ("Person 2: we'll it was nice working with you, we'll wire you the money once we get it luandered ")
      time.sleep(3)
      print ("Person 2: Names Cole, i'll keep in touch... if we find another job.")
      time.sleep(3)
      print ("Alex: I'll see you around " + characterName + " one day you gotta show me how to drive like you did back there.")
      time.sleep(3)
      print ("")
      print ("Alex and Cole walking away")
      print("")
      time.sleep(3)
      print ("Alex: I liked that one...")
      time.sleep(3)
      print ("Cole: I did too...")

      #End

      time.sleep(3)
      print (("""" _____  _             _____             _ 
                  |_   _|| |           |  ___|           | |
                    | |  | |__    ___  | |__   _ __    __| |
                    | |  | '_ \  / _ \ |  __| | '_ \  / _` |
                    | |  | | | ||  __/ | |___ | | | || (_| |
                    \_/  |_| |_| \___| \____/ |_| |_| \__,_|
                                          """))
      time.sleep(3)
      sys.exit()
      #call end, end program

   #Gunmam role
    elif role == "G" or "g":
     print ("Person 2: Gunner? ... cool")
     time.sleep (3)
     print ("Person 2: So...")
     time.sleep (3)
     print ("Person 2: We managed to source 3 weapons for you... ahead of time of coruse")
     time.sleep (3)
     print ("Sooo... we have a grenade launcher, M4 combat rifle and supperesd pistols as a back up. Five Seven's if you want to know")
     time.sleep (3)
     weaponChoice = str(input("Grenade Launcher (G) or AK 47 (A)"))
     time.sleep (3)

     #weapon choice
     if weaponChoice == "G" or "g":
       time.sleep (3)
       print ("Person 2: Well...")
       time.sleep (3)
       print ("Person 2: I take you as a guy who likes explosions...")
       time.sleep (3) 
       print ("Person 2: But i hate to break it to you... we're using gas grenades instead, I know... big bummer")
       time.sleep (3)
       print ("Person 2: Gas grenades offer a more abrupt approach, but will gaurntee little to no resitance")
       time.sleep (3)
       print ("Person 2: You'll want to shoot the canasters through the window. I'll get us gas masks so we can walk right in.")
       time.sleep (3)
       print ("Person 2: Anyways " + characterName + " Alex will be dropping us off, at the entrance of course." )
       time.sleep (3)
       print ("Person 2: He's gonna leave then pick us up at the EAST exit, got it?")
       time.sleep (3)
       print (characterName + ": ...")
       time.sleep (3)
       print ("Person 2: Good...")
       time.sleep (3)
       print ("Person 2: Meet back here tommorow, we got our work cut out so be on time... seriously though... don't be late.")
       time.sleep(3)
       print ("")
       print ("Hiest Day")
       print ("")
       print ("Alex drops off Person 2 and " + characterName)
       print ("")
       time.sleep(3)
       print ("Person 2 yelling: MEET BACK IN 30!")
       time.sleep(3)
       print ("Person 2: Alright let's get to work")
       time.sleep(3)
       print ("Person 2: Gas the place up")
       time.sleep 
       print ("")
       print ("Person 2 and " + characterName + " enter bank ")
       print ("")
       time.sleep(3)
       print ("Person 2: Jam the door with something, we don't wanna get locked in...")
       time.sleep(3)
       print ("person 2: comon... anything ")
       time.sleep(3)
       print (characterName + " what about this " + randomItem + " ?")
       time.sleep(3)
       print ("person 2: a " + randomItem + "?" + " fine that works")
       time.sleep(3)
       print ("Person 2: Alright...")
       time.sleep(3)
       print ("Person 2: Watch your step, you don't wanna wake em up")
       time.sleep(3)
       print ("Person 2: You wait here... im going to work on the saftey deposite boxes")
       time.sleep(3)
       print ("Person 2: If someone wakes up, i don't know... give them a smack or somthing")
       time.sleep(3)
       print ("")
       print ("15 min latter")
       print ("")
       time.sleep(3)
       print ("Person 2: Alright we're done let's go!")
       time.sleep(3)
       print (characterName + " Lets go?")
       time.sleep(3)
       print ("Gaurd: " + characterName + " I know your name! I've seen your face!, You can't hide!" )
       time.sleep(3)
       print ("Person 2: Well this complicates things...")
       time.sleep(3)
       print ("Person 2: Sooo... do we put him down or take our chances " + characterName) 
       
        #LET reader pick

       chance = str(input("Deal with witness (D) or Take off (T)"))
        #kill person
       if chance == "D" "d":
         print ("BANG!")
         time.sleep (3)
         print ("Person 2: Ruthless, but necessary. Good call " + characterName)
         time.sleep(3)
         print ("Person 2: Comon... we're done here, don't forget your " + randomItem + " though.")
         time.sleep(3)
         print ("")
         print ("Person 2 and " + characterName + " leave bank")
         print ("")
         time.sleep(3)
         print ("")
         print ("Person 2 and " + characterName + " enter car")
         print ("")
         time.sleep(3)
         print ("Alex: All good?")
         time.sleep(3)
         print (characterName + " and Person 2: ...")
         time.sleep(3)
         print ("Alex: Good.")
         time.sleep(3)
         print ("Person 2: You did good in there " + characterName + " don't get to caught up. You didn't have a choice")
         time.sleep(3)
         print ("")
         print ("The Crew Drive off")
         print ("")
         time.sleep(3)
         print ("Person 2: we'll it was nice working with you, we'll wire you the money once we get it luandered ")
         time.sleep(3)
         print ("Person 2: Names Cole, i'll keep in touch... but you'll need to lay low for a bit, we all do.")
         time.sleep(3)
         print ("Alex: I'll see you around " + characterName + " I'll be honest, at first i was worried... but you pulled your weight.")
         time.sleep(3)
         print ("")
         print ("Alex and Cole walking away")
         print("")
         time.sleep(3)
         print ("Alex: Are you going to tell him about the big job?")
         time.sleep(3)
         print ("Cole: Maybe...")

         #End

         time.sleep(3)
         print (("""" _____  _             _____             _ 
                  |_   _|| |           |  ___|           | |
                    | |  | |__    ___  | |__   _ __    __| |
                    | |  | '_ \  / _ \ |  __| | '_ \  / _` |
                    | |  | | | ||  __/ | |___ | | | || (_| |
                    \_/  |_| |_| \___| \____/ |_| |_| \__,_|
                                          """))
         time.sleep(3)
         sys.exit()
         #call end, end program

        #let person live
       elif chance == "T" or "t": 
        time.sleep(3)
        print ("Person 2: All right then lets go!")
        time.sleep(3)
        print ("Person 2: Alex should be waiting for us")
        time.sleep(3)
        print ("Person 2: leave the " + randomItem + characterName + " we don't have time")
        time.sleep(3)
        print ("")
        print ("Person 2 and " + characterName + " enter car")
        print("")
        time.sleep(3)
        print ("Person 2: Your a good person for what you did back there...")
        time.sleep(3)
        print ("Person 2: But sadly i can almost gaurntee you'll get caught, hopfully your cut will be enough to pay off bail... if not then maybe Alex and i can help you out.")
        time.sleep(3)
        print ("")
        print ("The Crew Drive off")
        print ("")
        time.sleep(3)
        print ("Person 2: we'll it was nice working with you, we'll wire you the money once we get it luandered ")
        time.sleep(3)
        print ("Person 2: I'd tell you my name but, its best if you didn't know.")
        time.sleep(3)
        print ("Alex: I'll see you around " + characterName + " Good work back there.")
        time.sleep(3)
        print ("")
        print ("Alex and Cole walking away")
        print("")
        time.sleep(3)
        print ("Alex: I liked that one...")
        time.sleep(3)
        print ("Person 2: I did too...")
        #End

        time.sleep(3)
        print (("""" _____  _             _____             _ 
                 |_   _|| |           |  ___|           | |
                   | |  | |__    ___  | |__   _ __    __| |
                   | |  | '_ \  / _ \ |  __| | '_ \  / _` |
                   | |  | | | ||  __/ | |___ | | | || (_| |
                   \_/  |_| |_| \___| \____/ |_| |_| \__,_|
                                          """))
        time.sleep(3)
        sys.exit()
         #call end, end program
        #weapon choice filters
     if weaponChoice == "A" or "a":
       time.sleep (3)
       print ("Person 2: Good o'l AK, great choice")
       time.sleep (3)
       print ("Person 2: The plan is simple, we walk in walk out...")
       time.sleep(3)
       print ("Person 2: I got theses AK's from a bud of mine... Will.")
       time.sleep(3)
       print ("Person 2: Anyways AK's are notoriously unreliable... good chance you might get a jam, there still pretty scary though...")
       time.sleep(3)
       print ("Person 2: Ideally we don't shoot anyone... we just flash the guns a bit")
       time.sleep(3)
       print ("Person 2: Thats it... Alex picks us up at the east exit we enter through the doors... uhhhhh... yeah.")
       time.sleep(3)
       print ("Person 2: see you tommorow")
       time.sleep(3)
       print ("")
       print ("Hiest Day")
       print ("")
       time.sleep (3)
       print ("Alex : I'll be back in 30")
       time.sleep (3)
       print ("Person 2: Alright... let's get to work")
       time.sleep (3)
       print ("")
       print ("Person 2 and " + characterName + " enter bank ")
       print ("")
       time.sleep(3)
       print ("Person 2: Jam the door with something, we don't wanna get locked in...")
       time.sleep(3)
       print ("person 2: comon... anything ")
       time.sleep(3)
       print (characterName + " what about this " + randomItem + " ?")
       time.sleep(3)
       print ("person 2: a " + randomItem + "?" + " fine that works")
       time.sleep(3)
       print ("Person 2: Alright...")
       time.sleep (3)
       print ("")
       print ("Gun Shots*")
       print ("All screaming")
       time.sleep(3)
       print ("Person 2 yelling: GET ON THE FLOOR!")
       time.sleep(3)
       print ("Person 2: " + characterName + " keep em under control... i'll be back")
       time.sleep(3)
       print (characterName + ": ...")
       time.sleep(3)
       print ("")
       print ("15 min later")
       print ("")
       time.sleep (3)
       print ("Person 2 yelling: " + characterNameUpper + " GET OVER HERE!")
       time.sleep (3)
       print ("Person 2: the lock won't budge")
       time.sleep(3)
       print ("Person 2: shoot it")
       time.sleep(3)
       print (characterName + ": k... ")
       time.sleep(3)

       #gun jam 
       gunJam = random.radint(1,3)

       #if gun jam
       if gunJam == 1:
         print("Cick*")
         time.sleep (3)
         print (characterName + ": Uhh...")
         time.sleep(3)
         print ("Person 2: Pull the charging handle back")
         time.sleep(3)
            
       print ("BANG!")
       time.sleep(3)
       print ("Person 2: Nice shot")
       time.sleep(3)
       print ("Person 2: Help me grab this cash and let's go")
       time.sleep(3)
       print ("Person 2: " + characterName + " we have time for another")
       time.sleep(3)
       print ("Person 2: Shoot this one too ")
       
       #if gun jam 2
       gunJam2 = random.radint(1,3)

       #if gun Jam
       if gunJam2 == 2:
         print ("Click*")
         time.sleep(3)
         print ("Person 2: Another jam? jeez")
         time.sleep(3)
         print ("Person 2: Just pull it ba-")
         time.sleep(3)
         print (characterName + ": I know...")
         time.sleep(3)
        
        #continue story
       print ("BANG!")
       time.sleep(3)
       print ("Person 2: Great... if we're quick we can grab another")
       time.sleep(3)
       print("Person 2: Alrighty... one more?")
       time.sleep (3)
       print (characterName + ": Sure")
       time.sleep(3)
       
       #if gun jam 3
       gunJam3 = random.radint(1,3)

       #if gun jam
       if gunJam3 == 1:
         print ("Click*")
         time.sleep(3)
         print ("Person 2: Another jam? what are the odds?")
         time.sleep (3)

        #continue story
       print ("BANG!")
       time.sleep(3)
       print ("Person 2: Lets grab and go")
       time.sleep(3)
       print ("Person 2: Theses bags are getting heavy... thats a good sign")
       time.sleep(3)
       print (characterName + ": Let's go")
       time.sleep(3)
       print ("")
       print("Person 2 and " + characterName + " leave bank")
       print ("")
       time.sleep(3)
       print ("Alex: Thoses bags look heavy")
       time.sleep(3)
       print ("Alex: Let's get outa here")
       time.sleep(3)
       print ("Person 2: You did great back there, even better for a " + characterAge + " year old")
       time.sleep(3)
       print ("Person 2: Big payout on this one")
       time.sleep(3)
       print ("Alex: How'd that AK treat you?")
       time.sleep(3)
       print (characterName + ": It was fine for an AK")
       time.sleep(3)
       print ("Person 2: we'll it was nice working with you, we'll wire you the money once we get it luandered ")
       time.sleep(3)
       print ("Person 2: Names Cole, i'll keep in touch... but you'll need to lay low for a bit, we all do.")
       time.sleep(3)
       print ("Alex: I'll see you around " + characterName + " I'll be honest, at first i was worried... but you pulled your weight.")
       time.sleep(3)
       print ("")
       print ("Alex and Cole walking away")
       print("")
       time.sleep(3)
       print ("Alex: He did well...")
       time.sleep(3)
       print ("Cole: Yes he did...")

        #End

       time.sleep(3)
       print (("""" _____  _             _____             _ 
                  |_   _|| |           |  ___|           | |
                    | |  | |__    ___  | |__   _ __    __| |
                    | |  | '_ \  / _ \ |  __| | '_ \  / _` |
                    | |  | | | ||  __/ | |___ | | | || (_| |
                    \_/  |_| |_| \___| \____/ |_| |_| \__,_|
                                          """))
       time.sleep(3)
       sys.exit()
       #call end, end prograM
 
    #"duffle bag guy" role
    elif role =="C" or "c":
     print ("Person 2: Carrying the goods? nice and simple")
     time.sleep(3)
     print ("Alex: Yup")
     time.sleep(3)
     print ("Alex: Nice and simple")
     time.sleep(3)
     print ("Person 2: Since you'll be carrying what we steal you also get to pick what we steal, cash or gold")
     time.sleep(3)
     print("Person 2: The procedure dosen't change but it's worth noting that you can while you can carry more cash its also worth less")
     time.sleep(3)
     print ("Alex: both will need to be laundered at the end and if all goes well the profit will be the same")

      #give user option of what to steal
     stealOption = str(input("Cash (C) or Gold (G)"))

     #steal option cash
     if stealOption == "c" or "C":
      print ("Alex: Cash is a great option... probely the better one too")
     #steal option gold
     elif stealOption == "g" or "G":
       print ("person 2: Gold... Great choice")

     time.sleep(3)
     print ("Person 2: Alright") 
     time.sleep(3)
     print ("Alex: I'll be droping you off and then picking you up at the east exit")
     time.sleep(3)
     print ("Person 2: Right, " + characterName + " you and i will walk in... you'll hit the the stash while i keep everyone occupied.")
     time.sleep(3)

     #password variable
     password = "Qn!jf*h" 
      #print password
     print ("Alex: We had someone on the inside tell us the password... it's " + password )
     time.sleep(3)
     print ("Person 2: Remember the target, remeber the code and you'll be fine")
     time.sleep(3)
     print ("Person 2: See you guys tommorow... don't be late... seriously")
     time.sleep(3)
     print ("")
     print ("Heist day")
     print ("")
     time.sleep(3)
     print ("Person 2 yelling: MEET BACK IN 30!")
     time.sleep(3)
     print ("Person 2: Alright let's give them a show")
     time.sleep 
     print ("")
     print ("Person 2 and " + characterName + " enter bank ")
     print ("")
     time.sleep(3)
     print ("Person 2: Jam the door with something, we don't wanna get locked in...")
     time.sleep(3)
     print ("person 2: comon... anything ")
     time.sleep(3)
     print (characterName + " what about this " + randomItem + " ?")
     time.sleep(3)
     print ("person 2: a " + randomItem + "?" + " fine that works")
     time.sleep(3)
     print ("Person 2: Alright... all good so far")
     time.sleep(3)
     print ("Person 2: You head to the back, i'll keep theses people busy")
     time.sleep(3)
     print (characterName + "yelling: WHATS THE PASSWORD!?")
     time.sleep(3)
     print ("Person 2: " +  password[0] + " " + password[1] + " " + password[2] + " " + password[3] + " " + password[4] + " " + password[5] + " " + password[6] + " !")
     time.sleep(3)
     print (characterName + ": k")
     print ("Person 2: Theses bags are looking heavy... thats a good sign")
     time.sleep(3)
     print (characterName + ": Let's go... thats all")
     time.sleep(3)
     print ("")
     print("Person 2 and " + characterName + " leave bank")
     print ("")
     time.sleep(3)
     print ("Alex: Wow you grabed alot")
     time.sleep(3)
     print ("Alex: Let's get outa here")
     time.sleep(3)
     print ("Person 2: You did great back there, even better for a " + characterAge + " year old")
     time.sleep(3)
     print ("Person 2: Big payout on this one")
     time.sleep(3)
     print ("Alex: you didn't forget the password did you?")
     time.sleep(3)
     print (characterName + ": No...")
     time.sleep(3)
     print ("Person 2: ... ")
     time.sleep(3)
     print ("Person 2: Names Cole, i'll keep in touch... you'll get paid when we cash out.")
     time.sleep(3)
     print ("Alex:" + characterName + " we got a biger job, its gonna need more people" )
     time.sleep(3)
     print ("Alex: we'll let you know...")
     time.sleep(3)
     print ("")
     print ("Alex and Cole walking away")
     print("")
     time.sleep(3)
     print ("Alex: He did great... grabbed alot more than i thought")
     time.sleep(3)
     print ("Cole: yeah...")

        #End

     time.sleep(3)
     print (("""" _____  _             _____             _ 
                  |_   _|| |           |  ___|           | |
                    | |  | |__    ___  | |__   _ __    __| |
                    | |  | '_ \  / _ \ |  __| | '_ \  / _` |
                    | |  | | | ||  __/ | |___ | | | || (_| |
                    \_/  |_| |_| \___| \____/ |_| |_| \__,_|
                                          """))
     time.sleep(3)
     print ("Heist 2?")
     sys.exit()
      #call end, end prograM

  elif storyNumber == 2:
    print ("Welcome to the casino " + characterName + " your a bit young but thats fine")

    #prize
    prize1 = int(input("pick a number from 1 - 100: "))

    #prize input
    prizeInput = random.randint(1,100)

    if prize1 == prizeInput:
      print ("Yay! you won")
    else:
      print ("Sorry, you didn't win this time... maybe you should try again?")
    
    time.sleep(3)
    print ("Don't leave yet " + characterName + ", even though you don't have money we'll be willing to take your " + randomItem + " as a bet")
    print (" The computer will generate a random number, if pick you the number you pick that is smaller than the computer generated number you win. but if you pick the same you still lose")

    #random number 50/50
    prize2 = random.randint(1,2)

    #userinput
    prizeInput2 = int(input("Pick 1 or 2: "))

    print (str(prize2) + " is the random number")
    print ("you picked " + str(prizeInput2))
    if prize2 > prizeInput2:
      print ("nice you won!")
    elif prize2 == prizeInput2:
      print ("Sorry you didn't win this time")
    elif prize2 < prizeInput2:
      print ("Nope, you didn'et win this one")

  #else:
    print ("Story 3 unfinished")

#congratulations on not dying
#story 1 = heist 
#story 2 = lost in woods/ survival story
#story 3 = stuck in alien ant farm for humans (solar oppisites the wall)
#casino random stuff

#different outcomes based on age
#characters retain personality throughout different branches
