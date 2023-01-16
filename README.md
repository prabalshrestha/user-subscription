# user-subscription
## Setup :
### Option 1 : Use Dockerfile
- Build image:
    - docker build -t [username]/[imagename] .
- Run image:
    - docker run -d -p 5000:5000 [username]/[imagename]

### Option 2 : 
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

    
