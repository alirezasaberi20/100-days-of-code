class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0
        self.following = 0




    def follow(self,user):
        self.following +=1
        user.follower +=1

user1 = User("001","Alireza")
user2 = User("002","John")
user3 = User("003","anna")
user1.follow(user2)
user3.follow(user2)
user3.follow(user1)
user2.follow(user3)


print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
