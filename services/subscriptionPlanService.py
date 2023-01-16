from models.subscriptionmodel import Subscription
from services.userService import UserService 




class SubscriptionPlanService:
    def __init__(self) -> None:
        pass
    def get_subscription_plans(self):
        return [{
            "name":"weekly",
            "price":9,
            "days":7
        },{
            "name":"monthly",
            "price":269,
            "days":7
        },{
            "name":"yearly",
            "price":3000,
            "days":7
        }]