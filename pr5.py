"""
practical no 7

aim : implement diffie hellman key exchange algorithm

"""
import random

def diffie_hellman(p, g):
    # Step 1: Each party selects a private key (a, b)
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    
    # Step 2: Each party computes their public value (A, B)
    A = pow(g, a, p)  # A = g^a mod p
    B = pow(g, b, p)  # B = g^b mod p

    # Step 3: Exchange the public values (A, B)
    print(f"Alice's public value (A): {A}")
    print(f"Bob's public value (B): {B}")

    # Step 4: Each party computes the shared secret key
    alice_shared_key = pow(B, a, p)  # Alice's shared key: B^a mod p
    bob_shared_key = pow(A, b, p)    # Bob's shared key: A^b mod p

    return alice_shared_key, bob_shared_key

if __name__ == "__main__":
    # Step 1: Agree on a large prime number p and a base g (publicly known)
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a base (g): "))

    # Perform the Diffie-Hellman key exchange
    alice_shared_key, bob_shared_key = diffie_hellman(p, g)

    print(f"Alice's shared key: {alice_shared_key}")
    print(f"Bob's shared key: {bob_shared_key}")

    # Verify that both shared keys are the same
    if alice_shared_key == bob_shared_key:
        print("Key exchange successful. Both parties have the same shared secret key.")
    else:
        print("Key exchange failed. The shared keys do not match.")
