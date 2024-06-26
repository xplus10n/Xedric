#!/usr/bin/env python
# coding: utf-8

# In[26]:


def shift_letter(letter, shift):

    if(letter==" "):
        letter="_"

    if(shift=="_"):
        shift=" "
    
    if 65<=(ord(str(letter)))<=90:
        return chr(((ord(str(letter))-65+int(shift))%26)+65)
    else:
        return " "

def caesar_cipher(message, shift):

    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message=""
    for letter in range(len(message)):
        if message[letter]==" ":
            new_message+=" "
        else:
            new_message+=alphabet[((alphabet.find(message[letter]))+shift)%26]
    return new_message

def shift_by_letter(letter, letter_shift):

    if(letter==" "):
        letter="_"

    if(letter_shift=="_"):
        shift=" "
    
    if 65<=(ord(str(letter)))<=90:
        return chr(((ord(str(letter))-65+(ord(letter_shift)-65))%26)+65)
    else:
        return " "

def vigenere_cipher(message, key):

    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message=""
    key=(str(key)*len(message))[0:len(message)]
    for i in range(len(message)):
        if message[i]==" ":
            new_message+=" "
        else:
            new_message+=alphabet[((alphabet.find(message[i])+alphabet.find(key[i]))%26)]
    return new_message
        
            
def scytale_cipher(message, shift):

    new_message=""
    while len(message)%int(shift)!=0:
        message+="_"
    for i in range(len(message)):
        new_message+=message[(i // int(shift)) + (len(message) // int(shift)) * (i % int(shift))]
    return new_message
        
def scytale_decipher(message, shift):

    new_message=""
    for i in range(len(message)):
        new_message+=message[((int(shift))*(i % (len(message)//int(shift))))+(i//(len(message)//int(shift)))]
    return new_message


# In[ ]:




