from django.http import JsonResponse
from django.shortcuts import render, redirect


from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet

from .forms import TaskForm
from .models import Task
from .serializers import TaskSerializer

from .tasks import post_submission, get_submission
from .service import service


class TaskApiView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def task_app(request):
    return render(request, 'base.html')


class AddTask(View):
    """ Taking a POST request and response task_ID"""
    def post(self, request):
        form = TaskForm(request.POST)
        context = {}
        if form.is_valid():
            form = form.save(commit=False)
            text = request.POST["text"]
            result = post_submission(text)
            form.status = result[1]
            form.task_id = result[0]
            form.save()
            context['task_id'] = result[0]
            return JsonResponse(context)
        return redirect('/')


def check_result(request, task_id):
    """ Checking result and save in db status """
    print(task_id)
    task = get_submission.delay(task_id)
    response_data = {'task_status': task.status, 'task_id': task.id, 'results': task.get()}
    if response_data['results'][1] != 'evaluation':
        service(response_data['results'][0], response_data['results'][1])
    return JsonResponse({"task_id": response_data['results'][0], "status": response_data['results'][1]})
