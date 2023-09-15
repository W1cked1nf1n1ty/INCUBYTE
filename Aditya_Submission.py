import unittest


class TestSpacecraft(unittest.TestCase):
    def test_spacecraft_initial_position(self):
        spacecraft = Spacecraft()
        self.assertEqual(spacecraft.position, [0, 0, 0])
        self.assertEqual(spacecraft.direction, 'N')

    def test_spacecraft_move_forward(self):
        spacecraft = Spacecraft()
        spacecraft.move('f')
        self.assertEqual(spacecraft.position, [0, 1, 0])
        self.assertEqual(spacecraft.direction, 'N')

    def test_spacecraft_move_backward(self):
        spacecraft = Spacecraft()
        spacecraft.move('b')
        self.assertEqual(spacecraft.position, [0, -1, 0])
        self.assertEqual(spacecraft.direction, 'N')

    def test_spacecraft_rotate_right(self):
        spacecraft = Spacecraft()
        spacecraft.rotate('r')
        self.assertEqual(spacecraft.position, [0, 0, 0])
        self.assertEqual(spacecraft.direction, 'E')

    def test_spacecraft_rotate_left(self):
        spacecraft = Spacecraft()
        spacecraft.rotate('l')
        self.assertEqual(spacecraft.position, [0, 0, 0])
        self.assertEqual(spacecraft.direction, 'W')

    def test_spacecraft_execute_commands(self):
        spacecraft = Spacecraft()
        commands = ["f", "r", "u", "b", "l"]
        spacecraft.execute_commands(commands)
        self.assertEqual(spacecraft.position, [0, 1, -1])
        self.assertEqual(spacecraft.direction, 'N')


class Spacecraft:
    def __init__(self):
        self.position = [0, 0, 0]
        self.direction = 'N'

    def move(self, command):
        movements = {
            'N': (0, 1, 0),
            'S': (0, -1, 0),
            'E': (1, 0, 0),
            'W': (-1, 0, 0),
            'Up': (0, 0, 1),
            'Down': (0, 0, -1),
        }

        if command == 'f':
            dx, dy, dz = movements[self.direction]
        elif command == 'b':
            dx, dy, dz = (-x for x in movements[self.direction])
        else:
            dx, dy, dz = (0, 0, 0)

        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz

    def rotate(self, command):
        rotations = {
            ('N', 'r'): 'E',
            ('E', 'r'): 'S',
            ('S', 'r'): 'W',
            ('W', 'r'): 'N',
            ('N', 'l'): 'W',
            ('W', 'l'): 'S',
            ('S', 'l'): 'E',
            ('E', 'l'): 'N',
            ('U', 'u'): 'N',
            ('N', 'd'): 'U',
        }

        self.direction = rotations.get((self.direction, command), self.direction)

    def execute_commands(self, commands):
        for command in commands:
            if command in ['f', 'b']:
                self.move(command)
            elif command in ['l', 'r', 'u', 'd']:
                self.rotate(command)

    def get_position(self):
        return tuple(self.position)

    def get_direction(self):
        return self.direction


if __name__ == "__main__":
    unittest.main()
