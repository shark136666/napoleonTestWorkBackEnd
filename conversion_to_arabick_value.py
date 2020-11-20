
class Solution:
     def romanToInt(self, s: str) -> int: 
            roman_symbols = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000                    
                   }
            s = str.upper(s)
            result = 0
            i = 0
            while (i <= len(s) - 1):
                roman_value = s[i]
                arab_value = roman_symbols[roman_value]                
                try:
                    next_roman_value = s[i + 1]
                    next_arab_value = roman_symbols[next_roman_value]                    
                except:
                    next_arab_value = 0

                if(arab_value < next_arab_value):
                    result += next_arab_value - arab_value
                    i += 2
                    continue

                if(arab_value > next_arab_value):
                    result += arab_value
                    i += 1
                    continue
                    
                else:
                    result += arab_value
                    i += 1
                    continue               
                
            return(result)
            
            