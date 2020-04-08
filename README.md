# Django Project: Chapter & Verse

## Project links
* [Repository](https://github.com/myraileen/GA-SEI-Script)

## Overview
This project overlays a user interface built using Python, Django and Postsql datbase with full CRUD on book chapter and verse models. The non-user data models this project demonstrates is "Chapter" and "Verse". 

To meet the 2 non-user model requirement, this project implements `Chapter` and `Verse` models with full CRUD on each for MVP. (There is a `Book` model for post-MVP time-permitting).

User authentication as learned in class is also implemented in this project.

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