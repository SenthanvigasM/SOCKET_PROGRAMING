import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        previous_units = float(input("Enter previous units consumed (or -1 to exit): "))
        if previous_units == -1:
            break

        current_units = float(input("Enter current units consumed: "))

        data = f"{previous_units} {current_units}"
        client_socket.sendto(data.encode('utf-8'), ('127.0.0.1', 12345))

        response, server_address = client_socket.recvfrom(1024)
        print(response.decode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    main()
