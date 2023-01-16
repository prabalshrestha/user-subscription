from models.usermodel import User
from models.subscriptionmodel import Subscription

default_user=User(1,"default_user","default_user@gmail.com","password")
user_list=[default_user]
class UserService:
    def __init__(self) -> None:
        pass
    def add_user(self,user):
        user['id']=len(user_list)+1
        user=User(**user)
        user_list.append(user)
        return user
    def get_user_by_id(self,id):
        matched_users=[user for user in user_list if user.id==id]
        print("matched_users",matched_users)
        if matched_users:
            user=matched_users[0]
            if user.subscriptions:
                user.subscriptions=[subs.__dict__ for subs in user.subscriptions]
            return user
        return None
    def get_all_users(self):
        if user_list:
            for user in user_list:
                if user.subscriptions:
                    user.subscriptions=[subs.__dict__ for subs in user.subscriptions]
            return user_list
        return None
    def subscribe(self, user_id: int, plan: str) -> Subscription:
        user=self.get_user_by_id(user_id)
        if user.is_subscribed():
            return user.resubscribe(plan)
        else:
            return user.subscribe(plan)

