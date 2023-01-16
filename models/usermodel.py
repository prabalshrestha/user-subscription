from dataclasses import dataclass, field
from typing import List
from models.subscriptionmodel import Subscription
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    subscriptions: List[Subscription] = field(default_factory=list)

    def subscribe(self,  plan: str) -> Subscription:
        new_subscription = Subscription(user_id=self.id, plan=plan, start_date=datetime.now())
        self.subscriptions.append(new_subscription)
        return new_subscription.tojson()
    
    def is_subscribed(self)-> bool:
        subscription = next((sub for sub in self.subscriptions ), None)
        print(subscription)
        if subscription: 
            if subscription.end_date > datetime.now():
                return True
            else:
                self.subscriptions.remove(subscription)
                return False
        else: 
            return False

    def resubscribe(self,  plan: str) -> Subscription:
        subscription = next((sub for sub in self.subscriptions ), None)
        if subscription:
            subscription.resubscribe(plan)
            return subscription.tojson()
        return None