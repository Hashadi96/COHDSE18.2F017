def encrypt(text, key):
    
 result = ''
 for char in text: 
  if char == ' ':
      result = result + char
  elif char.isupper():
      result = result + chr((ord(char) + key - 65) % 26 + 65)
  else:
      result = result + chr((ord(char) + key - 97) % 26 + 97)
  

 return result
    
string=input("enter text: ")
t = int(input("enter key: "))
print("text is: ", string)
print("encrypted text is: ", encrypt(string,t))
