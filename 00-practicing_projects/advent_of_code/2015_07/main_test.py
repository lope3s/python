from unittest import TestCase
from main import Command, WireAssembling

class TestWireAssemblingParseCommand(TestCase):
    def test_and_command(self):
        wire_assembling = WireAssembling()
        input = "x AND y -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": "x",
            "input2": "y",
            "operation": "AND",
            "destination": "z"
        }
        self.assertEqual(output, expected)

    def test_not_command(self):
        wire_assembling = WireAssembling()
        input = "NOT y -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": "",
            "input2": "y",
            "operation": "NOT",
            "destination": "z"
        }
        self.assertEqual(output, expected)

    def test_or_command(self):
        wire_assembling = WireAssembling()
        input = "x OR y -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": "x",
            "input2": "y",
            "operation": "OR",
            "destination": "z"
        }
        self.assertEqual(output, expected)

    def test_lshift_command(self):
        wire_assembling = WireAssembling()
        input = "x LSHIFT y -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": "x",
            "input2": "y",
            "operation": "LSHIFT",
            "destination": "z"
        }
        self.assertEqual(output, expected)

    def test_rshift_command(self):
        wire_assembling = WireAssembling()
        input = "x RSHIFT y -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": "x",
            "input2": "y",
            "operation": "RSHIFT",
            "destination": "z"
        }
        self.assertEqual(output, expected)

    def test_operationless_command(self):
        wire_assembling = WireAssembling()
        input = "1 -> z"
        output = wire_assembling.parse_command(input)
        expected: Command = {
            "input1": 1,
            "operation": "",
            "input2": "",
            "destination": "z"
        }
        self.assertEqual(output, expected)

class TestWireAssemblingAssemblyWires(TestCase):
    def test_empty_wires(self):
        wire_assembling = WireAssembling()
        command: Command = {
            'input1': 'x',
            'operation': 'OR',
            'input2': 'y',
            'destination': 'z'
        }
        output = wire_assembling.assembly_wires(command)
        self.assertFalse(output)
        self.assertIsNone(wire_assembling.wires.get('x'))
        self.assertIsNone(wire_assembling.wires.get("y"))
        self.assertIsNone(wire_assembling.wires.get("z"))
        

    def test_operationless_assembling(self):
        wire_assembling = WireAssembling()
        command: Command = {
            'input1': 123,
            'operation': '',
            'input2': '',
            'destination': 'x'
        }
        output = wire_assembling.assembly_wires(command)
        self.assertTrue(output)
        self.assertEqual(wire_assembling.wires['x'], 123)

    def test_operationless_redirect_assembling(self):
        wire_assembling = WireAssembling()
        wire_assembling.wires['lx'] = 0
        command: Command = {
            'input1': 'lx',
            'operation': '',
            'input2': '',
            'destination': 'x'
        }
        output = wire_assembling.assembly_wires(command)
        self.assertTrue(output)
        self.assertEqual(wire_assembling.wires['x'], 0)

    def test_example(self):
        wire_assembling = WireAssembling()
        commands: list[Command] = [
                { 'input1': 123, 'operation': '', 'input2': '', 'destination': 'x' },
                { 'input1': 456, 'operation': '', 'input2': '', 'destination': 'y' },
                { 'input1': 'x', 'operation': 'AND', 'input2': 'y', 'destination': 'd' },
                { 'input1': 'x', 'operation': 'OR', 'input2': 'y', 'destination': 'e' },
                { 'input1': 'x', 'operation': 'LSHIFT', 'input2': 2, 'destination': 'f' },
                { 'input1': 'y', 'operation': 'RSHIFT', 'input2': 2, 'destination': 'g' },
                { 'input1': '', 'operation': 'NOT', 'input2': 'x', 'destination': 'h' },
                { 'input1': '', 'operation': 'NOT', 'input2': 'y', 'destination': 'i' },
        ]
        for command in commands:
            output = wire_assembling.assembly_wires(command)
            self.assertTrue(output)

        self.assertEqual(wire_assembling.wires['d'], 72)
        self.assertEqual(wire_assembling.wires['e'], 507)
        self.assertEqual(wire_assembling.wires['f'], 492)
        self.assertEqual(wire_assembling.wires['g'], 114)
        self.assertEqual(wire_assembling.wires['h'], 65412)
        self.assertEqual(wire_assembling.wires['i'], 65079)
        self.assertEqual(wire_assembling.wires['x'], 123)
        self.assertEqual(wire_assembling.wires['y'], 456)
