# print("Hello Python word!")
message = "Hello Python word"
print(message)

message = "! Hello Python Crash Course world! "
print(message)
print(message.lower())
print("(message.upper()"+message.upper())
print(message.lower().count('cr'))
print("message.count('C')"+str(message.count('C')))
print('len(message)'+str(len(message)))
print("str(message.count(' '))"+str(message.count(' ')))
print('with strip'+str(message.strip().count(' ')))
print('find !' + str(message.find("!")))
print('replace! to ^:' + message.replace('!', '^'))