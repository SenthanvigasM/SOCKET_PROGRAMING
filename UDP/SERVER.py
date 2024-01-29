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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 12345))

    print("Server is listening...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        if not data:
            break

        # Assuming the received data is in the format "previous_units current_units"
        previous_units, current_units = map(float, data.decode('utf-8').split())
        total_amount = calculate_bill(previous_units, current_units)
        response = f"Total amount: ${total_amount:.2f}"

        server_socket.sendto(response.encode('utf-8'), client_address)

    server_socket.close()

if __name__ == '__main__':
    main()
