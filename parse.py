import re

with open('debug.log', 'r') as file:
    log_data = file.read()

# 1: Cetak pesan EHLO
ehlo_start = log_data.find("send: 'ehlo")
ehlo_end = log_data.find("\\r\\n'", ehlo_start)
ehlo_message = log_data[ehlo_start:ehlo_end]
print("1:", ehlo_message)

# 2: Cetaklah pesan yang menyatakan bahwa server mendukung TLS
tls_start = log_data.find("250-STARTTLS")
tls_end = log_data.find("\\r\\n", tls_start)
tls_message = log_data[tls_start:tls_end]
print("2:", tls_message)

# 3: Cetaklah pesan yang menyatakan server siap mengirim email
retcode_start = log_data.find("reply: retcode (220); Msg: b'2.0.0 SMTP server ready") 
retcode_end = log_data.find("\n", retcode_start)
retcode_message = log_data[retcode_start:retcode_end]
print("3:", retcode_message)

# 4: Cetaklah pesan yang menunjukkan username yang sudah di-hash
auth_login_start = log_data.find("send: 'AUTH LOGIN")
auth_login_end = log_data.find("\\r\\n'", auth_login_start)
auth_login_message = log_data[auth_login_start:auth_login_end]
print("4:", auth_login_message)

# 5: Cetaklah pesan balasan server dari sebuah hello message dari client
hello_start = log_data.find("reply: b'250-SG2PR03CA0119")
hello_end = log_data.find("\\r\\n", hello_start)
hello_message = log_data[hello_start:hello_end]
print("5:", hello_message)

# 6: Cetaklah pesan bahwa koneksi telah ditutup 
close_start = log_data.find("reply: retcode (221); Msg: b'")
close_end = log_data.find("\\n", close_start)
close_message = log_data[close_start:close_end]
print("6:", close_message)
