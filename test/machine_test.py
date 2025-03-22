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
        print(f'Test1 - \'{in_string}\' passed')

    def test_dfa2(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'acc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'Test2 - \'{in_string}\' passed')

    def test_dfa3(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bcccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'Test3 - \'{in_string}\' passed')


    def test_dfa4(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = ''
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'Test4 - \'{in_string}\' passed')

    def test_dfa5(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = 'ccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'Test5 - \'{in_string}\' passed')

    def test_dfa6(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'acccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'Test6 - \'{in_string}\' passed')

    def test_dfa7(self):
        """DFA test - expected to fail"""
        dfa = Dfa.Dfa()
        in_string = '  '
        result = dfa.input(in_string, 1)
        self.assertEqual(result, -1)
        print(f'Test7 - \'{in_string}\' passed')
    
    
    def test_dfa8(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bcccccccccccccccccccccccccccccccc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'Test8 - \'{in_string}\' passed')

    def test_dfa9(self):
        """DFA test - expected to pass in state 4"""
        dfa = Dfa.Dfa()
        in_string = 'ac'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 4)
        print(f'Test9 - \'{in_string}\' passed')

    def test_dfa_10(self):
        """DFA test - expected to pass in state 5"""
        dfa = Dfa.Dfa()
        in_string = 'bc'
        result = dfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'Test10 - \'{in_string}\' passed')

    def test_nfa_1(self):
        """nFA test - expected to pass"""
        nfa = Nfa.Nfa()
        in_string = 'aabb'
        result = nfa.input(in_string, 1)
        self.assertEqual(result, 5)
        print(f'Nfa Test1 - \'{in_string}\' passed')

       

    def cli_test(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Running DFA Tests')
        self.test_dfa1()
        self.test_dfa2()
        self.test_dfa3()
        self.test_dfa4()
        self.test_dfa5()
        self.test_dfa6()
        self.test_dfa7()


if __name__ == '__main__': 
    unittest.main()

