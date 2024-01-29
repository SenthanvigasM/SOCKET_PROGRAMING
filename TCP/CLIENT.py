import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    while True:
        previous_units = float(input("Enter previous units consumed (or -1 to exit): "))
        if previous_units == -1:
            break

        current_units = float(input("Enter current units consumed: "))
    
        data = f"{previous_units} {current_units}"
        client_socket.send(data.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
