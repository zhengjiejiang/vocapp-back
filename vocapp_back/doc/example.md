create all the command that how to interact the app
1. Register: This will let users create their account
urls:api/register
Method: POST

http --form POST http://127.0.0.1:8000/api/register   first_name="Sully"   last_name="Jiang"   email=898078550@qq.com   username="sully"   password=123
2. Login: This will login user's account
urls:api/login
Method: POST

http --form POST http://127.0.0.1:8000/api/register   username="sully"   password=123

3. Logout: This will logout user's account
urls:api/logout
Method: POST

http --form POST http://127.0.0.1:8000/api/logout
