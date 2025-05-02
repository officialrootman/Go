import socket
import paramiko

# Kullanıcıdan gerekli bilgileri al
host = input("Honeypot'un bağlanacağı IP adresini gir (varsayılan: 0.0.0.0): ") or "0.0.0.0"
port = int(input("SSH hizmeti için port numarasını gir (varsayılan: 2222): ") or 2222)

host_key = paramiko.RSAKey.generate(1024)

class FakeSSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        print(f"Giriş denemesi: {username}:{password}")
        return paramiko.AUTH_FAILED

# Sunucu başlat
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Honeypot çalışıyor: {host}:{port}")

while True:
    client, addr = server.accept()
    print(f"Bağlantı geldi: {addr}")
    transport = paramiko.Transport(client)
    transport.add_server_key(host_key)
    transport.start_server(server=FakeSSHServer())
