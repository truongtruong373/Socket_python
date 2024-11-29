import tkinter as tk
import socket
import threading
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 65432
FORMAT = "utf-8"

USER_NAME = 'truong'
my_username = USER_NAME
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

username = my_username.encode(FORMAT)
username_header = f"{len(username):<{HEADER_LENGTH}}".encode(FORMAT)
client_socket.send(username_header + username)


# Hàm gửi tin nhắn
def send_message():
    message = entry_message.get()  # Lấy nội dung từ ô nhập liệu

    message = message.encode(FORMAT)
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode(FORMAT)
    client_socket.send(message_header + message)

    if message.strip():  # Kiểm tra nếu tin nhắn không rỗng
        chat_box.insert(tk.END, f"{USER_NAME}: {message.decode(FORMAT)}")  # Thêm tin nhắn vào khung chat
        entry_message.delete(0, tk.END)  # Xóa nội dung trong ô nhập liệu
    else:
        chat_box.insert(tk.END, "Hệ thống: Vui lòng nhập nội dung!")


def receive_messages():
    while True:
        # receive things
        username_header_a = client_socket.recv(HEADER_LENGTH)
        if not len(username_header_a):
            print('Connection closed by server')
            sys.exit()
        username_length_a = int(username_header_a.decode(FORMAT).strip())
        username_a = client_socket.recv(username_length_a).decode(FORMAT)

        message_header_a = client_socket.recv(HEADER_LENGTH)
        message_length_a = int(message_header_a.decode(FORMAT).strip())
        message_a = client_socket.recv(message_length_a).decode(FORMAT)

        chat_box.insert(tk.END, f"{username_a}: {message_a}")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Khung Chat")
root.geometry("400x400")

# Khung hiển thị chat
chat_frame = tk.Frame(root)
chat_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Hộp văn bản hiển thị tin nhắn
chat_box = tk.Listbox(chat_frame, font=("Arial", 12), bg="lightgrey", height=15)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Thanh cuộn dọc cho khung chat
scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

# Khung nhập liệu
entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry_message = tk.Entry(entry_frame, font=("Arial", 12), width=30)
entry_message.pack(side=tk.LEFT, padx=5, pady=5)

# Nút gửi tin nhắn
btn_send = tk.Button(entry_frame, text="Gửi", font=("Arial", 12), command=send_message)
btn_send.pack(side=tk.RIGHT, padx=5, pady=5)


receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

# Chạy giao diện
root.mainloop()
