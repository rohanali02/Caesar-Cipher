text = input("Enter your Text: ")
number= int(input("Enter Number to encode: "))
ask = input("Do you want to Encrypt or Decrypt: ")

def encode(text, number):
    for i in range(len(text)):
        if text[i] == " ":
            print(" ", end="")
        else:
            print
            print(chr(ord(text[i]) + number), end="")

def decode(text, number):
    for i in range(len(text)):
        if text[i] == " ":
            print(" ", end="")
        else:
            print
            print(chr(ord(text[i]) - number), end="")

if ask.lower()== "encrypt" or ask.lower() == "e":
    encode(text, number)
elif ask.lower() == ("decrypt") or ask.lower() == "d":
    decode(text, number)
else:
    print("Invalid Input")


