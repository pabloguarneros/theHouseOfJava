class FirstPerson:

    def __init__(self,character):
        self.pov = character

    def write(self, story):
        ''' Changes how story is written given self.pov
        '''
        return story