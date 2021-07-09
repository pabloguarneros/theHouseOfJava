'''


see how the scenes change ( )

new.THREE . plot (
    "what is your controller?!!
)

narrator is the camera
plot is the controller


narrator.write(Story)

printStory()


Character
    Mix of different people
    Dialogue
    Age
    Sexuality
    Predispositions
    Obtain through series of questions, so not initalize it 
    Quirks
    Relationships
    Drives
    Disorder
    Or is it better to put a model of your character
    // but how do we get the data 

Motivations
    Theories of Motivation

Tribes
    Function (family, friends, activism)
    Network Strength


'''

class Motivation:
    def __init__(self, consciousness, interality):
        self.internality = 3 #int : 7 stages of external vs. internal motivation
        self.consciousness = 0.5 #float 0-1 : how conscious character is of motivation

class Dialogue:
    def __init__(self):
        self.topics = { "taboo",[] }

    def trainModel(self,speeches):
        ''' Trains the dialogue of a character by a real person's transcribed or recorded speeches
        '''

class Character:

    def __init__(self, name, age, sexuality = 1):
        self.name = name #str 
        self._age = age #int
        self.sexuality = sexuality # float 0 - 1 

    def set_age(self, new_age):
        self._age = new_age
    
    def get_age(self):
        return self._age