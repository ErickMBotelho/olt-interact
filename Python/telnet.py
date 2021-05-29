import time
import telnetlib

HOST = "10.10.0.30"
login = "GEPON"
lpassword = "GEPON"
user = "EN"
upassword = "GEPON"

try:
    print(f"\033[0;34m[?] Conectando-se à {HOST}\033[0;0m")
    tn = telnetlib.Telnet(HOST)

    # LOGIN
    tn.read_until(b"Login: ")
    tn.write(login.encode("ascii") + b"\n")

    if lpassword:
        tn.read_until(b"Password: ")
        tn.write(lpassword.encode("ascii") + b"\n")

    # USER
    tn.read_until(b"User> ")
    tn.write(user.encode("ascii") + b"\n")
    
    if upassword:
        tn.read_until(b"Password: ")
        tn.write(upassword.encode("ascii") + b"\n")

    print("\033[0;32m[+] Conectado!\033[0;0m")

except ValueError:
    print("\033[0;31m[-] Falha ao conectar!\033[0;0m")

def oltInteract(command=b"?"):
    tn.write(command + b"\n")
    time.sleep(1.5)
    print(f"\033[0;32m{tn.read_very_eager().decode('ascii')}\033[0;0m")

oltInteract()
# oltInteract(b"cd gpononu")
# oltInteract(b"show cpu_using slot 3 link 15 onu 6")
# oltInteract(b"show optic_module slot 3 link 15 onu 6")
# oltInteract(b"show onu_time slot 3 link 15 onu 6")
# oltInteract(b"show wifi_serv slot 3 link 15 onu 6")
# oltInteract(b"list")
# oltInteract(b"show authorization slot all link all")
