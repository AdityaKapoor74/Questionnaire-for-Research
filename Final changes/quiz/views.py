from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from validate_email import *
from django.core.exceptions import ValidationError
import random
# Create your views here.


def register(request):
    return render(request,'quiz/register.html')

def register_done(request):

    if request.method=="POST":
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['email'] and request.POST['city'] and request.POST['country']:
            # print('Hello')
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

                option = request.POST.get("option",None)
                if option in ["Male","Female","Other"]:
                    if option=="Male":
                        user.gender="Male"
                    elif option=="Female":
                        user.gender="Female"
                    else:
                        user.gender="Other"
                user.city = request.POST['city']
                user.country = request.POST['country']

                if 'terms' not in request.POST:
                    return render(request, 'quiz/register.html', {'error': 'Please accept the terms and conditions.'})

                user.save()
                request.session['user_id'] = user.id
            except ValueError as e:
                return render(request,'quiz/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'quiz/instructions.html')
        else:
            return render(request,'quiz/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'quiz/register.html')


def next_sample_question_set_one(request):

    if request.method == "POST":
        try:
            option = request.POST.get("category",None)
            if option not in ['A','B']:
                return render(request, 'quiz/sample_question_set_1.html', {'error': 'Please select an option.'})
        except ValueError as e:
            return render(request,'quiz/sample_question_set_1.html',{'error':'Please select either one of the categories.Go back to do so.'})


    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    user_attended_questions = user.question_attended_set_one_sample.all()

    if(QuestionForSetOneSample.objects.exclude(id__in=user_attended_questions).first()==None):
        question_features = QuestionFeaturesSetOneSample.objects.first()
        qid = QuestionFeaturesSetOneSample.objects.first().id
        choice_features = ChoiceFeaturesSetOneSample.objects.select_related().filter(question_rel=qid)

        context = {
            'question': question_features,
            'options': choice_features
        }
        return render(request,'quiz/sample_features_of_set_1.html',context)

    helper = QuestionForSetOneSample.objects.exclude(id__in=user_attended_questions).first().id

    context = {
        'question':QuestionForSetOneSample.objects.exclude(id__in=user_attended_questions).first(),
        'options':ChoiceForSetOneSample.objects.select_related().filter(question=helper)
    }
    request.session['question_id']=helper
    helper=QuestionForSetOneSample.objects.exclude(id__in=user_attended_questions).first().id
    user.question_attended_set_one_sample.add(helper)

    return render(request, 'quiz/sample_question_set_1.html',context)


def next_sample_question_set_two(request):
    if request.method == "POST":
        try:
            sample = request.POST.get("sample", None)
            if sample not in ['sample1', 'sample2','sample3','sample4','sample5','sample6','sample7','sample8','sample9','sample10']:
                return render(request,'quiz/sample_question_set_2.html',{'error':'Please select an option.'})
        except ValueError as e:
            return render(request,'quiz/sample_question_set_2.html',{'error':'Please select one of the options.'})


    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    user_attended_questions = user.question_attended_set_two_sample.all()

    if(QuestionForSetTwoSample.objects.exclude(id__in=user_attended_questions).first()==None):
        question_features = QuestionFeaturesSetTwoSample.objects.first()
        qid = QuestionFeaturesSetTwoSample.objects.first().id
        choice_features = ChoiceFeaturesForSetTwoSample.objects.select_related().filter(question_rel=qid)

        context = {
            'question': question_features,
            'options': choice_features
        }
        return render(request,'quiz/sample_features_of_set_2.html',context)

    helper = QuestionForSetTwoSample.objects.exclude(id__in=user_attended_questions).first().id

    context = {
        'question':QuestionForSetTwoSample.objects.exclude(id__in=user_attended_questions).first(),
        'options':ChoiceForSetTwoSample.objects.select_related().filter(question=helper)
    }
    request.session['question_id']=helper
    helper=QuestionForSetTwoSample.objects.exclude(id__in=user_attended_questions).first().id
    user.question_attended_set_two_sample.add(helper)

    return render(request, 'quiz/sample_question_set_2.html',context)



def save_responses_set_one(request):

    if request.method == "POST":
        user_response = UserResponsesForSetOne()
        try:
            option = request.POST.get("category",None)
            if option in ['A','B']:
                if option=='A':
                    print("I am here")
                    user_response.choice = 'A'
                elif option=='B':
                    user_response.choice = 'B'
            else:
                return render(request,'quiz/real_question_set_1.html',{'error':'Please select an option.'})
            uid = request.session['user_id']
            user_response.user_id = UserDetails.objects.get(pk=uid)
            qid=request.session['question_id']
            user_response.choice_corr = QuestionForSetOneReal.objects.get(pk=qid)
            user_response.save()


        except ValueError as e:
            return render(request,'quiz/real_question_set_1.html',{'error':'Please select either one of the categories.Go back to do so.'})


    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    user_attended_questions = user.question_attended_set_one_real.all()
    helper = list(QuestionForSetOneReal.objects.exclude(id__in=user_attended_questions))
    if len(helper)==0:
        question_features = QuestionFeaturesSetOne.objects.first()
        qid = QuestionFeaturesSetOne.objects.first().id
        choice_features = ChoiceFeaturesForSetOne.objects.select_related().filter(question_rel=qid)

        context = {
            'question':question_features,
            'options': choice_features
        }
        return render(request,'quiz/features_of_set_1.html',context)
    random.shuffle(helper)
    helper = helper[0].id


    context = {
        'question':QuestionForSetOneReal.objects.get(pk=helper),
        'options':ChoiceForSetOneReal.objects.select_related().filter(question=helper)
    }
    request.session['question_id']=helper
    helper=QuestionForSetOneReal.objects.get(pk=helper)
    user.question_attended_set_one_real.add(helper)

    return render(request, 'quiz/real_question_set_1.html',context)


def save_responses_set_two(request):

    if request.method == "POST":
        user_response = UserResponsesForSetTwo()
        try:
            sample = request.POST.get("sample", None)
            if sample not in ['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7', 'sample8','sample9', 'sample10']:
                return render(request, 'quiz/real_question_set_2.html', {'error': 'Please select an option.'})
            else:
                if 'sample1' in request.POST:
                    user_response.choice_1 = True
                else:
                    user_response.choice_1 = False
                if 'sample2' in request.POST:
                    user_response.choice_2 = True
                else:
                    user_response.choice_2 = False
                if 'sample3' in request.POST:
                    user_response.choice_3 = True
                else:
                    user_response.choice_3 = False
                if 'sample4' in request.POST:
                    user_response.choice_4 = True
                else:
                    user_response.choice_4 = False
                if 'sample5' in request.POST:
                    user_response.choice_5 = True
                else:
                    user_response.choice_5 = False
                if 'sample6' in request.POST:
                    user_response.choice_6 = True
                else:
                    user_response.choice_6 = False
                if 'sample7' in request.POST:
                    user_response.choice_7 = True
                else:
                    user_response.choice_7 = False
                if 'sample8' in request.POST:
                    user_response.choice_8 = True
                else:
                    user_response.choice_8 = False
                if 'sample9' in request.POST:
                    user_response.choice_9 = True
                else:
                    user_response.choice_9 = False
                if 'sample10' in request.POST:
                    user_response.choice_10 = True
                else:
                    user_response.choice_10 = False
                uid = request.session['user_id']
                user_response.user_id = UserDetails.objects.get(pk=uid)
                qid=request.session['question_id']
                user_response.choice_corr = QuestionForSetTwoReal.objects.get(pk=qid)
                user_response.save()

        except ValueError as e:
            return render(request,'quiz/real_question_set_2.html',{'error':'Please select one of the options.'})


    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    user_attended_questions = user.question_attended_set_two_real.all()
    helper = list(QuestionForSetTwoReal.objects.exclude(id__in=user_attended_questions))
    if len(helper)==0:
        question_features = QuestionFeaturesSetTwo.objects.first()
        qid = QuestionFeaturesSetTwo.objects.first().id
        choice_features = ChoiceFeaturesForSetTwo.objects.select_related().filter(question_rel=qid)

        context = {
            'question':question_features,
            'options': choice_features
        }
        return render(request,'quiz/features_of_set_2.html',context)
    random.shuffle(helper)
    helper = helper[0].id


    context = {
        'question':QuestionForSetTwoReal.objects.get(pk=helper),
        'options':ChoiceForSetTwo.objects.select_related().filter(question=helper)
    }
    request.session['question_id']=helper
    helper=QuestionForSetTwoReal.objects.get(pk=helper)
    user.question_attended_set_two_real.add(helper)

    return render(request, 'quiz/real_question_set_2.html',context)


def save_responses_set_one_features(request):
    if request.method=="POST":
        try:
            feature = request.POST.get("feature", None)
            if feature in ["feature1", "feature2", "feature3", "feature4", "feature5", "feature6"]:
                user_response = UserResponsesForFeaturesSetOne()
                if 'feature1' in request.POST:
                    user_response.choice_1 = True
                    user_response.choice_6 = False
                if 'feature2' in request.POST:
                    user_response.choice_2 = True
                    user_response.choice_6 = False
                if 'feature3' in request.POST:
                    user_response.choice_3 = True
                    user_response.choice_6 = False
                if 'feature4' in request.POST:
                    user_response.choice_4 = True
                    user_response.choice_6 = False
                if 'feature5' in request.POST:
                    user_response.choice_5 = True
                    user_response.choice_6 = False
                uid = request.session['user_id']
                user_response.user_id = UserDetails.objects.get(pk=uid)
                user_response.choice_corr = QuestionFeaturesSetOne.objects.first()
                user_response.save()

            else:
                return render(request, 'quiz/features_of_set_1.html', {'error': 'Please select atleast one option from the following'})

        except ValueError as e:
            return render(request,'quiz/features_of_set_1.html',{'error':'Please select atleast one option from the following'})



    return render(request,'quiz/distractor.html')


def save_responses_set_two_features(request):
    if request.method=="POST":
        try:
            feature = request.POST.get("feature", None)
            if feature not in ["feature1", "feature2", "feature3", "feature4", "feature5", "feature6"]:
                return render(request, 'quiz/features_of_set_2.html',{'error': 'Please select atleast one option from the following'})
            else:
                user_response = UserResponsesForFeaturesSetTwo()
                if 'feature1' in request.POST:
                    user_response.choice_1 = True
                    user_response.choice_6 = False
                if 'feature2' in request.POST:
                    user_response.choice_2 = True
                    user_response.choice_6 = False
                if 'feature3' in request.POST:
                    user_response.choice_3 = True
                    user_response.choice_6 = False
                if 'feature4' in request.POST:
                    user_response.choice_4 = True
                    user_response.choice_6 = False
                if 'feature5' in request.POST:
                    user_response.choice_5 = True
                    user_response.choice_6 = False
                if 'feature6' in request.POST:
                    user_response.choice_6=True
                uid = request.session['user_id']
                user_response.user_id = UserDetails.objects.get(pk=uid)
                user_response.choice_corr = QuestionFeaturesSetTwo.objects.first()
                user_response.save()


        except ValueError as e:
            return render(request,'quiz/features_of_set_2.html',{'error':'Please select atleast one option from the following'})

    return render(request,'quiz/thankyou.html')

def start_of_real_test_set_one(request):
    if request.method=="POST":
        feature = request.POST.get("feature", None)
        if feature not in ["feature1", "feature2","feature3","feature4","feature5"]:
            return render(request,'quiz/sample_features_of_set_1.html',{'error':'Please select atleast one option from the following'})

    return render(request,'quiz/start_of_real_test_set_one.html')

def start_of_real_test_set_two(request):
    if request.method=="POST":
        feature = request.POST.get("feature", None)
        if feature not in ["feature1", "feature2", "feature3", "feature4", "feature5"]:
            return render(request, 'quiz/sample_features_of_set_1.html',{'error': 'Please select atleast one option from the following'})

    return render(request,'quiz/start_of_real_test_set_two.html')

def contact(request):
    return render(request,'quiz/contact.html')

def about(request):
    return render(request,'quiz/about.html')

def terms(request):
    return render(request,'quiz/terms.html')

def distractor(request):
    return render(request,'quiz/distractor.html')

def start_of_set_two(request):
    if request.method=="POST":
        if request.POST['quantity1']!='65':
            return render(request,'quiz/distractor.html',{'error':'Please get the right answer for the first question.'})
        elif request.POST['quantity2']!='54':
            return render(request, 'quiz/distractor.html',{'error': 'Please get the right answer for the second question.'})
        elif request.POST['quantity3']!='121':
            return render(request, 'quiz/distractor.html',{'error': 'Please get the right answer for the third question.'})
        elif request.POST['quantity4']!='52':
            return render(request, 'quiz/distractor.html',{'error': 'Please get the right answer for the fourth question.'})
    return render(request,'quiz/start_set_2.html')

