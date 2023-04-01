import sys
from src.automata import Automata

automata_returns = {
    0: "Accepted input!",
    1: "Input didn't end in final state!",
    2: "Undefined transition!",
    3: "Input is not on the alphabet!"
}

def main():
    automata = Automata()

    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']
    transistions = [
        {'tiradoGancho': 'q1', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'apaga': None, 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2', 'apaga': None, 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q3', '1': 'q3', '2': 'q3', '3': 'q3', '4': 'q3', '5': 'q3', '6': 'q3', '7': 'q3', '8': 'q3', '9': 'q3', 'apaga': 'q1', 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q4', '1': 'q4', '2': 'q4', '3': 'q4', '4': 'q4', '5': 'q4', '6': 'q4', '7': 'q4', '8': 'q4', '9': 'q4', 'apaga': 'q2', 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q5', '1': 'q5', '2': 'q5', '3': 'q5', '4': 'q5', '5': 'q5', '6': 'q5', '7': 'q5', '8': 'q5', '9': 'q5', 'apaga': 'q3', 'liga': 'q11', 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q6', '1': 'q6', '2': 'q6', '3': 'q6', '4': 'q6', '5': 'q6', '6': 'q6', '7': 'q6', '8': 'q6', '9': 'q6', 'apaga': 'q4', 'liga': 'q11', 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q7', '1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9': 'q7', 'apaga': 'q5', 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8', 'apaga': 'q6', 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9', 'apaga': 'q7', 'liga': None, 'colocanoGancho': None},
        {'tiradoGancho': None, '0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10', 'apaga': 'q8', 'liga': 'q11', 'colocanoGancho': None},
        {'tiradoGancho': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'apaga': 'q9', 'liga': 'q11', 'colocanoGancho': None},
        {'tiradoGancho': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'apaga': None, 'liga': None, 'colocanoGancho': 'q12'},
        {'tiradoGancho': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'apaga': None, 'liga': None, 'colocanoGancho': None},
    ]
    initial = 'q0'
    finals = ['q12']

    automata.create(states, transistions, initial, finals)

    mode = input("Read input from terminal (1) or file (2): ")
    flag = 1
    text = '0'

    if mode == "1":
        while text != "" and flag not in [2, 3]:
            text = input()

            if text == "": continue

            flag = automata.run_step(text)

        print(automata_returns[flag])
    elif mode == "2":
        lines = []

        with open('test.txt') as f:
            lines = f.read().splitlines() 

        for line in lines:
            if line == "" or flag in [2, 3]: break

            flag = automata.run_step(line)

        print(automata_returns[flag])
    else:
        print("Invalid mode!")

if __name__ == "__main__":
    main()