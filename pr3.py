"""
practical no 5

aim : write a program to implement Rail fence -row and column Transformation 

"""

def rail_fence_encrypt(plaintext: str, num_rails: int) -> str:
    if num_rails <= 1 or num_rails >= len(plaintext):
        return plaintext

    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1  

    for char in plaintext:
        rails[rail] += char
        rail += direction

        
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return ''.join(rails)

def transpose_matrix(matrix):
    return [''.join(row) for row in zip(*matrix)]

def row_column_transformation(ciphertext: str, num_rails: int) -> str:
    num_cols = len(ciphertext) // num_rails
    if len(ciphertext) % num_rails != 0:
        num_cols += 1
    
    
    rail_matrix = [['' for _ in range(num_cols)] for _ in range(num_rails)]
    index = 0

    for i in range(num_rails):
        for j in range(num_cols):
            if index < len(ciphertext):
                rail_matrix[i][j] = ciphertext[index]
                index += 1

    
    transposed_matrix = transpose_matrix(rail_matrix)
    
    
    transformed_text = ''.join(''.join(row) for row in transposed_matrix)
    return transformed_text

def rail_fence_with_transformation(plaintext: str, num_rails: int) -> str:
    
    rail_fence_ciphertext = rail_fence_encrypt(plaintext, num_rails)
    
    
    final_ciphertext = row_column_transformation(rail_fence_ciphertext, num_rails)
    
    return final_ciphertext


plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
key = int(input("Enter the key (number of rails): "))


if key >= len(plaintext) or key < 2:
    print("The number of rails is too large or too small. Please enter a valid number.")
else:
    
    ciphertext = rail_fence_with_transformation(plaintext, key)
    print(f"Ciphertext: {ciphertext}")


