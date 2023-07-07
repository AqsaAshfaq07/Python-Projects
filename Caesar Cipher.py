# Encode and decode text for better security 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z']


# Step - 1 - Use caesar function for encryption and decryption

def caesar( direction_, message_, shift_):
    cipher_text = ""
    
    for char in message_:
        if char in letters:
            pos = letters.index(char)
            if direction == "encode":
                new_pos = pos + (shift_ % 26)  # shift_ % 26 -> to tackle with higher shift numbers 
            else:
                new_pos = pos - (shift_ % 26)
            if new_pos >= 26:
                new_pos -= 26 
            new_char = letters[new_pos]
            cipher_text += new_char
            
        else:  # to tackle with number/symbols/spaces
            cipher_text += char

    print(f"The cipher text is {cipher_text}")
    

# Step - 1  - Ask user for direction, message and shift and take decisions 

continue_ = True

while continue_:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  \n")
    message = input("Type your message:  \n")
    shift = int(input("Type the shift number:  \n"))
    caesar(direction, message, shift)
    
    result = input("Type 'yes' if you want to continue, otherwise type 'no'")
    if result == "no":
        continue_ = False
        print("Good Bye :)")