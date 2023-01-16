# user-subscription
## Steps:
- Create virtual env [Optional]: 
    - python3 -m venv env
    - source env/bin/activate
- Install dependencies :
    - pip3 install -r requirements.txt
- Run :
    - python3 app.py



## APIs
### Base url: http://localhost:5000
    GET:  /plans 
    GET:  /users
    GET:  /user/<user_id>
    POST: /user
        Requestbody:
        {
                "name":"name",
                "email":"email@gmail.com",
                "password":"password"
        }
    PUT: /user/<int:user_id>/subscribe
        Requestbody:
        {
                "plan":"plan name form GET:/plans",
        }

    
