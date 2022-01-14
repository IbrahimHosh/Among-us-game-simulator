# Among-us-game-simulator
Creates a simulated version of the popular murder mystery game Among-Us. Used objects and classes in python. 
Created 2 subclasses crewperson and pretender from character class, and I also created a game class to help simulate a game, check winner, and do meetings.
To properly run the program you need to do 3 things. Create a list of characters of your choice, create a Game object, and run the play_game() method for the Game object
Just like I did at the end of my code.
For example:
p_list = [Pretender("Jerry", "Blue", "mohawk", 6),
              Crewperson("Jackson", "Orange", "bird nest", 6),
              Crewperson("Yuchen", "Purple", "witch hat", 6),
              Crewperson("Zaela", "White", "party hat", 6),
              Crewperson("Audrey", "Lime", "wet floor sign", 5),
              Crewperson("Rachel", "Pink", "sticky note", 5),
              Crewperson("Nikhil", "Cyan", "pirate hat", 5),
              Pretender("Julia", "Yellow", "green fedora", 5),
              Crewperson("Greta", "Brown", "lab goggles", 5),
              Crewperson("Nate", "Red", "banana peel", 5)]
g = Game(p_list)
g.play_game()
