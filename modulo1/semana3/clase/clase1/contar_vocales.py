def couting_vowels(vowels:str="aeiou")->int:
    vowelsArray:list = ["a", "e", "i", "o", "u"]
    countVowels:int=0
    for i in vowels:
        if i in vowelsArray:
            countVowels += 1
    return countVowels

print(couting_vowels("Hola"))