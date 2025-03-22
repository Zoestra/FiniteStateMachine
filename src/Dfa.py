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

        if not test: print("Input accepted")
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