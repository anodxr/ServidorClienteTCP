import socket

HOST = '127.0.0.1'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Evitar errores de "puerto en uso"
s.bind((HOST, PORT))
s.listen()
print(f"Servidor escuchando en {HOST}:{PORT}")

try:
    while True:
        try:
            conn, addr = s.accept()
            conn.settimeout(10)
            print(f"Conexión establecida desde {addr}")
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        mensaje = data.decode().strip()
                        if mensaje == "hola servidor":
                            mensaje = "hola cliente"
                        if mensaje == "DESCONEXION":
                            print(f"Conexión con {addr} cerrada por solicitud")
                            break
                        respuesta = mensaje.upper().encode()
                        conn.sendall(respuesta)
                    except socket.timeout:
                        print(f"Timeout: Cerrando conexión con {addr}")
                        break
        except ConnectionResetError:
            print(f"Conexión con {addr} interrumpida")
        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario (Ctrl+C)")
            break  # Salir del bucle principal
except KeyboardInterrupt:
    print("\nServidor detenido por el usuario (Ctrl+C)")
finally:
    s.close()  # Cerrar el socket principal
    print("Socket del servidor cerrado correctamente.")
