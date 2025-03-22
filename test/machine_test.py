import unittest
import sys
sys.path.insert(0, '..')
from src import Dfa
from src import Nfa

class MachineTest(unittest.TestCase):
    


    def test_dfa1(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = 'abccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test1 - \'{in_string}\' passed')

    def test_dfa2(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'acc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test2 - \'{in_string}\' passed')

    def test_dfa3(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bcccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test3 - \'{in_string}\' passed')


    def test_dfa4(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = ''
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test4 - \'{in_string}\' passed')

    def test_dfa5(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = 'ccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test5 - \'{in_string}\' passed')

    def test_dfa6(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'acccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test6 - \'{in_string}\' passed')

    def test_dfa7(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = '  '
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'DFA Test7 - \'{in_string}\' passed')
    
    
    def test_dfa8(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bcccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test8 - \'{in_string}\' passed')

    def test_dfa9(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'ac'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'DFA Test9 - \'{in_string}\' passed')

    def test_dfa_10(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'DFA Test10 - \'{in_string}\' passed')

    def test_nfa1(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'aabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test1 - \'{in_string}\' passed')
    
    def test_nfa2(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'babb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test2 - \'{in_string}\' passed')

    def test_nfa3(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'aaabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test3 - \'{in_string}\' passed')

    def test_nfa4(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'bbabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test4 - \'{in_string}\' passed')


    def test_nfa5(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'ababb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test5 - \'{in_string}\' passed')


    def test_nfa6(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'bbbbbbbbbbbbbbbabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test6 - \'{in_string}\' passed')


    def test_nfa7(self):
        """NFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'aaaaaaaaaaaaaaaaaaaabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, True)
        print(f'Nfa Test7 - \'{in_string}\' passed')


    def test_nfa8(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
        in_string = ''
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test8 - \'{in_string}\' passed')


    def test_nfa9(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
        in_string = ' '
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test9 - \'{in_string}\' passed')


    def test_nfa_10(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
        in_string = 'ab'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test10 - \'{in_string}\' passed')


    def test_nfa_11(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
        in_string = 'bbbbbbbbbbbb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test11 - \'{in_string}\' passed')


    def test_nfa_12(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
        in_string = 'abcabb'
        nfa.input(in_string, 1)
        result = nfa.get_result()
        self.assertEqual(result, False)
        print(f'Nfa Test12 - \'{in_string}\' passed')

    def test_nfa_13(self):
        """NFA test - expected to fail"""
        nfa = Nfa.Nfa()
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
        
        
        
if __name__ == '__main__': 
    unittest.main()

