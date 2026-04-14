#Mini project : Emoji's converter in the message 

message = input("Enter the Message,Here:")

message = message.replace(":)","😊")
message = message.replace(":(","☹️")
message = message.replace(";)","😉")
message = message.replace(":D","😄")

print(message)

