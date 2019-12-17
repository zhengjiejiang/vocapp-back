<!-- Vocapp -->

## Get Index page
Exhibit the Orignal page for you

* **URL**

  ``/``

* **Method**

  ``Get``

* **URL Params**

  None

* **Data Params**

  None

* **Sample Call**

  ```bash
  http://127.0.0.1:9000/
  ```


## Register
Submit registration details into our system to automatically create a *user* account. System return the *user* details and authentication *token*.

Created *user* accounts are automatically granted access to the system even though these accounts have not had their email verified. The system sends a verification email after creation and if the *user* does not verify in the allotted timespan, their account gets locked.

It's important to note that emails must be unique and passwords strong or else validation errors get returned.

* **URL**

  ``/api/register``


* **Method**

  ``POST``


* **URL Params**

  None

* **Data Params**

  * email
  * password
  * first_name
  * last_name


* **Success Response**

  * **Code:** 200
  * **Content:**

    ```json
    {
        "email": "898078550@qq.com",
        "username" :"sully",
        "first_name": "Sully",
        "last_name": "Jiang",
        "password" : "123",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDkyOTY1MDAsInVzZXJfaWQiOjF9.QN9dyWL2dlxKgkm0xbQAmnaI6_4amHcSfqUGQ6pZbxM",
        "user_id": 1
    }
    ```


* **Error Response**

  * **Code:** 400
  * **Content:**

    ```json
    {
        "error": "Email is not unique.",
        "status": "Invalid request,please try it again."
    }
    ```


* **Sample Call**

  ```bash
  $ http post 127.0.0.1:8080/api/register \
    username= sully\
    password=123 \
    first_name=Zhengjie \
    last_name=Jiang
  ```


## Login
Returns the *user profile* and authentication *token* upon successful login in.

* **URL**

  ``/api/login``


* **Method**

  ``POST``


* **URL Params**

  None


* **Data Params**

  * email
  * password


* **Success Response**

  * **Code:** 200
  * **Content:**

    ```json
    {
        "email": "898078550@qq.com",
        "first_name": "Sully",
        "last_name": "Jiang",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDkyOTg1MDYsInVzZXJfaWQiOjF9.HrwHvfL4-1pMe7EcXEzlsxciFgK0xf2uC8BV1kfLT_c",
        "user_id": 1
    }
    ```


* **Error Response**

  * **Code:** 400
  * **Content:**

    ```json
    {
        "error": "Email or password is incorrect.",
        "status": "Invalid request."
    }
    ```


* **Sample Call**

  ```bash
  $ http post 127.0.0.1:8000/api/login \
    username=sully \
    password=123
  ```








  ## Logout
  Returns the *user profile* and authentication *token* upon successful login in.

  * **URL**

    ``/api/logout``


  * **Method**

    ``POST``


  * **Sample Call**

  http --form POST http://127.0.0.1:8000/api/logout
