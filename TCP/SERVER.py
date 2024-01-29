import socket

def calculate_bill(previous_units, current_units):
    units_consumed = current_units - previous_units
    if units_consumed <= 50:
        rate_per_unit = 25
    elif units_consumed <= 100:
        rate_per_unit = 80
    else:
        rate_per_unit = 250
    
    total_amount = units_consumed * rate_per_unit
    return total_amount

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server is listening...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        previous_units, current_units = map(float, data.split())
        total_amount = calculate_bill(previous_units, current_units)
        response = f"Total amount: ${total_amount:.2f}"
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
