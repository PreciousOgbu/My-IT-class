import sys

vowel = 'aeiou'
lst = []

if len(lst) ==0:
   print("The list is empty")

if not lst:
   print("The list is empty")
def get_vowel(string):
    for v in string:
        if v in vowel:
         lst.append(v)
    print(''.join(lst))
    
    return f'The original string is {string}'
    
result = get_vowel("Heyau")
print(result)


print(sys.getsizeof(result))
print(sys.getsizeof(vowel))
print(sys.getsizeof(lst))


