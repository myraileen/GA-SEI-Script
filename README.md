# Django Project: Chapter & Verse

## Project links
* [Repository](https://github.com/myraileen/GA-SEI-Script)
* [Heroku Deployment](http://mychapterapp.herokuapp.com)
* [REST-api implementation of master branch models](https://github.com/myraileen/GA-SEI-Script/tree/django_rest_api)

## Overview
This project overlays a user interface built using Python, Django and Postsql datbase with full CRUD on book chapter and verse models. The non-user data models this project demonstrates is "Chapter" and "Verse". 

#### MVP requirements:

   * Two non-user models: this project implements `Chapter` and `Verse` models with full CRUD on each for MVP. A third `Book` model was implemented.  
   * Full CRUD available on each model.  
   * Django built-in authentication requires sign-up/login.  

#### Stretch requirements:
   * Implemented social authorization from Github account using the social-auth-app-django library.
   * Deployed master repository branch using Heroku. _(I tried deploying with AWS: I was able to create the Postgres database with Amazon RDS, but was not able to connect to do the makemigrations)._
   * Created code branch 'django_rest_api' that renders and represents the models as a REST api service. (Will seek more learning here to use in project 4!)

---

### Models
#### Chapter
| Fields | type | FK relationship |
| --- | :---: | :---: |
| book   | text | on `Book` |
| chapter_num | int |   |
| chapter | text |  |
| description | text |    |
| image_url | text|    |

### Verse
| Fields | type | FK relationship |
| --- | :---: | :---: |
| chapter   | text | on `Chapter` |
| verse_num | int |   |
| verse | text |  |
| image_url | text|    |

### Book (post-MVP)
| Fields | type | FK relationship |
| --- | :---: | :---: |
| version   | text |  |
| book_num | int |   |
| book | text |  |
| description | text |    |
| image_url | text|    |

### Unsolved Stretch Features/Stories
I'd like to leverage python more (my knowledge is too high level at this point) to do the following: 
* Use the django json module to create a database seed migration file from reading json input converted to a python dictionary that can be passed into the postgres db.
* Get data from the 'current page' to pass into the view as variables (for example, after creating a verse, I'd rather send user to the chapter detail page with the chapter pk instead of redirecting user to the verse detail with the newly created verse id. Another example would be 'forward' and 'backward' buttons on the chapter and verse detail views... I'd like feedback here on approaches to research to do this?)
* I'd like to put a better user prompt for user to to confirm delete (especially parent model with cascading child deletes)... as a alternative to capturing confirmation in a django form, I added inline code to confirm (which I understand is not preferred approach).


### Credits/References 
* GA-SEI Lessons
* heroku deployment instructions from https://www.youtube.com/watch?v=6DI_7Zja8Zc
* Social Authorization reference: https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html 
* hiding keys/environment variables using dotenv: https://github.com/theskumar/python-dotenv