from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    blog_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return "{0}/{1}".format(self.blog_type, self.title)