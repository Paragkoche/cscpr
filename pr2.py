"""
practical no 4

aim : write a program to implement play fair cipher

"""
def generate_key_matrix(key_phrase: str) -> list:
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_phrase = key_phrase.upper().replace("J", "I")
    key_phrase = ''.join(sorted(set(key_phrase), key=lambda x: key_phrase.index(x)))
    matrix = [c for c in key_phrase if c in alphabet] + [c for c in alphabet if c not in key_phrase]
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def format_plaintext(plaintext: str) -> str:
    plaintext = plaintext.upper().replace("J", "I")
    formatted = ""
    i = 0
    while i < len(plaintext):
        formatted += plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted += 'X'
        else:
            i += 1
        i += 1
    if len(formatted) % 2 != 0:
        formatted += 'X'
    return formatted

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext: str, key_phrase: str) -> str:
    matrix = generate_key_matrix(key_phrase)
    plaintext = format_plaintext(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(matrix, plaintext[i])
        row2, col2 = find_position(matrix, plaintext[i + 1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

plan_text = str(input("Enter the plan text: "))
key = str(input("Enter the plan Key: "))
ciphertext = playfair_encrypt(plan_text, key)
print(ciphertext)
