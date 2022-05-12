#!/usr/bin/env python3

def get_keys(p, q, e, d):
    n = p * q
    pub_key = (e, n)
    priv_key = (d, n)
    return pub_key, priv_key

def encrypt(pub_key, plaintext):
    cipher_m = []
    plaintext = plaintext[2:]
    # Convert each hex character to its corresponding integer
    for i in plaintext:
        cipher_m.append(int(i, 16))
    print("Plaintext List:", cipher_m)
    cipher = []
    # Encrypt each integer
    for i in cipher_m:
        # Epub(m) = m^e mod n
        cipher.append(i ** pub_key[0] % pub_key[1])
    return cipher

def decrypt(priv_key, cipher):
    hex_list = []
    plaintext = []
    # Decrypt each integer
    for i in cipher:
        # Dpriv(c) = c^d mod n
        hex_list.append(i ** priv_key[0] % priv_key[1])
    print()
    print("Decrypted list:", hex_list)
    for i in hex_list:
        # Convert each integer to its corresponding hex character
        plaintext.append(hex(i)[2:])
    plaintext = "0x" + (''.join(plaintext))
    return plaintext

if __name__ == '__main__':
    p = 47
    q = 71
    e = 97
    d = 1693
    pub_key, priv_key = get_keys(p, q, e, d)
    phi = (p - 1) * (q - 1)
    print("Public key:", pub_key)
    print("Private key:", priv_key)
    print("Phi:", phi)
    print()
    plaintext = "0x012324b10afbecdd"
    print("Plaintext:", plaintext)
    cipher = encrypt(pub_key, plaintext)
    print("Ciphertext List:", cipher)
    decrypted = decrypt(priv_key, cipher)
    print ("Decrypted Plaintext:", decrypted)
    print()
    print("Success") if decrypted == plaintext else print("Failed")
    
