from flask import Flask
from controllers.userController import user_blueprint
from controllers.subscriptionController import subscription_plan_blueprint
app=Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(subscription_plan_blueprint)

if __name__=='__main__':
    app.run(host='0.0.0.0')
