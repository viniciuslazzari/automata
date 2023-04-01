class State:
    def __init__(self, name, transitions, is_inital, is_final):
        self.name = name
        self.transistions = transitions
        self.is_initial = is_inital
        self.is_final = is_final