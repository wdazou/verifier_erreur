#!/usr/bin/env python3

def parity_pair(byte_array):
    
    msg=bytearray() #prend le message et le transforme en bytearray
    
    for i in bytearray :
        rep=bin(byte_array).strip('0b') #bytearray en binaire pour savoir si paire/impaire
        
        if (Counter(rep)['1'] % 2 == 0):
            msg.append(int('0'+rep,2)) #ajout 0 si pair
            
        else:
            msg.append(int('1'+rep,2))
            
     return msg   
        
def parity_impaire(byte_array):
        msg=bytearray()
    
    for i in bytearray :
        rep=bin(byte_array).strip('0b')
        
        if (Counter(rep)['1'] % 2 == 0):
            
            msg.append(int('1'+rep,2)) # ajout 1 si c'est impaire
            
        else:
            msg.append(int('0'+rep,2))
            
    return msg