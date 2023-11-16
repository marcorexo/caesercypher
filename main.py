alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
"""
if position + shift > length of array
  then 
  position = position + shift - length of array

  else
  position = position + shift

for example:
  position = 14
  shift = 13
  length_of_array = 26
  position = 14 + 13 - 26 = 2
""" ""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"


def encrypt(text, shift):
    encrypted_text = ""
    """
    if position + shift > length of array
    then 
    position = position + shift - length of array

    else
    position = position + shift
    """
    for letter in text:
        position = alphabet.index(letter)
        if position + shift > 26:
            new_position = position + shift - 26
        else:
            new_position = position + shift
        encrypted_text += alphabet[new_position]
    return encrypted_text


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

print(encrypt(text=text, shift=shift))

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
