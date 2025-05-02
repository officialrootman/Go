package main

import (
	"fmt"
	"net"
	"os"
)

func handleConnection(conn net.Conn) {
	defer conn.Close()
	fmt.Println("Bağlantı geldi:", conn.RemoteAddr())
	conn.Write([]byte("Merhaba, bu bir honeypot!\n"))
}

func main() {
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println("Bağlantı başlatılamadı:", err)
		os.Exit(1)
	}
	defer listener.Close()

	fmt.Println("Honeypot çalışıyor, bağlantılar bekleniyor...")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Bağlantı hatası:", err)
			continue
		}
		go handleConnection(conn)
	}
}
