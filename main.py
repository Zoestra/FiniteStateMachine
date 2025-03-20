class FiniteStateMachine:
    def __init__(self):
        self.state = 1
        self.valid = True

    def input(self, input_string: str):
        input_list = input_string.split()
        for input in input_list:
            print(f"Input is: {input}\nMachine is in state {1}")
            output = self.action(input)
            if output == -1:
                print("Input invalid, sequence rejected")
                return None
            print(f"Machine advances to state {output}")

        print("Input accepted")
        return None

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
                self.state = 4
                return 4
            else:
                return -1

        if self.state == 4:
            if input == "c":
                return 4
            else:
                return -1


def main():
    machine = FiniteStateMachine()
    machine.input("abccc")
    print("~~~~~~~~~")
    machine.input("acc")
    print("~~~~~~~~~")
    machine.input("bccccc")


main()
