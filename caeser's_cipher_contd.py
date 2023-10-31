alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','y']

def caeser(text_input, shift_input, direction_input):
  output_text = ""
  if direction == "decode":
    shift_input *= -1
  for char in text_input:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_input
      output_text += alphabet[new_position]
    else:
      output_text += char
       
  print(f"Here is the {direction}d result: {output_text}")

should_play = True
while should_play:
  direction = input("Please type 'encode' to encrypt or 'decode' to decrypt:\n")    
  text = input("Please input the text:\n")
  shift = int(input("Please input the shift value:\n"))
  shift = shift % 26

  caeser(text_input = text, shift_input = shift, direction_input = direction)
    
     
  play = input("Do you want to encode or decrypt another text? Type 'yes' to or 'no' to end the program:\n")

  if play == "no":
    should_play = False    
    print("goodbye")
    break
#need to find out how to use breaks


      










            
  
    
