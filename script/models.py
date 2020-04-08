from django.db import models

# Book
class Book(models.Model):
    version = models.TextField()
    book_num = models.PositiveSmallIntegerField()
    book = models.CharField(max_length = 200)
    description = models.TextField()
    image_url = models.TextField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQSn_PGAQyYvtHTjh61RcvlKIgtFDM2e0IWg8bRMUvS1Bo0_kY5&usqp=CAU')

    def __str__(self):
        return self.book

# Chapter
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    chapter_num = models.PositiveSmallIntegerField()
    chapter = models.TextField()
    description = models.TextField()
    image_url = models.TextField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT77EfsaCllx-L584gO4MMywRWSr9VyPJxYJhveXHYCppsPNgLP&usqp=CAU')

    def __str__(self):
        return self.chapter

# Verse
class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='verses')
    verse_num = models.PositiveSmallIntegerField()
    verse = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.verse
