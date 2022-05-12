#!/usr/bin/env python3

def addRoundKey(state, key):
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

def invSBox(state):
    return state

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
    plain_int_val = int(plaintext, 16)
    # Convert to 64 bit binary
    plain_bin_val = bin(plain_int_val)[2:].zfill(64)
    print("Plaintext:", plaintext)
    # print("Plaintext (int):", plain_int_val)
    # print("Plaintext (bin):", plain_bin_val)

    # Key
    key = "0x0123456789ABCDEF".lower()
    key_int_val = int(key, 16)
    # Convert to 64 bit binary
    key_bin_val = bin(key_int_val)[2:].zfill(64)
    print("Key:", key)
    # print("Key (int):", key_int_val)
    # print("Key (bin):", key_bin_val)

    # Generate round keys (one iteration)
    roundkeys = generateRoundKeys(plain_bin_val, key_bin_val, 1)
    print("Round keys:", roundkeys)
