def vowel (text):
    vowels = "aeiouAEIOU"
    print (len ([letter for letter in text if letter in vowels]))
    print ([letter for letter in text if letter in vowels])
vowel ('elephent')