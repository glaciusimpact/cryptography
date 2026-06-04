#!/usr/bin/env python3

file_data = "./message.txt"
key = "depuis"
table_decoding = {
    "a": "abcdefghiklmnopqrstuxyz&",
    "b": "acbkdueiflgnhomypsqxrtz&",
    "c": "adbgczekfmhtixlrnpoqs&uy",
    "d": "aebzctdkfigshylqmxnro&pu",
    "e": "afblcidheugkmtnqorp&sxyz",
    "f": "ahbfcldgeqiykpmunso&rxtz",
    "g": "agbicldnerfphtkum&oxqysz",
    "h": "aibtcsdoelf&ghkmnqpruyxz",
    "i": "akbtcsdxeiflgzhym&npoqru",
    "j": "akbtcsdxeiflgzhym&npoqru",
    "k": "albocpdgerfshuixkymzn&qt",
    "l": "ambzcdegfihklnorpsqutyx&",
    "m": "anbocpdqerfsgthuixkylzm&",
    "n": "aobcdmepfsgnhyiuktlqr&xz",
    "o": "apblckdqesfugxhzi&monrty",
    "p": "aqbxcudzesfogyhtinkrl&mp",
    "q": "arbzctdheufqgoilknmpsyx&",
    "r": "asbncqdteufyg&hoipkrlxmz",
    "s": "atbpcqdre&fsguhxiykzlnmo",
    "t": "aubycmdxe&fhgqirkzlsnpot",
    "u": "axblcodqesfugthyinkzm&pr",
    "v": "axblcodqesfugthyinkzm&pr",
    "x": "ayb&czdefxguhiktlsmrnpoq",
    "y": "azbucgdhexfyiok&lnmpqsrt"
}
zero_or_one = 0
index_key = 0
key_length = len(key)


# Decoding function
def decode_function(message, key):

  global zero_or_one
  global index_key
  global key_length
  global table_decoding
  decoded_data = ""

  # Remove all special characters (return, new line, etc.)
  message = "".join(message.splitlines())

  # Read all characters
  for char in message:
    
    # Decoding or not?
    if zero_or_one == 0:

      # Decoding

      # Lower case
      char = char.lower()

      # Current key character
      key_char = key[index_key]

      # Key character existing in the decoding table?
      if key_char in table_decoding:

        # Yes

        # Check if message character is in the decoding table line
        if char in table_decoding[key_char]:

          # Index of the found character
          x = table_decoding[key_char].index(char)

          # Finding position of the character to use for replacement
          if (x & 1) == 0:
            x += 1
          else:
            x -= 1

          # Get decoded character
          char = table_decoding[key_char][x]

        else:

          # Error

          # Key character does not exist in decoding table
          char = "*"         
        
      else:

        # Error

        # Key character does not exist in decoding table
        char = "."

      # Next character of the key
      index_key += 1
      if index_key >= key_length:
        index_key = 0

    else:
      # Just copying the character
      pass

    # Copy character into decoded string
    decoded_data += char
    zero_or_one = (zero_or_one + 1) & 1

  # Return decoded string
  return decoded_data



# Message
print("[ Decoded message ]")

# Read file
with open(file_data) as f:

  # Read line by line
  for x in f:
    print(decode_function(x,key))

