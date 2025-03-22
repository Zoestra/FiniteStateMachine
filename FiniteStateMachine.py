import unittest

class Nfa:
    accepted = False
    
    def __init__(self):
        None
    
    def get_result(self):
        return self.accepted
    
    def input(self, input_string, test):
        self.accepted = False
        if len(input_string)== 0:
            return
        self.state_1(input_string, test) 


    def state_1(self, input_string, test):
        if len(input_string)== 0:
            return
        elif input_string[0] == 'a' or input_string[0] == 'b':
            self.state_1(input_string[1:], test)

        if input_string[0] == 'a':
            self.state_2(input_string[1:], test)

            
    def state_2(self, input_string, test):
        if len(input_string)== 0:
            return
        elif input_string[0] == 'b':
            self.state_3(input_string[1:], test)            

    def state_3(self, input_string, test):
        if len(input_string)== 0:
            return
        elif input_string[0] == 'b':
            self.state_A(input_string[1:], test)            


        
    def state_A(self, input_string, test):
        if len(input_string)== 0:
            self.accepted = True
            return
        else:
            self.accepted = False
            return



class Dfa:
    def __init__(self):
        self.state = 1
    def input(self, input_string: str, test):
        self.state = 1
        if input_string == '' or input_string == ' ':
            return -1
        input_list = list(input_string) 
        
        for input in input_list:
            if not test: print(f"Machine is in state 1\nInput is: {input}")
            output = self.action(input)
            if output == -1:
                if not test: print("Input invalid, sequence rejected")
                return output
            if not test: print(f"Machine advances to state {output}")

        if not test: 
            if output == 4 or output == 5:
                print("Input accepted")
            else:
                print("Input invalid, sequence rejected")

        return output

    def action(self, input):
        if self.state == 1:
            if input == "a":
                self.state = 2
                return 2
            elif input == "b":
                self.state = 3
                return 3
            else:
                return -1

        if self.state == 2:
            if input == "c":
                self.state = 4
                return 4
            else:
                return -1

        if self.state == 3:
            if input == "c":
                self.state = 5
                return 5
            else:
                return -1

        if self.state == 4:
            if input == "c":
                return 4
            else:
                return -1
        
        if self.state == 5:
            if input == "c":
                return 5
            else:
                return -1



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
            dfa = Dfa()
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
                nfa = Nfa()
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
            test = MachineTest()
            test.cli_test()
            
class MachineTest(unittest.TestCase):
    
    def test_dfa1(self):
        """DFA test - expected to fail"""
        dfa = Dfa()
        in_string = 'abccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test1 - \'{in_string}\' passed')

    def test_dfa2(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa()
        in_string = 'acc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test2 - \'{in_string}\' passed')

    def test_dfa3(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa()
        in_string = 'bcccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test3 - \'{in_string}\' passed')


    def test_dfa4(self):
        """DFA test - expected to fail"""
        dfa = Dfa()
        in_string = ''
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test4 - \'{in_string}\' passed')

    def test_dfa5(self):
        """DFA test - expected to fail"""
        dfa = Dfa()
        in_string = 'ccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test5 - \'{in_string}\' passed')

    def test_dfa6(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa()
        in_string = 'acccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test6 - \'{in_string}\' passed')

    def test_dfa7(self):
        """DFA test - expected to fail"""
        dfa = Dfa()
        in_string = '  '
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test7 - \'{in_string}\' passed')
    
    
    def test_dfa8(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa()
        in_string = 'bcccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test8 - \'{in_string}\' passed')

    def test_dfa9(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa()
        in_string = 'ac'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test9 - \'{in_string}\' passed')

    def test_dfa_10(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa()
        in_string = 'bc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test10 - \'{in_string}\' passed')

    def test_nfa1(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'aabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test1 - \'{in_string}\' passed')
    
    def test_nfa2(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'babb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test2 - \'{in_string}\' passed')

    def test_nfa3(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'aaabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test3 - \'{in_string}\' passed')

    def test_nfa4(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'bbabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test4 - \'{in_string}\' passed')


    def test_nfa5(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'ababb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test5 - \'{in_string}\' passed')


    def test_nfa6(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'bbbbbbbbbbbbbbbabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test6 - \'{in_string}\' passed')


    def test_nfa7(self):
        """NFA test - expected to pass"""
        nfa = Nfa()
        in_string = 'aaaaaaaaaaaaaaaaaaaabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test7 - \'{in_string}\' passed')


    def test_nfa8(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = ''
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test8 - \'{in_string}\' passed')


    def test_nfa9(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = ' '
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test9 - \'{in_string}\' passed')


    def test_nfa_10(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = 'ab'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test10 - \'{in_string}\' passed')


    def test_nfa_11(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = 'bbbbbbbbbbbb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test11 - \'{in_string}\' passed')


    def test_nfa_12(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = 'abcabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test12 - \'{in_string}\' passed')

    def test_nfa_13(self):
        """NFA test - expected to fail"""
        nfa = Nfa()
        in_string = 'abbb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test13 - \'{in_string}\' passed')



       

    def cli_test(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Running DFA Tests')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self.test_dfa1()
        self.test_dfa2()
        self.test_dfa3()
        self.test_dfa4()
        self.test_dfa5()
        self.test_dfa6()
        self.test_dfa7()
        self.test_dfa8()
        self.test_dfa9()
        self.test_dfa_10()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Running NFA Tests')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self.test_nfa1()
        self.test_nfa2()
        self.test_nfa3()
        self.test_nfa4()
        self.test_nfa5()
        self.test_nfa6()
        self.test_nfa7()
        self.test_nfa8()
        self.test_nfa9()
        self.test_nfa_10()
        self.test_nfa_11()
        self.test_nfa_12()
        self.test_nfa_13()
        
        

def zoeskull():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('         0                      1        ')
    print('        367     1321426910    842        ')
    print('        001367 132142691084 20013        ')
    print('         6713214269   1084200136         ')
    print('          71321426     91084200          ')
    print('         1367132142   6910842001         ')
    print('        3671321426910842001   367        ')
    print('        132      1426910       84        ')
    print('        200       136713       21        ')
    print('        426       91 084       20        ')
    print('         013   67132  14269 10842        ')
    print('           00136713214269108420          ')
    print('      0      136713214269108     4       ')
    print('      200     13 671  32  14   2691      ')
    print('      08420       0    1     367132      ')
    print('    142691084200         136713214269    ')
    print('    1084   200136713  2142691            ')
    print('                  0842001                ')
    print('              3671321   4269108  4200    ')
    print('      13   671321            4269108     ')
    print('      4200136                  713       ')
    print('        214                     26       ')
    print('        910                              ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~made by~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~Zoestra Hammer~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    








def main():
    
    cli_run()       
   
if __name__ == '__main__':
    main()

