from django.shortcuts import get_object_or_404,render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     #output = ','.join([q.question_test for q in latest_question_list])
#     return HttpResponse(template.render(context,request))
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return render(request,'polls/index.html',context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
       # return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request,'polls/detail.html',{'question':question})
#     #return HttpResponse("you're looking at question %s." % question_id)



# def results(request,question_id):
#     response = "you're looking at the results of question %s."
#     return  HttpResponse(response % question_id)
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def vote(request,question_id):
#     return HttpResponse("you're voting on question %s." % question_id)
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"you didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

# Create your views here.
