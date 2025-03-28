import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Conectado al servidor. Escribe 'DESCONEXION' para salir.")
    try:
        while True:
            mensaje = input("Mensaje: ").strip()
            if not mensaje:  # Si la entrada está vacía
                print("Entrada vacía. Cerrando conexión...")
                s.sendall("DESCONEXION".encode())  # Forzar desconexión
                break
            s.sendall(mensaje.encode())
            if mensaje == "DESCONEXION":
                print("Desconectando...")
                break
            data = s.recv(1024)
            print(f"Respuesta del servidor: {data.decode()}")
    except KeyboardInterrupt:  # Si el usuario presiona Ctrl+C
        print("\nDesconexión forzada")
        s.sendall("DESCONEXION".encode())
