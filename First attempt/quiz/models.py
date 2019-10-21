from django.db import models

# Create your models here.
class Question (models.Model):

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=100)

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,blank=True,null=True,default=None)

    #Category A
    sample1_A=models.ImageField(upload_to='images/')
    sample2_A = models.ImageField(upload_to='images/')
    sample3_A = models.ImageField(upload_to='images/')
    sample4_A = models.ImageField(upload_to='images/')
    sample5_A = models.ImageField(upload_to='images/')

    #Category B
    sample1_B = models.ImageField(upload_to='images/')
    sample2_B = models.ImageField(upload_to='images/')
    sample3_B = models.ImageField(upload_to='images/')
    sample4_B = models.ImageField(upload_to='images/')
    sample5_B = models.ImageField(upload_to='images/')


class UserDetails(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,blank=True,null=True,default=None)
    question_attended=models.ManyToManyField(Question)

    first_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    email = models.EmailField()
    gender = models.CharField(max_length=10,blank=True,null=True,default=None)
    city = models.CharField(max_length=100,blank=True,null=True,default=None)
    country = models.CharField(max_length=100,blank=True,null=True,default=None)

    def __str__(self):
        return self.first_name+' '+self.last_name