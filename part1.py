#!/usr/bin/env python3

def addRoundKey(state, key):
    return_state = []
    for i in range(len(state)):
        return_state.append(int(state[i]) ^ int(key[i]))
    # Put array back into string
    return_state = ''.join(str(x) for x in return_state)
    return return_state

def sBoxLayer(state):
    return state

def pLayer(state):
    return state

def generateRoundKeys(plaintext, key, rounds):
    state = plaintext
    for i in range(rounds):
        state = addRoundKey(state, key)
        state = sBoxLayer(state)
        state = pLayer(state)
    return state

if __name__ == "__main__":
    # Plaintext
    plaintext = "0x28B4D27B225F8BD8".lower()
    plain_hex_val = int(plaintext, 16)
    # Convert to 64 bit binary
    plain_bin_val = bin(plain_hex_val)[2:].zfill(64)
    print("Plaintext:", plaintext)
    print("Plaintext (hex):", plain_hex_val)
    print("Plaintext (bin):", plain_bin_val)

    # Key
    key = "0x0123456789ABCDEF".lower()
    key_hex_val = int(key, 16)
    # Convert to 64 bit binary
    key_bin_val = bin(key_hex_val)[2:].zfill(64)
    print("Key:", key)
    print("Key (hex):", key_hex_val)
    print("Key (bin):", key_bin_val)

    # Generate round keys (one iteration)
    roundkeys = generateRoundKeys(plain_bin_val, key_bin_val, 1)
    print("Round keys:", hex(int(roundkeys, 2)))
