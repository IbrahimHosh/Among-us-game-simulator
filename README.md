# Among-us-game-simulator
Created a text-based social deduction game in which players board a spaceship bound for Jupiter to do scientific research. Each player takes on the role of a Character with one of two specializations: Crewperson or Pretender. The Crewpersons' goal is to keep the ship running well by doing things like mending wiring, clearing waste chutes, and identifying and removing Pretenders from the ship. The Pretenders' purpose is to eliminate Crewpersons in a stealthy manner, preventing the crew from completing their task.
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
