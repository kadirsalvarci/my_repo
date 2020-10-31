pythondef InttoRoman(number):
    romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
        return "Not Valid Input !!!"
    number = int(number)    
    result = ""
    for key, value in romandict.items():
        while number >= value:
            quotient = number // value 
            result += key * quotient
            number %= value
    return result
print("###  This program converts decimal numbers to Roman Numerals ###",'\nTo exit the program, please type "exit")')
while True:
    number = input("Please enter a number between 1 and 3999, inclusively : ")
    if number == "exit":
        print("Exiting the program... Good Bye")
        break
    print(InttoRoman(number))