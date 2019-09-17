from django.db import models


#Sample Question for set 1
class QuestionForSetOneSample (models.Model):

    class Meta:
        verbose_name_plural="Question Set 1 Sample"

    def __str__(self):
        return self.question_text_for_sample_test

    question_text_for_sample_test = models.CharField(max_length=200)


#choice for sample test 1
class ChoiceForSetOneSample (models.Model):

    class Meta:
        verbose_name_plural="Choice Set 1 Sample"

    question = models.ForeignKey(QuestionForSetOneSample, on_delete=models.CASCADE, default=None, blank=True)

    sample1_A = models.ImageField(upload_to='images/')



# Question for set 1
class QuestionForSetOneReal (models.Model):

    class Meta:
        verbose_name_plural="Question Set 1"

    def __str__(self):
        return self.question_text_for_real_test

    question_text_for_real_test = models.CharField(max_length=200)


#Choice for set 1
class ChoiceForSetOneReal (models.Model):

    class Meta:
        verbose_name_plural="Choice Set 1"

    question = models.ForeignKey(QuestionForSetOneReal, on_delete=models.CASCADE, default=None, blank=True)

    sample1_A = models.ImageField(upload_to='images/')


#Sample Question for set 2
class QuestionForSetTwoSample (models.Model):

    class Meta:
        verbose_name_plural = "Sample Questions for Set 2"

    def __str__(self):
        return self.question_text_for_sample_test

    question_text_for_sample_test = models.CharField(max_length=200)


#Choice for set 2 sample
class ChoiceForSetTwoSample (models.Model):

    class Meta:
        verbose_name_plural = "Sample Choice for set 2"

    question = models.ForeignKey(QuestionForSetTwoSample, on_delete=models.CASCADE, default=None, blank=True)

    sample1_A = models.ImageField(upload_to='images/')
    sample2_A = models.ImageField(upload_to='images/')
    sample3_A = models.ImageField(upload_to='images/')
    sample4_A = models.ImageField(upload_to='images/')
    sample5_A = models.ImageField(upload_to='images/')
    sample6_A = models.ImageField(upload_to='images/')
    sample7_A = models.ImageField(upload_to='images/')
    sample8_A = models.ImageField(upload_to='images/')
    sample9_A = models.ImageField(upload_to='images/')
    sample10_A = models.ImageField(upload_to='images/')


#Question for set 2
class QuestionForSetTwoReal (models.Model):

    class Meta:
        verbose_name_plural = "Questions for set 2"

    def __str__(self):
        return self.question_text_for_real_test

    question_text_for_real_test = models.CharField(max_length=200, default=None)



#Choice for set 2
class ChoiceForSetTwo (models.Model):

    class Meta:
        verbose_name_plural = "Choice for set 2"

    question = models.ForeignKey(QuestionForSetTwoReal, on_delete=models.CASCADE, default=None, blank=True)

    sample1_A = models.ImageField(upload_to='images/')
    sample2_A = models.ImageField(upload_to='images/')
    sample3_A = models.ImageField(upload_to='images/')
    sample4_A = models.ImageField(upload_to='images/')
    sample5_A = models.ImageField(upload_to='images/')
    sample6_A = models.ImageField(upload_to='images/')
    sample7_A = models.ImageField(upload_to='images/')
    sample8_A = models.ImageField(upload_to='images/')
    sample9_A = models.ImageField(upload_to='images/')
    sample10_A = models.ImageField(upload_to='images/')


#User Details for Registeration
class UserDetails(models.Model):

    class Meta:
        verbose_name_plural = "User Details"

    question_attended_set_one_sample = models.ManyToManyField(QuestionForSetOneSample)
    question_attended_set_one_real = models.ManyToManyField(QuestionForSetOneReal)
    question_attended_set_two_sample = models.ManyToManyField(QuestionForSetTwoSample)
    question_attended_set_two_real = models.ManyToManyField(QuestionForSetTwoReal)

    first_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    email = models.EmailField()
    gender = models.CharField(max_length=10,blank=True,null=True,default=None)
    city = models.CharField(max_length=100,blank=True,null=True,default=None)
    country = models.CharField(max_length=100,blank=True,null=True,default=None)

    def __str__(self):
        return self.first_name+' '+self.last_name

class UserResponsesForSetOne (models.Model): #Saving only the responses of the real set

    class Meta:
        verbose_name_plural = "User Responses Set 1"

    choice = models.CharField(max_length=10, blank=True, null=True, default=None)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    choice_corr = models.ForeignKey(QuestionForSetOneReal, on_delete=models.CASCADE, default=None, blank=True)

class UserResponsesForSetTwo (models.Model):  #Saving only the responses of the real set

    class Meta:
        verbose_name_plural = "User Responses Set 2"

    choice_1 = models.BooleanField(default=False, verbose_name='sample1_A')
    choice_2 = models.BooleanField(default=False, verbose_name='sample2_A')
    choice_3 = models.BooleanField(default=False, verbose_name='sample3_A')
    choice_4 = models.BooleanField(default=False, verbose_name='sample4_A')
    choice_5 = models.BooleanField(default=False, verbose_name='sample5_A')
    choice_6 = models.BooleanField(default=False, verbose_name='sample6_A')
    choice_7 = models.BooleanField(default=False, verbose_name='sample7_A')
    choice_8 = models.BooleanField(default=False, verbose_name='sample8_A')
    choice_9 = models.BooleanField(default=False, verbose_name='sample9_A')
    choice_10 = models.BooleanField(default=False, verbose_name='sample10_A')
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    choice_corr = models.ForeignKey(QuestionForSetTwoReal, on_delete=models.CASCADE, default=None, blank=True)


class QuestionFeaturesSetOneSample (models.Model):

    class Meta:
        verbose_name_plural="Feature Question Set 1 Sample"

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)


class ChoiceFeaturesSetOneSample (models.Model):

    class Meta:
        verbose_name_plural="Feature Choice Set 1 Sample"


    question_rel = models.ForeignKey(QuestionFeaturesSetOneSample, on_delete=models.CASCADE, default=None, blank=True)
    feature1_A = models.ImageField(upload_to='images/')
    feature2_A = models.ImageField(upload_to='images/')
    feature1_B = models.ImageField(upload_to='images/')
    feature2_B = models.ImageField(upload_to='images/')
    feature1_C = models.ImageField(upload_to='images/')
    feature2_C = models.ImageField(upload_to='images/')
    feature1_D = models.ImageField(upload_to='images/')
    feature2_D = models.ImageField(upload_to='images/')
    feature1_E = models.ImageField(upload_to='images/')
    feature2_E = models.ImageField(upload_to='images/')


class QuestionFeaturesSetTwoSample (models.Model):

    class Meta:
        verbose_name_plural = "Sample Feature Questions for set 2"

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=100)


class ChoiceFeaturesForSetTwoSample (models.Model):

    class Meta:
        verbose_name_plural = "Feature Choice for Set 2 Sample"

    question_rel = models.ForeignKey(QuestionFeaturesSetTwoSample, on_delete=models.CASCADE, default=None, blank=True)
    feature1_A = models.ImageField(upload_to='images/')
    feature2_A = models.ImageField(upload_to='images/')
    feature1_B = models.ImageField(upload_to='images/')
    feature2_B = models.ImageField(upload_to='images/')
    feature1_C = models.ImageField(upload_to='images/')
    feature2_C = models.ImageField(upload_to='images/')
    feature1_D = models.ImageField(upload_to='images/')
    feature2_D = models.ImageField(upload_to='images/')
    feature1_E = models.ImageField(upload_to='images/')
    feature2_E = models.ImageField(upload_to='images/')


class QuestionFeaturesSetOne (models.Model):

    class Meta:
        verbose_name_plural="Feature Question Set 1"

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)


class ChoiceFeaturesForSetOne (models.Model):

    class Meta:
        verbose_name_plural="Feature Choice Set 1"

    question_rel = models.ForeignKey(QuestionFeaturesSetOne, on_delete=models.CASCADE, default=None, blank=True)
    feature1_A = models.ImageField(upload_to='images/')
    feature2_A = models.ImageField(upload_to='images/')
    feature1_B = models.ImageField(upload_to='images/')
    feature2_B = models.ImageField(upload_to='images/')
    feature1_C = models.ImageField(upload_to='images/')
    feature2_C = models.ImageField(upload_to='images/')
    feature1_D = models.ImageField(upload_to='images/')
    feature2_D = models.ImageField(upload_to='images/')
    feature1_E = models.ImageField(upload_to='images/')
    feature2_E = models.ImageField(upload_to='images/')


class QuestionFeaturesSetTwo (models.Model):

    class Meta:
        verbose_name_plural = "Feature Questions for set 2"

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=100)


class ChoiceFeaturesForSetTwo (models.Model):

    class Meta:
        verbose_name_plural = "Feature Choice for set 2"

    question_rel = models.ForeignKey(QuestionFeaturesSetTwo, on_delete=models.CASCADE, default=None, blank=True)
    feature1_A = models.ImageField(upload_to='images/')
    feature2_A = models.ImageField(upload_to='images/')
    feature1_B = models.ImageField(upload_to='images/')
    feature2_B = models.ImageField(upload_to='images/')
    feature1_C = models.ImageField(upload_to='images/')
    feature2_C = models.ImageField(upload_to='images/')
    feature1_D = models.ImageField(upload_to='images/')
    feature2_D = models.ImageField(upload_to='images/')
    feature1_E = models.ImageField(upload_to='images/')
    feature2_E = models.ImageField(upload_to='images/')


class UserResponsesForFeaturesSetOne (models.Model):

    class Meta:
        verbose_name_plural = "User Responses for features of Set 1"

    choice_1 = models.BooleanField(default=False, verbose_name='Feature_1')
    choice_2 = models.BooleanField(default=False, verbose_name='Feature_2')
    choice_3 = models.BooleanField(default=False, verbose_name='Feature_3')
    choice_4 = models.BooleanField(default=False, verbose_name='Feature_4')
    choice_5 = models.BooleanField(default=False, verbose_name='Feature_5')
    # choice_6 = models.BooleanField(default=True, verbose_name='None of the above')
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    choice_corr = models.ForeignKey(QuestionFeaturesSetOne, on_delete=models.CASCADE, default=None, blank=True)


class UserResponsesForFeaturesSetTwo (models.Model):

    class Meta:
        verbose_name_plural = "User Responses for features of Set 2"

    choice_1 = models.BooleanField(default=False, verbose_name='Feature_1')
    choice_2 = models.BooleanField(default=False, verbose_name='Feature_2')
    choice_3 = models.BooleanField(default=False, verbose_name='Feature_3')
    choice_4 = models.BooleanField(default=False, verbose_name='Feature_4')
    choice_5 = models.BooleanField(default=False, verbose_name='Feature_5')
    # choice_6 = models.BooleanField(default=False, verbose_name='None of the above')

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    choice_corr = models.ForeignKey(QuestionFeaturesSetTwo, on_delete=models.CASCADE, default=None, blank=True)