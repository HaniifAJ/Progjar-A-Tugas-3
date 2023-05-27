import sys
import socket
import logging
from multiprocessing import Process
import time


def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


def start_process():
    p = Process(target=kirim_data)
    p.start()
    p.join()


if __name__ == '__main__':
    process_count = 0  # Inisiasi counter
    start_time = time.time()  # Save waktu mulai
    
    # Terus buat proses selama 60 detik
    while time.time() - start_time < 60:
        start_process()
        process_count += 1  # Update counter di sini
    # Print jumlah proses yang telah dibuat
    logging.warning(f"Total processes created: {process_count}")
