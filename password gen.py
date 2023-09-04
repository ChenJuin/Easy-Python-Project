import random
import string

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
digit = string.digits
punctuation = string.punctuation

print("----------Python Password Generator----------")

#make it keep looping 
while True:
    
    print("Please input the details below to generate your password!")
    length_low_alphabet = int(input("Amount of lower alphabet: "))
    length_up_alphabet = int(input("Amount upper alphabet: "))
    length_digit = int(input("Amount of digits: "))
    length_punctuation = int(input("Amount of punctuation: ")) 

    #check whether the length have negative or not 
    if length_low_alphabet >= 0 and length_up_alphabet >= 0 and length_digit >= 0 and length_punctuation >= 0:
    
        final_low = random.choices(alphabet_lower,k=length_low_alphabet)
        final_up = random.choices(alphabet_upper,k=length_up_alphabet)
        final_digit = random.choices(digit,k=length_digit)
        final_punctuation = random.choices(punctuation,k=length_punctuation)

        #total up the password
        final = final_low + final_up + final_digit + final_punctuation
        
        #shuffle the total up password
        random.shuffle(final)
        
        #join the list form password into string form
        final_password = "".join(final)
        
        print("Your password is: ",final_password)
        
        #want to try again or not
        choice = input("Do you want to try other password?(y/n): ")
        if choice == "y":
            continue
        elif choice == "n":
            break
        else:
            print("Error input, try again!")
            break
    else:
        print("Invalid input!")
        break


#still got some bug need to fix!