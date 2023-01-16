import datetime

class Subscription:
    def __init__(self, user_id: int, plan: str, start_date: datetime.datetime):
        self.user_id = user_id
        self.plan = plan
        self.start_date = start_date
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self) -> datetime.datetime:
        if self.plan == "weekly":
            return self.start_date + datetime.timedelta(days=7)
        elif self.plan == "monthly":
            return self.start_date + datetime.timedelta(days=30)
        elif self.plan == "yearly":
            return self.start_date + datetime.timedelta(days=365)
        else:
            raise ValueError("Invalid subscription plan")

    def resubscribe(self, plan: str) -> None:
        if self.end_date < datetime.datetime.now():
            self.plan = plan
            self.start_date = datetime.datetime.now()
            self.end_date = self.calculate_end_date()
        else:
            self.plan = plan
            self.start_date = self.end_date
            self.end_date = self.calculate_end_date()

    def tojson(self):
        return{
            "user_id" : self.user_id,
            "plan" : self.plan,
            "start_date" : self.start_date,
            "end_date" : self.calculate_end_date()
        }