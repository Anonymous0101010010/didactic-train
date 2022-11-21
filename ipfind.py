import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

print("you are on " +hostname)
print("your ip is " + myip)

url = "google.com"
print("the ip is " + url + " from ",socket.gethostbyname(url))
