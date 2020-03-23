from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200,null = False)
    question_img = models.ImageField(default = 'polls.png',upload_to = 'polls_images')
    pub_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200,null = False)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text
    
class Comment(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    comment_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length = 100);
    
    def __str__(self):
        return f'{self.author}\'s comment'