import bluetooth

client_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

client_socket.connect(("7C:01:91:51:91:2F", 1))

client_socket.send("Hi Boss")

print("Finished")

client_socket.close()
