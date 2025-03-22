from data.zoe import *
import Dfa 
import Nfa
import test
from test import machine_test

def cli_run():
    """Runs the command line interface for this project"""
    run = True
    
    zoeskull()

    print('~Welcome to the Finite State Machine Cli~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~Enter dfa to test the~~~~~~~~~')
    print('~~~Deterministic Finite State Machine~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~Enter nfa to test the~~~~~~~~~')
    print('~~Non-Deterministic Finite State Machine~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~Enter test to run unit tests~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~Enter q at any time to quit~~~~~~~')   

    again = False    
    while run:
        if again: 
           print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
           print('~~~~~~~~Enter dfa, nfa, test, or q~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user_input = input('~')
        user_input = user_input.lower()
        again = True

        if user_input == 'q': 
                run = False
                break

        elif user_input == 'dfa':
            dfa = Dfa.Dfa()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~Deterministic Finite State Machine~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~~~~~~Enter an input string~~~~~~~~~~')
            dfa_input  = input('~')
            if dfa_input == 'q': 
                run = False
                break
            dfa.input(dfa_input, 0)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        elif user_input == 'nfa':
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('NFA not implemented yet')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        elif user_input == 'test':
            test = machine_test.MachineTest()
            test.cli_test()
            
