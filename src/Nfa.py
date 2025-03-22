
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
