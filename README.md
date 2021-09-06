# **Impact**

## Full Stack Application

### An app to share stories that have impacted us the most.

**Working Demo [Live Link](http://impact-v2.herokuapp.com/)**

## Front-End Technologies Used

- HTML
- CSS
- BOOTSTRAP4
- JQuery
- JavaScript
- Jinja Templates

## Back-End Technologies Used

- Flask
- Python
- SQLite
- SQLAlchemy (ORM)
- Anaconda Virtual Enviroment
- WTForms
- FlaskForm

# Features

## **User Authentication**

- Users can create an account
- Users can login to there account
- Users can logut of the account
- Users can access and update there account
- Users can create and edit post

| User Model   |             |
| ------------ | ----------- |
| id           | Primary Key |
| profileImage | String      |
| email        | String      |
| username     | String      |
| password     | String      |
| posts        | String      |

## **Blog Posts**

- Posts can be created
- Posts can be updated
- Posts can be deleted

| Post Model |             |
| ---------- | ----------- |
| id         | Primary Key |
| userId     | String      |
| date       | String      |
| title      | String      |
| text       | String      |
