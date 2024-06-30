#Purpose: A caesar cipher program
#Date:15/03/2023
#Author:g24m5008
def get_input():
    stringOfChars = str(input("Enter a string:")) #Get string from user
    stringOfChars = stringOfChars.upper() #Capitalize the string
    return stringOfChars

def encryptor(stringOfChars):
    i = 0
    new_string = ""
    while i < len(stringOfChars): #Extract characters from string and store extracted character in a variable
        ch = stringOfChars[i]
        if ch != " ": #Skip the character if it is a space
            chVal = ord(ch) + 13  #Represent the extracted string as a number and rotate it by 13 places
            if chVal > 90: #Check if chval is less than or equals to 90 ,if its greater,minus the character's value from 90
                wrap_val = chVal - 90
                chVal = 64 + wrap_val
            new_ch = chr(chVal) #Convert it back in to an alphabet
            new_string += new_ch #Make it a string
        else:
            new_string += " " #add the skipped char
        i += 1
    return new_string
def main():
    userInput = get_input()
    new_string_of_char = encryptor(userInput)
    print(new_string_of_char)
    
if __name__ == "__main__" :
    main()
    




 
