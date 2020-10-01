def convertCelsiusToKelvin(value):
    kelvin = round((float(value) + 273.15), 2)
    #return 0
    return kelvin

def convertCelsiusToFahrenheit(value):
    farenheit = round(((float(value) * 1.8) + 32), 2)
    #return 0
    return farenheit

def convertFahrenheitToKelvin(value):
    kelvin = round(((float(value) + 459.67) * 0.5555555556), 2)
    #return 0
    return kelvin

def convertFahrenheitToCelsius(value):
    celsius = round(((float(value) - 32.0) * 0.5555555556), 2)
    #return 0
    return celsius

def convertKelvinToFahrenheit(value):
    farenheit = round(((float(value) * 1.8) - 459.67), 2)
    #return 0
    return farenheit

def convertKelvinToCelsius(value):
    celsius = round((float(value) - 273.15), 2)
    #return 0
    return celsius

if __name__ == '__main__':
    known_ctof = [(0,32), (5,41), (12.5,54.5), (744,1371.2), (-10,14)]
    known_ctok = [(-273.15, 0), (-200,73.15), (-100,173.15), (0,273.15), (5, 278.15)]
    for ctof in known_ctof:
        f = convertCelsiusToFahrenheit(ctof[0])
        if f==ctof[1]: print ("convertCelsiusToFahrenheit({}) Succeded".format(ctof[0]))
        else: print ("convertCelsiusToFahrenheit({}) Failed! Returned {} instead of {}".format(ctof[0], f, ctof[1]))
    for ctok in known_ctok:
        k = convertCelsiusToKelvin(ctok[0])
        if k == ctok[1]: print ("convertCelsiusToKelvin({}) Succeded".format(ctok[0]))
        else: print ("convertCelsiusToKelvin({}) Failed! Returned {} instead of {}".format(ctok[0], f, ctok[1]))