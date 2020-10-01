class UnitDoesNotExistException(Exception):
    # print exception raised
    pass

class ConversionNotPossibleException(Exception):
    # print exception raised
    pass

def convert(from_unit, to_unit, value):
    # We use a unit conversion dictionary, with lambdas to complete the conversions
    unit_conversions = {
        'celsius': {
            'kelvin': lambda x: round((float(x) + 273.15), 2),
            'fahrenheit': lambda x: round(((float(x) * 1.8) + 32), 2)
        },
        'fahrenheit': {
            'kelvin': lambda x: round(((float(x) + 459.67) * 0.5555555556), 2),
            'celsius': lambda x: round(((float(x) - 32.0) * 0.5555555556), 2)
        },
        'kelvin': {
            'fahrenheit': lambda x: round(((float(x) * 1.8) - 459.67), 2),
            'celsius': lambda x: round((float(x) - 273.15), 2)
        },
        'miles': {
            'yards': lambda x: round((float(x) * 1760), 2),
            'meters': lambda x: round((float(x) * 1609.344), 2)
        },
        'yards': {
            'miles': lambda x: round((float(x) / 1760), 2),
            'meters': lambda x: round((float(x) / 1.094), 2)
        },
        'meters': {
            'miles': lambda x: round((float(x) / 1609.344), 2),
            'yards': lambda x: round((float(x) * 1.094), 2)
        }
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit in unit_conversions and to_unit in unit_conversions:
        if from_unit == to_unit:
            return float(value)
        elif to_unit in unit_conversions[from_unit]:
            return unit_conversions[from_unit][to_unit](value)
        else:
            raise ConversionNotPossibleException
    else:
        raise UnitDoesNotExistException
