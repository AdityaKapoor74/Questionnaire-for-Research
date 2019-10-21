from django.contrib import admin
from .models import *
# Register your models here.

#User Details
admin.site.register(UserDetails)

#Set One
admin.site.register(QuestionForSetOneSample)
admin.site.register(ChoiceForSetOneSample)
admin.site.register(QuestionForSetOneReal)
admin.site.register(ChoiceForSetOneReal)
admin.site.register(QuestionFeaturesSetOneSample)
admin.site.register(ChoiceFeaturesSetOneSample)
admin.site.register(QuestionFeaturesSetOne)
admin.site.register(ChoiceFeaturesForSetOne)
admin.site.register(UserResponsesForSetOne)
admin.site.register(UserResponsesForFeaturesSetOne)

#Set Two
admin.site.register(QuestionForSetTwoSample)
admin.site.register(ChoiceForSetTwoSample)
admin.site.register(QuestionFeaturesSetTwoSample)
admin.site.register(ChoiceFeaturesForSetTwoSample)
admin.site.register(QuestionForSetTwoReal)
admin.site.register(ChoiceForSetTwo)
admin.site.register(QuestionFeaturesSetTwo)
admin.site.register(ChoiceFeaturesForSetTwo)
admin.site.register(UserResponsesForSetTwo)
admin.site.register(UserResponsesForFeaturesSetTwo)