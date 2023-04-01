from src.state import State

class Automata:
    def __init__(self):
        self.all_states = []
        self.cur_state = None

    def create(self, states, transistions, initial, finals):
        num = len(states)

        name = ''
        cur_transistions = {}
        is_inital = False
        is_final = False

        for i in range(0, num):
            name = states[i]
            cur_transistions = transistions[i]
            is_inital = name == initial
            is_final = name in finals

            state = State(name, cur_transistions, is_inital, is_final)

            self.all_states.append(state)

        self.cur_state = self.return_initial_state()

        # self.mount()

    def mount(self):
        for state in self.all_states:
            print(state.name)
            print(state.transistions)
            print(state.is_initial)
            print(state.is_final)
            print("\n")

    def return_initial_state(self):
        for state in self.all_states:
            if state.is_initial:
                return state

    def return_state_by_name(self, name):
        for state in self.all_states:
            if state.name == name:
                return state

    def run_step(self, text):
        if text not in self.cur_state.transistions:
            return 3

        next_state_name = self.cur_state.transistions[text]
        self.cur_state = self.return_state_by_name(next_state_name)

        if self.cur_state == None:
            return 2

        if not self.cur_state.is_final:
            return 1

        return 0
