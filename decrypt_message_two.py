encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
def decrypt_transposition(encrypted_message):
    message_list = list(encrypted_message)
    start = 1
    end = len(message_list) - 2
    while start < end:
        message_list[start], message_list[end] = message_list[end], message_list[start]
        start += 2
        end -= 2
    decrypted_message = ''.join(message_list)
    print(decrypted_message)

myMessage = open('encrypted_message_two.txt')
myMessage = myMessage.readline()
decrypt_transposition(myMessage)
