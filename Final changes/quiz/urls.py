from django.urls import path
from django.conf.urls import include,url
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("registered/", views.register_done, name='register_done'),
    path("terms/", views.terms, name='terms'),
    path('sampleSetOne/',views.next_sample_question_set_one, name='next_sample_question_set_one'),
    path('startOfSetOne/',views.save_responses_set_one, name='save_responses_set_one'),
    path('startOfSetOneIndication/',views.start_of_real_test_set_one, name='start_of_real_test_set_one'),
    path('startOfSetOneFeatures/',views.save_responses_set_one_features, name='save_responses_set_one_features'),
    path('distractor/',views.distractor,name='distractor'),
    path('startOfSetTwo/',views.start_of_set_two,name='start_of_set_two'),
    path('sampleSetTwo/', views.next_sample_question_set_two, name='next_sample_question_set_two'),
    path('startOfSetTwoIndication/',views.start_of_real_test_set_two, name='start_of_real_test_set_two'),
    path('startofSetTwo',views.save_responses_set_two, name="save_responses_set_two"),
    path('startOfSetTwoFeatures/',views.save_responses_set_two_features,name="save_responses_set_two_features"),
]