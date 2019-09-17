from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice,UserDetails
from validate_email import *
from django.core.exceptions import ValidationError
# Create your views here.

current_session_id=0;

def register(request):
    return render(request,'quiz/register.html')

def register_done(request):
    global current_session_id
    if request.method=="POST":
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['email'] and request.POST['city'] and request.POST['country']:
            print('Hello')
            user=UserDetails()
            try:
                # check if email is valid or not
                email = request.POST['email']
                try:
                    validate_email(email)
                except ValidationError as e:
                    return render(request,'quiz/register.html',{'error':'Please verify your email.'})
                user.email=email
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                if 'option1' in request.POST:
                    user.gender = "Male"
                elif 'option2' in request.POST:
                    user.gender = "Female"
                else:
                    user.gender = "Other"
                user.city = request.POST['city']
                user.country = request.POST['country']
                user.save()
                current_session_id=user.id
            except ValueError as e:
                return render(request,'quiz/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'quiz/thankyou.html')
        else:
            return render(request,'quiz/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'quiz/register.html')


def detail(request, question_id):
    # question = get_object_or_404(Question,pk=question_id)
    return HttpResponse("You are looking at a question %s" %question_id)

def sample(request):
    # return render(request,'quiz/blank.html',{'sample_id':sample_id})
    user = get_object_or_404(UserDetails,pk=current_session_id)
    user_attended_questions = user.question_attended.all()
    context = {
        'question':Question.objects.exclude(id__in=user_attended_questions).first()
    }
    helper=Question.objects.exclude(id__in=user_attended_questions).first().id
    user.question_attended.add(helper)
    return render(request, 'quiz/blank.html', context)


def select_option(request,question_id):
    return HttpResponse("You're choosing an option for your question.")
