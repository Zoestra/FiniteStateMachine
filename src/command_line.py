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
            run_dfa = True
            dfa_count = 0
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~Deterministic Finite State Machine~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            while run_dfa:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('~~~~~~~~~~Enter an input string~~~~~~~~~~')
                print('~~~~~~~~~~Or enter q to return~~~~~~~~~~~')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                dfa_input  = input('~')
                if dfa_input != 'q': 
                    dfa.input(dfa_input, 0)
                    dfa_count += 1

                elif dfa_input == 'q':
                    run_dfa = False
                
                if dfa_count > 5:

                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~~~Accepted language is: (a+b)c*~~~~~~~')

        elif user_input == 'nfa':
            run_nfa = True
            nfa_count = 0
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~Non-Deterministic Finite State Machine~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            while run_nfa:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('~~~~~~~~~~Enter an input string~~~~~~~~~~')
                print('~~~~~~~~~~Or enter q to return~~~~~~~~~~~')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                nfa_input  = input('~')
                nfa = Nfa.Nfa()
                if nfa_input != 'q': 
                    nfa.input(nfa_input, 0)
                    if nfa.get_result() == True:
                        print('String accepted!')
                    else:
                        print('String Rejected')
                    nfa_count += 1
                else:
                    run_nfa = False
                if nfa_count > 5:
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('~~~Accepted language is: (a | b)*abb~~~~~')


        elif user_input == 'test':
            test = machine_test.MachineTest()
            test.cli_test()
            
