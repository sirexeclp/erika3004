import time
import unittest

from erika.erika import Erika

# TODO make parameter dynamic

# e.g. Linux
# (determine port by observing output of
#   dmesg
# on the command line after connecting USB)
#
# COM_PORT = "/dev/ttyACM0"

# e.g. Windows
COM_PORT = "COM3"


class ConnectTest(unittest.TestCase):
    def test_connect(self):
        """simple test that there is no exception when connecting"""
        with Erika(COM_PORT) as ignored:
            pass
        self.assertTrue(True)

    def test_movement(self):
        """simple test to test cursor movement - validation is manual check of cursor movement"""
        delay = 0
        with Erika(COM_PORT) as my_erika:
            for i in range(10):
                my_erika.move_right()
                time.sleep(delay)
            for i in range(10):
                my_erika.move_up()
                time.sleep(delay)
            for i in range(10):
                my_erika.move_left()
                time.sleep(delay)
            for i in range(10):
                my_erika.move_down()
                time.sleep(delay)


def main():
    unittest.main()


if __name__ == '__main__':
    main()