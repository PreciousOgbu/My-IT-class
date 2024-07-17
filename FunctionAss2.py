# A function that converts Celsius to Farehenit

def Convert_Celsius_to_Fahrenheit():

    # Convert temperature from Celsius to Fahrenheit

 celsuis =int(input('Enter temperature in Celsuis: ')) 
 fahrenheit = ( celsuis * 9/5) + 32
 return fahrenheit

fahrenheit = Convert_Celsius_to_Fahrenheit()
print(f' The temperature is {fahrenheit} degrees Fahrenheit')

