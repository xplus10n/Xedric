#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bin_to_dec(binary_string):

    decimal=0
    for i in range(len(str(binary_string))):
        decimal+=int(str(binary_string)[i])*(2**(len(str(binary_string))-i-1))
    return decimal

def dec_to_bin(number):

    import math
    binary=""
    digits=int((math.log2(number)//1)+1)
    for i in range(digits):
        binary+=str(number//(2**(digits-i-1)))
        number-=(2**(digits-i-1))*(number//(2**(digits-i-1)))
    return binary

def telephone_cipher(message):

    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    saver=""
    new_message=""
    for i in range(len(message)):
        if saver!=encoder_dict[message[i]][0]:
            new_message+=encoder_dict[message[i]]
            saver=encoder_dict[message[i]][0]
        else:
            new_message+="_"+encoder_dict[message[i]]
            saver=encoder_dict[message[i]][0]

    return new_message    

def telephone_decipher(telephone_string):

    decipher_dict = {
            "0":" ",
            '2': 'A',
            '22': 'B',
            '222': 'C',
            '3': 'D',
            '33': 'E',
            '333': 'F',
            '4': 'G',
            '44': 'H',
            '444': 'I',
            '5': 'J',
            '55': 'K',
            '555': 'L',
            '6': 'M',
            '66': 'N',
            '666': 'O',
            '7': 'P',
            '77': 'Q',
            '777': 'R',
            '7777': 'S',
            '8': 'T',
            '88': 'U',
            '888': 'V',
            '9': 'W',
            '99': 'X',
            '999': 'Y',
            '9999': 'Z'
        }
    
    new_message=[]
    real_message=""
    for i in range(len(telephone_string.split("_"))):
        x=0
        numb=0
        for j in range(len(telephone_string.split("_")[i])):
            y=len(telephone_string.split("_")[i])
            try:
                if telephone_string.split("_")[i][j]==telephone_string.split("_")[i][j+1]:
                    x+=1
                    numb+=1
                else:
                    new_message.append((telephone_string.split("_")[i][x])*(numb+1))
                    x+=1
                    numb=0
            except:
                new_message.append((telephone_string.split("_")[i][x])*(numb+1))
                x+=1
                numb=0
    
    for k in range(len(new_message)):
        real_message+=decipher_dict[new_message[k]]

    return real_message


# In[ ]:




