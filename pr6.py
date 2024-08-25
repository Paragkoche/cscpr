"""
practical no 8

aim : Calculate the message digest of text using the sha1 algorithmn

"""
import hashlib

def calculate_sha1(text: str) -> str:
    
    encoded_text = text.encode()

    
    sha1_hash = hashlib.sha1()

    
    sha1_hash.update(encoded_text)

    
    message_digest = sha1_hash.hexdigest()

    return message_digest

if __name__ == "__main__":
    
    text = input("Enter the text to hash using SHA-1: ")

    
    sha1_digest = calculate_sha1(text)

    
    print(f"SHA-1 Message Digest: {sha1_digest}")
