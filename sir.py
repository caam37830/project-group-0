# Python package includes class and function definitions


class individual(self):
    """
    class to create individuals
    the internal state of an individual can be
    susceptible, infected, or removed
    """
    
    def __init__(self, state):
        self.state = state
        
    def curstate(self):
        """
        method to determin the state of the individual
        """
        return self.state
    
    def changestate(self, newstate):
        """
        method to change state of the individual
        """
        self.state = newstate
        
