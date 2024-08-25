"""
practical no 3

aim : implemet caeser ciper substitution techniques

"""

def substitution_tech(plain_text: str, key: int) -> str:
    if len(plain_text) == 0:
        return ""
    if plain_text[0].isupper():
        new_char = chr(((ord(plain_text[0]) - ord('A') + key) % 26) + ord('A'))
    elif plain_text[0].islower():
        new_char = chr(((ord(plain_text[0]) - ord('a') + key) % 26) + ord('a'))
    else:
        new_char = plain_text[0]
    return new_char + substitution_tech(plain_text[1:], key)

plan_text = str(input("Enter the plan text: "))
key = int(input("Enter the plan Key: "))
print(substitution_tech(plan_text, key))
