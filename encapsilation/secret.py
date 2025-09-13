class SecretKeeper:
    def __init__(self, secret):
        self.__secret = secret
        self.creation_msg = "Secret Message Created"

    def get_secret(self):
        return self.__secret
    
    def reveal_creation_msg(self):
        print(self.creation_msg)

my_secret = SecretKeeper("I love python")
print("The secret is:", my_secret.get_secret())
my_secret.reveal_creation_msg()
