from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField




# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.user', verbose_name="Author",related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    publishing_date = models.DateTimeField(verbose_name='Publishing date',auto_now_add=True)
    image = models.ImageField(blank=True,null=True)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id':self.id})



    def get_create_url(self):
            return reverse('post:create', kwargs={'id':self.id})



    def get_update_url(self):
            return reverse('post:update', kwargs={'id':self.id})


    def get_delete_url(self):
            return reverse('post:delete', kwargs={'id':self.id})



    


    class Meta:
        ordering = ['-publishing_date', 'id']




class Comments(models.Model):
    post = models.ForeignKey("post.Post", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='name')
    content = models.TextField(verbose_name='comment')
    created_time = models.DateTimeField(auto_now_add=True)