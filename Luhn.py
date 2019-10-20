def Luhn (number):
  """ function Luhn validates a number against the Luhn checksum formula 
     - function call: Luhn (number) 
       number has to be an integer, digits only 
     - output: True | False 

     source: https://en.wikipedia.org/wiki/Luhn_algorithm 
      
     Press q to exit. """


  result = False

  i = 0
  LuhnSum = 0
  for digitC in reversed(str(number)):
     i = i+1
     digitN = int(digitC)
     
     if (i%2 == 0):
        if (2*digitN >=10):
           LuhnSum = LuhnSum+2*digitN-9
        else:
           LuhnSum = LuhnSum+2*digitN
     else:
        LuhnSum = LuhnSum+digitN

  
  result= (LuhnSum%10 == 0)
 
  return result

