from random import randint

class Device():
    local_key = None
    remote_key = None

    def generate_key(self):
        self.local_key = randint(129, 255)

    def get_remote_key(self, remote_key):
        self.remote_key = int(remote_key / 100)

    def sent_local_key(self):
        return self.local_key * 100

class Client(Device):
    pass

class Server(Device):
    pass


def man_in_the_middle(x):
    print(x)


client = Client()
server = Server()

client.generate_key()
server.generate_key()

print(client.local_key)
print(server.local_key)

key1 = server.sent_local_key()
key2 = client.sent_local_key()
man_in_the_middle(key1)
man_in_the_middle(key2)
client.get_remote_key(key1) #client.remote_key = server.local_key
server.get_remote_key(key2) #server.remote_key = client.local_key

print(client.local_key)
print(server.local_key)