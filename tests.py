import unittest
import conversions as conv
import conversions_refactored as conv_r


class ConversionsKnownValues(unittest.TestCase):
    valid_conversions = (
        (0.00, 32.00, 273.15), (32.00, 89.60, 305.15), (48.00, 118.40, 321.15),
        (100.00, 212.00, 373.15),(-273.15, -459.67, 0.00), (-373.15, -639.67, -100.00)
    )

    def testConvertCelsiusToKelvin(self):
        for val in self.valid_conversions:
            from_val = val[0]
            expected_val = val[2]
            returned_val = conv.convertCelsiusToKelvin(from_val)
            self.assertEqual(returned_val, expected_val, msg=( '{} Kelvin is not equal to expected value of {} Kelvin.').format(returned_val, expected_val))

    def testConvertCelsiusToFahrenheit(self):
        for val in self.valid_conversions:
            from_val = val[0]
            expected_val = val[1]
            returned_val = conv.convertCelsiusToFahrenheit(from_val)
            self.assertEqual(returned_val, expected_val, msg=('{} Fahrenheit is not equal to expected value of {} Fahrenheit.').format(returned_val, expected_val))

    def testConvertFahrenheitToKelvin(self):
        for val in self.valid_conversions:
            from_val = val[1]
            expected_val = val[2]
            returned_val = conv.convertFahrenheitToKelvin(from_val)
            self.assertEqual(returned_val, expected_val, msg=( '{} Kelvin is not equal to expected value of {} Kelvin.').format(returned_val, expected_val))

    def testConvertFahrenheitToCelsius(self):
        for val in self.valid_conversions:
            from_val = val[1]
            expected_val = val[0]
            returned_val = conv.convertFahrenheitToCelsius(from_val)
            self.assertEqual(returned_val, expected_val, msg=('{} Celsius is not equal to expected value of {} Celsius.').format(returned_val, expected_val))
                                                 
    def testConvertKelvinToFahrenheit(self):
        for val in self.valid_conversions:
            from_val = val[2]
            expected_val = val[1]
            returned_val = conv.convertKelvinToFahrenheit(from_val)
            self.assertEqual(returned_val, expected_val, msg=('{} Fahrenheit is not equal to expected value of {} Fahrenheit.').format(returned_val, expected_val))


    def testConvertKelvinToCelsius(self):
        for val in self.valid_conversions:
            from_val = val[2]
            expected_val = val[0]
            returned_val = conv.convertKelvinToCelsius(from_val)
            self.assertEqual(returned_val,expected_val, msg=('{} Celsius is not equal to expected value of {} Celsius.').format(returned_val, expected_val))

class ConversionsRefactoredValid(unittest.TestCase):
    valid_conversions = (
        ('celsius', 'kelvin', 0.00, 273.15),
        ('celsius', 'fahrenheit', 0.00, 32.00),
        ('fahrenheit', 'kelvin', 0.00, 255.37),
        ('fahrenheit', 'celsius', 0.00, -17.78),
        ('kelvin', 'celsius', 0.00, -273.15),
        ('kelvin', 'fahrenheit', 0.00, -459.67),
        ('miles', 'yards', 1.00, 1760.00),
        ('miles', 'meters', 1.00, 1609.34),
        ('meters', 'miles', 1000.00, 0.62),
        ('meters', 'yards', 1000.00, 1094.00),
        ('yards', 'miles', 1000.00, 0.57),
        ('yards', 'meters', 1000.00, 914.08)
    )
    # Not valid conversions can be placed in the tuple:
    # ('meters', 'meters', 1000.00, 1000.01) will return: 1000.0 != 1000.01 : 1000.0 meters is not equal to expected value of 1000.01 meters
    # ('yards', 'meters', 1000.00, 1914.08) will return: 914.08 != 1914.08 : 914.08 meters is not equal to expected value of 1914.08 meters

    def testConvert(self):
        for val in self.valid_conversions:
            from_unit = val[0]
            to_unit = val[1]
            from_val = val[2]
            expected_val = val[3]
            returned_val = conv_r.convert(from_unit, to_unit, from_val)
            self.assertEqual(returned_val, expected_val, msg=('{} {} is not equal to expected value of {} {}').format(returned_val, to_unit, expected_val, to_unit))
        
if __name__ == '__main__':
    unittest.main()
