from django.shortcuts import render
from feedbackapp.models import FeedbackData
from feedbackapp.forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date=dt.datetime.now()
def FeedbackView(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                date=date,
                feedback=feedback
            )
            data.save()
            fform=FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'feedback':feedbacks})
        else:
            return HttpResponse("user missed some values")
    else:
        fform=FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
