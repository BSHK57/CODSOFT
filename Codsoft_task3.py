import random
def PassWordGenerator(length):
    #Defining special Characters
    characters="!@#$%^&*()-=+><.,/?;:[]{}|~`"
    #Defining alphbets
    alphabet="abcdefghijklmnopqrstuvwxzy"
    #Defining number (digits)
    numbers="0123456789"
    #combining all the characters
    all_characters=characters+alphabet+numbers+alphabet.upper()
    #Password Should contain atlest one uppercase,one lowercase
    #one special Character and one digit
    rand_char=random.choice(characters)
    rand_lower=random.choice(alphabet)
    rand_upp=random.choice(alphabet.upper())
    rand_digit=random.choice(numbers)
    password=rand_char+rand_lower+rand_upp+rand_digit
    #Gerating the Passcode of desired Length
    for i in range(length-4):
        password+=random.choice(all_characters)
    pw=list(password)
    random.shuffle(pw)
    password=''.join(i for i in pw)
    return password
def main():
    #prompting user to get the length of password
    length=int(input("Enter the length for password(minimun length is 4): "))
    password=PassWordGenerator(length)
    #displaying Password
    print(f"\nGenerated password:  {password}\n")
if __name__=="__main__":
    main()
