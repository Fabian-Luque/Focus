from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")

def detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

def results(request, task_id):
    response = "You're looking at the results of tasks %s."
    return HttpResponse(response % task_id)