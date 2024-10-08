from typing import TypedDict

Command = TypedDict(
    'Command',
    {
        'input1': str | int,
        'input2': str | int,
        'operation': str,
        'destination': str
    }
)

class WireAssembling():
    wires: dict[str, int] = {}

    def parse_command(self, input: str) -> Command:
        parameters = input.split(" ")
        command: Command = {
            'input1': '',
            'operation': '',
            'input2': '',
            'destination': ''
        }
        keys = list(command.keys())

        for i in range(len(parameters)):
            parameter = parameters[i]
            if parameter == "->":
                command['destination'] = parameters[i + 1]
                break

            if i == 0 and parameter == "NOT":
                keys = keys[1:]

            if parameter.isnumeric():
                command[keys[i]] = int(parameter)
                continue
            command[keys[i]] = parameter

        return command

    def assembly_wires(self, command: Command) -> bool:
        destination = command["destination"]
        operation = command["operation"]

        for key in ['input1', 'input2']:
            input_value = command[key]
            if input_value and type(input_value) == str:
                if self.wires.get(input_value) == None and operation != "NOT":
                    return False
                    
        if not operation:
            input = command['input1']
            if type(input) == str:
                value = self.wires.get(input)
                if value == None:
                    return False
                self.wires[destination] = value
                return True
            
            self.wires[destination] = int(input)
            return True

        match operation:
            case 'NOT':
                input = command['input2']
                if type(input) == str:
                    input_value = self.wires.get(input)
                    if input_value == None:
                        return False
                    self.wires[destination] = (~input_value) & 0xFFFF
                    return True

                self.wires[destination] = (~int(input)) & 0xFFFF
                return True

            case 'OR':
                input1 = command['input1']
                input2 = command['input2']
                if type(input1) == str:
                    input1 = self.wires.get(input1)
                if type(input2) == str:
                    input2 = self.wires.get(input2)
                if input1 == None or input2 == None:
                    return False
                self.wires[destination] = int(input1) | int(input2)
                return True

            case 'AND':
                input1 = command['input1']
                input2 = command['input2']
                if type(input1) == str:
                    input1 = self.wires.get(input1)
                if type(input2) == str:
                    input2 = self.wires.get(input2)
                if input1 == None or input2 == None:
                    return False
                self.wires[destination] = int(input1) & int(input2)
                return True

            case 'LSHIFT':
                input1 = command['input1']
                input2 = command['input2']
                if type(input1) == str:
                    input1 = self.wires.get(input1)
                if input1 == None:
                    return False
                self.wires[destination] = int(input1) << int(input2)
                return True

            case 'RSHIFT':
                input1 = command['input1']
                input2 = command['input2']
                if type(input1) == str:
                    input1 = self.wires.get(input1)
                if input1 == None:
                    return False
                self.wires[destination] = int(input1) >> int(input2)
                return True

            case _:
                return False


if __name__ == '__main__':
    with open('input.txt') as f:
        wire_assembly = WireAssembling()
        commands = f.readlines()
        i = 0
        
        while len(commands) > 0:
            command_line = commands[i].strip()
            command = wire_assembly.parse_command(command_line)
            if wire_assembly.assembly_wires(command):
                commands.pop(i)
                i = 0
                continue
            i += 1

        print(f'The signal on wire a is {wire_assembly.wires.get("a")}')
