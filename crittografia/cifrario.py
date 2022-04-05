MAX_KEY = 26

def getMode():
    while True:
        print("criptare | decriptare")
        mode = input().lower()
        if mode in "criptare decriptare".split():
            return mode
        else:
            print("criptare | decriptare")

def getMessage():
    print("Inserisci il messaggio da criptare o decriptare: ")
    return input()

def getKey():
    key1 = 0
    key2 = 0
    key3 = 0
    while True:
        print("Inserisci le chiavi (1-%s)" % (MAX_KEY)) 
        key1 = int(input())
        key2 = int(input())
        key3 = int(input())
        if((key1 >= 1 and key1 <= MAX_KEY) and (key2 >= 1 and key2 <= MAX_KEY) and (key3 >= 1 and key3 <= MAX_KEY)):
            keys = key1, key2, key3
            return keys

def getTransazione(mode, message, keys):
    transazione = ""
    i = 0
    if mode == "decriptare":
        keys = -keys[0], -keys[1], -keys[2]

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            if(i == 3):
                i = 0
            num += keys[i]
            print(keys[i])

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            transazione += chr(num)
        else:
            transazione += symbol
        i = i + 1
        
    return transazione

mode = getMode()
message = getMessage()
keys = getKey()

print("Il messaggio finale è: ")
print(getTransazione(mode, message, keys))