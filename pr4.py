"""
practical no 6

aim : write a program to implement rsa algorithm

"""
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    
    d = modinv(e, phi)

    
    
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    e, n = pk
    
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    d, n = pk
    
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encryption/Decryption")
    
    
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))

    
    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    
    message = input("Enter the message to encrypt: ")
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_msg}")

    
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted Message: {decrypted_msg}")
