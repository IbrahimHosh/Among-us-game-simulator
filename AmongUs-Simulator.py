import random
class Character:
    '''
    Creates an object that represents a character.
    The instance variables for this class are self.name is name ,self.color is color ,self.hat is hat ,self.status is the characters status,self.task_list is the list of tasks remaining.
    and what does each represent in a few words?)
    __ init__ creates the instance variables, repr gives chracter information, get identity gets charchters identity.
    '''
    def __init__(self,name,color,hat,num_tasks):
        self.name = name
        self.color = color
        self.hat = hat
        self.status = True
        given_tasks = ['Adjust engine output', 'Calibrate distributor',
'Map course', 'Clear out O2 filter', 'Destroy asteroids',
'Redirect power', 'Empty garbage', 'Secure wiring',
'Fill engines tanks', 'Inspect laboratory', 'Move shields', 'Steady steering', 'Initiate reactor', 'Submit personal info',
'Sign in with ID', 'Enable manifolds', 'Sync data']
        self.task_list = []
        i = 0
        while i < num_tasks:
            y = random.choice(given_tasks)
            if y not in self.task_list:
                self.task_list += [y]
                i+=1
    def __repr__(self):
        if self.status == True:
            return self.name+': '+self.color+', wearing a '+self.hat+' - Health status: '+ 'Alive'
        else:
            return self.name+': '+self.color+', wearing a '+self.hat+' - Health status: '+ 'Ghost'
    def get_identity(self):
        return 'Character'
class Crewperson(Character):
    '''
    Represents a crewperson object
    inherits all instance variables from character.( I wasn't trying to list all the instance variables again)
    and what does each represent in a few words?)
    __init__ creates the instance variables,get identity gets charchters identity, and tasks list removes 1 task and prints that task.
    '''
    def __init__(self,name,color,hat,num_tasks):
        super().__init__(name,color,hat,num_tasks)
    def get_identity(self):
        return 'Crewperson'
    def complete_task(self):
        if len(self.task_list) > 0:
            print(self.name + ' completed the '+ self.task_list[0]+' task.')
            self.task_list = self.task_list[1:]
        else:
            print(self.name + ' has completed all their tasks.')
class Pretender(Character):
    '''
    Represents a pretender object
    inherits all instance variables from character.
    __init__ creates the instance variables,get identity gets charchters identity, and eliminate changes a targets status
    '''
    def __init__(self,name,color,hat,num_tasks):
        super().__init__(name,color,hat,num_tasks)
    def get_identity(self):
        return 'Pretender'
    def eliminate(self,target):
        target.status = False
        print(self.name+" eliminated "+ target.name+'.')
class Game:
    '''
    creates an object that helps simulates a game
    The instance variable is a player list
    __init__ creates instance variables, check_winner checks the winner, meeting method simulates a meeting, and playgame method plays a game.
    '''
    def __init__(self,player_list):
        self.player_list = player_list
    def check_winner(self):
        p = 0
        c = 0
        incomplete = 0
        for ele in self.player_list:
            if ele.get_identity() == "Crewperson" and ele.status == True:
                c +=1
                if len(ele.task_list) != 0:
                    incomplete +=1
            elif ele.get_identity() == "Crewperson" and ele.status == False:
                if len(ele.task_list) != 0:
                    incomplete +=1
            elif ele.get_identity() == 'Pretender':
                if ele.status == True:
                    p+=1
        if incomplete == 0 and p >= c:
            print('Crewpersons win!')
            return 'C'
        elif p >= c:
            print('Pretenders win!')
            return 'P'
        elif p == 0 or incomplete == 0:
            print('Crewpersons win!')
            return 'C'
        else:
            return '-'
    def meeting(self):
        y = random.choice(self.player_list)
        i = False
        while i == False:
            if y.status == False:
                y = random.choice(self.player_list)
            else:
                i = True
        for ele in self.player_list:
            if ele.status == True:
                print(ele.name+ " voted for " + y.name +'.')
        print(y.name +' was eliminated.')
        y.status = False
        return y.name
    def play_game(self):
        G = '-'
        while G == '-':
            for ele in self.player_list:
                if ele.get_identity() == "Crewperson":
                    x = random.randint(1,3)
                    for i in range(x):
                        ele.complete_task()
                elif ele.get_identity() == 'Pretender':
                    x = random.choice(self.player_list)
                    if ele.status == True and x.status == True and x.get_identity() == 'Crewperson':
                        ele.eliminate(x)
            G = self.check_winner()
            if G != '-':
                return G
            self.meeting()
            G = self.check_winner()
            if G != '-':
                return G
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
