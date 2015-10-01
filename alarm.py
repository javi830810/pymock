import unittest
from mock import MagicMock


class Temperature(object):
    def __init__(self, temperature):
        self.temperature = temperature

    def increase_temperature(self, grades):
        self.temperature += grades

    def get_temperature(self):
        return self.temperature


class Alarm(object):

    def __init__(self, threshold, temperature):
        self.state = 0 # off
        self.threshold = threshold
        self.temperature = temperature

    def check_temperature(self):
        if self.temperature.get_temperature() >= self.threshold:
            #self.set_on()
            pass
        else:
            self.set_off()

    def set_on(self):
        self.state = 1

    def set_off(self):
        self.state = 0


class TestAlarm(unittest.TestCase):

    def test_alarm_sets_on_with_stub(self):
        temperature = Temperature(30)
        alarm = Alarm(50, temperature) # threshold, temperature

        temperature.increase_temperature(30)
        alarm.check_temperature()

        self.assertEqual(alarm.state, 1)

    def test_alarm_sets_on_with_mock(self):

        temperature_mock = Temperature(30)
        temperature_mock.get_temperature = MagicMock(return_value=60)

        alarm = Alarm(60, temperature_mock)
        alarm.set_on = MagicMock()

        alarm.check_temperature()

        temperature_mock.get_temperature.assert_called_once_with()
        alarm.set_on.assert_called_once_with()




