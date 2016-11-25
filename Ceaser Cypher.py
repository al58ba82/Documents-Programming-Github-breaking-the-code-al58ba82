
def encrypt(string,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ''
    for letter in string:
        #print(letter)
        index = alphabet.find(letter)
        new_index = index - int(key)
        output += alphabet[new_index]
    print(output)


def decrypt(string,key):
    print('decrypt')


print("What do you want to do? Encrypt (Type in text to be decrypted by a friend) or Decrypt (Decrypt text, or have the computer decrypt offsetted text you want")

mode = input("E/D")
sentence = input("What is the phrase?")
key = input("What is the key?")

if mode == "E":
    encrypt(sentence,key)
elif mode == "D":
    decrypt(sentence,key)

#input the sentence
#input the key or the offset



#Hello

#list of the alphabet
#for each letter find the index
#new index = letter index - key
# Find the letter for the new key

#this is a change

#The main define variable to make the program work [Input sentence]
#Encrypt, get the alphabet to create offset [1-20]
#User, Get a user to write the text for encryption
#Run, Run the code to makw sure it works fine
#If it works, then we will have the encrypted text
#Afterwords, we Decrypt the text it gives us, by getting another User,
#And then repeat.


3