class User:
    def __init__(self, first_name, last_name, email, id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


marius = User("Marius", "Iordan", "marius@mail.com", "001")
vlad = User("Vlad", "Vieriu", "vlad@mail.com", "002")
sica = User("Marius", "Panait", "sica@mail.com", "003")

marius.follow(sica)
marius.follow(marius)
vlad.follow(sica)
sica.follow(marius)
sica.follow(vlad)
marius.follow(sica)

print(sica.followers)
print(marius.followers)
print(vlad.followers)




