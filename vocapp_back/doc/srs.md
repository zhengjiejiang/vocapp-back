VocApp - Software Requirements Specification (SRS)
A webapp which can help improve your vocabulary.
Use Cases:
1. Register
- Developers note: Please use "token authentication".
- Code:
     URL: /api/register
     METHOD: POST
     FIELDS:
         - username
         - first name
         - last name
         - email
         - password
         - (OPTIONAL) password (repeated)
2. Login
- Code:
    - URL: /api/login
    - METHOD: POST
    - FIELDS:
        - username
        - password
3. Dashboard
- Disply the daily sentence, improve new words, review the vocabulary.
- The ability to add / delete / list new words.
- Code:
    (1)
    URL: /api/learn
    METHOD: POST
    FIELDS:
        - word
        - definition
    (2)
    URL: /api/vocabulary
    METHOD: GET
    FIELDS:
        - List
            - Pagination
            - FIELDS:
                - word
                - definition
    (3)
    URL: /api/vocabulary/<id>
    METHOD: DELETE
    FIELDS:
        - NONE
    (4)
    URL: /api/daily-sentence
    METHOD: GET
    FIELD:
        - Dictionary
        - FIELDS:
            - sentence
            - explanation
    (5)
     URL: /api/daily-word
     METHOD: GET
     FIELD:
         - Dictionary
         - FIELDS:
             - word
             - definition
4. Logout
- Code:
    URL: /api/logout
    METHOD: POST
    FIELD:
        - NONE
5. (OPTIONAL) Profile Page
The user can see and change their profile information
    (1)
    URL: /api/profile
    METHOD: GET
    FIELDS:
        - username
        - first name
        - last name
        - email
    Returns the profile information of the authenticated user
    (2)
    URL: /api/profile
    METHOD: PUT
    FIELDS:
        - username
        - first name
        - last name
        - email
6. (OPTIONAL) Change Password
- You need to be logged in to use this API!
- You need to know the orginal password!
- CODE:
    URL: /api/change-password
    METHOD: PUT
    FIELDS:
        - password
        - password (repeated)
