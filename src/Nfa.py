
class Nfa:
    def __init__(self):
        None
    
    def input(self, input_string, test):
        if len(input_string)== 0:
            self.state_F
        self.state_1(input_string, test) 


    def state_1(self, input_string, test):
        if input_string[0] == 'a' or input_string[0] == 'b':
            self.state_1(input_string[1:], test)

        if input_string[0] == 'a':
            self.state_2(input_string[1:], test)

            
    def state_2(self, input_string, test):
        if input_string[0] == 'a' or input_string[0] == 'b':
            self.state_3(input_string[1:], test)            

    def state_3(self, input_string, test):
        if input_string[0] == 'a' or input_string[0] == 'b':
            self.state_A(input_string[1:], test)            

        
    def state_A(self, input_string, test):
        print('input accepted')
        
    def state_F(self, test):
        print('input rejected')