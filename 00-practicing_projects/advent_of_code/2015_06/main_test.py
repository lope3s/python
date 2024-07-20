from unittest import TestCase
from main import init_grid_bool, init_grid_int, instruction_parser, InstructionDict, count_lights_bool, count_lights_int, switcher_controller_bool, switcher_controller_int

class TestGridInitializer(TestCase):
    def test_init_grid_bool(self):
        output = init_grid_bool()
        self.assertEqual(len(output), 1000)
        self.assertEqual(len(output[0]), 1000)
        self.assertEqual(output[0][0], False)

    def test_init_grid_int(self):
        output = init_grid_int()
        self.assertEqual(len(output), 1000)
        self.assertEqual(len(output[0]), 1000)
        self.assertEqual(output[0][0], 0)
        

class TestInstructionParser(TestCase):
    def test_first_instruction_isnt_splited(self):
        input = 'turn off 660,55 through 986,197'
        output = instruction_parser(input)
        self.assertEqual(output["instruction"], "turn off")
        self.assertEqual(output["range_start"], (660,55))
        self.assertEqual(output["range_end"], (986,197))

    def test_instruction_doesnt_break_with_single_word_command(self):
        input = 'toggle 660,55 through 986,197'
        output = instruction_parser(input)
        self.assertEqual(output["instruction"], "toggle")
        self.assertEqual(output["range_start"], (660,55))
        self.assertEqual(output["range_end"], (986,197))

class TestCountLights(TestCase):
    def test_should_count_ten_lights_on(self):
        grid_input = init_grid_bool()
        for i in range(10):
            grid_input[i][i] = True

        output = count_lights_bool(grid_input)
        self.assertEqual(output, 10)

    def test_should_count_ten_lights_brightness(self):
        grid_input = init_grid_int()
        for i in range(10):
            grid_input[i][i] = 1

        output = count_lights_int(grid_input)
        self.assertEqual(output, 10)

class TestSwitcherController(TestCase):
    def test_turn_on_all_lights(self):
       grid_input = init_grid_bool()
       instruction_input: InstructionDict = {
           "instruction": "turn on",
           "range_start": (0, 0),
           "range_end": (999, 999)
       }
       switcher_controller_bool(grid_input, instruction_input)
       lights_on = count_lights_bool(grid_input)
       self.assertEqual(lights_on, 1_000_000)

    def test_turn_on_first_column(self):
       grid_input = init_grid_bool()
       instruction_input: InstructionDict = {
           "instruction": "toggle",
           "range_start": (0,0),
           "range_end": (999,0)
       }
       switcher_controller_bool(grid_input, instruction_input)
       lights_on = count_lights_bool(grid_input)
       self.assertEqual(lights_on, 1000)

    def test_toggle_lights_in_the_specified_range(self):
       grid_input = init_grid_bool()
       setup_input: InstructionDict = {
           "instruction": "turn on",
           "range_start": (0, 0),
           "range_end": (999, 999)
       }
       switcher_controller_bool(grid_input, setup_input)
       instruction_input: InstructionDict = {
           "instruction": "turn off",
           "range_start": (499,499),
           "range_end": (500,500)
       }
       switcher_controller_bool(grid_input, instruction_input)
       lights_on = count_lights_bool(grid_input)
       self.assertEqual(lights_on, 999_996)
        
    def test_increate_light_brightness(self):
       grid_input = init_grid_int()
       instruction_input: InstructionDict = {
           "instruction": "turn on",
           "range_start": (0, 0),
           "range_end": (999, 999)
       }
       switcher_controller_int(grid_input, instruction_input)
       lights_on = count_lights_int(grid_input)
       self.assertEqual(lights_on, 1_000_000)

    def test_increate_first_light_brightness_by_1(self):
       grid_input = init_grid_int()
       instruction_input: InstructionDict = {
           "instruction": "turn on",
           "range_start": (0, 0),
           "range_end": (0, 0)
       }
       switcher_controller_int(grid_input, instruction_input)
       lights_on = count_lights_int(grid_input)
       self.assertEqual(lights_on, 1)


    def test_increase_first_column_brightness_by_2(self):
       grid_input = init_grid_int()
       instruction_input: InstructionDict = {
           "instruction": "toggle",
           "range_start": (0,0),
           "range_end": (999,0)
       }
       switcher_controller_int(grid_input, instruction_input)
       lights_on = count_lights_int(grid_input)
       self.assertEqual(lights_on, 2000)

    def test_decease_brightness_leverl_by_1(self):
       grid_input = init_grid_int()
       setup_input: InstructionDict = {
           "instruction": "toggle",
           "range_start": (0, 0),
           "range_end": (999, 999)
       }
       switcher_controller_int(grid_input, setup_input)
       instruction_input: InstructionDict = {
           "instruction": "turn off",
           "range_start": (499,499),
           "range_end": (500,500)
       }
       switcher_controller_int(grid_input, instruction_input)
       lights_on = count_lights_int(grid_input)
       self.assertEqual(lights_on, 1_999_996)
