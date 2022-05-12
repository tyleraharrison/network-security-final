#!/usr/bin/env python3

def addRoundKey(state, key):
    # Plaintext
    plain_int_val = int(state, 16)
    # Convert to 64 bit binary
    state = bin(plain_int_val)[2:].zfill(64)

    # Key
    key_int_val = int(key, 16)
    # Convert to 64 bit binary
    key = bin(key_int_val)[2:].zfill(64)
    
    return_state = []
    for i in range(len(state)):
        return_state.append(int(state[i]) ^ int(key[i]))
    # Put array back into string
    return_state = ''.join(str(x) for x in return_state)
    # Convert binary string to hex
    return_state = str(hex(int(return_state, 2)))
    print("AddRoundKey:", return_state)
    return return_state

def sBox(state):
    x_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    s_box = ["c", "5", "6", "b", "9", "0", "a", "d", "3", "e", "f", "8", "4", "7", "1", "2"]
    return_state = ''
    for i in range(len(state)):
        if state[i] in x_list:    
            return_state += s_box[x_list.index(state[i])]
        else:
            return_state += state[i]
    print("S-Box:", return_state)
    return return_state

def inv_SBox(state):
    s_box = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    x_list = ["c", "5", "6", "b", "9", "0", "a", "d", "3", "e", "f", "8", "4", "7", "1", "2"]
    return_state = ''
    for i in range(len(state)):
        if state[i] in x_list:    
            return_state += s_box[x_list.index(state[i])]
        else:
            return_state += state[i]
    print("S-Box:", return_state)
    return return_state

def sBoxLayer(state):
    state = sBox(state)
    return state

def pLayer(state):
    return state

def generateRoundKeys(plaintext, key, rounds):
    state = plaintext
    for i in range(rounds):
        c1 = addRoundKey(state, key)
        c2 = sBoxLayer(c1)
        c3 = pLayer(c2)
    return c3

if __name__ == "__main__":
    # Plaintext
    plaintext = "0x28B4D27B225F8BD8".lower()
    print("Plaintext:", plaintext)

    # Key
    key = "0x0123456789ABCDEF".lower()
    print("Key:", key)

    # Generate round keys (one iteration)
    roundkeys = generateRoundKeys(plaintext, key, 1)
    print("Round keys:", roundkeys)
